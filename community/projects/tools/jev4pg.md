# jev4pg

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Natural-language-to-SQL and semantic operators for PostgreSQL: TypeSafe Jev answers typed questions per record while PostgreSQL handles joins and aggregation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sheltercosmo/jev4pg) |
| Product homepage | [jev4pg.com](https://jev4pg.com) |
| Maintainer | [Sheltercosmo](https://github.com/Sheltercosmo). Submitted by the maintainer in [issue #994](https://github.com/AppitStudio/awesome-jev/issues/994) with AI assistance disclosed. |
| Format | Application, HTTP API, and PostgreSQL interface (v0.7.0 at review; native execution and explainable embeddings are a development preview) |
| Requirements | Python 3.11+, Docker Compose, and PostgreSQL per the [installation guide](https://github.com/Sheltercosmo/jev4pg/blob/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f/docs/INSTALLATION.md). Hosted Jev uses `TYPESAFE_API_KEY` (or `SDD_JEV_API_KEY`) and `SDD_JEV_MODEL=jev-1.13.0`; hybrid planning also needs an LLM provider. The native preview targets PostgreSQL 17 on Linux. |
| License | [Apache-2.0](https://github.com/Sheltercosmo/jev4pg/blob/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f/LICENSE). External project keeps its own license. |
| Disclosure | Maintainer self-submission ([issue #994](https://github.com/AppitStudio/awesome-jev/issues/994)); AI-assisted catalog review. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Filter or tag free-text columns (support messages, documents) with reviewed yes/no definitions and keep the probabilities for later threshold changes.
- Ask natural-language questions over a PostgreSQL database where Jev selects context and plans without an LLM generation call, or combine it with an LLM in hybrid mode.
- Mismatch: if you only need exact SQL over structured columns, plain SQL is cheaper and deterministic.

## How it works

jev4pg sends selected record text and context to a System One endpoint (`https://api.typesafe.ai/v1/systemone` by default) as typed question batches, for example a Noul predicate per record ([evaluator implementation](https://github.com/Sheltercosmo/jev4pg/blob/a42404951c566571eb2322561295bd87e8771bc6/sdd/evaluators.py#L105-L163)). PostgreSQL executes joins, grouping, and aggregation. Named semantic features store a reviewed definition and evidence cache so a threshold change can reuse earlier observations. [Provider configuration](https://github.com/Sheltercosmo/jev4pg/blob/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f/docs/PROVIDERS.md) also documents compatible HTTP endpoints and local Python adapters.

## Get started

Follow the upstream [installation guide](https://github.com/Sheltercosmo/jev4pg/blob/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f/docs/INSTALLATION.md) (Docker Compose + PostgreSQL), then set the provider variables before running live queries:

```sh
git clone https://github.com/Sheltercosmo/jev4pg.git
cd jev4pg
# configure .env per docs/INSTALLATION.md, then for hosted Jev:
# TYPESAFE_API_KEY=<your key>
# SDD_JEV_MODEL=jev-1.13.0
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Project guide](https://jev4pg.com/guide/) with SQL examples; it distinguishes the release from the native preview.
- [NL2SQL query tutorial](https://github.com/Sheltercosmo/jev4pg/tree/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f/examples/nl2sql) with a runnable dataset and expected results (live provider required).
- Upstream README reports a historical BIRD Challenging comparison (Jev 20/99 vs an LLM baseline 39/99); that is the maintainer's result, not reproduced here.

## Limits and data handling

Hosted inference sends selected record text and context to TypeSafe (or the configured provider) and incurs separate provider charges. Custom endpoints never inherit `TYPESAFE_API_KEY`; redirects are rejected. Native execution and explainable embeddings are development-preview features.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 4d6b03c14a98](https://github.com/Sheltercosmo/jev4pg/tree/4d6b03c14a98e943659f05b1300b0bfb5c5c9b9f). Inspected README, `docs/PROVIDERS.md`, the provider request/response code in `sdd/evaluators.py`, and the LICENSE. The submitter reports inspecting provider tests at `a424049`; no installation or live inference was run for this listing. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
