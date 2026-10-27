![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Eight-hour course** for PhD students and faculty in economics. Four lessons of two hours, taught remotely in English.

**Instructor:** Marco Le Moglie · Catholic University of the Sacred Heart

Lesson 1 is in the repo. Lessons 2 to 4 are not written yet.

## Overleaf

Overleaf compiles **`main.tex`** at repo root. It inputs Lesson 1.

**Recompile** → `main.pdf`

| Method | Main document | PDF output |
|--------|---------------|------------|
| Default | `main.tex` | `main.pdf` |
| Lesson 1 direct | `lesson1/lesson1.tex` | [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf) |

`main.tex` is a thin Overleaf stub. Slide content lives under `lesson1/`.

## The four lessons

| Lesson | Question | In the repo |
|--------|----------|-------------|
| 1. Vocabulary | What are these things? | [`lesson1/`](lesson1/) |
| 2. Second brain | How do agents remember? | not yet |
| 3. Control | How do I check their work? | not yet |
| 4. Automations | How do they run without me? | not yet |

One-page outline: [`syllabus.tex`](syllabus.tex).

## Repository layout

```
Agentic_Economic_Research/
├── main.tex            # Overleaf entry point
├── syllabus.tex        # One-page outline of the 8-hour course
├── assets/             # Banner and the figures used in Lesson 1
├── demos/lesson1/      # Folder for the Lesson 1 live demos
└── lesson1/            # Lesson 1 deck
```

## File guide

What each major file is.

### Root

| Path | What it is |
|------|------------|
| `main.tex` | Overleaf stub. Inputs `lesson1/lesson1.tex`. |
| `syllabus.tex` | One-page English syllabus: four sessions of two hours. |
| `README.md` | This file. |
| `.gitattributes` | Git LFS rules. |

### `lesson1/` — Vocabulary (hours 1–2)

Theme file is `lesson1/preamble_v2.tex`. Sources for figures and numbers: [`assets/lesson1/SOURCES.md`](assets/lesson1/SOURCES.md).

| Path | What it is |
|------|------------|
| `lesson1.tex` | Main Beamer document for Lesson 1. |
| `lesson1.pdf` | Compiled Lesson 1. |
| `preamble_v2.tex` | Beamer theme: ink `#163A59`, accent `#D97706`. |
| `lesson1.bib` | BibTeX database for Lesson 1. |
| `preflight.sh` | Checks the deck for em dashes, en dashes and numbered section labels. |
| `sections/00_opening.tex` | Title, the four lessons, the words for today. |
| `sections/01_chat_to_agent.tex` | Model plus harness, the loop on a real Stata trace, the 2022–2026 timeline, METR time horizon, first live demo. |
| `sections/02_vocabulary.tex` | Prompt vs task, context window, compaction, rules files, permissions, MCP, skills, sub-agents, memory. |
| `sections/03_harnesses.tex` | Five surfaces, chat and the agent merging, the terminal, IDE diffs. |
| `sections/04_models.tex` | Who builds models, one index, intelligence per dollar, OpenRouter traffic, closed and open weights. |
| `sections/05_cost_data_reliability.tex` | Subscription vs API, a cost spike, data risk, reliability words. |
| `sections/06_closing.tex` | One-line glossary, the Cruscotto Italia live exercise, homework, references. |

### `assets/`

| Path | What it is |
|------|------------|
| `banner.png` | Header image at the top of this README. |
| `lesson1/screens/` | Screenshots and vendor images used in Lesson 1. |
| `lesson1/charts/data/` | CSV behind the pgfplots charts. |
| `lesson1/traces/` | Real agent logs and the table the agent wrote. |
| `lesson1/files/` | `AGENTS.md` and `SKILL.md` excerpts shown on slides. |
| `lesson1/SOURCES.md` | Origin and date of every Lesson 1 number and image. |
| `real/` | Interface screenshots reused in Lesson 1, including Antigravity. |

### `demos/lesson1/`

Live material for Lesson 1. The slides point here:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/main/demos/lesson1

| Path | What it is |
|------|------------|
| `README.md` | What each demo does, and what to have installed. |
| `AGENTS.md` | Rules file the agent reads at the start of a session. |
| `code/analysis.do` | Stata do-file with a deliberate bug (`ln(prise)`). Do not fix it before class. |
| `data/auto.dta` | Stata's `auto` dataset, the input to that do-file. |
| `.agents/skills/regression-table/SKILL.md` | Skill the agent should load when asked for a regression table. |
| `output/` | Where the agent writes the table. Empty in the repo. |

## Local build

```bash
# From the repo root. The output directory must exist.
mkdir -p /tmp/lesson1
tectonic -X compile main.tex --outdir /tmp/lesson1

# or, with pdflatex
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
bibtex lesson1/lesson1
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
```

Docker: `texlive/texlive:latest` if the local TeX is too old.

## Licence

Third-party screenshots are used under fair use for non-commercial teaching.
Replace with institutional captures or live demos before public distribution if
required by your institution.
