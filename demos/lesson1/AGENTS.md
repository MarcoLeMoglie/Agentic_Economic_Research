# Instructions for coding agents

Project: a two-regression exercise on Stata's 1978 auto data,
used live in Lesson 1 of "Agentic AI for Economic Research".

## Layout

- `data/auto.dta`: raw data. Never modify or overwrite.
- `code/analysis.do`: the only analysis script.
- `output/`: generated tables. Safe to overwrite.

## How to run

```
stata-mp -b do code/analysis.do
```

On macOS, if `stata-mp` is not on the PATH, use
`/Applications/Stata/StataMP.app/Contents/MacOS/stata-mp`.

The log is written to `analysis.log` in the repository root.
Read it after every run: Stata reports errors there, not on
the terminal, and the exit code is 0 even when the do-file fails.

## Rules

1. Change the do-file, never the data.
2. Keep variable names short and lower case.
3. Report robust standard errors (`vce(robust)`) unless asked.
4. Before saying a task is done, run the do-file and show the
   last 20 lines of the log.
5. Do not install Stata packages without asking.
