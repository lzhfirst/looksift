"""Behavior tests using isolated profiles and real CLI processes, never real defaults."""
import concurrent.futures
import importlib.util
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = Path(os.environ.get('LOOKSIFT_PREFERENCES_SCRIPT', str(
    PROJECT / 'skills/looksift/scripts/preferences.py')))

sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location('looksift_preferences_under_test', SCRIPT)
preferences = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preferences)


class PreferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='preferences-test-', dir=PROJECT/'tmp')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'state'
        self.sequence = 0

    def call(self, request, profile='test-main', *, args=(), expect_ok=True, root=None):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), '--data-root', str(root or self.root),
             '--profile', profile, '--test', *args],
            input=json.dumps(request), text=True, encoding='utf-8',
            capture_output=True, cwd=self.temp.name, timeout=25)
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            self.fail('Preference CLI must return a structured result: '+result.stderr[-800:])
        self.assertEqual(result.returncode, 0 if expect_ok else 2, data)
        self.assertEqual(data['ok'], expect_ok, data)
        return data

    def record(self, value='16:9', *, key='aspect_ratio', scope='explicit',
               source='user', event=None, request=None, profile='test-main', expect_ok=True):
        self.sequence += 1
        return self.call({'action':'record', 'key':key, 'value':value, 'scope':scope,
                          'source':source, 'event_id':event or f'event-{self.sequence}',
                          'request_id':request or f'drawing-{self.sequence}'},
                         profile=profile, expect_ok=expect_ok)

    def view(self, profile='test-main'):
        return self.call({'action':'view'}, profile=profile)

    def test_first_load_is_empty_and_does_not_create_storage(self):
        result = self.view()
        self.assertEqual(result['status'], 'missing')
        self.assertEqual(result['defaults'], {})
        self.assertEqual(result['candidates'], {})
        self.assertFalse(self.root.exists())

    def test_explicit_default_survives_a_new_process_and_resolves(self):
        self.assertTrue(self.record()['persisted'])
        self.assertEqual(self.view()['defaults'], {'aspect_ratio':'16:9'})
        result = self.call({'action':'resolve'})
        self.assertEqual(result['effective'], {'aspect_ratio':'16:9'})
        self.assertEqual(result['sources']['aspect_ratio'], 'explicit_long_term')

    def test_temporary_choice_overrides_this_request_without_changing_default(self):
        self.record()
        self.assertFalse(self.record('1:1', scope='temporary')['persisted'])
        result = self.call({'action':'resolve', 'current':{'aspect_ratio':'1:1'}})
        self.assertEqual(result['effective']['aspect_ratio'], '1:1')
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '16:9')
        self.assertEqual(self.view()['candidates'], {})

    def test_explicit_later_default_replaces_old_value(self):
        self.record()
        self.record('1:1')
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '1:1')

    def test_current_then_confirmed_then_long_term_precedence(self):
        self.record('16:9')
        self.record('B', key='mode')
        result = self.call({'action':'resolve', 'confirmed':{'aspect_ratio':'4:3','mode':'A'},
                            'current':{'aspect_ratio':'1:1'}})
        self.assertEqual(result['effective'], {'aspect_ratio':'1:1','mode':'A'})
        self.assertEqual(result['sources'], {'aspect_ratio':'current','mode':'confirmed'})

    def test_ignore_this_time_keeps_confirmed_context_and_does_not_delete(self):
        self.record()
        result = self.call({'action':'resolve','ignore_preferences':True,
                            'confirmed':{'mode':'B'},'current':{'aspect_ratio':'5:7'}})
        self.assertEqual(result['effective'], {'mode':'B','aspect_ratio':'5:7'})
        self.assertEqual(result['candidates'], {})
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '16:9')

    def test_agent_and_unknown_choices_never_become_user_preferences(self):
        for source in ['agent','unknown']:
            for scope in ['explicit','choice']:
                result = self.record(source=source, scope=scope)
                self.assertEqual(result['status'], 'ignored')
                self.assertFalse(result['persisted'])
        self.assertFalse(self.root.exists())

    def test_three_distinct_user_choices_create_candidate_not_default(self):
        self.record(scope='choice')
        self.record(scope='choice')
        self.assertEqual(self.view()['candidates'], {})
        self.record(scope='choice')
        result = self.view()
        self.assertEqual(result['defaults'], {})
        self.assertEqual(result['candidates']['aspect_ratio'][0]['value'], '16:9')
        self.assertEqual(result['candidates']['aspect_ratio'][0]['count'], 3)
        self.assertEqual(self.call({'action':'resolve'})['effective'], {})

    def test_replayed_event_does_not_count_twice(self):
        for _ in range(5):
            self.record(scope='choice', event='same', request='same-drawing')
        self.record(scope='choice')
        self.assertEqual(self.view()['candidates'], {})

    def test_same_drawing_counts_once_even_if_user_repeats_in_later_turns(self):
        for index in range(4):
            self.record(scope='choice', event=f'e-{index}', request='one-drawing')
        self.assertEqual(self.view()['candidates'], {})

    def test_changed_choice_within_drawing_replaces_its_observation(self):
        self.record(scope='choice', event='first', request='r1')
        self.record('1:1', scope='choice', event='correction', request='r1')
        self.record('1:1', scope='choice', request='r2')
        self.record('1:1', scope='choice', request='r3')
        candidates = self.view()['candidates']['aspect_ratio']
        self.assertEqual([(x['value'],x['count']) for x in candidates], [('1:1',3)])

    def test_same_event_with_changed_payload_is_rejected(self):
        self.record(event='same', request='r')
        result = self.record('1:1', event='same', request='r', expect_ok=False)
        self.assertEqual(result['reason'], 'event_conflict')
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '16:9')

    def test_replaying_old_long_term_event_does_not_roll_back_new_default(self):
        self.record(event='old', request='r1')
        self.record('1:1', event='new', request='r2')
        self.record(event='old', request='r1')
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '1:1')

    def test_forget_one_key_removes_default_and_observations_only_for_that_key(self):
        self.record()
        self.record('B', key='mode')
        for _ in range(3): self.record(scope='choice')
        self.call({'action':'forget','key':'aspect_ratio','source':'user','event_id':'forget'})
        view = self.view()
        self.assertEqual(view['defaults'], {'mode':'B'})
        self.assertEqual(view['candidates'], {})

    def test_clearing_values_retains_only_receipts_to_prevent_old_event_replay(self):
        self.record(event='remember', request='r')
        for _ in range(3): self.record(scope='choice')
        self.call({'action':'clear','source':'user','event_id':'clear'})
        self.record(event='remember', request='r')
        self.assertEqual(self.view()['defaults'], {})
        self.assertEqual(self.view()['candidates'], {})
        self.record('1:1', event='later')
        self.call({'action':'clear','source':'user','event_id':'clear'})
        self.assertEqual(self.view()['defaults'], {'aspect_ratio':'1:1'})

    def test_clear_requires_user_intent(self):
        self.record()
        self.call({'action':'clear','source':'agent','event_id':'clear'})
        self.assertEqual(self.view()['defaults']['aspect_ratio'], '16:9')

    def test_profiles_are_isolated_for_defaults_and_candidates(self):
        self.record(profile='test-alice')
        for _ in range(3): self.record('1:1', scope='choice', profile='test-bob')
        self.assertEqual(self.view('test-alice')['candidates'], {})
        self.assertEqual(self.view('test-bob')['defaults'], {})
        self.assertEqual(self.view('test-bob')['candidates']['aspect_ratio'][0]['value'], '1:1')

    def test_shared_host_requires_explicit_profile(self):
        result = subprocess.run([sys.executable,str(SCRIPT),'--shared','--data-root',str(self.root)],
                                input='{"action":"view"}',text=True,capture_output=True,encoding='utf-8')
        data = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(data['reason'], 'profile_required')
        self.assertFalse(self.root.exists())

    def test_shared_profile_is_supported(self):
        self.record(profile='test-host-user-1')
        result = self.call({'action':'view'}, profile='test-host-user-1', args=['--shared'])
        self.assertEqual(result['defaults']['aspect_ratio'], '16:9')

    def test_test_mode_requires_explicit_isolated_root(self):
        result = subprocess.run([sys.executable,str(SCRIPT),'--test','--profile','test-isolated'],
                                input='{"action":"view"}',text=True,capture_output=True,encoding='utf-8')
        self.assertEqual(json.loads(result.stdout)['reason'], 'test_root_required')
        self.assertEqual(result.returncode, 2)

    def test_test_mode_rejects_real_profile_name(self):
        result = self.call({'action':'view'}, profile='real-user', expect_ok=False)
        self.assertEqual(result['reason'], 'test_profile_required')
        self.assertFalse(self.root.exists())

    def test_corrupt_storage_is_not_silently_overwritten(self):
        self.record()
        db = next(self.root.glob('*.sqlite3'))
        db.write_bytes(b'corrupt preference file')
        view = self.call({'action':'view'}, expect_ok=False)
        self.assertEqual(view['defaults'], {})
        self.assertEqual(view['status'], 'unavailable')
        result = self.record('1:1', expect_ok=False)
        self.assertFalse(result['persisted'])
        self.assertEqual(db.read_bytes(), b'corrupt preference file')

    def test_corrupt_storage_falls_back_to_current_context(self):
        self.record()
        next(self.root.glob('*.sqlite3')).write_bytes(b'corrupt')
        result = self.call({'action':'resolve','current':{'aspect_ratio':'1:1'}},expect_ok=False)
        self.assertEqual(result['effective'], {'aspect_ratio':'1:1'})
        self.assertEqual(result['sources'], {'aspect_ratio':'current'})

    def test_explicit_clear_can_clear_corrupt_current_profile(self):
        self.record()
        next(self.root.glob('*.sqlite3')).write_bytes(b'corrupt')
        result = self.call({'action':'clear','source':'user','event_id':'clear-bad'})
        self.assertEqual(result['status'], 'cleared')
        self.assertEqual(self.view()['defaults'], {})

    def test_write_failure_does_not_claim_saved(self):
        self.root.write_text('not a directory',encoding='utf-8')
        result = self.record(expect_ok=False)
        self.assertFalse(result['persisted'])
        self.assertEqual(result['status'], 'unavailable')
        self.assertEqual(self.root.read_text(encoding='utf-8'),'not a directory')

    def test_concurrent_observations_are_not_lost(self):
        def record(index):
            return self.call({'action':'record','key':'aspect_ratio','value':'16:9',
                              'scope':'choice','source':'user','event_id':f'concurrent-{index}',
                              'request_id':f'drawing-{index}'})
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            list(executor.map(record,range(12)))
        self.assertEqual(self.view()['candidates']['aspect_ratio'][0]['count'],12)

    def test_only_allowed_preference_fields_can_be_saved(self):
        for key in ['api_key','chat_text','email','image','arbitrary']:
            result = self.record('secret',key=key,expect_ok=False)
            self.assertEqual(result['reason'],'invalid_input')
        self.assertFalse(self.root.exists())

    def test_invalid_values_and_unknown_style_are_rejected(self):
        for key,value in [('aspect_ratio','16:0'),('mode','C'),('language','../../secret'),
                          ('detail_handling','silence'),('style_id','12oops'),('style_id','9999')]:
            with self.subTest(key=key,value=value):
                self.record(value,key=key,expect_ok=False)
        self.assertFalse(self.root.exists())

    def test_values_are_normalized_and_known_style_uses_bundled_lookup(self):
        for key,value in [('aspect_ratio','1200x800'),('mode','b'),('style_id','#1813'),
                          ('language','de'),('detail_handling','agent_complete')]:
            self.record(value,key=key)
        self.assertEqual(self.view()['defaults'], {'aspect_ratio':'3:2','mode':'B',
                          'style_id':'1813','language':'de','detail_handling':'agent_complete'})

    def test_ratio_default_does_not_create_content_permission(self):
        self.record()
        self.assertNotIn('detail_handling',self.call({'action':'resolve'})['effective'])

    def test_content_candidate_is_not_ongoing_permission_but_explicit_default_is(self):
        for _ in range(3): self.record('agent_complete',key='detail_handling',scope='choice')
        self.assertNotIn('detail_handling',self.call({'action':'resolve'})['effective'])
        self.record('agent_complete',key='detail_handling')
        self.assertEqual(self.call({'action':'resolve'})['effective']['detail_handling'],'agent_complete')

    def test_database_contains_no_raw_event_request_or_profile_identifiers(self):
        self.record(event='private-raw-event',request='private-raw-request',profile='test-private-name')
        db = next(self.root.glob('*.sqlite3'))
        raw = db.read_bytes()
        for value in [b'private-raw-event',b'private-raw-request',b'test-private-name']:
            self.assertNotIn(value,raw)
        self.assertNotIn('test-private-name',db.name)

    def test_unknown_schema_fails_closed(self):
        self.record()
        db = next(self.root.glob('*.sqlite3'))
        with closing(sqlite3.connect(db)) as connection:
            connection.execute('PRAGMA user_version = 999')
        result = self.call({'action':'view'},expect_ok=False)
        self.assertEqual(result['reason'],'unsupported_schema')
        self.assertEqual(result['defaults'],{})

    def test_missing_event_and_request_ids_cannot_create_observations(self):
        result = self.call({'action':'record','key':'mode','value':'B','scope':'choice','source':'user'},expect_ok=False)
        self.assertEqual(result['reason'],'invalid_input')
        self.assertFalse(self.root.exists())

    def test_communication_style_persists_but_current_style_wins(self):
        self.record('light and humorous', key='communication_style')
        result = self.call({'action':'resolve','current':{'communication_style':'formal and concise'}})
        self.assertEqual(result['effective']['communication_style'],'formal and concise')
        self.assertEqual(self.view()['defaults']['communication_style'],'light and humorous')
        self.assertNotIn('detail_handling',result['effective'])

    def test_temporary_communication_style_is_not_saved(self):
        self.record('humorous',key='communication_style',scope='temporary')
        self.assertEqual(self.view()['defaults'],{})
        self.assertEqual(self.view()['candidates'],{})

    def test_forget_communication_style_does_not_remove_visual_style(self):
        self.record('humorous',key='communication_style')
        self.record('1813',key='style_id')
        self.call({'action':'forget','key':'communication_style','source':'user','event_id':'cancel-tone'})
        self.assertEqual(self.view()['defaults'],{'style_id':'1813'})

    def test_communication_style_is_a_short_data_value_not_a_transcript(self):
        for value in ['', 'x'*121, 'line one\nline two', '\x00hidden']:
            self.record(value,key='communication_style',expect_ok=False)
        self.assertFalse(self.root.exists())

    def test_invalid_action_fields_do_not_trigger_a_mutation(self):
        result = self.call({'action':'clear','key':'mode','source':'user','event_id':'bad-clear'},expect_ok=False)
        self.assertFalse(result['persisted'])
        self.assertFalse(self.root.exists())

    def test_ignore_flag_must_be_boolean(self):
        for value in ['true',1,None]:
            self.call({'action':'resolve','ignore_preferences':value},expect_ok=False)

    def test_malformed_json_returns_structured_failure(self):
        result = subprocess.run([sys.executable,str(SCRIPT),'--test','--data-root',str(self.root),
                                 '--profile','test-malformed'],input='{broken',text=True,capture_output=True)
        self.assertEqual(result.returncode,2)
        self.assertEqual(json.loads(result.stdout)['reason'],'invalid_input')
        self.assertFalse(self.root.exists())

    def test_read_permission_failure_retains_current_context(self):
        with mock.patch.object(preferences.Store,'read',side_effect=PermissionError('denied')):
            result = preferences.handle({'action':'resolve','current':{'mode':'B'}},
                         data_root=self.root,profile='test-denied',test=True)
        self.assertFalse(result['ok'])
        self.assertFalse(result['persisted'])
        self.assertEqual(result['effective'],{'mode':'B'})

    def test_commit_failure_rolls_back_and_never_claims_persistence(self):
        self.record()
        class FailCommit(sqlite3.Connection):
            def commit(self):
                raise sqlite3.OperationalError('simulated disk failure at commit')
        real_connect = sqlite3.connect
        def failing_connect(*args,**kwargs):
            return real_connect(*args,**kwargs,factory=FailCommit)
        with mock.patch.object(preferences.sqlite3,'connect',side_effect=failing_connect):
            result = preferences.handle({'action':'record','key':'aspect_ratio','value':'1:1',
                         'scope':'explicit','source':'user','event_id':'failed-commit'},
                         data_root=self.root,profile='test-main',test=True)
        self.assertFalse(result['ok'])
        self.assertFalse(result['persisted'])
        self.assertEqual(self.view()['defaults']['aspect_ratio'],'16:9')

    def test_test_mode_cannot_touch_the_default_runtime_root(self):
        with mock.patch.object(preferences,'runtime_root',return_value=self.root):
            result = preferences.handle({'action':'view'},data_root=self.root,
                                         profile='test-dangerous',test=True)
        self.assertEqual(result['reason'],'unsafe_runtime_location')
        self.assertFalse(self.root.exists())

    def test_runtime_storage_cannot_be_inside_distributed_bundle(self):
        result = preferences.handle({'action':'view'},data_root=preferences.BUNDLE/'runtime-test',
                                     profile='test-denied')
        self.assertEqual(result['reason'],'unsafe_runtime_location')

    def test_profile_path_is_opaque_even_when_identifier_contains_path_characters(self):
        self.record(profile='test-../../other-user')
        self.assertEqual(len(list(self.root.glob('*.sqlite3'))),1)
        self.assertEqual(list(self.root.iterdir())[0].parent,self.root)

    def retired_style_library(self):
        """A separate fake index retires 1813; no real style files are changed."""
        refs = Path(self.temp.name)/'changed-library'
        (refs/'styles').mkdir(parents=True,exist_ok=True)
        record = {'id':'1988','name':'Fixture survivor',
                  'full_prompt_en':'Fixture scene','full_prompt_zh':'测试场景',
                  'style_prompt_en':'Fixture marks','style_prompt_zh':'测试笔触'}
        (refs/'styles/1988.json').write_text(json.dumps(record),encoding='utf-8')
        (refs/'styles.json').write_text(json.dumps([
            {'id':'1988','record':'styles/1988.json'}]),encoding='utf-8')
        real_lookup = preferences.lookup_style
        return mock.patch.object(preferences,'lookup_style',
                                 side_effect=lambda value: real_lookup(value,refs))

    def local_handle(self, request):
        return preferences.handle(request,data_root=self.root,profile='test-main',test=True)

    def test_retired_style_view_keeps_other_defaults_and_does_not_rewrite_storage(self):
        self.record('1813',key='style_id')
        self.record('de',key='language')
        self.record('9:16')
        db = next(self.root.glob('*.sqlite3'))
        before = db.read_bytes()
        with self.retired_style_library():
            result = self.local_handle({'action':'view'})
        self.assertTrue(result['ok'],result)
        self.assertFalse(result['persisted'])
        self.assertEqual(result['defaults'],{'language':'de','aspect_ratio':'9:16'})
        self.assertNotIn('style_id',result['default_sources'])
        self.assertEqual(result['unavailable'],[{'key':'style_id','value':'1813',
                         'source':'explicit_user_long_term','reason':'style_unavailable'}])
        self.assertEqual(db.read_bytes(),before)

    def test_retired_style_resolve_preserves_priority_without_selecting_a_substitute(self):
        self.record('1813',key='style_id')
        self.record('de',key='language')
        self.record('9:16')
        with self.retired_style_library():
            result = self.local_handle({'action':'resolve','confirmed':{'mode':'A'},
                                        'current':{'aspect_ratio':'1:1'}})
        self.assertTrue(result['ok'],result)
        self.assertEqual(result['effective'],{'mode':'A','language':'de','aspect_ratio':'1:1'})
        self.assertEqual(result['sources']['language'],'explicit_long_term')
        self.assertNotIn('style_id',result['effective'])

    def test_retired_style_candidates_do_not_hide_valid_candidates_or_defaults(self):
        self.record('de',key='language')
        for _ in range(3): self.record('1813',key='style_id',scope='choice')
        for _ in range(3): self.record('1988',key='style_id',scope='choice')
        with self.retired_style_library():
            result = self.local_handle({'action':'view'})
        self.assertTrue(result['ok'],result)
        self.assertEqual(result['defaults'],{'language':'de'})
        self.assertEqual(result['candidates']['style_id'],[
            {'value':'1988','count':3,'source':'repeated_user_choices'}])
        self.assertEqual(result['unavailable'],[{'key':'style_id','value':'1813',
                         'source':'repeated_user_choices','reason':'style_unavailable','count':3}])

    def test_retired_style_does_not_block_an_unrelated_explicit_update(self):
        self.record('1813',key='style_id')
        with self.retired_style_library():
            result = self.local_handle({'action':'record','key':'language','value':'de',
                         'scope':'explicit','source':'user','event_id':'language-after-retirement'})
        self.assertTrue(result['ok'],result)
        self.assertTrue(result['persisted'])
        self.assertEqual(result['defaults'],{'language':'de'})
        self.assertEqual(self.view()['defaults']['language'],'de')
        self.assertEqual(self.view()['defaults']['style_id'],'1813')

    def test_retired_style_can_be_explicitly_replaced_or_forgotten(self):
        self.record('1813',key='style_id')
        self.record('de',key='language')
        with self.retired_style_library():
            replaced = self.local_handle({'action':'record','key':'style_id','value':'1988',
                         'scope':'explicit','source':'user','event_id':'replace-style'})
            self.assertTrue(replaced['ok'],replaced)
            self.assertEqual(replaced['defaults']['style_id'],'1988')
            self.assertEqual(replaced['unavailable'],[])
        self.record('1813',key='style_id')
        with self.retired_style_library():
            forgotten = self.local_handle({'action':'forget','key':'style_id',
                                            'source':'user','event_id':'forget-retired'})
        self.assertTrue(forgotten['persisted'])
        self.assertEqual(forgotten['unavailable'],[])
        self.assertEqual(forgotten['defaults'],{'language':'de'})

    def test_retired_style_still_cannot_be_saved_as_a_new_valid_choice(self):
        self.record('de',key='language')
        with self.retired_style_library():
            rejected = self.local_handle({'action':'record','key':'style_id','value':'1813',
                         'scope':'explicit','source':'user','event_id':'invalid-new-selection'})
        self.assertFalse(rejected['ok'])
        self.assertFalse(rejected['persisted'])
        self.assertEqual(self.view()['defaults'],{'language':'de'})

    def test_retired_style_lookup_read_error_is_not_claimed_as_confirmed_deletion(self):
        self.record('1813',key='style_id')
        self.record('de',key='language')
        with mock.patch.object(preferences,'lookup_style',side_effect=OSError('unreadable index')):
            result = self.local_handle({'action':'view'})
        self.assertTrue(result['ok'],result)
        self.assertEqual(result['defaults'],{'language':'de'})
        self.assertEqual(result['unavailable'][0]['reason'],'style_unavailable')


if __name__ == '__main__':
    unittest.main()
