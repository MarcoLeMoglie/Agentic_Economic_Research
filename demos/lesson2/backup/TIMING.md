# OpenCode runs, 1 November 2026

Model: `opencode/glm-5.3-flash-free`. Flag `--pure --auto`. Vault: `~/Documents/SecondBrain-Lecture-Demo` on `main` at `pre-audit`. No files were edited. `git status` was clean after both runs.

## Run 1, network up

| Step | Clock | Exit |
|---|---|---|
| Bootstrap | 09:38:39 to 09:39:16 | 0 |
| Recall | 09:39:29 to 09:39:45 | 0 |
| Panel skill | 09:39:45 to 09:40:01 | 0 |
| Audit, propose only | 09:40:01 to 09:40:31 | 0 |

Bootstrap opened AGENTS.md, BOOTSTRAP.md, MEMORY.md, and the four project files. It reported the simulated ATT 0.031 and noticed the broken wikilink. It also said the 2 September tract rule was superseded. The decisions file still marks that rule in force. The audit step got this right.

Recall cited `transit-jobs_DECISIONS.md`, 14 September 2026, and made the same supersede mistake.

The skill loaded `check-synthetic-panel`. `python` is not on PATH (exit 127). `python3` exited 0: 400 tracts, 2010 to 2022, 0 duplicate keys, absorbing treatment.

The audit listed certain items 1 to 3 (unindexed wiki page, broken link, unmarked superseded decision) and possible items 4 and 5 (overlap, Jaccard 0.59, and the 2008 placebo still only in raw). It waited for approval.

## Run 2, network down

Bootstrap 09:43:20 and audit 09:49:13 both died with `ENOTFOUND opencode.ai` / connection refused. The model read some files and then stopped. This is not a second successful pass.

Codex was not driven. The ChatGPT app was open; it was not given the vault.
