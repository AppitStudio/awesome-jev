# Typed Evals

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evaluate LLM responses, RAG samples, and agent traces with TypeSafe Jev as the judge, including optional calibration against human labels and tool-call guards before execution.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TrustifAI/typed_evals) |
| Maintainer | [TrustifAI](https://github.com/TrustifAI) / [Aaryan Verma](https://github.com/Aaryanverma). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package and CLI (`typed_evals`); root-level package layout. |
| Requirements | Python ≥ 3.11; live judging uses `TYPESAFE_API_KEY` and `typesafe-sdk` 0.7.x (default model `jev-1.13.0`). Offline demo needs the `calibration` extra. |
| License | [MIT](https://github.com/TrustifAI/typed_evals/blob/0d54b0ab612127d82034bbb00331fb667b12210f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, offline demo, and offline pytest inspected. Live TypeSafe calls were not run. |

## When to use

Use it when you want preset or custom typed metrics (faithfulness, relevancy, task completion, tool grounding, …) judged by Jev over supplied evidence, or when you want to gate tools before they run. Prefer a thinner SDK client when you only need raw Noul/Choice/Score calls without an evaluation harness.

## How it works

[`typed_evals/backends/jev.py`](https://github.com/TrustifAI/typed_evals/blob/0d54b0ab612127d82034bbb00331fb667b12210f/typed_evals/backends/jev.py) builds `Choice` / `Noul` / `Score` questions and calls `AsyncTypeSafeClient.system_one` (default `jev-1.13.0`). Presets such as `"rag"` and `"agent"` assemble fixed metric panels; application code still owns thresholds and what happens after `passed`. Optional calibration maps raw scores to probabilities using human labels. Tool guards can block execution when judgments fail.

## Get started

```sh
git clone https://github.com/TrustifAI/typed_evals.git
cd typed_evals
git checkout 0d54b0ab612127d82034bbb00331fb667b12210f
python -m pip install -e '.[dev,calibration]'
python examples/offline_demo.py
python -m pytest -q --ignore=tests/test_live.py
```

Live evaluation needs `TYPESAFE_API_KEY` and incurs TypeSafe usage. The offline demo prints synthetic calibration numbers—not live Jev results.

## Examples and demos

- [`examples/offline_demo.py`](https://github.com/TrustifAI/typed_evals/blob/0d54b0ab612127d82034bbb00331fb667b12210f/examples/offline_demo.py) — credential-free calibration illustration.
- [`examples/rag_evaluation.py`](https://github.com/TrustifAI/typed_evals/blob/0d54b0ab612127d82034bbb00331fb667b12210f/examples/rag_evaluation.py), agent/runtime examples under `examples/`.
- Docs: [`docs/EVALUATION.md`](https://github.com/TrustifAI/typed_evals/blob/0d54b0ab612127d82034bbb00331fb667b12210f/docs/EVALUATION.md).

## Limits and data handling

Evaluation inputs (queries, responses, contexts, traces) leave the host on live judging. Missing evidence and judge errors raise by default. Adapter extras (LangChain/CrewAI/agent frameworks) were skipped on the review host when those packages were absent. Do not treat upstream or demo scores as measured quality on your workload.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 0d54b0a](https://github.com/TrustifAI/typed_evals/tree/0d54b0ab612127d82034bbb00331fb667b12210f): MIT. AI-assisted source review of the Jev backend, metrics, README, and LICENSE. On Python 3.13 with `typesafe-sdk` 0.7.0: **`python examples/offline_demo.py`** completed; **`pytest -q --ignore=tests/test_live.py`**: **302 passed, 6 skipped**. Upstream GitHub Actions `tests` succeeded on the same SHA. No live TypeSafe calls.

Related: [daf-jev](daf-jev.md), [jev-align](jev-align.md), [Responsible AI Harness](responsible-ai-harness.md).
