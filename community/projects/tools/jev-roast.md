# jev-roast (rubric scores for copy with Jev, citing exact source sentences for weak dimensions)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Node CLI and library that scores landing pages, résumés and similar copy against a declared rubric with TypeSafe Jev, then asks Jev to pick an original span only for weak dimensions so the report quotes the source byte-for-byte.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-roast) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js 22+ CLI/library (MIT; zero runtime deps) |
| Requirements | Node.js 22+ and `TYPESAFE_API_KEY` for live scoring (offline `--fake` demos available). |
| License | [MIT](https://github.com/gbesse/jev-roast/blob/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-client.mjs`](https://github.com/gbesse/jev-roast/blob/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499/src/jev-client.mjs) at the pinned commit. |

## When to use

- Score marketing or résumé copy against an explicit rubric.
- Need citations that are substrings of the original, not paraphrases.
- Mismatch: does not rewrite copy or suggest replacements.

## How it works

`src/jev-client.mjs` posts to `https://api.typesafe.ai/v1/systemone` with pinned `jev-1.13.0`; pass one scores dimensions, pass two chooses spans for weak marks. Integration evidence: [`src/jev-client.mjs`](https://github.com/gbesse/jev-roast/blob/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499/src/jev-client.mjs).

## Get started

Clone, run the offline demo, then set `TYPESAFE_API_KEY` for a live pack.

```sh
git clone https://github.com/gbesse/jev-roast.git && cd jev-roast
npm run demo
export TYPESAFE_API_KEY=...
node bin/jev-roast.mjs run examples/sample.txt --pack landing-page
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-roast/blob/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499/README.md](https://github.com/gbesse/jev-roast/blob/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499/README.md)

## Limits and data handling

Copy text is sent to TypeSafe on your key. Public alpha; English works best; arithmetic and counting remain weak.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 4555f9adf7a7](https://github.com/gbesse/jev-roast/tree/4555f9adf7a7aa5d0857f1a5b86a94d2d9e8c499). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
