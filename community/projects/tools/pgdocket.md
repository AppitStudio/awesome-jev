# pgdocket (durable AI decisions for Postgres)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python tool that stores Jev decisions about Postgres rows as versioned, calibrated data kept current as rows change, with a `check` command that measures how trustworthy a decision is on your own table and a Phase 0 benchmark of jev-1.13.0 through pg-jev on 2,000 complaint narratives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ElyasEbrahim/pgdocket) |
| Maintainer | [ElyasEbrahim](https://github.com/ElyasEbrahim). Independently curated. |
| Format | Python CLI and worker with a Postgres ledger; Docker benchmark harness |
| Requirements | Postgres; Python; Docker for the benchmark harness; a TypeSafe key for live runs (mock and simulated backends need none). |
| License | [Apache-2.0](https://github.com/ElyasEbrahim/pgdocket/blob/4c404a2425fa88aa74691b3f0e6ef505497873ff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pgdocket/backend.py`](https://github.com/ElyasEbrahim/pgdocket/blob/4c404a2425fa88aa74691b3f0e6ef505497873ff/pgdocket/backend.py) at the pinned commit. |

## When to use

- Make semantic WHERE-style labels (from pg-jev or Jev directly) stable and auditable in production.
- Calibrate decision scores against about 100 of your own labels and get counts with confidence intervals.
- Mismatch: Phase 1 in progress; version comparison and other backend adapters are not built yet.

## How it works

You declare a decision once; `pgdocket/backend.py` sends rows to Jev's `/v1/systemone` (or any compatible endpoint), the ledger stores answers in Postgres, and the worker re-judges rows that change. `pgdocket check` calibrates against human labels, and `estimate` returns counts with intervals. The Phase 0 findings document over-confidence, run-to-run changes and batch-neighbour effects in jev-1.13.0. Integration evidence: [`pgdocket/backend.py`](https://github.com/ElyasEbrahim/pgdocket/blob/4c404a2425fa88aa74691b3f0e6ef505497873ff/pgdocket/backend.py).

## Get started

From the upstream README (not run on the review host):

```sh
make up      # Postgres 16 + pg-jev, mock API and simulated backend
make test
make bench   # simulated backend
cp .env.example .env   # add TYPESAFE_API_KEY
make bench BACKEND=jev ARGS=--yes   # prints estimated spend; refuses over $1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/phase0/FINDINGS-jev-1.13.md
- examples/quickstart/

## Limits and data handling

Row text goes to TypeSafe when you use the live backend. Phase 0 figures are the author's (about $0.30 of API calls); not rerun here.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 4c404a2425fa](https://github.com/ElyasEbrahim/pgdocket/tree/4c404a2425fa88aa74691b3f0e6ef505497873ff). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
