# Second Brain

This folder is the Lesson 2 demo in the course repository. Open it as its own vault. The project inside is synthetic.

A local-first, Obsidian-compatible knowledge base designed to be read and written by **any** AI agent. Markdown files are the memory; no database, cloud service, API key, or paid product is required.

This vault is also a working demonstration: it contains a fully synthetic research project so you can watch an agent recover state, make decisions, and close a session without rereading an entire chat history.

## Open it

- **Obsidian:** *Open folder as vault* → select this folder.
- **Any AI agent:** point it at this folder and say *"Read AGENTS.md and bootstrap."*
- **Humans:** start at [general/INDEX.md](general/INDEX.md).

## The three layers

| Layer | Holds | Canonical? |
|---|---|---|
| `general/` | Global memory, routing, agent protocols, decisions, templates, reusable skills | Yes |
| `areas/` | Project-specific knowledge and memory, grouped by area | Yes |
| `.infra/` | Optional scripts that check the memory, not memory itself | No |

`.agents/skills/` is a thin discovery adapter: it exposes the skills stored under `general/capabilities/skills/` to agent runtimes that scan `.agents/skills/`. The skill text lives in exactly one place.

## Map

| File | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | Contract every agent must accept before touching the vault |
| [general/INDEX.md](general/INDEX.md) | Global map: what exists, what to read, in which order |
| [general/MEMORY.md](general/MEMORY.md) | Compact project router — the only global file that changes often |
| [general/GLOBAL_DECISIONS.md](general/GLOBAL_DECISIONS.md) | Decisions that apply to the whole Brain |
| [general/agent/BOOTSTRAP.md](general/agent/BOOTSTRAP.md) | Start-of-session protocol |
| [general/agent/SESSION_CLOSE.md](general/agent/SESSION_CLOSE.md) | End-of-session protocol |
| [general/agent/MEMORY_POLICY.md](general/agent/MEMORY_POLICY.md) | What may be written, by whom, and how conflicts are resolved |
| [general/agent/WIKI_WORKFLOW.md](general/agent/WIKI_WORKFLOW.md) | Ingest, query, lint, promote — the LLM Wiki loop |
| [general/templates/](general/templates/) | The 11 project files, prefixed `project-slug-` |
| [general/capabilities/skills/](general/capabilities/skills/) | Canonical, portable skills |
| [areas/INDEX.md](areas/INDEX.md) | Area routing |
| [example project](areas/Research/public-transport-employment/INDEX.md) | Synthetic worked example |

## The loop

```text
session start  -> BOOTSTRAP.md   -> read router, one project, report state
work           -> project files  -> update facts in place, log decisions
session close  -> SESSION_CLOSE.md -> state, actions, decisions, log, summary
maintenance    -> WIKI_WORKFLOW.md -> lint links, promote stable knowledge
```

## Project anatomy

Every project is a folder under `areas/<Area>/<slug>/` containing exactly these core files:

`INDEX.md`, `PROJECT_BRIEF.md`, `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `AGENT_MEMORY.md`, `DECISIONS.md`, `TECHNICAL_NOTES.md`, `SOURCES.md`, `LOG.md`, `PROMPTS.md`, `SESSION_SUMMARIES.md`.

Optional, only when useful: `raw/` (source documents), `wiki/` (long stable notes linked from `INDEX.md`), `skills/` (project-local skills).

## Commands

```bash
# check structure, links, registration, wiki indexing
bash .infra/scripts/validate.sh

# scaffold a new project from the templates (slug: lowercase-with-dashes)
bash .infra/scripts/new-project.sh Research my-new-project "My New Project"
```

`new-project.sh` does not edit [general/MEMORY.md](general/MEMORY.md) or the area index; it prints the two lines you must add. Registration stays a deliberate human act.

## Rules that make it portable

1. Plain Markdown, UTF-8, ISO dates (`YYYY-MM-DD`). Do not open a note with a YAML property block.
2. Relative Markdown links (`[text](../path/file.md)`), not Obsidian-only `[[wikilinks]]`, so the vault renders on GitHub and in any editor.
3. No secrets, credentials, API keys, or full chat transcripts. See [MEMORY_POLICY.md](general/agent/MEMORY_POLICY.md).
4. One project per session unless the user explicitly expands scope.
5. Verified Markdown outranks any agent's recollection. External memory tools are optional mirrors, never the source of truth.
6. Skills are discovered by metadata (name + description) and loaded in full only when the task matches.

## Scope of this demo

All research content in the example project is **fictional and synthetic**. It contains no empirical estimates and no real citations. It exists to demonstrate memory structure, not to make scientific claims.
