# clickhouse-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Natural-language predicates, probabilities and classification for ClickHouse via executable UDFs backed by TypeSafe Jev; inspired by pg-jev with a separate columnar implementation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ahwlsqja/clickhouse-jev) |
| Maintainer | [ahwlsqja](https://github.com/ahwlsqja). Independently curated. |
| Format | Python (stdlib) executable UDFs |
| Requirements | ClickHouse with executable UDFs; Python; TypeSafe key. |
| License | [MIT](https://github.com/ahwlsqja/clickhouse-jev/blob/196960f6977213a347ba54010acf69239f14a035/LICENSE) |
| Jev evidence | [`clickhouse_jev/protocol.py`](https://github.com/ahwlsqja/clickhouse-jev/blob/196960f6977213a347ba54010acf69239f14a035/clickhouse_jev/protocol.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Filter or classify ClickHouse rows with natural-language conditions.
- Mismatch: every evaluated row costs a Jev call; batch large scans.

## How it works

ClickHouse streams rows to the UDF process, which batches them into Jev requests and returns typed results. (Summarized from the upstream [README](https://github.com/ahwlsqja/clickhouse-jev/blob/196960f6977213a347ba54010acf69239f14a035/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the UDF config and script per the README.

## Limits and data handling

Row data goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 196960f69772](https://github.com/ahwlsqja/clickhouse-jev/tree/196960f6977213a347ba54010acf69239f14a035). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
