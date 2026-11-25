---
title: Session Close Protocol
type: protocol
status: active
updated: 2026-11-18
---

# SESSION_CLOSE — Leaving the Brain Ready

Run this before ending any session that produced durable knowledge, and always when the user says *close*, *wrap up*, *save memory*, or *hand off*. The test: could a different agent, with a different context window, resume correctly from the files alone?

Do the steps in order. Each maps to one file. Do not create new files to avoid touching existing ones.

## Step 1 — Update current state

`CURRENT_STATE.md`

- Replace the "as of" date with today.
- Move completed items out of "in progress" into "completed", with the date.
- State what is confirmed, what is in progress, what is blocked, and on what.
- Do not append a new state section per session; keep one current picture and let `LOG.md` hold history.

## Step 2 — Update next actions

`NEXT_ACTIONS.md`

- Remove or mark actions that are done (`~~A-01~~ done 2026-11-18`).
- Add new concrete actions discovered this session.
- Each action needs: ID, action, done-when condition, dependency (or `none`), and a date if time-bound.
- Keep the list short (3–7). If it grows, the work is not decomposed enough.
- Never leave "continue working" as an action.

## Step 3 — Record confirmed decisions

`DECISIONS.md`

- Add an entry only for a choice that is **confirmed** and constrains future work.
- Format: ID, date, decision, rationale, alternatives rejected, consequences.
- Ideas, preferences under discussion, and proposed designs go to `NEXT_ACTIONS.md` or `PROJECT_BRIEF.md`, not here.
- If a decision changes an earlier one, mark the old one `superseded by D-xxx`; never delete it.
- If the decision binds the whole vault, also add it to [GLOBAL_DECISIONS.md](../GLOBAL_DECISIONS.md).

## Step 4 — Save technical findings

`TECHNICAL_NOTES.md`

- Exact commands that worked (copy-pasteable), errors and their fixes, environment constraints, data paths and formats.
- One finding per subsection: symptom → cause → fix → verification.
- No secrets, tokens, or connection strings. Record *where* a credential lives, never the value.
- If nothing technical happened, say so in one line instead of padding.

## Step 5 — Update essential agent memory

`AGENT_MEMORY.md`

- This is the briefing for the next agent, not a diary.
- Keep only what a competent newcomer would get wrong without being told: vocabulary, traps, hard constraints, ownership, where things live, what not to touch.
- Remove anything now obvious from the other core files. Target under ~80 lines.
- Update the "last verified" date.

## Step 6 — Add a dated log entry

`LOG.md`

Append, newest entry last (or first — follow the file's existing convention), using:

```markdown
## 2026-11-18 — Short title

**Intent:** what this session was meant to achieve.
**Did:** concrete actions, files changed.
**Learned:** durable findings, with links to the files that now hold them.
**Decided:** D-xxx references, or "none".
**Open:** what remains, with the action ID that covers it.
**Next:** the single most useful next step.
```

Rules: factual, dated, no transcript, no hidden reasoning. If the entry is a demonstration, label it `[DEMO]` in the title.

## Step 7 — Write a session summary

`SESSION_SUMMARIES.md`

- One entry per session, 5–10 lines: goal, outcome, decisions, open threads, where to resume.
- Append at the end (chronological). Do not rewrite old summaries.
- The summary must stand alone: a reader who reads only it should know whether to resume or re-scope.
- Detail stays in the log and the core files; the summary is the index to them.

## Step 8 — Validate, then report

```bash
bash .infra/scripts/validate.sh
```

- Fix errors before finishing. Warnings may be reported and accepted deliberately.
- Report: files changed, validation result, what remains uncertain, and the next action ID.
- If Git is available and the user permits commits, commit with a message naming the project and the durable change. Never push to a remote.

## Definition of done

- [ ] `CURRENT_STATE.md` reflects reality as of today.
- [ ] `NEXT_ACTIONS.md` has 3–7 concrete, testable actions.
- [ ] Every confirmed decision is in `DECISIONS.md` with a date and rationale.
- [ ] Technical findings are reproducible from `TECHNICAL_NOTES.md`.
- [ ] `AGENT_MEMORY.md` is short, current, and free of stale advice.
- [ ] `LOG.md` has a dated entry with intent, actions, learning, open threads.
- [ ] `SESSION_SUMMARIES.md` has a standalone summary.
- [ ] `MEMORY.md` updated only if project status/focus changed.
- [ ] No secrets, credentials, personal data, or transcript dumps were added.
- [ ] Validation passes; remaining warnings are named.

## Anti-patterns

- Rewriting history so the session looks cleaner than it was.
- Saving a chat transcript "just in case".
- Adding a wiki page because the session felt productive.
- Marking an action done without a done-when check.
- Recording a decision the user has not actually confirmed.
- Leaving the only copy of an insight in the conversation.
