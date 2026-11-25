---
title: Global Memory Router
type: memory
status: active
updated: 2026-11-18
---

# Global Memory — Project Router

**This is an index, not a knowledge dump.** Keep it under ~120 lines. Process knowledge belongs in the protocols, project knowledge in `areas/`, binding constraints in [GLOBAL_DECISIONS.md](GLOBAL_DECISIONS.md). Add a project row only when the project is created; update a row only when its status or focus changes.

## Active projects

| Project | Area | Slug | Entry point | Status | Current focus | Updated |
|---|---|---|---|---|---|---|
| Does Better Public Transport Increase Employment? | Research | public-transport-employment | [INDEX](../areas/Research/public-transport-employment/INDEX.md) | active | Fix treatment definition; draft data request | 2026-11-18 |

Status vocabulary: `active` (work in progress), `paused` (resumable, no current work), `archived` (read-only, kept for provenance), `seed` (brief only, not yet started).

## Standing global facts

- Vault root: `demos/lesson2/` in the course repository.
- Markdown is canonical. There is no database, vector store, MCP server, or paid API in the stack.
- Global protocols: [BOOTSTRAP](agent/BOOTSTRAP.md), [SESSION_CLOSE](agent/SESSION_CLOSE.md), [MEMORY_POLICY](agent/MEMORY_POLICY.md), [WIKI_WORKFLOW](agent/WIKI_WORKFLOW.md).
- The example research project is **synthetic**. It has no real data, results, or citations.
- Skills live once, in `general/capabilities/skills/`; `.agents/skills/` only mirrors them for discovery.

## Standing preferences

- Answer in the user's language; write vault content in English unless the project says otherwise.
- Be explicit about what was read, what was inferred, and what remains unknown.
- Prefer small, dated edits to one canonical file over duplicated summaries.
- Ask before restructuring folders, renaming projects, or expanding session scope.
- End every work session with the close protocol; never leave state only in chat.

## Global open questions

- Should the Brain keep a single `areas/Personal/` area, or split it once a second personal project appears? (Revisit at 2+ projects.)
- Should archived projects keep their `wiki/` pages, or promote stable pages to `general/`? (Revisit when a page is reused by a second project.)

## Not stored here

Project state, decisions, sources, technical findings, session logs, and prompts. Those belong to the project that owns them. If you are tempted to write a paragraph here, it almost certainly belongs in a project file or in a protocol instead.
