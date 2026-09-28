"""Local Looksift preference facts. JSON on stdin/stdout; Python standard library only.

The calling Agent interprets intent. This module never parses chat text, chooses a
drawing mode, invents authorization, or turns a candidate habit into a default.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
import sys

from lookup_style import lookup_style

KEYS = {'aspect_ratio', 'mode', 'style_id', 'language', 'detail_handling', 'communication_style'}
ACTION_FIELDS = {
    'view': {'action'},
    'resolve': {'action','current','confirmed','ignore_preferences'},
    'record': {'action','key','value','scope','source','event_id','request_id'},
    'forget': {'action','key','source','event_id'},
    'clear': {'action','source','event_id'},
}
SCHEMA = 1
CANDIDATE_MIN_REQUESTS = 3
BUNDLE = Path(__file__).resolve().parents[3]


class PreferenceError(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def runtime_root():
    """Per-OS-user data, never the working directory or distributable Skill."""
    if os.name == 'nt':
        value = os.environ.get('LOCALAPPDATA')
        if not value or not Path(value).is_absolute():
            raise PreferenceError('runtime_location_unavailable')
        return Path(value) / 'Looksift' / 'preferences'
    if sys.platform == 'darwin':
        return Path.home() / 'Library' / 'Application Support' / 'Looksift' / 'preferences'
    value = os.environ.get('XDG_DATA_HOME')
    home = Path(value) if value and Path(value).is_absolute() else Path.home() / '.local/share'
    return home / 'looksift' / 'preferences'


def normalize(key, value):
    if key not in KEYS or isinstance(value, bool) or not isinstance(value, (str, int)):
        raise PreferenceError('invalid_input')
    text = str(value).strip()
    if key == 'aspect_ratio':
        match = re.fullmatch(r'([0-9]{1,7})\s*[:x×]\s*([0-9]{1,7})', text)
        if not match:
            raise PreferenceError('invalid_input')
        width, height = map(int, match.groups())
        if not 0 < min(width, height) <= max(width, height) <= 1_000_000:
            raise PreferenceError('invalid_input')
        divisor = math.gcd(width, height)
        return f'{width // divisor}:{height // divisor}'
    if key == 'mode' and text.upper() in {'A', 'B'}:
        return text.upper()
    if key == 'style_id':
        try:
            return lookup_style(text)['id']
        except (LookupError, ValueError, OSError):
            raise PreferenceError('invalid_input') from None
    if key == 'language' and re.fullmatch(r'[a-zA-Z]{2,3}(?:-[a-zA-Z0-9]{2,8}){0,4}', text):
        return text.lower()
    if key == 'communication_style' and isinstance(value, str) and 0 < len(text) <= 120:
        if all(ord(char) >= 32 and ord(char) != 127 and char not in '\u2028\u2029' for char in value):
            return text
    if key == 'detail_handling' and text in {'agent_complete', 'no_additions', 'ask_each_time'}:
        return text
    raise PreferenceError('invalid_input')


def values(mapping):
    if not isinstance(mapping, dict):
        raise PreferenceError('invalid_input')
    return {key: normalize(key, value) for key, value in mapping.items()}


def token(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 512:
        raise PreferenceError('invalid_input')
    return value


def empty(status='missing'):
    return {'ok': True, 'status': status, 'persisted': False,
            'defaults': {}, 'default_sources': {}, 'candidates': {}, 'unavailable': []}


def failure(reason):
    result = empty('invalid' if reason in {'invalid_input', 'event_conflict',
                    'profile_required', 'test_root_required', 'test_profile_required',
                    'unsafe_runtime_location'} else 'unavailable')
    return {**result, 'ok': False, 'reason': reason}


class Store:
    def __init__(self, data_root=None, profile=None, shared=False, test=False):
        profile = profile or os.environ.get('LOOKSIFT_PROFILE')
        shared = shared or os.environ.get('LOOKSIFT_SHARED_HOST') == '1'
        if shared and (not profile or profile in {'local', 'default'}):
            raise PreferenceError('profile_required')
        if test and data_root is None:
            raise PreferenceError('test_root_required')
        profile = profile or 'local'
        token(profile)
        if test and not profile.startswith('test-'):
            raise PreferenceError('test_profile_required')
        self.root = Path(data_root).expanduser().resolve() if data_root is not None else runtime_root().resolve()
        if not test and self.root.is_relative_to(BUNDLE):
            raise PreferenceError('unsafe_runtime_location')
        if test:
            try:
                real_root = runtime_root().resolve()
            except PreferenceError:
                real_root = None
            if real_root and (self.root.is_relative_to(real_root) or real_root.is_relative_to(self.root)):
                raise PreferenceError('unsafe_runtime_location')
        self.path = self.root / (digest(profile) + '.sqlite3')
        if self.path.is_symlink():
            raise PreferenceError('unsafe_runtime_location')

    @staticmethod
    def check_schema(connection):
        if connection.execute('PRAGMA user_version').fetchone()[0] != SCHEMA:
            raise PreferenceError('unsupported_schema')

    @staticmethod
    def initialize(connection):
        version = connection.execute('PRAGMA user_version').fetchone()[0]
        if version == SCHEMA:
            return
        if version != 0 or connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchone():
            raise PreferenceError('unsupported_schema')
        connection.execute('CREATE TABLE preferences (key TEXT PRIMARY KEY, value TEXT NOT NULL, event_hash TEXT NOT NULL, updated_at TEXT NOT NULL)')
        connection.execute('CREATE TABLE observations (key TEXT NOT NULL, request_hash TEXT NOT NULL, value TEXT NOT NULL, PRIMARY KEY (key, request_hash))')
        connection.execute('CREATE TABLE receipts (event_hash TEXT PRIMARY KEY, payload_hash TEXT NOT NULL)')
        connection.execute(f'PRAGMA user_version = {SCHEMA}')

    @staticmethod
    def snapshot(connection):
        result = empty('loaded')

        def stored_value(key, raw, source, **details):
            original = json.loads(raw)
            try:
                return normalize(key, original)
            except PreferenceError:
                # A mutable external library can retire a formerly valid ID.
                # Ignore only that unusable style, preserving all other facts.
                if key != 'style_id':
                    raise
                result['unavailable'].append({'key': key, 'value': original,
                    'source': source, 'reason': 'style_unavailable', **details})
                return None

        for key, raw, event_hash, updated in connection.execute('SELECT key,value,event_hash,updated_at FROM preferences ORDER BY key'):
            value = stored_value(key, raw, 'explicit_user_long_term')
            if value is None:
                continue
            result['defaults'][key] = value
            result['default_sources'][key] = {'source': 'explicit_user_long_term',
                                             'event_hash': event_hash, 'updated_at': updated}
        rows = connection.execute('SELECT key,value,COUNT(*) FROM observations GROUP BY key,value HAVING COUNT(*) >= ? ORDER BY key,COUNT(*) DESC,value', (CANDIDATE_MIN_REQUESTS,))
        for key, raw, count in rows:
            value = stored_value(key, raw, 'repeated_user_choices', count=count)
            if value is None:
                continue
            result['candidates'].setdefault(key, []).append(
                {'value': value, 'count': count, 'source': 'repeated_user_choices'})
        return result

    def read(self):
        if not self.path.exists():
            if self.root.exists() and not self.root.is_dir():
                raise OSError('Runtime location is not a directory')
            return empty()
        connection = sqlite3.connect(self.path.as_uri()+'?mode=ro', uri=True, timeout=10)
        try:
            self.check_schema(connection)
            return self.snapshot(connection)
        finally:
            connection.close()

    def mutate(self, request):
        action = request['action']
        key = request.get('key', '*')
        if action in {'record', 'forget'} and key not in KEYS:
            raise PreferenceError('invalid_input')
        if request.get('source') not in {'user', 'agent', 'unknown'}:
            raise PreferenceError('invalid_input')
        if request['source'] != 'user':
            return empty('ignored')
        scope = request.get('scope')
        if action == 'record':
            if scope not in {'explicit', 'choice', 'temporary'}:
                raise PreferenceError('invalid_input')
            value = normalize(key, request.get('value'))
            if scope == 'temporary':
                return empty('ignored')
        else:
            value = None
        event_hash = digest(token(request.get('event_id'))+'\0'+key)
        request_hash = digest(token(request.get('request_id'))) if action == 'record' and scope == 'choice' else ''
        payload_hash = digest(json.dumps([action,key,value,scope,request_hash],ensure_ascii=False))
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        connection = None
        try:
            connection = sqlite3.connect(self.path, timeout=10)
            connection.execute('PRAGMA secure_delete = ON')
            connection.execute('BEGIN IMMEDIATE')
            self.initialize(connection)
            prior = connection.execute('SELECT payload_hash FROM receipts WHERE event_hash=?', (event_hash,)).fetchone()
            if prior:
                if prior[0] != payload_hash:
                    raise PreferenceError('event_conflict')
                result = self.snapshot(connection)
                connection.rollback()
                return {**result, 'status': 'duplicate', 'persisted': False}
            if action == 'record' and scope == 'explicit':
                connection.execute('INSERT INTO preferences VALUES (?,?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,event_hash=excluded.event_hash,updated_at=excluded.updated_at',
                                   (key,json.dumps(value),event_hash,datetime.now(timezone.utc).isoformat()))
            elif action == 'record':
                connection.execute('INSERT INTO observations VALUES (?,?,?) ON CONFLICT(key,request_hash) DO UPDATE SET value=excluded.value',
                                   (key,request_hash,json.dumps(value)))
            elif action == 'forget':
                connection.execute('DELETE FROM preferences WHERE key=?',(key,))
                connection.execute('DELETE FROM observations WHERE key=?',(key,))
            elif action == 'clear':
                connection.execute('DELETE FROM preferences')
                connection.execute('DELETE FROM observations')
            connection.execute('INSERT INTO receipts VALUES (?,?)',(event_hash,payload_hash))
            result = self.snapshot(connection)
            connection.commit()
            return {**result, 'status': {'record':'saved','forget':'forgotten','clear':'cleared'}[action], 'persisted': True}
        except sqlite3.DatabaseError as error:
            if connection is not None:
                connection.close()
                connection = None
            # Only the user's explicit clear may remove this profile's corrupt DB.
            # Busy, denied and unknown-schema errors never trigger deletion.
            if action == 'clear' and getattr(error, 'sqlite_errorcode', None) in {sqlite3.SQLITE_CORRUPT, sqlite3.SQLITE_NOTADB}:
                for suffix in ['', '-journal', '-wal', '-shm']:
                    target = self.path.with_name(self.path.name+suffix)
                    if target.is_symlink():
                        raise PreferenceError('unsafe_runtime_location')
                    target.unlink(missing_ok=True)
                return {**empty('cleared'), 'persisted': True}
            raise
        finally:
            if connection is not None:
                connection.close()


def error_reason(error):
    if isinstance(error, PreferenceError):
        return error.reason
    if isinstance(error, sqlite3.DatabaseError) and getattr(error, 'sqlite_errorcode', None) in {sqlite3.SQLITE_CORRUPT, sqlite3.SQLITE_NOTADB}:
        return 'corrupt_storage'
    return 'storage_unavailable'


def handle(request, *, data_root=None, profile=None, shared=False, test=False):
    try:
        if not isinstance(request, dict):
            raise PreferenceError('invalid_input')
        action = request.get('action')
        if action not in ACTION_FIELDS or set(request)-ACTION_FIELDS[action]:
            raise PreferenceError('invalid_input')
        if 'ignore_preferences' in request and not isinstance(request['ignore_preferences'], bool):
            raise PreferenceError('invalid_input')
        current = values(request.get('current',{})) if action == 'resolve' else {}
        confirmed = values(request.get('confirmed',{})) if action == 'resolve' else {}
        if action == 'resolve' and request.get('ignore_preferences',False) is True:
            result = empty('context_only')
        else:
            try:
                store = Store(data_root,profile,shared,test)
                result = store.read() if action in {'view','resolve'} else store.mutate(request)
            except (PreferenceError, OSError, sqlite3.Error, json.JSONDecodeError) as error:
                result = failure(error_reason(error))
        if action == 'resolve':
            effective = dict(result['defaults'])
            sources = {key:'explicit_long_term' for key in effective}
            for kind, mapping in [('confirmed',confirmed),('current',current)]:
                effective.update(mapping)
                sources.update({key:kind for key in mapping})
            result.update(effective=effective,sources=sources)
        return result
    except (PreferenceError, TypeError, ValueError):
        return failure('invalid_input')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--profile')
    parser.add_argument('--shared', action='store_true')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    try:
        request = json.load(sys.stdin)
    except (ValueError, OSError):
        result = failure('invalid_input')
    else:
        result = handle(request, data_root=args.data_root, profile=args.profile,
                        shared=args.shared,test=args.test)
    print(json.dumps(result,ensure_ascii=False,separators=(',',':')))
    return 0 if result['ok'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
