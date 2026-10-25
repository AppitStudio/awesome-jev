# Deterministic Text-to-SQL (Jev picks schema slots, sqlglot builds the SQL AST)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Japanese-documented text-to-SQL engine that never lets a model write SQL: Jev classifies the question into dataset, field and metric slots generated from a semantic schema, foreign-key paths come from a NetworkX graph search, and the query is assembled as a sqlglot AST; a mock mode runs offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snaga/Deterministic-Text-to-SQL) |
| Maintainer | [snaga](https://github.com/snaga). Independently curated. |
| Format | Python package |
| Requirements | Python 3.11+; a TypeSafe API key for live classification (offline demos use a mock). |
| License | [Apache-2.0](https://github.com/snaga/Deterministic-Text-to-SQL/blob/06a80cb03eefab4ca5831a979d63657b35451cf9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/deterministic_text_to_sql/jev/client.py`](https://github.com/snaga/Deterministic-Text-to-SQL/blob/06a80cb03eefab4ca5831a979d63657b35451cf9/src/deterministic_text_to_sql/jev/client.py) at the pinned commit. |

## When to use

- Answer natural-language analytics questions with SQL that is assembled, not generated.
- Build Jev criteria automatically from your schema's datasets, fields, metrics and synonyms.
- Mismatch: README is in Japanese; tutorial uses TPC-H.

## How it works

`jev/client.py` posts the question and schema-derived criteria to `https://api.typesafe.ai/v1/systemone` with retries and timeout handling; the chosen slots feed a deterministic AST builder. Integration evidence: [`src/deterministic_text_to_sql/jev/client.py`](https://github.com/snaga/Deterministic-Text-to-SQL/blob/06a80cb03eefab4ca5831a979d63657b35451cf9/src/deterministic_text_to_sql/jev/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -e .
export TYPESAFE_API_KEY=...
python examples/tpch/run_tutorial.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Article (Japanese): [zenn.dev/snaga/articles/2026-10-25-deterministic-text-to-sql-jev-ast](https://zenn.dev/snaga/articles/2026-10-25-deterministic-text-to-sql-jev-ast)
- README: [github.com/snaga/Deterministic-Text-to-SQL#readme](https://github.com/snaga/Deterministic-Text-to-SQL#readme)

## Limits and data handling

The user question and schema-derived criteria go to TypeSafe; database rows are not sent. Generated SQL still runs against your own database.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 06a80cb03eef](https://github.com/snaga/Deterministic-Text-to-SQL/tree/06a80cb03eefab4ca5831a979d63657b35451cf9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
