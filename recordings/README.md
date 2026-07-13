# Lecture recordings

Trimmed, compressed captures of the live mini-course sessions. Pre-lesson waiting time is removed; subtitles are synced to the trimmed video.

## Session 1 (`session1/`)

| File | What it is |
|------|------------|
| [`session1_trimmed_softsubs.mp4`](session1/session1_trimmed_softsubs.mp4) | Session 1 lecture video (concepts, tools, architecture). H.264 720p. English subtitles embedded as a **toggleable** soft track (`mov_text`). Trimmed `00:11:20` → `02:19:40`. |
| [`session1_trimmed.en.vtt`](session1/session1_trimmed.en.vtt) | WebVTT subtitle file for Session 1, rebased to the trimmed video. Use for editing captions or players that prefer external subs. |
| [`session1_trimmed_transcript.txt`](session1/session1_trimmed_transcript.txt) | Plain-text transcript of Session 1, speaker-labelled, aligned to the trimmed recording. |

## Session 2 (`session2/`)

| File | What it is |
|------|------------|
| [`session2_trimmed_hardsubs.mp4`](session2/session2_trimmed_hardsubs.mp4) | Session 2 lecture video (live demos, success stories, brain/WIP). H.264 720p. English subtitles **burned into the picture**. Trimmed `00:07:30` → `02:29:23`. |
| [`session2_trimmed.en.vtt`](session2/session2_trimmed.en.vtt) | WebVTT subtitle file for Session 2, rebased to the trimmed video. Same text as the burned-in captions. |
| [`session2_trimmed_transcript.txt`](session2/session2_trimmed_transcript.txt) | Plain-text transcript of Session 2, speaker-labelled, aligned to the trimmed recording. |

## Processing notes

- Source files and scripts live in the Cursor workspace `Agentic_course/session2-recording-review/` (not in this repo).
- Large `.mp4` files are stored with **Git LFS** (`recordings/**/*.mp4`).
