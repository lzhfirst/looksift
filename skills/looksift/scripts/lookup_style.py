"""Read exactly one bundled Looksift record; requires only Python's standard library."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def normalize_id(value):
    if isinstance(value, bool):
        raise ValueError('Use a style number containing 1 to 4 digits.')
    text = str(value).strip()
    if not re.fullmatch(r'#?[0-9]{1,4}', text):
        raise ValueError('Use a style number containing 1 to 4 digits, optionally prefixed by #.')
    return text.lstrip('#').zfill(4)


def lookup_style(value, references=REFERENCES):
    identifier = normalize_id(value)
    references = Path(references).resolve()
    entries = json.loads((references / 'styles.json').read_text(encoding='utf-8'))
    matches = [entry for entry in entries if entry['id'] == identifier]
    if not matches:
        raise LookupError(f'Style {identifier} is not in the current Looksift library; no substitute was selected.')
    if len(matches) != 1:
        raise ValueError(f'Duplicate identifier in index: {identifier}')
    path = (references / matches[0]['record']).resolve()
    if not path.is_relative_to(references):
        raise ValueError('Record path is outside the bundled references directory.')
    record = json.loads(path.read_text(encoding='utf-8'))
    if record.get('id') != identifier:
        raise ValueError(f'Record identifier does not match {identifier}.')
    fields = ('full_prompt_en', 'full_prompt_zh', 'style_prompt_en', 'style_prompt_zh')
    if any(not isinstance(record.get(key), str) or not record[key].strip() for key in fields):
        raise ValueError(f'Incomplete bilingual prompt record: {identifier}')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number')
    args = parser.parse_args()
    try:
        result = lookup_style(args.number)
    except (LookupError, ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
