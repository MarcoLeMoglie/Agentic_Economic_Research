# Global Index

The map of the Brain. Read this after [AGENTS.md](../AGENTS.md), then read [MEMORY.md](MEMORY.md) to find the active project.

## Reading order for a new session

1. [AGENTS.md](../AGENTS.md) — the contract.
2. This index — what exists and where.
3. [MEMORY.md](MEMORY.md) — the compact project router.
4. [GLOBAL_DECISIONS.md](GLOBAL_DECISIONS.md) — constraints that apply everywhere.
5. [agent/BOOTSTRAP.md](agent/BOOTSTRAP.md) — the exact start protocol.
6. Only then: the active project's `INDEX.md` and its core files.

## Global files

| File | What it is | Read when |
|---|---|---|
| [MEMORY.md](MEMORY.md) | Registry of projects + standing global facts. Index only, never a dump. | Every session |
| [GLOBAL_DECISIONS.md](GLOBAL_DECISIONS.md) | Dated decisions binding on the whole vault | Every session, or before structural changes |
| [agent/BOOTSTRAP.md](agent/BOOTSTRAP.md) | Session-start protocol and read budget | Every session |
| [agent/SESSION_CLOSE.md](agent/SESSION_CLOSE.md) | Session-end protocol and definition of done | Before ending work |
| [agent/MEMORY_POLICY.md](agent/MEMORY_POLICY.md) | Authority, write rules, privacy, conflicts, staleness | Before writing memory; when sources disagree |
| [agent/WIKI_WORKFLOW.md](agent/WIKI_WORKFLOW.md) | Ingest, query, lint, promotion | When knowledge must be distilled or promoted |

## Capabilities

- Canonical skills: [capabilities/skills/](capabilities/skills/) — currently [research-literature-synthesis](capabilities/skills/research-literature-synthesis/SKILL.md).
- Discovery adapter: [.agents/skills/](../.agents/skills/) — a symlink to the canonical skill folder, for runtimes that scan `.agents/skills/`.
- Skill loading rule: read `name` + `description`; load the body only when the task matches.

## Templates

[general/templates/](templates/) holds the 11 project files, each named `project-slug-*.md`. Instantiate them with [.infra/scripts/new-project.sh](../.infra/scripts/new-project.sh), which strips the `project-slug-` prefix and fills `{{slug}}`, `{{title}}`, `{{area}}`, `{{date}}`. Templates are scaffolding, not memory: they are excluded from link validation.

## Areas and projects

| Area | Index | Projects |
|---|---|---|
| Research | [areas/Research/INDEX.md](../areas/Research/INDEX.md) | 1 active |
| Teaching | [areas/Teaching/INDEX.md](../areas/Teaching/INDEX.md) | 0 |
| Personal | [areas/Personal/INDEX.md](../areas/Personal/INDEX.md) | 0 |

Full routing table: [MEMORY.md](MEMORY.md).

## Conventions

**File names** — `SCREAMING_SNAKE_CASE.md` for the 11 core project files; `kebab-case.md` for wiki pages, raw notes, skills, and folders. Project folder = slug, lowercase kebab-case.

**Dates** — ISO 8601, never `11/18/26`. Use `YYYY-MM-DD` in headings, tables, and prose.

**Links** — relative Markdown links only. No `[[wikilinks]]`, no absolute paths, no links to files outside the vault. Link text should name the destination.

**Uncertainty** — mark with an explicit block:

```markdown
> [!warning] Unresolved
> Claim, why it is uncertain, and what would settle it.
```

**Contradictions** — never delete the losing claim. Record both, date the resolution, and link the evidence.

## Maintenance

- Update [MEMORY.md](MEMORY.md) only when a project is added, archived, or its status/focus changes.
- Run `bash .infra/scripts/validate.sh` before every commit and at the end of every session.
- Full lint (duplicates, stale claims, promotion candidates) follows [WIKI_WORKFLOW.md](agent/WIKI_WORKFLOW.md), at least monthly.
