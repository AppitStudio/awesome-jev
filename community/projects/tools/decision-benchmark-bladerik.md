# decision-benchmark by bladerik (agent skill that tests Jev and other decision models on your own labelled sample)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill (Slovak README) that first checks whether a decision model suits your task, helps you build 50 to 100 labelled items, then runs every decision model on OpenRouter (Jev and others) on them and reports accuracy, calibration, speed and cost per 1,000 items with a recommendation. Separate from the listed system1-decision-benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bladerik/decision-benchmark) |
| Maintainer | [bladerik](https://github.com/bladerik). Independently curated. |
| Format | Agent skill with a Python script (standard library, MIT) |
| Requirements | An agent that reads `SKILL.md` (Claude Code, Codex, Cursor, Gemini CLI and others), Python 3, and `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/bladerik/decision-benchmark/blob/cedf99f6b0bdd0e7e355609238de3e009345647f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decision-benchmark/scripts/bench.py`](https://github.com/bladerik/decision-benchmark/blob/cedf99f6b0bdd0e7e355609238de3e009345647f/decision-benchmark/scripts/bench.py) at the pinned commit. |

## When to use

- Check whether Jev or another decision model is good enough for your own task before building on it.
- Mismatch: results depend on your small sample; README is in Slovak.

## How it works

`decision-benchmark/scripts/bench.py` lists OpenRouter models with decisions output and sends the same labelled sample to each, including Jev, then scores the answers. Integration evidence: [`decision-benchmark/scripts/bench.py`](https://github.com/bladerik/decision-benchmark/blob/cedf99f6b0bdd0e7e355609238de3e009345647f/decision-benchmark/scripts/bench.py).

## Get started

Install the skill with the skills CLI and ask your agent to benchmark your task.

```sh
npx skills add bladerik/decision-benchmark
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bladerik/decision-benchmark/blob/cedf99f6b0bdd0e7e355609238de3e009345647f/README.md](https://github.com/bladerik/decision-benchmark/blob/cedf99f6b0bdd0e7e355609238de3e009345647f/README.md)

## Limits and data handling

Your sample goes to each OpenRouter decision model on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit cedf99f6b0bd](https://github.com/bladerik/decision-benchmark/tree/cedf99f6b0bdd0e7e355609238de3e009345647f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
