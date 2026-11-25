---
title: "{{title}} — Prompts"
type: prompts
status: active
project: "{{slug}}"
updated: "{{date}}"
---

# Reusable Prompts

Prompts that worked, parameterised with `<angle-bracket>` slots. Keep the reason each one exists, and the failure mode it avoids.

## Boot this project

> Read `AGENTS.md` and `general/agent/BOOTSTRAP.md`. Active project: `{{slug}}`. Recover the question, current state, decisions, and next actions. Show which files you read and do not start work until I confirm.

## Session close

> Follow `general/agent/SESSION_CLOSE.md` for `{{slug}}`. Update state, actions, decisions, technical notes, agent memory, log, and summaries. Run validation and report what changed.

## Critique the current design

> Read `PROJECT_BRIEF.md`, `CURRENT_STATE.md`, and `DECISIONS.md` for `{{slug}}`. Identify the three strongest threats to the design, rank them, and propose a test for each. Do not propose new scope.

## Draft a section

> Using only verified material in this project, draft `<section>`. Mark every claim with its source ID, mark inferences as inferences, and list what is missing.
