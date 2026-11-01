---
name: brain-maintenance
description: Audit this demo vault for unindexed wiki pages, broken wikilinks, superseded decisions, overlapping notes, and raw notes not yet distilled. Use when asked to maintain, lint, or audit the brain.
---

# Skill: brain maintenance

A short version of a weekly vault review. Nothing is deleted.

## Steps
From the vault root:

```bash
python scripts/lint_demo_brain.py
```

The report splits **certain** errors from **possible** anomalies.
Show both to the user. Do not edit until the user names the items to apply.

Then, only for approved item numbers:

```bash
python scripts/lint_demo_brain.py --apply 1,2,3 --distill 5
python scripts/validate_demo_brain.py
```

## Success
`validate_demo_brain.py` exits 0 after the approved edits, and `git diff` shows only those edits.
