---
title: Research
type: index
status: active
updated: 2026-11-18
---

# Research

Empirical work, grants, papers, replication packages, and methodological notes.

## Projects

| Project | Slug | Status | Current focus | Entry point |
|---|---|---|---|---|
| Does Better Public Transport Increase Employment? | public-transport-employment | active | Treatment definition; data request | [INDEX](public-transport-employment/INDEX.md) |

The row above is mirrored in [general/MEMORY.md](../../general/MEMORY.md). Update both when status or focus changes.

## Adding a project

```bash
bash .infra/scripts/new-project.sh Research <slug> "<Title>"
```

Then register it here and in [general/MEMORY.md](../../general/MEMORY.md), fill `PROJECT_BRIEF.md`, and set two or three actions in `NEXT_ACTIONS.md`.

## Area conventions

- Project folders are kebab-case slugs, stable forever; rename only with a recorded decision.
- Cite sources through each project's `SOURCES.md`. Never cite from memory.
- Synthetic or demonstration projects must say so in their `INDEX.md` and `PROJECT_BRIEF.md`.
- Methodological notes that are reused across projects should become a skill under [general/capabilities/skills/](../../general/capabilities/skills/), not a shared wiki folder.
