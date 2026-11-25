---
title: "{{title}} — Project Index"
type: index
status: active
project: "{{slug}}"
area: "{{area}}"
updated: "{{date}}"
---

# {{title}}

> One sentence: what this project is trying to establish or produce.

**Status:** active · **Owner:** _name_ · **Started:** {{date}} · **Last updated:** {{date}}

## Start here

| Order | File | Read when |
|---|---|---|
| 1 | [PROJECT_BRIEF.md](PROJECT_BRIEF.md) | First contact: question, scope, approach |
| 2 | [CURRENT_STATE.md](CURRENT_STATE.md) | Every session: what is true now |
| 3 | [NEXT_ACTIONS.md](NEXT_ACTIONS.md) | Every session: what to do next |
| 4 | [DECISIONS.md](DECISIONS.md) | Before changing design or scope |
| 5 | [AGENT_MEMORY.md](AGENT_MEMORY.md) | New agent: traps and vocabulary |
| 6 | [TECHNICAL_NOTES.md](TECHNICAL_NOTES.md) | Running commands, data, or code |
| 7 | [SOURCES.md](SOURCES.md) | Making claims that need provenance |
| 8 | [LOG.md](LOG.md) | Recent chronology (last 3 entries only) |
| 9 | [SESSION_SUMMARIES.md](SESSION_SUMMARIES.md) | Recovering continuity |
| 10 | [PROMPTS.md](PROMPTS.md) | Reusing a working prompt |

## Current focus

- _The single most important thing this project is doing right now._
- _The blocking constraint, if any._

## Workspace

- `raw/` — original, unedited sources. See [raw/README.md](raw/README.md) for intake rules.
- `wiki/` — optional long, stable notes; every page must be linked below.
- `skills/` — optional project-local skills, only if they cannot be generalised.

### Wiki pages

_None yet. Add a page only when content is long, stable, and modular, then link it here and remove this line._

## External references

- _Repository, data location, shared drive, ethics approval: where it lives, never a secret._

## Session contract

Boot with the global [BOOTSTRAP protocol](../../../general/agent/BOOTSTRAP.md); close with [SESSION_CLOSE](../../../general/agent/SESSION_CLOSE.md). Run `bash .infra/scripts/validate.sh` from the vault root before finishing.
