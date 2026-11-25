---
title: Public Transport and Employment — Sources
type: sources
status: active
project: public-transport-employment
updated: 2026-11-18
---

# Sources and Provenance

All sources in this project are **synthetic or unavailable**. Nothing here is a real citation, and no real document is claimed to exist.

## Register

| ID | Title | Author / publisher | Date | Type | File / locator | Accessed | Reliability | Status |
|---|---|---|---|---|---|---|---|---|
| S-001 | Rivervale BRT and employment — concept note (fictional) | Demonstration author | 2026-11-10 | internal memo | [raw/2026-11-10-concept-note.md](raw/2026-11-10-concept-note.md) | 2026-11-10 | illustrative only | acquired |
| S-002 | Applied econometrics handbook for staggered designs (fictional title) | — | — | handbook | not acquired | — | unknown | unavailable |
| S-003 | Rivervale district–quarter employment panel: data dictionary (fictional) | Rivervale Statistical Office (fictional) | — | data documentation | not acquired | — | unknown | unavailable |
| S-004 | BRT implementation timetable with station opening dates (fictional) | Rivervale Transport Authority (fictional) | — | administrative data | not acquired | — | unknown | unavailable |
| S-005 | Rivervale mobility survey, 2016 and 2022 waves (fictional) | Rivervale Mobility Survey (fictional) | — | survey | not acquired | — | unknown | unavailable |

Status vocabulary: `acquired` · `partial` · `unavailable` · `superseded`.

## What each source would support

- **S-001** — only the project's origin: question, mechanisms, and the synthetic framing. It is not evidence.
- **S-002** — methodological background for the wiki page on staggered DiD. It has not been read; the wiki page therefore states its basis as standard practice, not as a literature review.
- **S-003** — variable definitions, outcome measurement (residence vs workplace), missingness. Needed for Q-03 and the data request (A-01).
- **S-004** — treatment dates and station counts; determines cohorts and exposure. Needed for Q-01.
- **S-005** — commute-time mechanism (H-01), only if the survey is comparable across waves.

## Provenance rules

- Quote exactly with a section locator; paraphrase everything else.
- Separate the source's finding, the source's interpretation, and our inference.
- A source that has not been read is `unavailable`, not "cited".
- If two sources disagree, add a dated contradiction note in [CURRENT_STATE.md](CURRENT_STATE.md) and do not resolve it silently.
- Never edit a file in `raw/`.

## Missing sources

| What is missing | Why it matters | Attempted | Next step |
|---|---|---|---|
| Data dictionary | Outcome definition, geography, missingness | None — fictional owner | Include in A-01 request |
| Station opening timetable | Cohort assignment and treatment definition | None | Request with A-01; needed for A-03 |
| Methodology reference | Confirming the choice in D-001 against a citable text | None | Acquire before any real write-up |
| Commute survey documentation | Whether the two waves are comparable | None | Defer until mechanism stage |
