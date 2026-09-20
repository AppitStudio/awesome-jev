# jsort

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic sort CLI: order lines (or paragraphs/files/JSONL/CSV fields) along a plain-English dimension using pairwise TypeSafe Jev comparisons and a Bradley–Terry scale.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/keltokhy/jsort) |
| Maintainer | [keltokhy](https://github.com/keltokhy) (Khaled Eltokhy). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-sort 0.1.2** (CLI `jsort`; `uv tool install jev-sort`). |
| Requirements | Python ≥ 3.10; live ranking needs `TYPESAFE_API_KEY`, `OPENROUTER_API_KEY`, or a System One gateway (`JEV_GATEWAY_URL` + `JEV_GATEWAY_API_KEY`). Shares an answer cache with sibling Jev CLIs under `~/.cache/jev`. |
| License | [MIT](https://github.com/keltokhy/jsort/blob/ae17939333de44da8eca375ca24ba6064c944c20/LICENSE). |

## When to use

Use it to rank texts by meaning (“more urgent”, “more hawkish about inflation”) when lexical sort is the wrong tool. Prefer [jegrep](jegrep.md) to *find* matching snippets rather than *order* a set; the tools share client/cache conventions but solve different jobs.

## How it works

[`src/jsort/core.py`](https://github.com/keltokhy/jsort/blob/ae17939333de44da8eca375ca24ba6064c944c20/src/jsort/core.py) posts Noul pairwise questions to TypeSafe `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) or OpenRouter `https://openrouter.ai/api/alpha/decisions` (`~typesafe/jev-latest`). [`engine.py`](https://github.com/keltokhy/jsort/blob/ae17939333de44da8eca375ca24ba6064c944c20/src/jsort/engine.py) schedules comparisons, refits a Bradley–Terry scale, and can stop early for `--top`. A per-run dollar budget defaults via `JSORT_BUDGET` (or $1).

## Get started

```sh
uv tool install jev-sort
# or:
git clone https://github.com/keltokhy/jsort.git
cd jsort
git checkout ae17939333de44da8eca375ca24ba6064c944c20
uv sync --group dev
uv run pytest -q
# Live (billable): jsort "more urgent" tickets.txt | head
```

This listing did not call TypeSafe; offline tests were not run on the review host.

## Examples and demos

- README examples for lines, paragraphs, whole files, JSONL, and CSV.
- Fed-statement bench under [`bench/`](https://github.com/keltokhy/jsort/tree/ae17939333de44da8eca375ca24ba6064c944c20/bench).
- Unit tests under [`tests/`](https://github.com/keltokhy/jsort/tree/ae17939333de44da8eca375ca24ba6064c944c20/tests).

## Limits and data handling

Compared text slices (truncated to `--max-chars`) go to the chosen provider. Budget and concurrency caps limit spend/latency but do not remove provider charges. Scores are relative to the supplied set, not absolute truth.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ae17939](https://github.com/keltokhy/jsort/tree/ae17939333de44da8eca375ca24ba6064c944c20): **0.1.2**, MIT. AI-assisted source review of README, `core.py`, `engine.py`, and `pyproject.toml`. No live sort and no `pytest` on the review host.

Related: [jegrep](jegrep.md), [typesafe-cli](typesafe-cli.md).
