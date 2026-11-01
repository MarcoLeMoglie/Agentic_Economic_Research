# Lecture demo: SecondBrain-Lecture-Demo

A small vault for Lesson 2. It is not Marco's Brain. Do not point an agent at the Dropbox Brain folder during class.

## Where it lives

- Seed, scripts, and this readme: `demos/lesson2/` in the course repository.
- Live vault: `~/Documents/SecondBrain-Lecture-Demo`.
- Build it with `bash demos/lesson2/setup_demo.sh`. The script stops if the destination already exists.
- Reset with `bash demos/lesson2/reset_demo.sh`. It checks the `.demo-brain` marker and the folder name, then returns `main` to the tag `pre-audit`.

There is no git remote. To put the vault on GitHub, create an empty private repository and add it yourself. Do not push from the course repository, and do not push unless Marco says so.

## What the agent should find on `main`

The tag `pre-audit` is the state at the start of class. Five defects are on purpose:

1. `wiki/event-study-pitfalls.md` is not in the project index.
2. The state file links to `[[transit-jobs_DECISION]]`, and the decisions file has another name.
3. The 2 September 2026 clustering decision is not marked superseded. The 14 September decision (cluster by district) is the one in force.
4. `wiki/staggered-did.md` and `wiki/staggered-did-notes.md` overlap. The lint report may list this as possible rather than certain.
5. The 28 October coauthor call, including a 2008 placebo, is under `raw/chats/` and is not in the state file.

`python scripts/validate_demo_brain.py` fails on `main` because of the missing index row and the broken link. That failure is the demo.

The branch `final-verified` is the ending if the live agent stalls. It indexes the wiki page, fixes the link, and marks the earlier decision superseded. The overlap in item 4 is still there.

## Numbers that must stay labelled

`code/02_did.py` prints a lecture line: simulated ATT 0.031 (s.e. 0.012). It is not estimated from `data/synthetic_panel.csv`. Callaway and Sant'Anna (2021) is the estimator named in the design note.

`python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py` should exit 0: 400 tracts, 2010 to 2022, no duplicate keys, treatment that stays on once it starts.

## Skills

- `general/capabilities/skills/research-report`
- `general/capabilities/skills/brain-maintenance`
- `areas/Research/transit-jobs/skills/check-synthetic-panel`
- Discovery copies under `.agents/skills/`, which is where Codex and OpenCode look.

Discovery copies live under `.agents/skills/`, which is where Codex and OpenCode look. On 1 November 2026 OpenCode (`glm-5.3-flash-free`, `--pure`) ran the bootstrap, the recall, the panel check, and the audit once. Transcripts and times are in `backup/`. A second pass the same morning stopped because `opencode.ai` did not resolve. Codex was not given the vault.

## Commands that do not need a model

```bash
cd ~/Documents/SecondBrain-Lecture-Demo
python scripts/lint_demo_brain.py
python scripts/validate_demo_brain.py
python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py
python code/02_did.py   # from the project code directory, or the path above
git log --oneline --decorate --graph --all
git diff pre-audit final-verified --stat
```

`02_did.py` lives in `areas/Research/transit-jobs/code/`.

## Sunday schedule

`launchd-example.plist` is an example. It is not loaded. Do not `launchctl load` it on the teaching machine unless you mean to.
