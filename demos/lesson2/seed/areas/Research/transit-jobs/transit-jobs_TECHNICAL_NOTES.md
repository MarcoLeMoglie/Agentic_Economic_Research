# Technical notes

## 2026-10-01
- `data/synthetic_panel.csv` drawn with `random.Random(2026)`.
- 400 tracts, years 2010-2022, 20 districts.
- Treatment years 2016, 2018, 2020, plus never-treated tracts.
- Treatment is coded absorbing.

## 2026-10-12. Bug
`check_panel.py` once treated a blank cell as untreated. A blank is now a failure. The generator does not write blanks.

## Commands
- `python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py`
- `python areas/Research/transit-jobs/code/02_did.py` prints the lecture line and does not fit a model.
