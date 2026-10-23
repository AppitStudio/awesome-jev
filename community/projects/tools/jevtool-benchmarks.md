# jevtool benchmarks (weekly leaderboard of System One models on OpenRouter)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Weekly run of every decision model on OpenRouter's Decisions API, including Jev, against jevtool's ten example suites, publishing mean accuracy, the share you could automate at 95% accuracy, median latency and cost per 1,000 calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jevtool/benchmarks) |
| Maintainer | [jevtool](https://github.com/jevtool). Independently curated. |
| Format | Benchmark repository and leaderboard (Node.js) |
| Requirements | Node.js; an OpenRouter API key to rerun it. |
| License | [MIT](https://github.com/jevtool/benchmarks/blob/f80644c4798fb96bcf8423c1e95ba2017c34e5c6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.mjs`](https://github.com/jevtool/benchmarks/blob/f80644c4798fb96bcf8423c1e95ba2017c34e5c6/run.mjs) at the pinned commit. |

## When to use

- Compare Jev with other decision models on accuracy, automation share, latency and cost.
- Rerun the same suites on your own data with jevtool.
- Mismatch: ten small example suites, not a domain benchmark for your workload.

## How it works

`run.mjs` loads jevtool's example suites and evaluates each OpenRouter decision model (including `typesafe/jev-1.13` and `typesafe/jev-1.14`) through jevtool's client, then rewrites the leaderboard table in the README. Integration evidence: [`run.mjs`](https://github.com/jevtool/benchmarks/blob/f80644c4798fb96bcf8423c1e95ba2017c34e5c6/run.mjs).

## Get started

From the repository (not run on the review host; needs an OpenRouter key):

```sh
npm install
node run.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Leaderboard page: [jevtool.dev/leaderboard](https://jevtool.dev/leaderboard)

## Limits and data handling

Results are the maintainer's own measurements on example suites; rankings move weekly.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit f80644c4798f](https://github.com/jevtool/benchmarks/tree/f80644c4798fb96bcf8423c1e95ba2017c34e5c6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
