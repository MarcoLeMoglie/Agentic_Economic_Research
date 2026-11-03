# SecondBrain — Lecture Demo

**Synthetic teaching vault; no genuine participant or research data.** Open this folder as a vault in Obsidian or another Markdown editor.

The intentionally imperfect initial state illustrates the *Sunday audit* workflow. Do not import or overwrite any actual Brain documents. Use `bash scripts/setup_git.sh` once to make a local Git baseline, then run `python3 scripts/audit.py` and `python3 scripts/repair_known_demo_issues.py` (only after reviewing its diff).

## Lesson
A fictional municipal project investigates whether better transit access affects employment. The numbers are simulated and have **no empirical meaning**.

## Agent instructions
Start from `general/agent/BOOTSTRAP.md`; end by reading `general/agent/SESSION_CLOSE.md`.

## Demo commands

```bash
bash scripts/setup_git.sh
python3 scripts/audit.py
python3 scripts/validate.py
python3 scripts/repair_known_demo_issues.py
python3 scripts/audit.py
python3 scripts/validate.py
git diff -- areas/Research/transit-employment/
git add general areas && git commit -m "docs: maintenance audit and closeout"
```

The audit should flag the intentionally orphaned wiki note, broken Markdown link and stale project path. After the repair, validation should pass. The source data file remains unchanged.
