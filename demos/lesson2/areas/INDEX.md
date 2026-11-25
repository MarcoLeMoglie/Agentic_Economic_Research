---
title: Areas
type: index
status: active
updated: 2026-11-18
---

# Areas

Projects are grouped by area so that the router stays short and domains stay separable.

| Area | Index | Purpose |
|---|---|---|
| Research | [Research/INDEX.md](Research/INDEX.md) | Papers, grants, empirical work, replication |
| Teaching | [Teaching/INDEX.md](Teaching/INDEX.md) | Courses, lectures, materials, supervision |
| Personal | [Personal/INDEX.md](Personal/INDEX.md) | Personal projects and life administration |

Global navigation: [general/INDEX.md](../general/INDEX.md) · Registry: [general/MEMORY.md](../general/MEMORY.md).

## Rules

1. A project is a folder `areas/<Area>/<slug>/` with all 11 core files. Scaffold it with `bash .infra/scripts/new-project.sh <Area> <slug> "<Title>"`.
2. One project, one memory. Do not mix two projects in one folder, and do not store project state in this index.
3. Registration is deliberate: add the project to the area index **and** to [general/MEMORY.md](../general/MEMORY.md) (the validator checks both directions).
4. Areas are not tags. If a project genuinely belongs to two areas, choose the primary one and link across; do not duplicate the folder.
5. Archive, do not delete. Set `status: archived` in project frontmatter and in the registry; keep the history.
