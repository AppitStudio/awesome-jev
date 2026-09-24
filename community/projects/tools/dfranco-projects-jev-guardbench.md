# jev-guardbench

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Benchmark harness asking whether a System One model (hosted TypeSafe Jev or self-hosted open-source Kev) can stand in for LLM-as-judge in agent `before_model` / `after_model` guardrail callbacks—with fixed hypotheses before counted runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dfranco-projects/jev-guardbench) |
| Maintainer | [dfranco-projects](https://github.com/dfranco-projects). Independently curated. |
| Format | Python package (`guardbench`) with configs, guards, metrics, and reports. |
| Requirements | Python/`uv`; optional TYPESAFE_API_KEY, Anthropic/Google keys; optional local Kev. |
| License | No LICENSE file at the reviewed tip—reuse terms unspecified. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Counted runs not executed here. Confirm redistribution rights (no LICENSE at tip). |

## When to use

Use to **measure** System One vs LLM judges on guardrail detection quality/latency. Prefer [jev-guardrails (deepansh-saxena)](deepansh-saxena-jev-guardrails.md) for a smaller fixed-rule A/B demo.

## How it works

`guards/` adapters call systemone (Jev/Kev), llm_judge (Gemini/Claude), or cascades. `runner.py` writes resumable JSONL; `metrics.py` / `report.py` summarize F1, FPR, AUROC, ECE, latency.

## Get started

```sh
git clone https://github.com/dfranco-projects/jev-guardbench.git
cd jev-guardbench
git checkout 8a7bf3c353b9541b4930b2d5aa9d4fc689b4b034
uv sync
uv run pytest
# optional live: uv run python -m guardbench run configs/smoke.yaml --guards jev,gemini-flash
```

## Examples and demos

- `HYPOTHESES.md` / `METHODOLOGY.md` pre-registered rules.
- `configs/smoke.yaml` and `configs/full.yaml`.

## Limits and data handling

No LICENSE at tip. Full Kev-9B runs need substantial GPU. Live arms spend provider budget.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 8a7bf3c](https://github.com/dfranco-projects/jev-guardbench/tree/8a7bf3c353b9541b4930b2d5aa9d4fc689b4b034). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [jev-guardrails (deepansh-saxena)](deepansh-saxena-jev-guardrails.md), [Sureband](sureband.md).
