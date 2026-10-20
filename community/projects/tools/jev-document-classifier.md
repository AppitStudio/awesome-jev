# Document classifier (financial document types)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Node app and benchmark that names a financial document's type (10-K, proxy statement, fund fact sheet, trade confirmation and 17 more) with one Jev Choice call, compared on 43 synthetic documents against frontier and small LLMs, a bi-encoder and keyword rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LandoCole/document-classifier) |
| Maintainer | [LandoCole](https://github.com/LandoCole). Independently curated. |
| Format | Node.js web demo, serverless API route and benchmark scripts |
| Requirements | Node.js and npm; a TypeSafe key (`TYPESAFE_API_KEY`) for live classification; LLM keys only to rerun the comparison. |
| License | [MIT](https://github.com/LandoCole/document-classifier/blob/d3a220cf901b7935dd766510979c9b175761f689/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/LandoCole/document-classifier/blob/d3a220cf901b7935dd766510979c9b175761f689/src/jev.js) at the pinned commit. |

## When to use

- Route incoming filings and statements by type before any other processing.
- See a reproducible cost and latency comparison of a decision model against LLMs on one routing task.
- Mismatch: 43 synthetic documents; the author calls the numbers a demonstration, not a leaderboard.

## How it works

`src/excerpt.js` cuts long documents to an outline (opening, headings, closing). `src/jev.js` sends the excerpt and the 21 type definitions to `/v1/systemone` as one Choice question and returns the type with its probability, so a pipeline can file confident answers and send close calls to a person. `bench/run.js` runs the same excerpts through each comparison method. Integration evidence: [`src/jev.js`](https://github.com/LandoCole/document-classifier/blob/d3a220cf901b7935dd766510979c9b175761f689/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/LandoCole/document-classifier.git && cd document-classifier
npm ci
export TYPESAFE_API_KEY=...
npm run demo     # local web demo
npm run bench    # reproduce bench/results.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [landonthornton.com/classifier/](https://landonthornton.com/classifier/)
- bench/results.json (Jev 43/43 at 136 ms median, per the README)

## Limits and data handling

Document excerpts go to TypeSafe (and to the LLM providers if you rerun the comparison). Benchmark figures are the author's, on synthetic documents; not rerun here.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit d3a220cf901b](https://github.com/LandoCole/document-classifier/tree/d3a220cf901b7935dd766510979c9b175761f689). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
