#!/usr/bin/env python3
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
file=root/'areas/Research/transit-employment/data/simulated_panel.csv'
with file.open() as fh: rows=list(csv.DictReader(fh))
missing=sum(1 for r in rows if not r['employment_share'])
assert all(r['synthetic']=='YES' for r in rows)
assert all(float(r['employment_share'])>=0 and float(r['employment_share'])<=1 for r in rows)
report=f"""# Dataset audit — SIMULATED DATA

- Rows: {len(rows)}
- Municipalities: {len(set(r['municipality'] for r in rows))}
- Missing employment share: {missing}
- Observational status: NONE. This file is entirely fictitious.

Never interpret simulated numbers as real labor-market evidence.
"""
out=root/'outputs/dataset-audit.md';out.parent.mkdir(exist_ok=True);out.write_text(report)
print(out, 'written; rows=',len(rows))
