# Lesson 2: live-demo guide (25 minutes)

The `demo_brain/` folder in the ZIP is a **fully synthetic** Obsidian vault. It includes a fictional transit-employment study and a local Git repository tagged `demo-baseline`. It does not access the user's real Brain.

## 0. Preflight (before class)

1. Copy the folder to `~/Documents/SecondBrain-Lecture-Demo` if that path is available, otherwise use a unique safe new path.
2. Open the folder from Obsidian **Open folder as vault**. This is not a copy of the actual Dropbox Brain.
3. Run: `bash scripts/setup_git.sh` (a no-op if the provided `.git` history is already intact).
4. Run `python3 scripts/audit.py` and confirm exactly three deliberately seeded problems: unindexed wiki page, broken Markdown link, stale path.
5. Confirm no Git remote is configured: `git remote -v` should produce no remote lines.
6. Open your locally available AI agent in **this new folder**, not the real Brain; supply the bootstrap path and read-only permission initially.
7. Have the PDF and notes open in another window and keep `git status` visible.

## 1. Demo script by minute

### 0–3: Open the Brain

Show the actual synthetic files in Obsidian. Start at `general/INDEX.md` and open `areas/Research/transit-employment/transit-employment_INDEX.md`. Show the backlinks from `identification.md`. Highlight Markdown as source of truth.

### 3–7: Bootstrap

Prompt: `Read general/agent/BOOTSTRAP.md and then reconstruct the state of the transit-employment demo. Read only the needed files. Do not modify anything.`

Expected: The agent identifies a **synthetic** panel, unverified pretrend assumptions, and validation as the next action.

### 7–10: Recover a past choice

Prompt: `What was the 2026-10-22 rule on using the data, and where is it recorded? Cite the exact project file.`

Expected: No simulated numbers may be represented as observed facts, with citation to DECISIONS.

### 10–13: Create a project

Prompt: `Within this synthetic vault only, propose a second teaching project, with PROJECT_BRIEF, CURRENT_STATE, NEXT_ACTIONS and DECISIONS. Show your planned filenames before writing.`

Human reviews the new tree. If no agent access, demonstrate a static template instead.

### 13–16: Trigger skill

Prompt: `Find the dataset-audit skill. Read its SKILL.md only when activated, execute the script and summarize the output.`

Use `python3 scripts/audit_dataset.py` if needed. It writes `outputs/dataset-audit.md` labeled SIMULATED DATA.

### 16–20: Audit

Prompt: `Perform a read-only audit. Find orphaned wiki files, broken links and stale locations; show proposed minimal edits, no destructive changes.`

Run `python3 scripts/audit.py` (non-zero status is expected before fixes). Then review and optionally run `python3 scripts/repair_known_demo_issues.py` to apply the three known synthetic repairs.

### 20–23: Git diff / validate

Run `git diff`, `python3 scripts/audit.py`, `python3 scripts/validate.py`. If correct, commit locally: `git add general areas && git commit -m 'docs: approved demo audit'`. No remote push.

### 23–25: Closeout

Prompt: `Read SESSION_CLOSE.md; record a concise closeout summary of verified changes. Show the diff before any write. Do not claim any synthetic result is real.`

Explain the next agent can restart from core state + approved decisions without full chat history.

## 2. Reset

To prepare for another demo, run `bash scripts/reset_demo.sh`. It requires typing `RESET-DEMO` and only resets the included **synthetic demo repository**. Check directory before running. It reverts committed files back to `demo-baseline` and removes the generated audit report. It never writes to Dropbox.

If the presenter commits further changes, the baseline tag remains the explicit source state. A full re-extraction of the ZIP is a safe alternative.

## 3. Emergency fallback

- If an AI agent cannot see the folder, show the bootstrap path in Obsidian and read the file roles directly.
- If the audit is slow, run the deterministic `scripts/audit.py` and discuss the three findings.
- If Git is unavailable, use the included before/after examples from README and the planned diff in the script.
- If Internet is unavailable, the workflow still works locally; only the interactive agent response may be missing.

## 4. Files and security

No external services, schedules or connections are installed. No GitHub remote is configured. All examples are synthetic. Run scripts only after verifying the working directory is the demo vault. If you need an actual private GitHub remote, configure it manually after reviewing all files and permissions.
