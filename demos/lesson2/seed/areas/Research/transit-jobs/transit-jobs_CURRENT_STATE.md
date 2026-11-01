---
type: project-state
project: transit-jobs
updated: 2026-10-30
status: active
---

# Current state

Last updated: 2026-10-30.

## Design
Staggered station openings. The estimator named in the design note is Callaway and Sant'Anna (2021), which allows treatment to turn on at different dates. The code that would run it is not in this vault. `code/02_did.py` only prints a fixed lecture line.

## Data
Synthetic panel, 400 tracts, 2010 to 2022. Seed 2026. File: `data/synthetic_panel.csv`. Treatment is absorbing: once a tract is treated it stays treated.

## Lecture reporting line
Simulated ATT 0.031 (s.e. 0.012). Labelled as simulated. Not estimated from the CSV. Not a result about any real city.

## Clustering
In force since 14 September 2026: cluster by district, not tract. See [[transit-jobs_DECISION]].

## What runs
`skills/check-synthetic-panel` checks the CSV. It does not estimate a treatment effect.
