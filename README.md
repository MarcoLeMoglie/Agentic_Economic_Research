# Agentic AI for Economic Research

**Instructor:** Marco Le Moglie, Catholic University of the Sacred Heart

I teach this to PhD students and faculty in economics. Three lessons of two hours, in English, on a video call.

A paper is still the same job: read, get the data in shape, estimate, write, answer the referee. An agent can take a piece of that job inside the project folder. It opens the files, runs Stata, and changes the line that failed. The course is how you point it at the right files, what you let it change, and how you check the result.

**Lesson 1. Vocabulary.**  

**Lesson 2. Second brain.** 

**Lesson 3. Automations and control.** 

## Slides

| Lesson | PDF |
|--------|-----|
| 1. Vocabulary | [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf) |
| 2. Second brain | [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf) |
| 3. Automations and control | [`lesson3/lesson3.pdf`](lesson3/lesson3.pdf) |

One-page outline: [`syllabus.pdf`](syllabus.pdf).

## Class files

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

### `demos/lesson2/`

Live material for Lesson 2:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/main/demos/lesson2

| Path | What it is |
|------|------------|
| `README.md` | What the synthetic project is, and the commands for class. |
| `DEMO_GUIDE.md` | The order of the demo. |

## Licence

Third-party material in the slides is used under fair use for non-commercial teaching.
