# Drone Flight Analyzer

A small command-line tool: give it a drone flight log (CSV), it returns a flight safety report.

## What it solves

After a flight, the log holds rows of `time, altitude, speed, battery`. Read by eye, that will not reliably
tell you:

- how many times the flight breached the altitude limit (default 120 m)
- peak and mean altitude
- when battery dropped below a safe threshold
- flight duration and mean speed

Output is a Markdown report (`report.md`) that drops straight into a post-flight review document.

## How to run

```bash
python3 analyzer.py
```

Reads `data/flight_log.csv` and writes `report.md`.

> **Known issue (#1):** the input path is hard-coded, so a filename passed on the command line is ignored.
> Found by testing the tool with input that should break it. See [issue #1](https://github.com/liyifen0329-evelyn/drone-flight-analyzer/issues/1).

## Example output

Terminal:

```
一共: 10 条记录
最高高度： 140 米
超限次数： 3 次
报告已生成: report.md
```

`report.md`:

```markdown
# 无人机飞行安全报告

- 分析记录数：10 条
- 最高飞行高度： 140 米
- 高度超限次数 (>120米): 3次
结论：本次飞行共 3 次超过 120 米安全高度限制，建议复查航线规划。
```

## Two implementations, one answer

`analyzer.py` parses the CSV with a plain Python loop. `analyzer_pandas.py` does the same job with pandas.
Both are kept on purpose: when two independent implementations land on the same figures, I treat the number
as sound. On the sample log both report peak altitude 140 m and 3 breaches.

## How I checked it

- **Hand-count first.** Before running anything, I worked out the expected answers by hand on the 10-row
  sample — peak 140 m, three breaches at 125 / 140 / 132 m — then compared them with the program output.
- **Build it twice.** The plain-Python and pandas versions were cross-checked against each other.
- **Break it on purpose.** I ran an empty file and a file missing the `battery` column. Both returned a
  complete, plausible-looking report instead of failing, because the script reads a fixed path and ignores
  the filename supplied. No crash and no warning — a silent success on the wrong input. Logged as issue #1.
- **Commit only what runs.** Five commits, each independently working.

The lesson I took from it: a tool that fails loudly is easy to catch. A tool that succeeds quietly on the
wrong input is the one that gets you.

## Built with AI, reviewed by me

I used an AI coding agent (Claude Code) as a reviewer rather than a ghostwriter — I type every line myself;
the agent explains, reviews and debugs. `AI协作规则.md` records the rules I set before starting, and
`ROADMAP.md` holds the step-by-step plan behind the commit history.

## Tech

Python 3 · pandas (in one of the two versions) · Git
