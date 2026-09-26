# jevtok

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Exact token counting and request-cost prediction for TypeSafe Jev—a `tiktoken`-style encoder reconstructed from the API’s `usage.input_tokens` (o200k_base vocabulary with Jev’s non-public encoder).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LabGuy94/jevtok) |
| Maintainer | [LabGuy94](https://github.com/LabGuy94). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **jevtok 0.1.0** (`pip`/`uv`) with CLI `jevtok`. |
| Requirements | Python ≥ 3.10; dependencies `tiktoken`, `regex`. Offline counting needs no API key. |
| License | [MIT](https://github.com/LabGuy94/jevtok/blob/698c53b778ce901be82c166d809e4b1f7948a465/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest run; live API oracle rebuild not re-run. |

## When to use

Use it to estimate billed input tokens and catch over-limit requests before calling Jev. Prefer raw `tiktoken` only if you accept systematic under-counts versus Jev’s encoder.

## How it works

[`src/jevtok/tokenizer.py`](https://github.com/LabGuy94/jevtok/blob/698c53b778ce901be82c166d809e4b1f7948a465/src/jevtok/tokenizer.py) exposes `get_encoding("jev-1.13")` (aliases `jev-latest`, `typesafe/jev-1.13`). [`src/jevtok/request.py`](https://github.com/LabGuy94/jevtok/blob/698c53b778ce901be82c166d809e4b1f7948a465/src/jevtok/request.py) estimates whole-request `input_tokens` for structured state + questions the way the API serializes them (not plain `json.dumps`). Upstream documents verification against measured API usage for model `jev-1.13-20260917`.

## Get started

```sh
uvx --from git+https://github.com/LabGuy94/jevtok jevtok count "The tokenization of evidence"
# or: pip install git+https://github.com/LabGuy94/jevtok
```

```python
import jevtok
enc = jevtok.get_encoding("jev-1.13")
enc.count("The tokenization of evidence")  # 7
```

Pinned review checkout:

```sh
git clone https://github.com/LabGuy94/jevtok.git
cd jevtok
git checkout 698c53b778ce901be82c166d809e4b1f7948a465
pip install -e '.[dev]'
pytest -q
```

## Examples and demos

- CLI `count` / `encode --pieces` in the README.
- Fixture-backed tokenizer and request tests under [`tests/`](https://github.com/LabGuy94/jevtok/tree/698c53b778ce901be82c166d809e4b1f7948a465/tests).
- This listing ran `pytest -q`: **2626 passed**. No live TypeSafe calls.

## Limits and data handling

Encoder fidelity is claimed against a recorded oracle; re-verify if TypeSafe changes tokenization. Counting is local—no data leaves the machine unless you separately call the API.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 698c53b](https://github.com/LabGuy94/jevtok/tree/698c53b778ce901be82c166d809e4b1f7948a465): MIT; AI-assisted source review of README, LICENSE, tokenizer/request modules; pytest **2626 pass**. No live TypeSafe call.

Related: [jevkit](jevkit.md), [typesafeai-cli](typesafeai-cli.md), [jevals](jevals.md).

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev setup guide: batch questions to cut API costs](../../knowledge-base/articles/jev-api-cost-setup.md) — Independently suggested by JevList; not an endorsement by darkzodchi. Estimate each request's input tokens and catch over-limit state before calling Jev.
<!-- knowledge:backlinks:end -->
