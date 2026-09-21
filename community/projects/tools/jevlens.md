# jevlens

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evaluate, calibrate, replay, and monitor TypeSafe Jev decisions from labeled CSV/JSONL: store full answer distributions, report accuracy/Brier/F1, suggest thresholds, and optionally open a Streamlit dashboard or fail CI on regression.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/k4its1t/jevlens) |
| Maintainer | [k4its1t](https://github.com/k4its1t) / JevLens contributors. Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **jevlens 0.1.0** (Typer CLI) + optional Streamlit dashboard extras + composite GitHub Action. |
| Requirements | Python ≥ 3.10; `typesafe-sdk`, `pyyaml`, `typer`, `python-dotenv`. Live runs need `TYPESAFE_API_KEY`. Metrics/config tests run offline. |
| License | [MIT](https://github.com/k4its1t/jevlens/blob/cd21fce0bdde16f02856a55c792645bd3b18605b/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest run; live eval and dashboard not executed. |

## When to use

Use it when you have labeled cases and want calibration/threshold tooling with replayable probability archives. Prefer [jevals](jevals.md) for an interactive local workbench focused on authoring/comparing cases; prefer [Typed Evals](typed-evals.md) for RAG/agent judge libraries.

## How it works

[`src/jevlens/runner.py`](https://github.com/k4its1t/jevlens/blob/cd21fce0bdde16f02856a55c792645bd3b18605b/src/jevlens/runner.py) drives `Choice` / `Noul` / `Score` questions via `typesafe_sdk.TypeSafeClient`. Predictions, probabilities, confidence, usage, and latency are stored as JSONL so thresholds can change without another API call. Reporting covers accuracy, precision/recall/F1, Brier, MAE, review rate, and confusion matrices; an Action can fail when classification accuracy regresses.

## Get started

```sh
pip install 'jevlens @ git+https://github.com/k4its1t/jevlens'
# Configure YAML + dataset per upstream examples/ticket-routing/
# export TYPESAFE_API_KEY=...   # required for live runs
jevlens --help
```

Pinned review checkout:

```sh
git clone https://github.com/k4its1t/jevlens.git
cd jevlens
git checkout cd21fce0bdde16f02856a55c792645bd3b18605b
pip install -e '.[dev]'
pytest -q
```

## Examples and demos

- [`examples/ticket-routing/`](https://github.com/k4its1t/jevlens/tree/cd21fce0bdde16f02856a55c792645bd3b18605b/examples/ticket-routing): sample config + dataset.
- [`action.yml`](https://github.com/k4its1t/jevlens/blob/cd21fce0bdde16f02856a55c792645bd3b18605b/action.yml): composite GitHub Action.
- This listing ran `pytest -q`: **10 passed**. Live TypeSafe eval and Streamlit dashboard not run.

## Limits and data handling

Live evaluation sends dataset states/questions to TypeSafe. Treat suggested thresholds as starting points for your own policy. Dashboard extras pull pandas/plotly/streamlit.

## Review and maintenance

Reviewed on **2026-09-21** at [commit cd21fce](https://github.com/k4its1t/jevlens/tree/cd21fce0bdde16f02856a55c792645bd3b18605b): MIT; AI-assisted source review of README, LICENSE, runner/metrics/cli; pytest **10 pass**. No live TypeSafe call.

Related: [jevals](jevals.md), [Typed Evals](typed-evals.md), [jeval](jeval.md), [daf-jev](daf-jev.md).
