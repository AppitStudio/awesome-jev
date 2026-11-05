# MariaDB Jev (native MariaDB functions for semantic predicates backed by TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MariaDB plugin that adds `jev_all`, `jev_any` and `jev_probability` SQL functions so one row can carry up to eight natural-language conditions in a single TypeSafe Jev request. Initial open-source release; not a throughput claim.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/mariadb-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | MariaDB C++ plugin (MIT) |
| Requirements | Linux MariaDB with CMake, libcurl and Jansson; set `JEV_API_KEY` / `TYPESAFE_API_KEY` in the **server** environment before start. |
| License | [MIT](https://github.com/gbesse/mariadb-jev/blob/82ee9f721cc79b183113f62f9d45681466562b9d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engine.cpp`](https://github.com/gbesse/mariadb-jev/blob/82ee9f721cc79b183113f62f9d45681466562b9d/src/engine.cpp) at the pinned commit. |

## When to use

- Filter rows with natural-language predicates after classical SQL filters.
- Batch up to eight conditions per row into one Jev call.
- Mismatch: each uncached row is an HTTPS call; not a vector index.

## How it works

`src/engine.cpp` reads the TypeSafe key from the environment and posts to `https://api.typesafe.ai/v1/systemone`; SQL helpers expose all/any/probability semantics with per-expression caching. Integration evidence: [`src/engine.cpp`](https://github.com/gbesse/mariadb-jev/blob/82ee9f721cc79b183113f62f9d45681466562b9d/src/engine.cpp).

## Get started

From the upstream README (not run on the review host):

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build --parallel
# copy build/mariadb_jev.so into plugin_dir, run sql/install.sql, set JEV_API_KEY in the server env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/mariadb-jev/blob/82ee9f721cc79b183113f62f9d45681466562b9d/README.md](https://github.com/gbesse/mariadb-jev/blob/82ee9f721cc79b183113f62f9d45681466562b9d/README.md)

## Limits and data handling

Row text and conditions leave MariaDB toward TypeSafe. Defaults cap requests and payload sizes; filter with ordinary columns first.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 82ee9f721cc7](https://github.com/gbesse/mariadb-jev/tree/82ee9f721cc79b183113f62f9d45681466562b9d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
