# JevRAG Workbench by ashishdhillon (side-by-side comparison of naive vector RAG and a three-stage Jev-gated RAG)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

A Next.js workbench that runs the same document and question through naive top-15 vector RAG and a Jev-gated pipeline: a pre-retrieval router, a parallel filter and rerank that keeps chunks contradicting a false premise, and a sufficiency gate that can block generation. Three presets show a missing-information trap, a false-premise question and a noisy-context case, with a decision trace and a report export.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashishdhillon/jevrag-workbench) |
| Maintainer | [ashishdhillon](https://github.com/ashishdhillon). Independently curated. |
| Format | Next.js web app |
| Requirements | Node.js; a TypeSafe API key and an OpenAI-compatible key for live runs (without keys it runs in a simulated demo mode). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev-client.ts`](https://github.com/ashishdhillon/jevrag-workbench/blob/e1e7d4c0791789f7eb550f166251b49a6af3beb0/lib/jev-client.ts) at the pinned commit. |

## When to use

- Show, on one screen, what Jev gates add to a RAG pipeline: routing, premise checks and refusing to answer without support.
- Mismatch: judging real results from demo mode; without keys the Jev results are simulated.

## How it works

`lib/jev-client.ts` posts Choice, Noul and Score questions to `JEV_BASE_URL` (default `https://api.typesafe.ai/v1/systemone`) with a 5-second fail-open that falls back to standard top-5 RAG. Generation uses the OpenAI SDK with a configurable base URL. Integration evidence: [`lib/jev-client.ts`](https://github.com/ashishdhillon/jevrag-workbench/blob/e1e7d4c0791789f7eb550f166251b49a6af3beb0/lib/jev-client.ts).

## Get started

Install and run; add keys in the settings dialog for live runs.

```sh
git clone https://github.com/ashishdhillon/jevrag-workbench && cd jevrag-workbench
npm install
npm run dev   # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev client: [github.com/ashishdhillon/jevrag-workbench/blob/e1e7d4c0791789f7eb550f166251b49a6af3beb0/lib/jev-client.ts](https://github.com/ashishdhillon/jevrag-workbench/blob/e1e7d4c0791789f7eb550f166251b49a6af3beb0/lib/jev-client.ts)

## Limits and data handling

Demo mode uses calibrated simulations, not Jev calls, so its numbers (such as about 78% prompt-token savings) are illustrative. Live runs send the query and chunks to TypeSafe and the generator. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit e1e7d4c07917](https://github.com/ashishdhillon/jevrag-workbench/tree/e1e7d4c0791789f7eb550f166251b49a6af3beb0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
