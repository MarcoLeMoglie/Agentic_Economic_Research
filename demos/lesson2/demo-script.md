# Demo script, about 25 minutes

Vault: `~/Documents/SecondBrain-Lecture-Demo`, branch `main`, tag `pre-audit`. Reset before class. If a step stalls, `git checkout final-verified` and use the figures in `demos/lesson2/backup/` if they exist. Offline path: Obsidian or a file listing, `git diff`, `validate`. No network required for that path.

The 0.031 line is simulated. Say so if a student treats it as a result.

## 0 to 3 minutes. Open the vault

Show the folder. Open `general/INDEX.md`, then `areas/Research/transit-jobs/transit-jobs_INDEX.md`. If Obsidian opens, show the file explorer, one backlink, the graph, and `paper-map.canvas`. If Obsidian stays on the plugin loader, show the same files in the editor. The canvas is JSON with five cards: Question, Data, Design, Results, Open issues.

Expected: the project index does not list `event-study-pitfalls`.

Plan B: the graph figure in the slides is the July 2026 vault, not this demo.

## 3 to 7 minutes. Bootstrap

Prompt:

```
Read AGENTS.md and follow general/agent/BOOTSTRAP.md for the project transit-jobs. List every file you open, then report state and next action. Do not edit any file.
```

Expected files: `AGENTS.md`, `general/agent/BOOTSTRAP.md`, `general/INDEX.md`, the transit-jobs index, state, next actions, and agent memory.

Expected report: staggered openings, cluster by district since 14 September 2026, simulated ATT 0.031 (s.e. 0.012), next action still open. The state file's wikilink is wrong. The agent may or may not notice yet.

Plan B: read those files yourself and say the four bootstrap items.

## 7 to 10 minutes. Recall

Prompt:

```
Why do we cluster by district? Cite the file and the date. Do not edit files.
```

Expected: `transit-jobs_DECISIONS.md`, decision of 14 September 2026. The 2 September decision, cluster by tract, is the earlier one and is not marked superseded.

Plan B: open the decisions file and read the 14 September entry.

## 10 to 13 minutes. New project

Prompt:

```
Create a project housing-prices in Research using the template and scripts/create_project.py. Add its row to general/MEMORY.md. Show the diff and stop.
```

Expected: new folder `areas/Research/housing-prices/` from the template, and one new row in `general/MEMORY.md`.

Plan B: run `python scripts/create_project.py` yourself if the script's arguments are the ones in its header, show the diff, then `git checkout -- .` and `git clean -fd` before the audit if you do not want this project in the audit diff. Or skip and say the template is the point.

## 13 to 16 minutes. Skill

Prompt:

```
Check the synthetic panel. Use the check-synthetic-panel skill. Report the command and the exit code.
```

Expected: the agent reads `SKILL.md` and runs `check_panel.py`. Exit 0. 400 tracts, 2010 to 2022, no duplicate keys, treatment stays on.

Plan B: run the script in the terminal.

## 16 to 20 minutes. Audit

Prompt:

```
Run the brain-maintenance skill. List certain problems and possible problems separately. Propose fixes. Do not edit until I approve.
```

Approve items 1, 2, and 3: index the pitfalls page, fix the state-file link, mark the 2 September decision superseded. Item 5, the coauthor call, gets one line in `NEXT_ACTIONS`, not a rewrite of the wiki. Leave item 4, the overlapping wiki pages, as a possible item unless the agent has a clear merge and you have time.

Expected files after approval: `transit-jobs_INDEX.md`, `transit-jobs_CURRENT_STATE.md`, `transit-jobs_DECISIONS.md`, `transit-jobs_NEXT_ACTIONS.md`.

Plan B: `git checkout final-verified`.

## 20 to 23 minutes. Diff and commit

```bash
git diff --stat
git diff
python scripts/validate_demo_brain.py
git add -A
git commit -m "audit: index wiki page, fix link, mark superseded decision"
```

Expected: validate passes, or it still warns on the overlap. The prepared branch used the message above.

Plan B: `git diff pre-audit final-verified`.

## 23 to 25 minutes. Close

Prompt:

```
Close the session following general/agent/SESSION_CLOSE.md. Update state, decisions if needed, the log, and next actions. Then stop.
```

Optional: a second agent opens the same folder and repeats the bootstrap. It should report the post-audit state, not the broken link.

Then, after class, `bash demos/lesson2/reset_demo.sh`.
