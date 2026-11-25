---
title: Public Transport and Employment — Current State
type: state
status: active
project: public-transport-employment
updated: 2026-11-21
---

# Current State

**As of 2026-11-21.** Synthetic project; all items describe a fictional design exercise. History: [LOG.md](LOG.md).

## Confirmed

- **Question fixed (2026-11-10):** causal effect of BRT station openings on the formal employment rate in fictional Rivervale districts, 2014Q1–2023Q4.
- **Design family fixed (2026-11-12):** staggered difference-in-differences with group-time ATTs and not-yet-treated comparisons (D-001).
- **Primary outcome fixed (2026-11-12):** district formal employment rate. Secondary outcomes are exploratory and reported separately (D-002).
- **Unit and time fixed (2026-11-12):** district × quarter, event time in quarters, at least four pre-periods required for a cohort to enter the main estimate (D-003).
- **No data acquired.** No empirical estimate exists. Nothing in this project is a finding.

## In progress

- **A-01 — Data request draft.** Variable-level request for the synthetic district–quarter panel. Not started in substance; due 2026-11-25.
- **A-02 — Pre-analysis specification grid.** Six to nine specifications crossing treatment definitions, comparison groups, and event windows. Not started; due 2026-12-02.

## Blocked

- **A-03 — Final treatment definition.** Blocked since 2026-11-12 on a decision from the fictional coauthor: first station opening versus 25% network coverage. See Q-01. Until resolved, the working definition is *first station opening*, labelled provisional.
- **Data access.** Fictional data owner has not supplied a data dictionary. No request has been sent. This blocks panel construction, not the design work.

## Completed

- **2026-11-10** — Project scaffolded from the global templates (11 core files).
- **2026-11-10** — Brief v1: question, mechanisms H-01 to H-04, scope, data needs ([PROJECT_BRIEF.md](PROJECT_BRIEF.md)).
- **2026-11-12** — Design session: D-001 to D-003 recorded; methodological reference written ([wiki page](wiki/difference-in-differences-design.md)).
- **2026-11-18** — **[DEMO]** Bootstrap and session-close simulation: state recovered from 11 files, validation passed, memory updated. No substantive research change; A-01 and A-02 remain open.
- **2026-11-21** — **[DEMO]** Close protocol run on request: memory re-verified, validation passed, log and summary updated. No research change.

## Not started

- Panel-construction protocol and synthetic-data dry run.
- Pre-registration note (specification grid frozen before estimation).
- Small-cluster inference check.
- Mechanism analysis using commute-time and job-posting data.

## Open questions

| ID | Question | Why it matters | What would settle it |
|---|---|---|---|
| Q-01 | Is a district treated at first station opening, or when 25% of planned stations are open? | Changes cohort assignment, effect size, and interpretation; partial rollouts are currently ambiguous. | Coauthor decision; record as a new decision and rerun the specification grid. |
| Q-02 | Drop the three districts with partial rollout and no completion date? | Dropping them improves definitional cleanliness but may select on political economy and reduce clusters to 21. | Pre-specified rule plus a robustness table with and without them. |
| Q-03 | Is the formal employment rate measured at residence or workplace? | Residence supports the access story; workplace supports the firm-relocation story (H-04). | Data dictionary from the fictional statistical office. |

## Confidence and caveats

The design is internally consistent but **untested**. The weakest points are the unresolved treatment definition (Q-01), the small number of clusters, and the impossibility of separating access from residential sorting with district-level data alone. No statement in this file should be read as an empirical claim.
