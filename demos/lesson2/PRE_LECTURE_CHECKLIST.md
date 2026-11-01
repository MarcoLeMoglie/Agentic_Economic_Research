# Pre-lecture checklist

## The evening before

- [ ] `bash demos/lesson2/setup_demo.sh` if `~/Documents/SecondBrain-Lecture-Demo` is missing. If it exists, `bash demos/lesson2/reset_demo.sh`.
- [ ] `git -C ~/Documents/SecondBrain-Lecture-Demo status` is clean, on `main`, at tag `pre-audit`.
- [ ] `python scripts/validate_demo_brain.py` fails on `main`. That is the planted defect.
- [ ] `python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py` exits 0.
- [ ] Agent login works in the harness you will use in class. Open the lecture vault, not the Dropbox Brain.
- [ ] Obsidian opens this vault. If it sits on "loading plugins", quit it and use the files directly. Do not let it open the real Brain vault.
- [ ] `lesson2/lesson2.pdf` opens. Speaker notes are `lesson2/speaker-notes.md`.

## Thirty minutes before

- [ ] Wi-Fi, or decide now to use the offline path (`git checkout final-verified`).
- [ ] Terminal font large enough for the back row.
- [ ] Notifications off.
- [ ] One prompt from `demo-script.md` pasted into the harness, then undo any edit before class starts.
- [ ] Backup figures: the slides already contain the git log, the diff, the canvas, and the graph.

## After class

- [ ] `bash demos/lesson2/reset_demo.sh`
- [ ] Confirm `git status` is clean and `git describe --tags` is `pre-audit`.
- [ ] No remote was added.
