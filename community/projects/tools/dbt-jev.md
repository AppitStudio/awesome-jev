# dbt_jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Classify non-NULL SQL values with TypeSafe Jev (or OpenRouter→Jev) from dbt macros on DuckDB and ClickHouse—inference runs when the database executes SQL, not at parse time.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smithclay/dbt_jev) |
| Maintainer | [smithclay](https://github.com/smithclay). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | dbt package (`macros/classify.sql`) + Python runtime (`dbt_jev`) with DuckDB plugin and ClickHouse UDF install path. |
| Requirements | dbt Core v1 + tested DuckDB/ClickHouse adapters (see upstream table); `TYPESAFE_API_KEY` or OpenRouter key for live classify. Mock HTTP fixtures cover offline unit tests. |
| License | [MIT](https://github.com/smithclay/dbt_jev/blob/55993cf06ff4c9af66f8a14aadfc29ceb75b19d7/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest inspected. Live TypeSafe / live warehouse classify were not run. MVP targets dbt Core v1 Python plugins—not dbt v2. |

## When to use

Use it when warehouse rows need a closed label set judged by Jev and you already run dbt on DuckDB or ClickHouse. Prefer [pg-jev](pg-jev.md) / [mysql-ailike](mysql-ailike.md) / [JevSQL](jevsql.md) for those engines' native paths.

## How it works

The `dbt_jev.classify` macro emits SQL that calls into the runtime; [`src/dbt_jev/runtime.py`](https://github.com/smithclay/dbt_jev/blob/55993cf06ff4c9af66f8a14aadfc29ceb75b19d7/src/dbt_jev/runtime.py) posts to TypeSafe (`jev-latest`) or OpenRouter (`typesafe/jev-…`) and validates answers against supplied criteria. Materialize results as tables so downstream reads do not re-call the API.

## Get started

```sh
git clone https://github.com/smithclay/dbt_jev.git
cd dbt_jev
git checkout 55993cf06ff4c9af66f8a14aadfc29ceb75b19d7
python -m pip install -e '.[dev]'
python -m pytest -q tests/test_runtime.py tests/test_clickhouse_udf.py
```

Follow upstream README for DuckDB plugin registration or ClickHouse UDF install before any live `dbt run`. Live classify sends column values to the chosen provider.

## Examples and demos

- README SQL snippet classifying agent tool-call context.
- `tests/mock_service.py` deterministic Jev-shaped HTTP fixture.
- Integration test projects under `integration_tests/` (not executed in this review).

## Limits and data handling

Classified cell text leaves the runner/warehouse host on live calls. Retries/backoff are configurable; auth and malformed responses raise. Upstream version matrix is the compatibility claim—re-verify on your adapters.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 55993cf](https://github.com/smithclay/dbt_jev/tree/55993cf06ff4c9af66f8a14aadfc29ceb75b19d7): MIT. AI-assisted source review of runtime, macros, and README. **`pytest tests/test_runtime.py tests/test_clickhouse_udf.py`**: **30 passed** with mock HTTP. No live TypeSafe calls; full DuckDB/ClickHouse dbt integration not run here.

Related: [pg-jev](pg-jev.md), [mysql-ailike](mysql-ailike.md), [JevSQL](jevsql.md), [nf-jev](nf-jev.md).
