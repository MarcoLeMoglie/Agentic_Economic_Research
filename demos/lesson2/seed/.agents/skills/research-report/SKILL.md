---
name: research-report
description: Write a one-page status report for a project in this vault. Use when asked for a status report, a research report, or a summary of where a project stands.
---

# Skill: research report

## When to use
The user asks for a status report on a project in this vault.

## Steps
1. Read the project's INDEX, CURRENT_STATE, DECISIONS, and SOURCES.
2. Run `python scripts/write_status_report.py <slug>` from the vault root.
3. Open `reports/<date>-<slug>-status.md` and check that every number names its source file.
4. If a number has no source file, delete that sentence and say it was removed.

## Success
The report exists, the script exits 0, and each figure is tied to a file path.
Do not add numbers that are not already in the vault.
