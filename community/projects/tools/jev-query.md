# jev-query

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript natural-language-to-PostgreSQL composer where the model never writes SQL: code enumerates the legal moves of a typed QueryPlan, Jev (or a self-hosted logprob oracle) assigns probabilities, and code compiles parameterized SQL or asks a clarifying question.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jaketimothy/jev-query) |
| Maintainer | [jaketimothy](https://github.com/jaketimothy). Independently curated. |
| Format | TypeScript library (`package.json` 0.1.0; npm package not found at review — install from source) |
| Requirements | Node.js 20+; `pg` or `@electric-sql/pglite`; `JEV_API_KEY`, `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` for `JevOracle`. |
| License | [MIT](https://github.com/jaketimothy/jev-query/blob/029239c8c2a9c2fcb7549363931d12c1a097b6c7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add a natural-language query box to an app without letting a model emit raw SQL.
- Turn low-confidence interpretations into clarifying questions built from the runner-up options.
- Mismatch: v1 composes a defined set of query shapes; writes and unrelated requests are declined.

## How it works

A schema model drives a `Composer` that enumerates legal next moves; the `Oracle` interface (`JevOracle` in [`src/oracle/jev.ts`](https://github.com/jaketimothy/jev-query/blob/029239c8c2a9c2fcb7549363931d12c1a097b6c7/src/oracle/jev.ts), default endpoint OpenRouter's `/v1/systemone`, or TypeSafe/Workers AI via `JEV_URL`) returns probabilities in batched rounds (typically three or four). Code assembles, validates and compiles the plan; `execute()` runs in a `READ ONLY` transaction with a statement timeout.

## Get started

The README documents `npm install jev-query`, but no npm package was found at review; build from source:

```sh
git clone https://github.com/jaketimothy/jev-query.git
cd jev-query
npm install && npm run build
export OPENROUTER_API_KEY=...   # or TYPESAFE_API_KEY with JEV_URL
# Composer.create({ db: fromPg(pool), oracle: new JevOracle() })
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README request-flow walkthrough and the *Evaluation on `nlsql-testbed`* section (maintainer-reported).
- PGlite option for in-process demos and tests.

## Limits and data handling

Question text and schema-derived options go to the oracle provider. Use a read-only database role and Postgres RLS for tenancy (upstream guidance). Evaluation numbers are upstream. npm availability unverified. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 029239c8c2a9](https://github.com/jaketimothy/jev-query/tree/029239c8c2a9c2fcb7549363931d12c1a097b6c7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
