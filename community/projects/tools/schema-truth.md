# schema-truth by Hamza Ahmad Aslam (CLI that checks whether a page's JSON-LD prices, ratings, dates and FAQ answers are really shown to visitors, with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

For SEO specialists and developers who look after structured data: reads a page's JSON-LD claims (price, availability, rating, review, author, date, headline, FAQ answer, address, phone) and asks Jev, one yes/no question per value, whether the visible page text supports it. Each claim comes back supported, unsupported or review, so drifted markup such as a stale price is caught before search engines see it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/schema-truth) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/schema-truth/blob/b302e1887dba56221e7b7b07245f52b1b143cfcf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/schema-truth/blob/b302e1887dba56221e7b7b07245f52b1b143cfcf/src/jev.mjs) at the pinned commit. |

## When to use

- Shops and publishers that want a CI check that their JSON-LD matches what visitors actually see.
- Mismatch: pages built by client-side scripts (save the rendered HTML instead) or Microdata/RDFa markup, which are not read.

## How it works

`src/jev.mjs` sends one request per page to `https://api.typesafe.ai/v1/systemone`: the visible text is the state and each claim is a `noul` question with the claim passed as data. Code normalises ISO dates and availability URLs to words first, and the verdict uses one threshold (0.8 by default). Exit code 1 when a claim is unsupported, for CI. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/schema-truth/blob/b302e1887dba56221e7b7b07245f52b1b143cfcf/src/jev.mjs).

## Get started

Install from npm, set your key and check a URL, several URLs or a folder of saved HTML pages.

```sh
npm install -g @hamzaahmadaslam/schema-truth
export TYPESAFE_API_KEY=...
schema-truth page.html --dry-run   # claims and token estimate; nothing sent
schema-truth https://shop.example/trail-runner-2
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worked example in the README: [github.com/hamzaahmadaslam/schema-truth#example](https://github.com/hamzaahmadaslam/schema-truth#example)

## Limits and data handling

Visible page text and claims go to TypeSafe. Scripts and stylesheets are not run, so text hidden only by CSS counts as visible. Jev reads numbers and dates as text and the tool does no arithmetic, so prices in another currency or ratings shown as percentages usually go to review. Text written to steer a model can move answers; the tool never edits anything.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit b302e1887dba](https://github.com/hamzaahmadaslam/schema-truth/tree/b302e1887dba56221e7b7b07245f52b1b143cfcf). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
