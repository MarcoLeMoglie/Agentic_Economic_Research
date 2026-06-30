![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Four-hour mini-course** for PhD students and faculty in economics: agentic AI
vocabulary, tool landscape, research workflows, and responsible use.

**Instructor:** Marco Le Moglie · Catholic University of the Sacred Heart  
**Format:** two sessions of two hours each  
**This repository:** Session 1 deck (hours 1–2 — concepts, interfaces,
governance, architecture). Session 2 (hours 3–4 — applied case studies from
live research workflows) is planned as a separate deck.

## What is inside

- Beamer slide source (`main.tex` + `sections/00`–`08`)
- Custom theme: deep blue `#163A59` + accent orange `#D97706`
- Real screenshots, charts, and a BibTeX bibliography with sourced claims
- Project notes in the Marco Brain vault:
  `Desktop/Marco/Brain/Marco/02_AREAS/Teaching/AI_course/`

## Compiled deck

Pre-built slide PDF (Session 1): [`Agentic_Economic_Research.pdf`](Agentic_Economic_Research.pdf) — regenerate with the build steps below.

## Build

Compile on **Overleaf** with **pdflatex** (recommended). Local build:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Layout

```
main.tex            entry point (\input each section)
preamble.tex        custom Beamer theme
bibliography.bib    cited sources
sections/           one file per block (00..08)
assets/
  banner.png        repository header image
  real/             product screenshots
  charts/           data-backed figures
  icons/            theme icons
  legacy/           v1 reference materials
```

## Workflow

- Block-by-block writing with Marco's review between blocks.
- Quality gates: `tools/prose-check` (Slopless + Vale) and the `bugbot`
  subagent per block.
- One `feat(block-N): ...` commit per block on `main`.
- Release tags: `v1.0` (Session 1 baseline).

## Project memory

Canonical project state lives in the **Marco Brain** Obsidian vault
(`02_AREAS/Teaching/AI_course/`). Active memory layers: **memanto** (long-term
decisions) and **hivemind** (session capture). Markdown in the vault is the
source of truth for scope, decisions, and next actions.

## Licence

Third-party screenshots are used under fair use for non-commercial teaching.
Replace with institutional captures or live demos before public distribution if
required by your institution.
