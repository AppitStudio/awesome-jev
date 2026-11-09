# Jev実験レポート集 (sample code and measurements for a Japanese book of 11 Jev experiments)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Companion repo to a Japanese book: 11 experiments (text classification, document matching, image judgments) plus SO-101 robot-arm observations, measuring Jev accuracy, cost and latency; saved results re-aggregate without the API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akiraNuma/jev-experiments) |
| Maintainer | [akiraNuma](https://github.com/akiraNuma). Independently curated. |
| Format | TypeScript samples + data (MIT) |
| Requirements | Node.js 22.12+, npm, and a TypeSafe key for live calls. |
| License | [MIT](https://github.com/akiraNuma/jev-experiments/blob/5f865257e9e46cb332b1ab5026d8d498daf9ad89/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/jev.ts`](https://github.com/akiraNuma/jev-experiments/blob/5f865257e9e46cb332b1ab5026d8d498daf9ad89/harness/jev.ts) at the pinned commit. |

## When to use

- Learn Jev through measured, reproducible experiments.
- Re-aggregate published results offline.
- Mismatch: the book text itself is not included; docs are Japanese.

## How it works

`harness/jev.ts` wraps `TypeSafeClient` and `noul` from `@typesafe-ai/sdk`; `examples/first.ts` is chapter 1's first call and the stored results reproduce each chapter's numbers. Integration evidence: [`harness/jev.ts`](https://github.com/akiraNuma/jev-experiments/blob/5f865257e9e46cb332b1ab5026d8d498daf9ad89/harness/jev.ts).

## Get started

Clone the `v1` tag, run `npm ci`, set `TYPESAFE_API_KEY` and run `npm run example:first`.

```sh
git clone -b v1 https://github.com/akiraNuma/jev-experiments.git && cd jev-experiments
npm ci
export TYPESAFE_API_KEY=...
npm run example:first
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/akiraNuma/jev-experiments/blob/5f865257e9e46cb332b1ab5026d8d498daf9ad89/README.md](https://github.com/akiraNuma/jev-experiments/blob/5f865257e9e46cb332b1ab5026d8d498daf9ad89/README.md)

## Limits and data handling

Experiment inputs go to TypeSafe on your key; re-aggregation is offline.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 5f865257e9e4](https://github.com/akiraNuma/jev-experiments/tree/5f865257e9e46cb332b1ab5026d8d498daf9ad89). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
