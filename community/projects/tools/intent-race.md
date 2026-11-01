# Intent Race (side-by-side race of Jev against a frontier LLM classifying 1,000 search keywords by intent)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Web demo that classifies 1,000 search keywords into informational, commercial, transactional and navigational intent with Jev (four yes/no questions per keyword) and races it against an LLM, adding up speed and cost live. By default the LLM side is simulated from measured call times and list prices, which the README states plainly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/admin-selka/intent-race) |
| Maintainer | [admin-selka](https://github.com/admin-selka). Independently curated. |
| Format | Node.js web app |
| Requirements | Node.js; a Vercel AI Gateway or OpenRouter key for live Jev calls. |
| License | [MIT](https://github.com/admin-selka/intent-race/blob/8708531be859a008f35e995f2f690cea4aa364f9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`intent-race/api.mjs`](https://github.com/admin-selka/intent-race/blob/8708531be859a008f35e995f2f690cea4aa364f9/intent-race/api.mjs) at the pinned commit. |

## When to use

- See Jev's latency and cost on a bulk tagging job next to an LLM.
- Mismatch: the LLM side is simulated by default; not a rigorous benchmark.

## How it works

`intent-race/api.mjs` asks `typesafe-ai/jev` (or `typesafe/jev-1.13` on OpenRouter) four intent questions per keyword and tags anything at 50% or more; `record-jev.mjs` can record one full Jev pass for replay. Integration evidence: [`intent-race/api.mjs`](https://github.com/admin-selka/intent-race/blob/8708531be859a008f35e995f2f690cea4aa364f9/intent-race/api.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/admin-selka/intent-race#readme](https://github.com/admin-selka/intent-race#readme)

## Limits and data handling

Keywords are sent to the configured Jev provider. Numbers are the author's measurements. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 8708531be859](https://github.com/admin-selka/intent-race/tree/8708531be859a008f35e995f2f690cea4aa364f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
