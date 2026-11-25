# Project Brief

> **SYNTHETIC DEMONSTRATION.** Fictional setting and hypothetical data only. No result in this file is real.

## Question

What is the causal effect of a substantial improvement in public transport access — measured by the opening of new BRT stations — on the **formal employment rate of residents** in served districts of the fictional Rivervale metropolitan area, over 2014–2023?

**Secondary question:** does the effect operate through shorter commutes and better job accessibility, or mainly through residential sorting and employer relocation?

## Why it matters

The fictional Rivervale regional government is deciding whether to extend the BRT network. The policy case assumes that transport access raises employment. That assumption is plausible but not established: stations may be placed where employment was already growing, and workers may move toward stations rather than into work. A credible design would tell the region whether the access improvement itself changes employment, and for whom.

This is a demonstration project. Its purpose in this vault is to show how a research project's memory is structured, recovered, and closed — not to answer the policy question.

## Scope

**In scope**

- Districts of the fictional Rivervale metropolitan area, 2014Q1–2023Q4.
- Openings of BRT stations within the district, staggered across districts and years.
- Formal employment as the primary outcome; commute time, job postings, and entry wages as secondary.
- District-level reduced-form effects.

**Out of scope**

- Individual-level job search behaviour.
- Informal employment as a primary outcome (measurement is not credible in the synthetic registry).
- Cost–benefit analysis of the network, welfare evaluation, or optimal network design.
- Generalising to real cities.

## Mechanisms and hypotheses

| ID | Mechanism | Direction | Status |
|---|---|---|---|
| H-01 | **Job accessibility:** stations shorten travel time to job-dense districts, lowering search and commute costs. | + | untested |
| H-02 | **Labour supply:** lower commute cost raises the effective return to work, especially for second earners. | + | untested |
| H-03 | **Residential sorting:** stations attract new residents, changing district composition rather than employment. | ambiguous for the district rate | untested |
| H-04 | **Firm relocation:** employers move toward stations, so local employment rises while the metro-wide effect is smaller. | + local, ~0 metro | untested |

H-03 and H-04 are the main threats to a causal reading, not side notes.

## Approach

Difference-in-differences with staggered adoption. Treatment cohort = districts whose first BRT station enters revenue service in year *t*. Primary estimand: group-time average treatment effects on the treated, aggregated to an event-study path, using not-yet-treated districts as the comparison group. Naive two-way fixed-effects estimates are reported only as a descriptive benchmark.

1. Assemble a district × quarter panel (24 districts, 40 quarters).
2. Code treatment cohorts from the synthetic implementation timetable.
3. Estimate group-time ATTs with district and quarter fixed effects and district-clustered inference.
4. Run pre-trend and placebo checks; report sensitivity to the treatment definition and to dropping partially served districts.
5. Interpret against H-01 to H-04 without claiming mechanisms the design cannot separate.

Design detail and assumptions: [wiki/difference-in-differences-design.md](wiki/difference-in-differences-design.md). Binding choices: [DECISIONS.md](DECISIONS.md).

## Data and inputs (all hypothetical)

| Input | Needed for | Source or owner | Status |
|---|---|---|---|
| District–quarter formal employment counts and working-age population | Primary outcome | Rivervale Statistical Office (fictional) | not requested |
| BRT station coordinates, planned and actual opening dates | Treatment timing, exposure | Rivervale Transport Authority (fictional) | unavailable |
| District covariates: population, baseline employment rate, median income, distance to CBD | Controls, balance, heterogeneity | Statistical Office (fictional) | not requested |
| Commute-time survey, 2016 and 2022 waves | Mechanism H-01 | Rivervale Mobility Survey (fictional) | unavailable |
| Job postings by district | Mechanism H-04 | Fictional job-board extract | not requested |

No real dataset is used or needed. The data request is a paper exercise to demonstrate how a project records data dependencies.

## Success criteria

- A pre-specified design with an explicit treatment definition, comparison group, and inference strategy.
- A reproducible panel-construction protocol that another analyst could run on the synthetic data.
- A results table that separates the primary estimate from robustness checks, with null and negative results reported.
- An honest limitations section that does not claim mechanisms the design cannot identify.

## Risks and constraints

- **Few clusters:** 24 districts, of which 11 are ever treated. Conventional clustered standard errors may over-reject; inference needs a small-cluster check.
- **Endogenous timing:** rollout may target growing districts. Pre-trends and political-economy covariates are diagnostics, not proof.
- **Treatment definition:** opening the first station is not the same as a usable network. This is unresolved (Q-01).
- **Composition:** district-level rates mix incumbents and newcomers (H-03).
- **No real data:** every quantitative statement must remain a design parameter, not a finding.

## Provenance

**Synthetic.** Created 2026-11-10 for the Second Brain demonstration. Setting, institutions, and data are invented. No real citation is used anywhere in this project.
