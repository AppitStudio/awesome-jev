# text-to-sql-guardrails (a local LLM writes SQL; deterministic guards and Jev decide whether it runs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Text-to-SQL assistant where the model that writes the query is not the one that decides whether it runs: Jev first classifies the request (answerable, needs clarification, injection), deterministic guards enforce an allowlist, read-only access and limits, and a second Jev request checks the SQL and result answer the question. Measured on 124 gold questions against an LLM alone with the policy in its prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Guilherme-pxt/text-to-sql-guardrails) |
| Maintainer | [Guilherme-pxt](https://github.com/Guilherme-pxt). Independently curated. |
| Format | Python (numpy, SQLite) with a local Ollama server |
| Requirements | Python, numpy and Ollama; a TypeSafe API key for the Jev decisions. |
| License | [MIT](https://github.com/Guilherme-pxt/text-to-sql-guardrails/blob/7b2527de143ee610794ded650cb14ac275cf3dc4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sqlguard/jev.py`](https://github.com/Guilherme-pxt/text-to-sql-guardrails/blob/7b2527de143ee610794ded650cb14ac275cf3dc4/sqlguard/jev.py) at the pinned commit. |

## When to use

- Put a decision step and hard guards between an LLM and your database.
- Mismatch: synthetic company data; results are the author's.

## How it works

`sqlguard/jev.py` posts the question (and later the SQL and result) to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`); the pipeline turns the probabilities into run, ask or refuse. Integration evidence: [`sqlguard/jev.py`](https://github.com/Guilherme-pxt/text-to-sql-guardrails/blob/7b2527de143ee610794ded650cb14ac275cf3dc4/sqlguard/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Guilherme-pxt/text-to-sql-guardrails && cd text-to-sql-guardrails
python3 -m sqlguard run-all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/Guilherme-pxt/text-to-sql-guardrails#readme](https://github.com/Guilherme-pxt/text-to-sql-guardrails#readme)

## Limits and data handling

Questions, generated SQL and result samples go to TypeSafe. The database stays local.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7b2527de143e](https://github.com/Guilherme-pxt/text-to-sql-guardrails/tree/7b2527de143ee610794ded650cb14ac275cf3dc4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
