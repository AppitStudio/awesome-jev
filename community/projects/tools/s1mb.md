# S1MB (System One Mosaic Benchmark: English, Japanese and vision evaluations that compare Jev and other decision models on the same inputs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open benchmark harness and leaderboard for System One decision models: 137 English benchmarks, Japanese and a 26-benchmark vision set across Choice, Noul, Score and optional Box tasks, with adapters for TypeSafe/Jev, OpenAI Decisions and many open decision models, plus a results dataset and submission workflow.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hotchpotch/S1MB) |
| Maintainer | [hotchpotch](https://github.com/hotchpotch). Independently curated. |
| Format | Python evaluator (uv) with Hugging Face leaderboard and datasets |
| Requirements | Python 3.11 and uv; real runs need the evaluated model's key or weights and Hugging Face access (the vision dataset is private). |
| License | [MIT](https://github.com/hotchpotch/S1MB/blob/dbfc74699b814cadc8e3384ffa8705a39958cc91/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`evaluator/src/s1mb/adapters/typesafe.py`](https://github.com/hotchpotch/S1MB/blob/dbfc74699b814cadc8e3384ffa8705a39958cc91/evaluator/src/s1mb/adapters/typesafe.py) at the pinned commit. |

## When to use

- Compare Jev with other decision models on one shared benchmark.
- Submit your own model's results through the documented workflow.
- Mismatch: Jev is one of many adapters; this is a benchmark, not a Jev application.

## How it works

`adapters/typesafe.py` sends each benchmark item to the TypeSafe System One API and maps answers to the benchmark schema; the same contract is implemented for the other adapters. Integration evidence: [`evaluator/src/s1mb/adapters/typesafe.py`](https://github.com/hotchpotch/S1MB/blob/dbfc74699b814cadc8e3384ffa8705a39958cc91/evaluator/src/s1mb/adapters/typesafe.py).

## Get started

From the upstream README (not run on the review host):

```sh
cd evaluator
uv sync --locked
uv run s1mb run --adapter dummy --category smoke-v1 --limit 2 --run-id smoke-001
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with scopes and quick start: [github.com/hotchpotch/S1MB/blob/dbfc74699b814cadc8e3384ffa8705a39958cc91/README.md](https://github.com/hotchpotch/S1MB/blob/dbfc74699b814cadc8e3384ffa8705a39958cc91/README.md)
- Leaderboard: [huggingface.co/spaces/hotchpotch/S1MB-leaderboard](https://huggingface.co/spaces/hotchpotch/S1MB-leaderboard)

## Limits and data handling

Benchmark scores depend on the chosen scope and adapter version; live runs against Jev spend TypeSafe credits on your key. The vision evaluation dataset is private.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit dbfc74699b81](https://github.com/hotchpotch/S1MB/tree/dbfc74699b814cadc8e3384ffa8705a39958cc91). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
