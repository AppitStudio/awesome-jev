# stale-claims by Hamza Ahmad Aslam (CLI that finds time-sensitive claims in your docs with no as-of date, with Jev judging each one)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Finds sentences in documentation that are true only for a while (versions, prices, dates, statistics, status, people and roles) and carry no as-of date, before the docs are indexed for retrieval. Word lists pick candidates and work out document age in code; Jev answers narrow typed questions about each, and one threshold puts them on a review list or a check-by-hand list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/stale-claims) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/stale-claims/blob/eb686414e159c9154117fa059bd26357ae92c323/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/stale-claims/blob/eb686414e159c9154117fa059bd26357ae92c323/src/jev.mjs) at the pinned commit. |

## When to use

- Docs owners and RAG builders who want undated prices, versions and status claims found before indexing.
- Mismatch: fact-checking; it flags claims that may age, not whether they are true today.

## How it works

`src/jev.mjs` posts batches of up to 20 claims to `https://api.typesafe.ai/v1/systemone` with typed questions from `src/questions.mjs`, including one that flags text written to steer a model; code applies `--threshold` (default 0.8). Sentences matching injection patterns are listed and never sent. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/stale-claims/blob/eb686414e159c9154117fa059bd26357ae92c323/src/jev.mjs).

## Get started

Install from npm and point it at a docs folder; `--dry-run` shows the candidates, questions and a token estimate without sending anything.

```sh
npm install -g @hamzaahmadaslam/stale-claims
export TYPESAFE_API_KEY=...
stale-claims docs/ --dry-run
stale-claims docs/ --date-from git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example report: [github.com/hamzaahmadaslam/stale-claims/blob/main/examples/report.txt](https://github.com/hamzaahmadaslam/stale-claims/blob/main/examples/report.txt)

## Limits and data handling

Candidate sentences go to TypeSafe; code blocks, navigation and matched injection text do not. Jev reads dates as text, so age comparisons are done in code. English works best.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit eb686414e159](https://github.com/hamzaahmadaslam/stale-claims/tree/eb686414e159c9154117fa059bd26357ae92c323). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
