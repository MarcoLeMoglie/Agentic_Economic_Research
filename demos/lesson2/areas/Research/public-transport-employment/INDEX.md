---
title: Public Transport and Employment — Project Index
type: index
status: active
project: public-transport-employment
area: Research
updated: 2026-11-18
---

# Does Better Public Transport Increase Employment?

> **SYNTHETIC DEMONSTRATION PROJECT.** Every place, institution, date, and number in this folder is fictional. There are no empirical results and no real citations. Do not reuse this as evidence.

**Question:** What is the causal effect of a large improvement in public transport access — the opening of new bus rapid transit (BRT) stations — on the formal employment rate of residents in served districts of the fictional Rivervale metropolitan area?

**Status:** active, design stage. No data acquired. Two actions open, one question blocking the treatment definition.

## Start here

| Order | File | Read when |
|---|---|---|
| 1 | [PROJECT_BRIEF.md](PROJECT_BRIEF.md) | Question, mechanisms, design, scope |
| 2 | [CURRENT_STATE.md](CURRENT_STATE.md) | What is true now |
| 3 | [NEXT_ACTIONS.md](NEXT_ACTIONS.md) | What to do next |
| 4 | [DECISIONS.md](DECISIONS.md) | Binding design choices |
| 5 | [AGENT_MEMORY.md](AGENT_MEMORY.md) | Traps and vocabulary for a new agent |
| 6 | [TECHNICAL_NOTES.md](TECHNICAL_NOTES.md) | Environment, commands, data conventions |
| 7 | [SOURCES.md](SOURCES.md) | Provenance register |
| 8 | [LOG.md](LOG.md) | Chronology (last 3 entries only) |
| 9 | [SESSION_SUMMARIES.md](SESSION_SUMMARIES.md) | Continuity across sessions |
| 10 | [PROMPTS.md](PROMPTS.md) | Reusable prompts |

## Current focus

- Draft the variable-level data request for the district–quarter panel (A-01).
- Write the pre-analysis specification grid (A-02).
- **Blocked:** final treatment definition — first station opening versus 25% network coverage (Q-01, A-03).

## Workspace

- [raw/README.md](raw/README.md) — intake rules for original sources; currently one synthetic concept note.
- [wiki/difference-in-differences-design.md](wiki/difference-in-differences-design.md) — stable methodological reference for the chosen design.
- `skills/` — none. No project-specific skill is warranted at this stage.

## Wiki pages

- [Difference-in-differences with staggered adoption](wiki/difference-in-differences-design.md) — assumptions, estimator choice, diagnostics, reporting checklist.

The rule that produced this list: core files first, wiki only for long, stable, modular content (see [WIKI_WORKFLOW.md](../../../general/agent/WIKI_WORKFLOW.md)).

## External references

- Synthetic data owner: Rivervale Statistical Office (fictional). No real contact, repository, or dataset exists.
- No ethics approval, funding, or coauthor is real.

## Session contract

Boot with [BOOTSTRAP.md](../../../general/agent/BOOTSTRAP.md); close with [SESSION_CLOSE.md](../../../general/agent/SESSION_CLOSE.md); validate with `bash .infra/scripts/validate.sh` from the vault root.
