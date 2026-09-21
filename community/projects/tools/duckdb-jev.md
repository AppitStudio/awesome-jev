# duckdb-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Native C++ DuckDB extension for TypeSafe Jev semantic predicates, Choice classification, and Score rubrics in SQL—without Python UDFs or a separate inference server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prasanthj/duckdb-jev) |
| Maintainer | [prasanthj](https://github.com/prasanthj). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Native DuckDB loadable extension (`jev.duckdb_extension`) with SQL helpers and Python host examples. |
| Requirements | DuckDB **1.5.5** matching platform build (macOS/Linux x86-64/ARM64); `TYPESAFE_API_KEY` or a DuckDB `jev` secret for live calls. Build needs a C++17 toolchain, libcurl, and `uv`. |
| License | [Apache-2.0](https://github.com/prasanthj/duckdb-jev/blob/9bc4d92fd024047c3de04fe789728712a869f120/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Native extension build and pytest suite were **not** executed in this review (require compiling against pinned DuckDB). Source, README, LICENSE, and HTTP-stub test layout were inspected. No live TypeSafe calls. |

## When to use

Use it when evidence already lives in DuckDB and you want Noul/Choice/Score in SQL with batching, caching, and budgets. Prefer [pg-jev](pg-jev.md) / [mysql-ailike](mysql-ailike.md) / [JevSQL](jevsql.md) for those engines. Prefer [dbt_jev](dbt-jev.md) when classification should run through dbt macros rather than a native extension. Extension binaries must match DuckDB version and platform.

## How it works

The extension posts typed questions to TypeSafe System One from C++, packing many judgments per request and streaming across DuckDB chunks. SQL surfaces include `jev`, `jev_noul`, `jev_choice`, `jev_score`, and `jev_usage()`. Credentials come from a scoped DuckDB secret or `TYPESAFE_API_KEY` and are kept out of result sets and cache keys.

## Get started

Follow upstream [distribution and installation](https://github.com/prasanthj/duckdb-jev/blob/9bc4d92fd024047c3de04fe789728712a869f120/docs/distribution.md) for a prebuilt archive, or build locally:

```sh
git clone https://github.com/prasanthj/duckdb-jev.git
cd duckdb-jev
git checkout 9bc4d92fd024047c3de04fe789728712a869f120
./build.sh
# Offline tests use a local HTTP stub (no paid inference) after the extension binary exists:
# uv run pytest -q
```

Load an unsigned local build in DuckDB, then try the README SQL examples (`jev`, `jev_choice`, `jev_score`). Live queries send row evidence to TypeSafe and may incur charges.

## Examples and demos

- README SQL snippets for refund detection, ticket routing, and frustration scoring.
- Terminal walkthrough GIF / `vhs` tape under `examples/` (may show live timings from one local run).
- `tests/` HTTP stub server for deterministic offline pytest once built.

## Limits and data handling

Live SQL sends selected column/struct evidence to TypeSafe. Match extension builds to DuckDB 1.5.5 and platform. Budgets, retries, and cancellation are documented upstream; treat vendor timing claims as single-run measurements. No endorsement of production readiness.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9bc4d92](https://github.com/prasanthj/duckdb-jev/tree/9bc4d92fd024047c3de04fe789728712a869f120): Apache-2.0. AI-assisted source review of README, LICENSE, `tests/conftest.py` stub design, and SQL examples. **Native build + pytest not run here.** No live TypeSafe.

Related: [pg-jev](pg-jev.md), [dbt_jev](dbt-jev.md), [JevSQL](jevsql.md), [mysql-ailike](mysql-ailike.md).
