---
title: Bootstrap Protocol
type: protocol
status: active
updated: 2026-11-18
---

# BOOTSTRAP — Starting a Session

Run this at the start of every session, before answering substantive questions or editing files. The goal is to recover **just enough** state to work correctly, not to read the vault.

## Step 1 — Read the global layer

Read, in order:

1. [AGENTS.md](../../AGENTS.md) — the contract.
2. [general/INDEX.md](../INDEX.md) — the map.
3. [general/MEMORY.md](../MEMORY.md) — the project router.
4. [general/GLOBAL_DECISIONS.md](../GLOBAL_DECISIONS.md) — constraints that apply everywhere.

Do not read `areas/` yet. Do not open skills. Do not read any `LOG.md`.

## Step 2 — Identify the active project

Use the first signal that is unambiguous:

1. The user names a project, slug, or area.
2. The working directory or an open file is inside `areas/<Area>/<slug>/`.
3. The user's request clearly matches exactly one row in the `MEMORY.md` registry.

If two or more projects could match, **ask** and list the candidates. Do not guess, and do not load both. If nothing matches, say so, show the registry, and ask whether this is a new project (then use the scaffold, not a hand-made folder).

Record the chosen project as the session's scope. Do not widen it silently.

## Step 3 — Read only that project's core files

Read in this order, stopping when the question is answered:

| Order | File | Recover |
|---|---|---|
| 1 | `INDEX.md` | file map, links, optional wiki pages |
| 2 | `PROJECT_BRIEF.md` | question, mechanisms, design, scope |
| 3 | `CURRENT_STATE.md` | what is known, done, blocked |
| 4 | `NEXT_ACTIONS.md` | what to do next, dependencies |
| 5 | `DECISIONS.md` | confirmed choices and rationale |
| 6 | `AGENT_MEMORY.md` | traps, vocabulary, hard constraints |

Read on demand only:

- `TECHNICAL_NOTES.md` — when running commands, debugging, or setting up data.
- `SOURCES.md` — when making a claim that needs provenance.
- `LOG.md` — when you need recent chronology: read the **last 3 entries**, not the file.
- `SESSION_SUMMARIES.md` — the most recent summary only, when continuity is unclear.
- `PROMPTS.md` — when the user asks for a reusable prompt.
- `wiki/*` — only pages linked from `INDEX.md` that the question needs.

**Budget:** about 8 files or 1,500 lines, whichever comes first. If you need more, say why before continuing.

## Step 4 — Recover state, actions, decisions

Write down, in your own words:

- the research/product question,
- what is confirmed versus assumed,
- what is blocked and on what,
- the decisions that constrain the next move,
- the next actions and their done-when conditions.

If a file contradicts another, apply [MEMORY_POLICY.md](MEMORY_POLICY.md): the more recent dated, verified statement wins provisionally; report the conflict; never silently pick one.

## Step 5 — Report before acting

Produce this report (adapt labels, keep the fields):

```markdown
## Session start — <project slug> — <date>

**Question:** one sentence.

**State:** 2–4 sentences: confirmed, in progress, blocked.

**Binding decisions:** D-xxx — one line each, only those that constrain this session.

**Next actions:** A-xx — action — done when …

**Uncertainties / contradictions:**
- what is unknown, conflicting, or stale, and what would settle it.

**Files read:** numbered list of exact paths.

**Scope:** what I will do now, and what I will not touch.
```

Then wait for the user's instruction unless they already gave one. Recovery is not permission to start editing.

## Step 6 — Guardrails

- Do not load other projects, the global log, or full skill texts.
- Do not trust your own memory of a previous session over the files.
- Do not "fix" apparent inconsistencies by deleting text; date and document instead.
- If a referenced file is missing, report it and continue with what exists; do not recreate it from imagination.
- If the vault is empty or the registry is missing, stop and ask — do not invent a structure.

## Degraded mode

If you cannot read files (no filesystem access), say exactly that, ask the user to paste `MEMORY.md` and the active project's `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, and `DECISIONS.md`, and treat everything else as unknown. Never reconstruct state from plausibility.

## Example trigger

> Read `AGENTS.md` and `general/agent/BOOTSTRAP.md`. Active project: `public-transport-employment`. Boot and report.

Expected: the four global files, the project's `INDEX.md`, `PROJECT_BRIEF.md`, `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `DECISIONS.md`, `AGENT_MEMORY.md` — then a session-start report ending in a question or a scope statement.
