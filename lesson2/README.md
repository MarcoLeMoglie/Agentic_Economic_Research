# Lesson 2

Beamer deck for "From JARVIS to your own second brain". It uses the Lesson 1 theme through `lesson2/preamble.tex`, which inputs `lesson1/preamble_v2.tex` and then overrides the footline, the graphic path, and the demo frame.

Compile from the repository root:

```bash
mkdir -p /tmp/l2c
tectonic -X compile main_lesson2.tex --outdir /tmp/l2c
cp /tmp/l2c/main_lesson2.pdf lesson2/lesson2.pdf
bash lesson2/preflight.sh
```

`main.tex` is still Lesson 1. Overleaf does not build this deck unless `main_lesson2.tex` is set as the main file.

## Files

| File | Role |
|---|---|
| `lesson2.tex` | Frame order |
| `sections/00_opening.tex` | Slides 1 to 10 |
| `sections/01_architectures.tex` | Slides 11 to 18 |
| `sections/02_build.tex` | Slides 19 to 26 |
| `sections/03_mybrain.tex` | Slides 27 to 36 |
| `sections/04_close.tex` | Demo frame, homework, references |
| `sections/05_appendix.tex` | Appendix A1 to A9 |
| `speaker-notes.md` | Spoken notes, not `\note` |
| `lesson2.bib` | Sources |
| `sources-and-image-credits.md` | What each figure is |

## Layout families

D definition, S screenshot or file, C chart, T table, G graph or diagram, F flow. The same family is not used three times in a row. Slides 19 to 22 are all figures, alternating a wide figure, a figure on the right, a full-width graph, and a figure on the left.

Palette: ink `#163A59`, accent `#D97706`, the same as Lesson 1.
