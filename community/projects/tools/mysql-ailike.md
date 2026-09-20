# mysql-ailike (AILIKE)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Native MySQL plugin that adds natural-language row filters and joins (`AILIKE` / `ailike(...)`) powered by TypeSafe Jev—MySQL’s counterpart niche to PostgreSQL [pg-jev](pg-jev.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maayanlevy/mysql-ailike) |
| Maintainer | [maayanlevy](https://github.com/maayanlevy). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | MySQL native UDF/plugin (C++ / CMake) with Docker demo, prebuilt Linux AMD64/ARM64 bundles (**v0.2.0** preview). |
| Requirements | Linux MySQL **8.0.46** / **8.4.8** verified paths (glibc 2.34+, libcurl); administrative install; outbound HTTPS to TypeSafe; `TYPESAFE_API_KEY`. MariaDB / Windows / macOS not verified. |
| License | [GPL-2.0](https://github.com/maayanlevy/mysql-ailike/blob/80070b72edf22ebdf397a456fb049a1ec9844d26/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, docs, and mock-server tests layout inspected; Docker install and live Jev SQL judgments were not run on the review host. Discovered via X ([post](https://x.com/amasen02/status/2101630729910366424)) and GitHub. |

## When to use

Use it when you want semantic `WHERE` / join predicates over MySQL text columns without leaving SQL. Prefer [pg-jev](pg-jev.md) / [pg_typesafe](pg-typesafe.md) on PostgreSQL, or [JevSQL](jevsql.md) for SQLite helpers. Each uncached evaluation is an API call—narrow with ordinary SQL first.

## How it works

The plugin registers `AILIKE` / `ailike` UDFs that POST typed questions to `https://api.typesafe.ai/v1/systemone` ([`src/typesafe.cc`](https://github.com/maayanlevy/mysql-ailike/blob/80070b72edf22ebdf397a456fb049a1ec9844d26/src/typesafe.cc)). Unary form asks whether a value satisfies a natural-language condition; ternary form asks whether two values satisfy a described relationship. Returns `1`/`0`/`NULL`. Offline tests include a mock TypeSafe HTTP server (`tests/mock_typesafe.py`) and C++ unit tests.

## Get started

Follow upstream [install docs](https://github.com/maayanlevy/mysql-ailike/blob/80070b72edf22ebdf397a456fb049a1ec9844d26/docs/install.md) for the `v0.2.0` Linux plugin bundle, or the Docker demo in [docs/sample-data.md](https://github.com/maayanlevy/mysql-ailike/blob/80070b72edf22ebdf397a456fb049a1ec9844d26/docs/sample-data.md):

```sh
git clone https://github.com/maayanlevy/mysql-ailike.git
cd mysql-ailike
git checkout 80070b72edf22ebdf397a456fb049a1ec9844d26
# see docs/install.md for plugin install; Docker demo needs a TypeSafe key file
```

Live queries send evaluated column values and prompts to TypeSafe and can incur charges. This listing did not install the plugin or call live Jev.

## Examples and demos

- README Sakila `description AILIKE '…'` screenshots and join-demo SQL under `sql/`.
- Upstream reports 63 local/CI SQL checks on Linux ARM64/AMD64 for v0.2.0; live Sakila judgments reported by author—not re-run here.
- `tests/mock_typesafe.py` + `typesafe_test.cc` for offline HTTP client checks.

## Limits and data handling

Preview release. Column values and prompts leave the MySQL host on uncached evaluations. Managed MySQL must allow custom native plugins. GPL-2.0 applies to the plugin distribution—review compatibility with your deployment. Accuracy claims from sample judgments are not a general guarantee.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 80070b7](https://github.com/maayanlevy/mysql-ailike/tree/80070b72edf22ebdf397a456fb049a1ec9844d26): tag **v0.2.0**, GPL-2.0. AI-assisted source review of README, LICENSE, install docs, UDF/TypeSafe client, and test layout. No Docker install and no live TypeSafe calls on the review host.

Related: [pg-jev](pg-jev.md), [pg_typesafe](pg-typesafe.md), [JevSQL](jevsql.md).
