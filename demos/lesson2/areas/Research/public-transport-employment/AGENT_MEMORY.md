# Agent Memory

**Last verified:** 2026-11-21. Briefing for an agent about to work here. If the other core files already say it, it should not be repeated at length.

## Context

A **synthetic** design-stage project asking whether BRT station openings raise formal employment in fictional Rivervale districts. Three decisions are binding: staggered DiD with group-time ATTs (D-001), formal employment rate as the only primary outcome (D-002), district × quarter panel with ≥4 pre-periods (D-003). No data exists and no estimate has been produced.

## Hard constraints

- Never present a number here as an empirical finding. There is no data.
- Never switch the primary outcome or estimator without a new dated decision.
- Do not use naive TWFE as the headline estimate; D-001 forbids it.
- Do not edit anything in `raw/`; cite it.
- Do not invent citations. The project deliberately has none.
- The setting is fictional. Do not "verify" Rivervale facts online or import real-city numbers.

## Vocabulary

| Term | Means here | Not to be confused with |
|---|---|---|
| Treated district | District whose first BRT station entered revenue service | District crossed by a line without a station |
| Cohort | Year/quarter of treatment | Calendar year of analysis |
| Not-yet-treated | Districts untreated at period *t*, used as comparison | Never-treated (may not exist for late periods) |
| Exposure | Stations per 10,000 residents (secondary, not yet used) | Treatment indicator |
| Formal employment rate | Formal employment / working-age population | Employment count, labour-force participation |

## Traps

- **Cohort leakage:** assigning treatment at announcement or construction start instead of revenue service. The working definition is first revenue service, provisional.
- **Last-cohort problem:** the final treated cohort has no not-yet-treated comparison. Handle explicitly; do not silently drop it.
- **Population denominator:** using a constant population hides sorting (H-03). Use contemporaneous estimates and show sensitivity.
- **Few clusters:** 24 districts, 11 treated. Do not report conventional clustered p-values alone.
- **Validation masking:** the validator ignores links inside backticks and fenced blocks. A broken link hidden in code still breaks for readers.
- **Wiki drift:** the DiD wiki page is a stable reference, not the project's state. State lives in [CURRENT_STATE.md](CURRENT_STATE.md).

## Where things live

- Design and scope: [PROJECT_BRIEF.md](PROJECT_BRIEF.md)
- Current truth: [CURRENT_STATE.md](CURRENT_STATE.md)
- Open work: [NEXT_ACTIONS.md](NEXT_ACTIONS.md)
- Binding choices: [DECISIONS.md](DECISIONS.md)
- Method reference: [wiki/difference-in-differences-design.md](wiki/difference-in-differences-design.md)
- Intake rules: [raw/README.md](raw/README.md)

## Ask the user before

- Changing the treatment definition (Q-01) or the primary outcome.
- Adding a new data source that implies a real-world contact.
- Rewriting D-001 to D-003 rather than superseding them.
- Expanding scope to mechanisms the design cannot identify.
