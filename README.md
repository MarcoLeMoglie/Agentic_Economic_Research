![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Eight-hour course** for PhD students and faculty in economics. Four lessons of two hours, taught remotely in English.

**Instructor:** Marco Le Moglie · Catholic University of the Sacred Heart

This branch, `course-8h`, is the current course. Lesson 1 is in the repo. Lessons 2 to 4 are not written yet. The earlier four-hour mini-course is still here, under `session1/` and `session2/`, as an archive.

## Overleaf

Overleaf compiles **`main.tex`** at repo root by default. Set the session on the `\CompileSession` line (change the number only):

```latex
\newcommand{\CompileSession}{3}  % 1 = old Session 1 | 2 = old Session 2 | 3 = Lesson 1
```

**Recompile** → `main.pdf`

| Method | Main document | PDF output |
|--------|---------------|------------|
| Default (switch in `main.tex`) | `main.tex` | `main.pdf` |
| Lesson 1 direct | `lesson1/lesson1.tex` | `lesson1/lesson1.pdf` |
| Old Session 1 direct | `session1/session1.tex` | `session1/session1.pdf` |
| Old Session 2 direct | `session2/session2.tex` | `session2/session2.pdf` |

`main.tex` is a thin Overleaf stub. Slide content lives under `lesson1/`, `session1/` and `session2/`.

The deck checked into this branch with the latest comment pass is [`lesson1/lesson1-red.pdf`](lesson1/lesson1-red.pdf). New and rewritten lines are in red. A black version comes after that pass is accepted.

## The four lessons

| Lesson | Question | In the repo |
|--------|----------|-------------|
| 1. Vocabulary | What are these things? | [`lesson1/`](lesson1/) |
| 2. Second brain | How do agents remember? | not yet |
| 3. Control | How do I check their work? | not yet |
| 4. Automations | How do they run without me? | not yet |

## Repository layout

```
Agentic_Economic_Research/
├── main.tex                 # Overleaf entry point; switches the deck
├── preamble.tex             # Theme for the archived 4-hour course
├── bibliography.bib         # References for the archived Session 1
├── syllabus.tex             # One-page outline sent for the 8-hour course
├── assets/                  # Banner, old-course figures, lesson 1 figures
├── demos/lesson1/           # Folder for the Lesson 1 live demos
├── recordings/              # Trimmed videos of the 4-hour course
├── lesson1/                 # Lesson 1 of the 8-hour course
├── session1/                # Archived Session 1 (4-hour course)
└── session2/                # Archived Session 2 (4-hour course)
```

## File guide

What each major file is. Not when it was committed.

### Root

| Path | What it is |
|------|------------|
| `main.tex` | Overleaf stub: sets `\CompileSession` and inputs the chosen deck. |
| `preamble.tex` | Beamer preamble for the archived 4-hour course. |
| `bibliography.bib` | BibTeX database for the archived Session 1. |
| `syllabus.tex` | One-page English syllabus for the 8-hour course. |
| `README.md` | This file. |
| `.gitattributes` | Git LFS rules for large video files under `recordings/`. |

### `lesson1/` — Vocabulary (hours 1–2)

Theme file is `lesson1/preamble_v2.tex`, not the root preamble. Sources for figures and numbers: [`assets/lesson1/SOURCES.md`](assets/lesson1/SOURCES.md).

| Path | What it is |
|------|------------|
| `lesson1.tex` | Main Beamer document for Lesson 1. |
| `lesson1-red.pdf` | Compiled Lesson 1 with the latest review pass in red. |
| `lesson1.pdf` | Earlier compile of the same deck. |
| `preamble_v2.tex` | Beamer theme for the 8-hour course: ink `#163A59`, accent `#D97706`, review macro `\rev`. |
| `lesson1.bib` | BibTeX database for Lesson 1. |
| `preflight.sh` | Checks the deck for em dashes, en dashes and numbered section labels. |
| `README.md` | Layout map used while the deck was designed. |
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
| `real/` | Screenshots from the archived Session 1 (Codex, Antigravity, NotebookLM). |
| `mafia-culture/` | Figures for the Mafia Culture slides in archived Session 2. |

### `demos/lesson1/`

Live material for Lesson 1. The slides point here:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/course-8h/demos/lesson1

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
# Lesson 1, from the repo root. The output directory must exist.
mkdir -p /tmp/lesson1
tectonic -X compile main.tex --outdir /tmp/lesson1

# or, with pdflatex
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
bibtex lesson1/lesson1
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
pdflatex -output-directory=lesson1 lesson1/lesson1.tex
```

Docker: `texlive/texlive:latest` if the local TeX is too old.

## Archived four-hour course

Taught as two sessions of two hours. Decks, baselines and recordings stay in the repo. They are not the course this branch opens on.

### `session1/` — concepts and tools

| Path | What it is |
|------|------------|
| `session1.tex` | Main Beamer document for Session 1. |
| `session1.pdf` | Compiled Session 1 slide deck. |
| `sections/00_opening.tex` | Title, roadmap, course scope. |
| `sections/01_why_now.tex` | Why agentic AI matters for research now. |
| `sections/02_concepts.tex` | Core vocabulary: agents, context, tokens, tool use. |
| `sections/03_interfaces.tex` | Desktop apps, IDEs, CLIs, browser tools. |
| `sections/04_cost_privacy.tex` | Pricing, tokens, privacy, institutional constraints. |
| `sections/05_reliability.tex` | Hallucinations, automation bias, verification gates. |
| `sections/06_architecture.tex` | Rules, MCP, memory, skills, hooks, agent loops. |
| `sections/07_case_studies.tex` | Teaser for Session 2 live examples. |
| `sections/08_closing.tex` | Wrap-up, references, GitHub link. |
| `course_abstract_bio_onepage.tex` | One-page course abstract and instructor bio. |
| `OVERLEAF.md` | Overleaf compile notes for Session 1. |

### `session2/` — live demos and case studies

| Path | What it is |
|------|------------|
| `session2.tex` | Main Beamer document for Session 2. |
| `session2.pdf` | Compiled Session 2 slide deck. |
| `BASELINE.md` | Frozen restart point for the Session 2 deck (2026-07-07). |
| `sections/00_opening.tex` | Title and roadmap for the practical session. |
| `sections/03_success_stories.tex` | Live success stories: YouTube, ASSIST, Mafia Culture. |
| `sections/04_brain_and_wip.tex` | Second-brain setup and work-in-progress demo. |
| `sections/05_success_stories_extra.tex` | Additional demos: `/referaggio`, Purge. |
| `OVERLEAF.md` | Overleaf compile notes for Session 2. |

### Baselines

| Session | Baseline | PDF |
|---------|----------|-----|
| 1 | Git `a7f8590` lineage → `session1/` | [`session1/session1.pdf`](session1/session1.pdf) |
| 2 | **Frozen 2026-07-07** → `session2/BASELINE.md` | [`session2/session2.pdf`](session2/session2.pdf) |

### Recordings

| Session | Video | Trim window |
|---------|-------|-------------|
| 1 | [`recordings/session1/session1_trimmed_softsubs.mp4`](recordings/session1/session1_trimmed_softsubs.mp4) | `00:11:20` → `02:19:40` |
| 2 | [`recordings/session2/session2_trimmed_hardsubs.mp4`](recordings/session2/session2_trimmed_hardsubs.mp4) | `00:07:30` → `02:29:23` |

Captions and plain-text transcripts are in the same folders. Details: [`recordings/README.md`](recordings/README.md).

Large `.mp4` files use **Git LFS**. Run `git lfs install` before cloning.

```bash
pdflatex -output-directory=session1 session1/session1.tex
bibtex session1/session1
pdflatex -output-directory=session1 session1/session1.tex
pdflatex -output-directory=session1 session1/session1.tex

pdflatex -output-directory=session2 session2/session2.tex
```

## Licence

Third-party screenshots are used under fair use for non-commercial teaching.
Replace with institutional captures or live demos before public distribution if
required by your institution.
