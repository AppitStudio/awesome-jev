# jev for DuckDB (judoaseeta)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

DuckDB extension port of pg-jev: `jev()`, `jev_prob()`, `jev_choice()` and `jev_score()` SQL functions ask TypeSafe Jev typed questions about each row. Distinct from the separately listed [duckdb-jev](duckdb-jev.md) by prasanthj.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/judoaseeta/duckdb-jev) |
| Maintainer | [judoaseeta](https://github.com/judoaseeta). Independently curated. |
| Format | C++ DuckDB extension |
| Requirements | DuckDB build toolchain (CMake, vcpkg) per README; `jev_api_key` set in SQL. |
| License | [MIT](https://github.com/judoaseeta/duckdb-jev/blob/58e548463b0bfb25d86bc68b11515a1daaf87ab3/LICENSE) |
| Jev evidence | [`src/include/jev_client.hpp`](https://github.com/judoaseeta/duckdb-jev/blob/58e548463b0bfb25d86bc68b11515a1daaf87ab3/src/include/jev_client.hpp) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Filter, rank or bucket DuckDB rows with natural-language conditions while keeping pg-jev function names portable.
- Mismatch: if you want the other DuckDB implementation, see [duckdb-jev](duckdb-jev.md); every judged row is a billed Jev call.

## How it works

Each function receives the row as a struct, batches rows into TypeSafe requests, and returns booleans, probabilities, choices or scores that compose with ordinary SQL. (Summarized from the upstream [README](https://github.com/judoaseeta/duckdb-jev/blob/58e548463b0bfb25d86bc68b11515a1daaf87ab3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): build the extension per the README, `LOAD jev;`, then `SET jev_api_key = '...';`.

## Limits and data handling

Row contents go to TypeSafe; batch size controls request count and cost. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 58e548463b0b](https://github.com/judoaseeta/duckdb-jev/tree/58e548463b0bfb25d86bc68b11515a1daaf87ab3). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
