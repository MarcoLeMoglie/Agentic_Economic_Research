# Lesson 2

Slide text comes from the 1 November 2026 source pack (`From JARVIS to Your Own Second Brain`). The Beamer theme is Lesson 1: `lesson2/preamble.tex` inputs `lesson1/preamble_v2.tex`, then adds the source pack's boxes, kickers, and image paths.

Compile from the repository root:

```bash
mkdir -p /tmp/l2c
tectonic -X compile main_lesson2.tex --outdir /tmp/l2c
cp /tmp/l2c/main_lesson2.pdf lesson2/lesson2.pdf
```

`main.tex` is still Lesson 1.

Speaker notes: `speaker-notes.md` (Italian, from the source pack). Sources: `REFERENCES.md`. Image provenance: `sources-and-image-credits.md`. Live demo: `demos/lesson2/` and `DEMO_GUIDE.md`. Do not run `scripts/setup_git.sh` inside this repository. Copy the demo folder out first.
