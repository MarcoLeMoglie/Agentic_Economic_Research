![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Instructor:** Marco Le Moglie, Catholic University of the Sacred Heart

I teach this to PhD students and faculty in economics. Eight hours, four lessons of two hours, in English, on a video call.

A paper is still the same job: read, get the data in shape, estimate, write, answer the referee. An agent can now take a piece of that job inside the project folder. It opens the files, runs Stata, and changes the line that failed. The course is about that setup. How you point the agent at the right files, what you let it do, and how you check the result before you trust it.

We start with the vocabulary, because the product names change and the pieces underneath do not. A model writes the next bit of text. The harness is the program around it: it holds the conversation, calls tools, and stops when it needs permission. Lesson 1 is those pieces. Context and tokens, and what happens when the window fills. Rules, MCP, and skills. Which model you are calling, what a long run costs, and which data should stay off a consumer chat. The slides are [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf). In class we use [`demos/lesson1`](demos/lesson1): a Stata do-file with a bug left in on purpose, a skill the agent should load when you ask for a regression table, and a short pull of public municipal data through the Cruscotto Italia MCP.

Lesson 2 is how the agent keeps this project the next time you open it. We start from two clips. In the film, JARVIS already knows the workshop and designs the suit with Tony. In the second clip, someone builds that kind of assistant with an AI agent. What used to be science fiction is now a folder of files. A new chat does not have those files, and a long chat buries the decision you need. The lesson then walks through the real choices: paste everything into the prompt, search the documents when a question arrives (RAG), keep a wiki the agent updates, or a hybrid of project files plus search when the sources get large. We build the small version in Obsidian. Ordinary Markdown, four files that say where the project stands, links, a canvas, and Git so every change has a diff. I show the Brain I actually use, including the Sunday pass that checks it, and the rule that I read the diff before a change sticks. The slides are [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf). The synthetic vault, a fake project on education and labour supply, is [`lesson2/obsidian-vault`](lesson2/obsidian-vault). The demo notes are in [`demos/lesson2`](demos/lesson2). In class the demo continues from Lesson 1: the short scripts, the Sportello Italia pull, then filing that project into the vault, and the same folder open in Overleaf, Dropbox, the phone and ChatGPT.

Lesson 3 is automations: the same checks running when you are not in the session. A schedule ingests the notes, updates the project files, and leaves a log. The Sunday pass in Lesson 2 is the picture. The slides are not written yet. The cover is [`assets/covers/03_automation_background.png`](assets/covers/03_automation_background.png).

Lesson 4 is control: how you check the diff, the table and the log before you trust them. Lesson 1 already ends on a table that runs and still needs a reader. This session makes that check a habit. The slides are not written yet. The cover is [`assets/covers/04_control_background.png`](assets/covers/04_control_background.png).

## Overleaf

Overleaf compiles **`main.tex`** at repo root. It inputs Lesson 1.

**Recompile** → `main.pdf`

| Method | Main document | PDF output |
|--------|---------------|------------|
| Default | `main.tex` | `main.pdf` |
| Lesson 1 direct | `lesson1/lesson1.tex` | [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf) |
| Lesson 2 direct | `main_lesson2.tex` | [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf) |
| Lesson 3 cover | `main_lesson3.tex` | [`lesson3/lesson3.pdf`](lesson3/lesson3.pdf) |
| Lesson 4 cover | `main_lesson4.tex` | [`lesson4/lesson4.pdf`](lesson4/lesson4.pdf) |

`main.tex` is a thin Overleaf stub. It compiles Lesson 1. Lessons 3 and 4 are covers only.

## The four lessons

| Lesson | Question | In the repo |
|--------|----------|-------------|
| 1. Vocabulary | What are these things? | [`lesson1/`](lesson1/) |
| 2. Second brain | How do agents remember? | [`lesson2/`](lesson2/) |
| 3. Automations | How do they run without me? | cover only, [`lesson3/`](lesson3/) |
| 4. Control | How do I check their work? | cover only, [`lesson4/`](lesson4/) |

One-page outline: [`syllabus.tex`](syllabus.tex).

## Repository layout

```
Agentic_Economic_Research/
├── main.tex            # Overleaf entry point
├── syllabus.tex        # One-page outline of the 8-hour course
├── assets/             # Banner, lesson covers, and the figures
├── demos/lesson1/      # Folder for the Lesson 1 live demos
├── demos/lesson2/      # Notes for the Lesson 2 demo
├── lesson1/            # Lesson 1 deck
├── lesson2/            # Lesson 2 deck and the synthetic vault
├── lesson3/            # Lesson 3 cover only
└── lesson4/            # Lesson 4 cover only
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

### `lesson2/` — Second brain (hours 3–4)

Theme file is `lesson2/preamble.tex`. It loads the Lesson 1 theme, then the Lesson 2 boxes and the YouTube cards. Image provenance: [`lesson2/sources-and-image-credits.md`](lesson2/sources-and-image-credits.md).

| Path | What it is |
|------|------------|
| `lesson2.tex` | Main Beamer document for Lesson 2. |
| `lesson2.pdf` | Compiled Lesson 2. |
| `preamble.tex` | Lesson 2 additions on top of `lesson1/preamble_v2.tex`. |
| `sections/01_jarvis.tex` | The film clip and the built assistant, then what JARVIS has that a chatbot does not. |
| `sections/02_benefits.tex` | Why a new chat starts from nothing, and what the vault should remember. |
| `sections/03_architectures.tex` | Prompt, RAG, a linked graph, an LLM wiki, and the hybrid we use. |
| `sections/04_obi_build.tex` | The Obsidian vault: files, links, canvas, Git. |
| `sections/05_my_brain.tex` | The Brain I use, the Sunday pass, and the review before a change sticks. |
| `sections/06_appendix.tex` | Sources, the live demo, references. |
| `obsidian-vault/` | Synthetic vault shown in the screenshots. Education and labour supply. Invented. |
| `speaker-notes.md` | Notes for the lecture, in Italian. |
| `REFERENCES.md` | Reading list behind the slides. |

### `assets/`

| Path | What it is |
|------|------------|
| `banner.png` | Header image at the top of this README. Same bottom band as the lesson covers. |
| `covers/` | Full-bleed covers for the four lessons. Lessons 3 and 4 are not taught yet. |
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
