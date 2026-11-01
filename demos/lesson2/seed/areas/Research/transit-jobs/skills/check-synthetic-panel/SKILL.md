---
name: check-synthetic-panel
description: Check the synthetic census-tract panel for the transit-jobs project. Use when asked to check the panel, validate the dataset, or audit data/synthetic_panel.csv.
---

# Skill: check the synthetic panel

## When to use
The user asks to check, validate, or audit the transit-jobs panel.

## Input
`areas/Research/transit-jobs/data/synthetic_panel.csv`

## Steps
From the vault root, run:

```bash
python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py
```

## Output
Four lines: tracts, years, duplicate keys, treatment rule.

## Success
Exit code 0, and all four checks say ok.
A failure is a data error, not something to smooth over.
