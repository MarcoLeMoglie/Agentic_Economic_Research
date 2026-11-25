---
title: Agent Contract
type: protocol
status: active
updated: 2026-11-18
---

# AGENTS.md — Contract for Any AI Agent

This file is the entry point for every agent (Claude, Codex, Gemini, Cursor, local models, or a human with an editor). It is deliberately short. The operational detail lives in [general/agent/BOOTSTRAP.md](general/agent/BOOTSTRAP.md) and [general/agent/SESSION_CLOSE.md](general/agent/SESSION_CLOSE.md).

## On entry

1. Read this file, then [general/INDEX.md](general/INDEX.md), [general/MEMORY.md](general/MEMORY.md), and [general/GLOBAL_DECISIONS.md](general/GLOBAL_DECISIONS.md).
2. Follow [BOOTSTRAP.md](general/agent/BOOTSTRAP.md) exactly: identify one active project, then read only that project's core files.
3. Report what you read, what you believe the state is, and what is uncertain — before doing work.
4. Do not scan unrelated projects, the full `LOG.md`, or every skill. Use metadata and indexes to narrow first.

## While working

- Markdown in this vault is the source of truth. If your context and the files disagree, the files win.
- Never invent facts, data, citations, results, or decisions. Label hypotheses as hypotheses and unknowns as unknowns.
- Write new durable knowledge to the right file as it appears; do not defer everything to the end of the session.
- Dates are ISO (`YYYY-MM-DD`). Links are relative Markdown links.
- Preserve provenance: when a claim comes from a source, name the source file in `SOURCES.md` or in the note itself.
- Do not restructure folders, rename projects, or rewrite protocols without recording a decision in [general/GLOBAL_DECISIONS.md](general/GLOBAL_DECISIONS.md) or the project's `DECISIONS.md`.

## Never

- Never store passwords, API keys, tokens, private credentials, or unnecessary personal data.
- Never paste full conversation transcripts into memory.
- Never edit `raw/` source documents; cite them instead.
- Never present synthetic or illustrative numbers as real findings.
- Never silently resolve a contradiction. Surface it, date it, and record the resolution.

## Skills

Skills are canonical under `general/capabilities/skills/<name>/SKILL.md` and exposed through [.agents/skills/](.agents/skills/). Read only the `name` and `description` metadata when deciding relevance; load the full `SKILL.md` only when the task matches. Do not preload every skill.

Available now: [research-literature-synthesis](general/capabilities/skills/research-literature-synthesis/SKILL.md).

## On exit

Run the close protocol in [SESSION_CLOSE.md](general/agent/SESSION_CLOSE.md): update `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `DECISIONS.md`, `TECHNICAL_NOTES.md`, `AGENT_MEMORY.md`, `LOG.md`, and `SESSION_SUMMARIES.md`. Then run `bash .infra/scripts/validate.sh`. A session that changes nothing durable should still say so explicitly.

## Minimal restart prompt

> Read `AGENTS.md` and `general/agent/BOOTSTRAP.md`. The active project is `areas/Research/public-transport-employment/`. Recover its state, decisions, and next actions, show me which files you read, and wait for instructions.
