# Prose gate, Lesson 2 speaker notes

File scored: `lesson2/speaker-notes.md`. Slide text was checked with `lesson2/preflight.sh` (no em dash, no en dash, no TeX double hyphen in the prose).

## Detectors

Vale, profile academic-en (AntiSlop, BrainVoice, AcademicEnglish), run from the Brain binary with a temporary config. Reports stayed in this folder. Nothing was written into the Brain vault.

- Delivered notes: 0 errors, 0 warnings, 1 suggestion. The suggestion is BrainVoice.ArtificialSymmetry on the three retrieval styles (lexical, semantic, hybrid). That split is the content of the slide, so it stays.

Slopless, same file, after the paragraph split:

- paragraph-length: 0
- demonstrative-emphasis: 17. These are "the left box is..." lines that point at the slide. Left as spoken deixis.
- negation-reframe: 3. Each one is the claim (direction rather than a product; the window is assembled; a chat is a poor record of a decision).
- summative-closer: 4, contrastive-aphorism: 2, and a handful of single hits (sentence-case, triple-repeat on the word "week", which is the slide's own week list).
- Blocking leftovers are the teaching voice, not filler. No second rewrite aimed at the detector.

Fast-DetectGPT, gpt-neo-2.7B, device mps, one score of the delivered notes (32,450 characters, truncated to 2,047 tokens by the scorer):

- criterion 0.63
- P(machine) 0.38
- Advisory only. Not used as a rewrite target.

There is no separate pre/mid/post triple. The Vale fixes and the paragraph breaks were made first, then this single score. A second pass to push the probability down is the thing the scorer's own note forbids.

## Ten categories, delivered notes

| Category | Score | Note |
|---|---|---|
| Hedging stacks | 0 | |
| Formulaic transitions | 0 | No Moreover / Furthermore / In conclusion |
| Uniform cadence | 1 | Some parallel teaching sentences, on purpose |
| Generic fillers | 0 | |
| Significance inflation | 0 | |
| Template openers | 0 | |
| Copula padding | 0 | |
| Mechanical contrast | 1 | Three real contrasts kept; see Slopless |
| Vague attribution | 0 | Names and dates stay attached |
| Process leaks | 0 | |
| Sum | 2 | Pass 2 left the text |

Numbers, dates, and citations were not changed to satisfy a detector. The 15 percent QJE figure and the 14 percent working-paper figure both remain, labelled as the published and the earlier number.
