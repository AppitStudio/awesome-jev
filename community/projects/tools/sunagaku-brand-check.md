# Sunagaku Brand Check (small app that scores a draft post against written brand criteria with OpenAI Decisions and Jev side by side; Japanese)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Small open-source React demo (loopback server) with fixed brand criteria (an interesting practice or lesson plus work-relevant expertise) that scores a draft post separately with OpenAI Decisions and TypeSafe Jev, keeps the two results independent and shows a comparison report. An eval script runs six synthetic examples through both providers and two instruction variants. The README is in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sean-sunagaku/sunagaku-brand-check) |
| Maintainer | [sean-sunagaku](https://github.com/sean-sunagaku). Independently curated. |
| Format | React demo served locally with tsx, plus a TypeScript evaluation script |
| Requirements | Node.js 22+; your own `OPENAI_API_KEY` and `TYPESAFE_API_KEY` in the local environment. |
| License | [MIT](https://github.com/sean-sunagaku/sunagaku-brand-check/blob/8214f18732dada5c2844a37be9c56263fda5722f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers.ts`](https://github.com/sean-sunagaku/sunagaku-brand-check/blob/8214f18732dada5c2844a37be9c56263fda5722f/src/providers.ts) at the pinned commit. |

## When to use

- Compare how two decision providers score the same brand criteria on short posts.
- Mismatch: a local comparison demo (loopback only) with author-set expectations, not a brand-safety service.

## How it works

`src/providers.ts` keeps independent adapters: the Jev one uses the `@typesafe-ai/sdk` client (`jev-1.13.0`) to ask typed choice questions with shared state, no retries and a 12 s timeout, and validates the answer schema before the comparison view. Integration evidence: [`src/providers.ts`](https://github.com/sean-sunagaku/sunagaku-brand-check/blob/8214f18732dada5c2844a37be9c56263fda5722f/src/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run check
export OPENAI_API_KEY=...
export TYPESAFE_API_KEY=...
npm run dev   # http://127.0.0.1:4300
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the criteria, run steps and evaluation (Japanese): [github.com/sean-sunagaku/sunagaku-brand-check#readme](https://github.com/sean-sunagaku/sunagaku-brand-check#readme)
- Design notes: [github.com/sean-sunagaku/sunagaku-brand-check/blob/main/docs/design.md](https://github.com/sean-sunagaku/sunagaku-brand-check/blob/main/docs/design.md)

## Limits and data handling

Draft text goes to OpenAI and TypeSafe on your keys, and `npm run eval` costs API fees (up to 24 calls). Expectations are the author's own, and raw confidence is not comparable between providers. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 8214f18732da](https://github.com/sean-sunagaku/sunagaku-brand-check/tree/8214f18732dada5c2844a37be9c56263fda5722f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
