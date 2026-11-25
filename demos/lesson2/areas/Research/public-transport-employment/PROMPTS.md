---
title: Public Transport and Employment — Prompts
type: prompts
status: active
project: public-transport-employment
updated: 2026-11-18
---

# Reusable Prompts

Parameterised prompts that worked in this project. Keep them short; the protocol files carry the detail.

## Boot and recover

> Read `AGENTS.md` and `general/agent/BOOTSTRAP.md`. Active project: `public-transport-employment`. Recover the research question, current state, binding decisions, and next actions. Show me every file you read, flag any contradiction, and do not start work until I confirm.

*Use when:* a fresh agent or a new context window resumes the project. *Avoids:* reading the whole vault, or improvising state from model memory.

## Critique the design

> Read `PROJECT_BRIEF.md`, `CURRENT_STATE.md`, and `DECISIONS.md` for `public-transport-employment`. Identify the three strongest threats to the design, rank them by how much they would change the conclusion, and propose one diagnostic for each. Do not propose new scope and do not invent results.

*Use when:* stress-testing D-001 to D-003. *Avoids:* generic methodology commentary that ignores this project's constraints.

## Draft the data request (A-01)

> Using only the variable list and conventions in `TECHNICAL_NOTES.md` and the data needs in `PROJECT_BRIEF.md`, draft a one-page data request for the fictional Rivervale Statistical Office. Include units, coverage (2014Q1–2023Q4), format, missing-value convention, and the residence/workplace question (Q-03). Mark every field that cannot be specified until the data dictionary arrives. Save it under `raw/` and register it in `SOURCES.md`.

*Use when:* turning the design into an intake document. *Avoids:* requesting variables the design does not use.

## Specification grid (A-02)

> Build the pre-analysis grid for `public-transport-employment`: rows are 6–9 specifications, columns are treatment definition, comparison group, event window, and label (primary / robustness). The primary specification must use the working treatment definition and not-yet-treated comparisons. Flag the column that depends on A-03. Do not estimate anything.

*Use when:* freezing the analysis before data arrives. *Avoids:* post hoc specification search.

## Session close

> Follow `general/agent/SESSION_CLOSE.md` for `public-transport-employment`. Update state, actions, decisions, technical notes, agent memory, log, and summaries. Run `bash .infra/scripts/validate.sh` and report exactly what changed and what remains uncertain.

*Use when:* ending any session that produced durable knowledge.
