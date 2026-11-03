#!/usr/bin/env python3
"""Read-only structural and semantic lint for the synthetic course vault."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
base=root/'areas/Research/transit-employment'
index=(base/'transit-employment_INDEX.md').read_text()
state=(base/'transit-employment_CURRENT_STATE.md').read_text()
print('SECOND BRAIN DEMO — MAINTENANCE AUDIT')
issues=[]
for p in sorted((base/'wiki').glob('*.md')):
 if p.name not in index:issues.append(f'ORPHAN: wiki/{p.name} not in INDEX')
for relative in re.findall(r'\]\((wiki/[^)]+)\)',index):
 if not (base/relative).exists():issues.append(f'BROKEN LINK: {relative}')
if 'DEPRECATED_PATH=' in state: issues.append('STALE PATH: CURRENT_STATE contains deprecated desktop path')
for issue in issues: print(' -',issue)
print(f'{len(issues)} issue(s) detected.')
raise SystemExit(1 if issues else 0)
