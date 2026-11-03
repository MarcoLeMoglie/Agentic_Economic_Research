#!/usr/bin/env python3
"""Only for the synthetic classroom demo. Review git diff after running."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'areas/Research/transit-employment'
index=p/'transit-employment_INDEX.md'
text=index.read_text().replace('- [Research design](wiki/identification.md)','- [Research design](wiki/identification.md)\n- [Quality gates](wiki/quality-gates.md)').replace('- [Broken path for audit exercise](wiki/nonexistent-source.md)','')
index.write_text(text)
state=p/'transit-employment_CURRENT_STATE.md';txt=state.read_text();txt=txt.replace('Notes: check that `DEPRECATED_PATH=~/Desktop/OldBrain/transit-employment` is not used by future agents.','Notes: canonical demo vault lives in the current folder; old paths retired.')
state.write_text(txt)
print('Applied THREE known synthetic demo repairs. Inspect git diff before commit.')
