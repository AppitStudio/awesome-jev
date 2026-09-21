# jev-agent-failure-benchmark

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Offline-reproducible harness that scores TypeSafe Jev on the text subset of Who&When Pro (agent-failure attribution: who / when / what) and compares against published LLM baselines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TokenTrim/jev-agent-failure-benchmark) |
| Maintainer | [TokenTrim](https://github.com/TokenTrim). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package/CLI **jevbench** (`sample` / `estimate` / `run` / `report`). |
| Requirements | Python + `uv`; `TYPESAFE_API_KEY` for live runs. Dataset downloaded separately (CC-BY-4.0; not redistributed). |
| License | Code [Apache-2.0](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/4d46af795a4a4409940a65857da73e45abaea2db/LICENSE); Who&When Pro data keeps CC-BY-4.0. TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest run; full 6,257-trace Jev run and live billing not performed. Upstream result tables are reported, not re-measured. |

## When to use

Use it to study whether typed Jev choices can attribute injected multi-agent failures competitively with frontier LLMs on a fixed public subset. Prefer [jevals](jevals.md) / [jev-sec-bench](jev-sec-bench.md) for authoring your own eval packs or security corpora.

## How it works

Each trace becomes three typed `choice` questions (responsible agent, step, error type) via a Jev backend ([`backends/jev.py`](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/4d46af795a4a4409940a65857da73e45abaea2db/src/jevbench/backends/jev.py)). Scoring uses the pinned official `whowhen_eval` scorer. LLM numbers come from the paper; comparability notes for Who/When vs What are in the README. Leakage tests assert labels never enter Jev input.

## Get started

```sh
git clone https://github.com/TokenTrim/jev-agent-failure-benchmark.git
cd jev-agent-failure-benchmark
git checkout 4d46af795a4a4409940a65857da73e45abaea2db
uv sync --extra dev
uv run pytest -q
```

Live `jevbench run` needs the Hugging Face text subset download and a TypeSafe key (incurs charges).

## Examples and demos

- Upstream README results table and `RESULTS.md` (treat as upstream reports).
- This listing ran `uv run pytest -q`: **18 passed**, **2 skipped**. No live TypeSafe run.

## Limits and data handling

Failed-agent traces reach TypeSafe during `run`. Benchmark failures are injected by Who&When Pro’s pipeline, not natural production incidents. Do not treat this as a leaderboard submission.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4d46af7](https://github.com/TokenTrim/jev-agent-failure-benchmark/tree/4d46af795a4a4409940a65857da73e45abaea2db): Apache-2.0 code; AI-assisted source review of README, LICENSE, backends, tests; pytest **18 pass / 2 skip**. No live TypeSafe call.

Related: [jevals](jevals.md), [jev-sec-bench](jev-sec-bench.md), [Typed Evals](typed-evals.md), [Responsible AI Harness](responsible-ai-harness.md).
