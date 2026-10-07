# postgres-search

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Algolia-style product search in plain PostgreSQL (whole and partial words, typos, barcodes, typeahead, facets) with an optional TypeSafe Jev second stage asking two questions per search — keep or sink each result, and which spelling the user meant; the README doubles as a dated evaluation report on 440k USDA products with failures, costs and threats to validity.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexforman1/postgres-search) |
| Maintainer | [alexforman1](https://github.com/alexforman1). Independently curated. |
| Format | SQL search functions with a Node demo server and evaluation scripts |
| Requirements | Docker and Node 22.18+ for the demo; a TypeSafe key for the optional Jev stage. |
| License | [MIT](https://github.com/alexforman1/postgres-search/blob/f8740e6d4f7ac3fe65476582e5af5f292f52c413/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Improve product search ranking and misspelling handling without leaving Postgres.
- Study a pre-registered style evaluation of a Jev re-rank stage.
- Mismatch: results are on USDA Branded Foods; your catalogue may differ.

## How it works

[`docs/jev.md`](https://github.com/alexforman1/postgres-search/blob/f8740e6d4f7ac3fe65476582e5af5f292f52c413/docs/jev.md) describes the two Jev questions; [`docs/how-it-works.md`](https://github.com/alexforman1/postgres-search/blob/f8740e6d4f7ac3fe65476582e5af5f292f52c413/docs/how-it-works.md) and [`docs/measurements.md`](https://github.com/alexforman1/postgres-search/blob/f8740e6d4f7ac3fe65476582e5af5f292f52c413/docs/measurements.md) cover the SQL stages and evaluation (model pinned to `jev-1.13.0`).

## Get started

Run the demo on a 100,000-product sample (README *Try it*):

```sh
git clone https://github.com/alexforman1/postgres-search && cd postgres-search
npm install
npm run db && npm run load
npm start   # http://localhost:3000
```

With the Jev stage enabled, each search makes Jev requests billed to your TypeSafe key.

## Examples and demos

- README *Summary* and *Results*.
- [Using it with your data](https://github.com/alexforman1/postgres-search/blob/f8740e6d4f7ac3fe65476582e5af5f292f52c413/docs/your-data.md).

## Limits and data handling

Search queries and candidate product text go to TypeSafe when the Jev stage is on. Reported accuracy figures are upstream results. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit f8740e6d4f7a](https://github.com/alexforman1/postgres-search/tree/f8740e6d4f7ac3fe65476582e5af5f292f52c413). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
