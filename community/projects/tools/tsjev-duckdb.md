# tsjev for DuckDB

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DuckDB extension from Querio that adds SQL functions to classify, filter, and score table rows with TypeSafe Jev, with deduplication of identical rows, memory and disk caching, and 32 concurrent requests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Querio-App/duckdb-jev) |
| Maintainer | [Querio-App](https://github.com/Querio-App). Independently curated. |
| Format | DuckDB extension (C++) |
| Requirements | DuckDB; TypeSafe API key. |
| License | [MIT](https://github.com/Querio-App/duckdb-jev/blob/b73aad10d0f69131ca8f5dd95996b6b0cffd71d1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/include/tsjev/tsjev.hpp`](https://github.com/Querio-App/duckdb-jev/blob/b73aad10d0f69131ca8f5dd95996b6b0cffd71d1/src/include/tsjev/tsjev.hpp) at the pinned commit. |

## When to use

- Label or filter rows in SQL, such as support tickets by topic.
- Need caching and dedupe so large tables stay cheap.
- Mismatch: build the extension yourself; every uncached row is a paid call.

## How it works

Functions like `tsjev_label(text, [options])` send each distinct value to Jev with a pinned model id so answers and the cache stay stable; results come back as SQL values. Integration evidence: [`src/include/tsjev/tsjev.hpp`](https://github.com/Querio-App/duckdb-jev/blob/b73aad10d0f69131ca8f5dd95996b6b0cffd71d1/src/include/tsjev/tsjev.hpp).

## Get started

From the upstream README: build and load the extension, set your TypeSafe key, then call the `tsjev_*` functions in queries.

```sh
SELECT tsjev_label(body, ['billing', 'bug', 'feature request', 'other']) AS topic, count(*)
FROM tickets GROUP BY ALL;
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README function reference
- src/include/tsjev/tsjev.hpp

## Limits and data handling

Row text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit b73aad10d0f6](https://github.com/Querio-App/duckdb-jev/tree/b73aad10d0f69131ca8f5dd95996b6b0cffd71d1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
