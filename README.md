![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Instructor:** Marco Le Moglie, Catholic University of the Sacred Heart

I teach this to PhD students and faculty in economics. Three lessons of two hours, in English, on a video call.

A paper is still the same job: read, get the data in shape, estimate, write, answer the referee. An agent can take a piece of that job inside the project folder. It opens the files, runs Stata, and changes the line that failed. The course is how you point it at the right files, what you let it change, and how you check the result.

**Lesson 1. Vocabulary.** We start here because the names of the products change faster than the pieces. A model writes the next bit of text. The harness holds the conversation, calls tools, and stops when it needs permission. The lesson covers context and a full window, rules, MCP, skills, which model you are calling, what a long run costs, and which data should stay off a consumer chat. In class there is a Stata do-file with a bug left in on purpose, a skill the agent should load for a regression table, and a short pull of public municipal data. Slides: [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf). Files for class: [`demos/lesson1`](demos/lesson1).

**Lesson 2. Second brain.** A new chat does not have the decision from last time. We start from two clips: an assistant that already knows the workshop, and someone building that kind of assistant from files. Then the options that exist now. Paste the project into the prompt, search the documents when a question arrives, keep a wiki the agent updates, or keep the project files and search when the pile gets large. We build the small version in Obsidian. I show the vault I use, and the rule that I read the diff before a change sticks. Slides: [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf). The vault in the repo is invented, a project on education and labour supply: [`lesson2/obsidian-vault`](lesson2/obsidian-vault). The class demo continues from Lesson 1 into that vault. Notes: [`demos/lesson2`](demos/lesson2).

**Lesson 3. Automations and control.** A schedule, an event, or a condition can start a script or an agent when you are not in the session. You decide first which computer runs the job and what it may change without asking. A newsletter already works this way: it collects candidate papers, waits for an editorial check, and sends only after an explicit release. The same session is the check. A message that the agents are done is not the check. You put the source next to the value taken from it, you read the diff, and a second pass lists what still disagrees. One project in the lesson corrects figures read from the 1940 census. A study of analysts keeps a randomized effect on judgment separate from a descriptive difference in error rates. Slides: [`lesson3/lesson3.pdf`](lesson3/lesson3.pdf).

You then use the same setup on your own project. The course has no further session for that.

## Overleaf

Overleaf compiles **`main.tex`** at the repo root. That file inputs one lesson. Switch the active lesson by commenting and uncommenting the `\input` line.

**Recompile** → `main.pdf`

| Lesson | In `main.tex` | PDF |
|--------|----------------|-----|
| 1 | uncomment `\input{lesson1/lesson1.tex}` | [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf) |
| 2 | uncomment `\input{lesson2/lesson2.tex}` | [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf) |
| 3 | uncomment `\input{lesson3/lesson3.tex}` | [`lesson3/lesson3.pdf`](lesson3/lesson3.pdf) |

## The three lessons

| Lesson | Question | In the repo |
|--------|----------|-------------|
| 1. Vocabulary | What are these things? | [`lesson1/`](lesson1/) |
| 2. Second brain | How does the project survive the next chat? | [`lesson2/`](lesson2/) |
| 3. Automations and control | When does the job start, and how do I check it? | [`lesson3/`](lesson3/) |

One-page outline: [`syllabus.tex`](syllabus.tex).

## Repository layout

```
Agentic_Economic_Research/
├── main.tex            # Overleaf entry. One active lesson.
├── syllabus.tex        # One-page outline
├── assets/             # Figures used in the slides
├── demos/lesson1/      # Live material for Lesson 1
├── demos/lesson2/      # Notes for the Lesson 2 demo
├── lesson1/            # Lesson 1 deck
├── lesson2/            # Lesson 2 deck and the synthetic vault
└── lesson3/            # Lesson 3 deck
```

## File guide

### `lesson1/` — Vocabulary (hours 1–2)

`lesson1.tex` is the deck. `lesson1.pdf` is the compiled file. The theme is `preamble_v2.tex`. Where the figures and the numbers come from: [`assets/lesson1/SOURCES.md`](assets/lesson1/SOURCES.md).

### `lesson2/` — Second brain (hours 3–4)

`lesson2.tex` is the deck. `lesson2.pdf` is the compiled file. `preamble.tex` loads the Lesson 1 theme and adds the Lesson 2 boxes. `obsidian-vault/` is the invented project shown in class. `speaker-notes.md` is the lecture notes, in Italian. `REFERENCES.md` is the reading list.

### `lesson3/` — Automations and control (hours 5–6)

`lesson3.tex` is the whole deck in one file. It uses the Lesson 2 preamble. `lesson3.pdf` is the compiled file. `main.tex` currently inputs this lesson.

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
# From the repo root. Uncomment one \input in main.tex first.
mkdir -p /tmp/lesson
tectonic -X compile main.tex --outdir /tmp/lesson
```

Docker: `texlive/texlive:latest` if the local TeX is too old.

## Licence

Third-party screenshots are used under fair use for non-commercial teaching.
Replace with institutional captures or live demos before public distribution if
required by your institution.
