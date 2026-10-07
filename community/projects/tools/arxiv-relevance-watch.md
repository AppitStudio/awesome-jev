# arxiv-relevance-watch

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Zero-dependency Node CLI that screens arXiv for one research topic and ranks papers with five typed questions to a System One decision model (Jev via OpenRouter, TypeSafe or a local `/v1/systemone`), with no generative model anywhere and a second stage for reading survivors against your open items.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/johnlam1968/arxiv-relevance-watch) |
| Maintainer | [johnlam1968](https://github.com/johnlam1968). Independently curated. |
| Format | Node CLI (`src/cli.mjs`, `src/read.mjs`) with JSON topic/question configs; no npm dependencies |
| Requirements | Node.js; `--dry-run` needs no key; scoring needs `OPENROUTER_API_KEY` (default), a TypeSafe key or a local `/v1/systemone` endpoint. |
| License | [MIT](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Track new papers on a narrow subject and see exactly why each was ranked.
- Re-point the question set and topic profile at your own field by editing JSON.
- Mismatch: it reads only titles, authors, categories and abstracts and never summarises; scores are relative ranks, not calibrated probabilities.

## How it works

[`src/arxiv.mjs`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/src/arxiv.mjs) queries the arXiv API with your keyword patterns; [`src/systemone.mjs`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/src/systemone.mjs) sends each paper with the instrument in [`config/questions-paper-relevance.json`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/config/questions-paper-relevance.json) (on-topic Noul, overlap Score, open-problem and worth-reading Nouls, relation Choice). A paper is reported when it clears both a rank and an on-topic threshold; seen-state prevents re-reporting.

## Get started

Screen for free, then score:

```sh
git clone https://github.com/johnlam1968/arxiv-relevance-watch && cd arxiv-relevance-watch
node src/cli.mjs --dry-run           # no model, no key
export OPENROUTER_API_KEY=sk-or-...
node src/cli.mjs
```

Upstream estimates about $0.001 per run of 20–40 papers on the default model; `--dry-run` is free.

## Examples and demos

- Sample report: [`examples/sample-report.md`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/examples/sample-report.md); worked example: [`docs/worked-example.md`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/docs/worked-example.md).
- Authoring your own question set: [`docs/authoring-question-sets.md`](https://github.com/johnlam1968/arxiv-relevance-watch/blob/488369074b3c9187115d23966d20a2860b06794a/docs/authoring-question-sets.md).

## Limits and data handling

Paper metadata and abstracts go to the chosen decision service; keyword queries bound recall. Cost is an upstream estimate. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 488369074b3c](https://github.com/johnlam1968/arxiv-relevance-watch/tree/488369074b3c9187115d23966d20a2860b06794a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
