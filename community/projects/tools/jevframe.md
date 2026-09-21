# jevframe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library that adds a `.jev` accessor on pandas and Polars DataFrames: classify, score, and ask natural-language questions per row with TypeSafe Jev, returning structured Series/DataFrames with full probability distributions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ktaletsk/jevframe) |
| Maintainer | [ktaletsk](https://github.com/ktaletsk) (Konstantin Taletskiy). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | PyPI package **`jevframe` 0.1.0**; optional extras `pandas` / `polars` / both. |
| Requirements | Python ≥ 3.10; `typesafe-sdk>=0.7,<0.8`. Live evaluation needs `TYPESAFE_API_KEY` (or an injected client). DataFrame backends are optional extras. |
| License | [MIT](https://github.com/ktaletsk/jevframe/blob/16bd3eae69b71284a75747fb4bf199b14ba1b075/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `uv run pytest`: **108 passed** (with pandas+polars+examples). No live TypeSafe calls. Distinct from [hunch](hunch.md) (verb API over scalars/lists/columns) and [jev-table](jev-table.md) (CSV/JSONL CLI columns). |

## When to use

Use it for row-wise semantic labeling, sentiment, or rubric scoring inside pandas/Polars pipelines with preserved indexes and bounded async concurrency. Prefer [hunch](hunch.md) for scalar/list verbs without a DataFrame-first accessor; prefer [Advocaat](advocaat.md) for TypeScript batching.

## How it works

Importing [`jevframe.pandas`](https://github.com/ktaletsk/jevframe/blob/16bd3eae69b71284a75747fb4bf199b14ba1b075/src/jevframe/pandas.py) or [`jevframe.polars`](https://github.com/ktaletsk/jevframe/blob/16bd3eae69b71284a75747fb4bf199b14ba1b075/src/jevframe/polars.py) registers the `.jev` accessor. [`_engine.py`](https://github.com/ktaletsk/jevframe/blob/16bd3eae69b71284a75747fb4bf199b14ba1b075/src/jevframe/_engine.py) builds typed questions, runs `AsyncTypeSafeClient` with concurrency/cache options, and packs answers back into frame-shaped outputs. Null handling and error policies stay in code.

## Get started

```sh
uv add 'jevframe[pandas]==0.1.0'   # or [polars] / [pandas,polars]
export TYPESAFE_API_KEY=your_key
# From source at the reviewed commit:
git clone https://github.com/ktaletsk/jevframe.git
cd jevframe
git checkout 16bd3eae69b71284a75747fb4bf199b14ba1b075
uv sync --extra pandas --extra polars --extra examples --group dev
uv run pytest -q
```

Live `.jev` calls send row text to TypeSafe and can incur charges. Tests use mocks/fakes.

## Examples and demos

- Interactive marimo notebook (`examples/reviews.py`) with a sponsored gateway for cached demo reviews; **Evaluate reviews** is the live path.
- Offline unit tests under `tests/` (executed for this listing).

## Limits and data handling

Row content leaves the host on live evaluation. A personal invalid key does not silently fall back to sponsorship (upstream behavior; covered in tests). This listing did not run live inference or the molab demo against a real key.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 16bd3ea](https://github.com/ktaletsk/jevframe/tree/16bd3eae69b71284a75747fb4bf199b14ba1b075): `jevframe` **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `_engine.py`, pandas/polars accessors. Offline pytest: 108 passed. No live TypeSafe calls.

Related: [hunch](hunch.md), [jev-table](jev-table.md), [dbt_jev](dbt-jev.md).
