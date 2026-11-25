# Next Actions

Synthetic project. Actions concern a design exercise, not real data collection.

| ID | Action | Done when | Depends on | Owner | Added | Due |
|---|---|---|---|---|---|---|
| A-01 | Draft the variable-level data request for the district–quarter panel | A one-page request lists every variable, unit, coverage (2014Q1–2023Q4), format, and the fictional data owner; saved in `raw/` and registered in [SOURCES.md](SOURCES.md) | none | researcher | 2026-11-12 | 2026-11-25 |
| A-02 | Write the pre-analysis specification grid | A table of 6–9 specifications crosses two treatment definitions, two comparison groups, and two event windows; each is labelled primary or robustness; stored in [TECHNICAL_NOTES.md](TECHNICAL_NOTES.md) | A-03 for the final treatment column | researcher | 2026-11-12 | 2026-12-02 |
| A-03 | Settle the final treatment definition with the coauthor | Q-01 is answered, the choice is recorded in [DECISIONS.md](DECISIONS.md) as a new dated decision, and the specification grid is updated | coauthor decision | researcher + coauthor | 2026-11-12 | — |

## Blocked or waiting

| ID | Action | Waiting on | Since |
|---|---|---|---|
| A-03 | Final treatment definition | Fictional coauthor's decision between first opening and 25% coverage | 2026-11-12 |
| — | Data dictionary and panel extract | Fictional statistical office; no request sent | 2026-11-10 |

## Done recently

- **2026-11-18 — [DEMO]** Validation-only session: bootstrap and close protocols exercised. No research action completed; A-01, A-02, and A-03 are unchanged.
- **2026-11-21 — [DEMO]** Close-protocol-only session: no research action completed; A-01, A-02, and A-03 remain unchanged.

## Definition of done for this phase

The design phase closes when A-01 and A-02 are complete **and** A-03 is resolved. At that point the next actions become panel construction, a dry run on synthetic data, and a frozen pre-registration note. Do not start estimation before the grid is frozen.
