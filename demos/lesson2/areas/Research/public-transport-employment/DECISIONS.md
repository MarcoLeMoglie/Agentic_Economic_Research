---
title: Public Transport and Employment — Decisions
type: decision-log
status: active
project: public-transport-employment
updated: 2026-11-18
---

# Decisions

Append-only. Confirmed choices only. Proposals stay in [PROJECT_BRIEF.md](PROJECT_BRIEF.md) or [NEXT_ACTIONS.md](NEXT_ACTIONS.md).

| ID | Date | Decision | Status |
|---|---|---|---|
| D-001 | 2026-11-12 | Staggered DiD with group-time ATTs; not-yet-treated comparison | active |
| D-002 | 2026-11-12 | Formal employment rate is the sole primary outcome | active |
| D-003 | 2026-11-12 | District × quarter panel, event time in quarters, ≥4 pre-periods | active |

---

## D-001 — Staggered DiD with group-time ATTs

**Date:** 2026-11-12
**Status:** active
**Decision:** The primary design is difference-in-differences with staggered treatment timing. Effects are estimated as cohort-by-period average treatment effects on the treated and aggregated into an event-study path. The comparison group is districts not yet treated at a given period. Naive two-way fixed-effects estimates are reported only as a descriptive benchmark, not as the main result.

**Rationale:** Districts adopt BRT at different times, and effects are likely heterogeneous across cohorts and over exposure. In that setting, a single two-way fixed-effects coefficient is a variance-weighted mix that can be biased, including sign-reversed, when effects move over time. Group-time estimation keeps the comparison explicit and makes pre-trends inspectable.

**Alternatives rejected:**
- *Naive TWFE as primary* — simple, but the weighting problem is exactly the one this design must avoid.
- *Synthetic control* — too few pre-periods and multiple treated units; donor pools would be arbitrary.
- *Cross-sectional IV* — no credible instrument in the fictional setting; distance to the CBD is not excludable.

**Consequences:** Requires a clean cohort variable, a not-yet-treated pool in every period, and explicit handling of the last-treated cohorts. Fewer effective clusters. The treatment definition must be fixed before estimation; it is currently provisional (Q-01). Small-cluster inference must be checked.

**Supersedes:** none.

---

## D-002 — One primary outcome

**Date:** 2026-11-12
**Status:** active
**Decision:** The primary outcome is the district formal employment rate (formal employment divided by working-age population). Commute time, job postings, and entry wages are secondary and exploratory; they are reported in a separate table and never substituted for the primary result.

**Rationale:** Fixing one outcome before seeing data prevents outcome shopping and keeps the headline claim interpretable. Secondary outcomes probe mechanisms H-01 and H-04 but cannot carry the causal claim on their own.

**Alternatives rejected:**
- *Multiple co-primary outcomes* — inflates the multiple-testing problem and weakens the headline.
- *Employment counts instead of rates* — confounded by district population growth (H-03).

**Consequences:** Population estimates become a required input. A null primary result is still a result and must be reported as such. Any change to the primary outcome requires a new decision and a dated log entry.

**Supersedes:** none.

---

## D-003 — Unit of analysis and event time

**Date:** 2026-11-12
**Status:** active
**Decision:** The panel is district × quarter. Treatment is assigned at the district level. Event time is measured in quarters relative to the district's treatment date. A cohort enters the main estimate only if it has at least four pre-treatment quarters.

**Rationale:** Quarterly data matches the fictional registry and gives enough pre-periods for a meaningful event study. A four-quarter minimum prevents cohorts with no baseline from dominating the pre-trend check.

**Alternatives rejected:**
- *Annual panel* — too few pre-periods for the event study and hides within-year timing.
- *Station-level analysis* — stations are not the unit that employment policy targets, and catchment areas overlap.

**Consequences:** Cohorts treated in 2014–2015 are excluded from the main estimate and appear only in a separate descriptive table. Standard errors cluster at the district level, with a small-cluster robustness check.

**Supersedes:** none.
