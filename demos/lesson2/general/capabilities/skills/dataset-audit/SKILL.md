---
name: dataset-audit
description: Audit a synthetic municipal panel used for the lecture; generate counts, missingness, and an output Markdown report.
---
# Dataset Audit

## When to use
A user requests verification of the transit-employment demo dataset. Do not use this skill for genuine academic data.

## Steps
1. Check dataset path: `areas/Research/transit-employment/data/simulated_panel.csv`.
2. Run `python3 scripts/audit_dataset.py` from the demo vault root.
3. Read `outputs/dataset-audit.md` and confirm it identifies the data as fictional.
4. If checks fail, report the issue rather than altering raw rows.

## Output
A reproducible Markdown report containing sample size, ranges, null counts and a synthetic-data warning.
