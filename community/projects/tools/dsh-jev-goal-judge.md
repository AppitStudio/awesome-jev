# dsh-jev-goal-judge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeSafe Jev progress judgment between DeepSeek Harness goal rounds: one fan-out per round end, budgeted steer nudges, shadow mode by default and fail-open everywhere.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kittimzhe/dsh-jev-goal-judge) |
| Maintainer | [kittimzhe](https://github.com/kittimzhe). Independently curated. |
| Format | npm package `dsh-jev-goal-judge` |
| Requirements | DeepSeek Harness; TypeSafe key. |
| License | [MIT](https://github.com/kittimzhe/dsh-jev-goal-judge/blob/f8c7e829df31da65a02931cbab2723ae8081e54c/LICENSE) |
| Jev evidence | [`src/judge.ts`](https://github.com/kittimzhe/dsh-jev-goal-judge/blob/f8c7e829df31da65a02931cbab2723ae8081e54c/src/judge.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch stalled or drifting agent goals between rounds cheaply.
- Mismatch: DeepSeek Harness only.

## How it works

At each round end it sends one batched Jev request over progress questions; in enforce mode it injects limited steer nudges, otherwise it only logs. (Summarized from the upstream [README](https://github.com/kittimzhe/dsh-jev-goal-judge/blob/f8c7e829df31da65a02931cbab2723ae8081e54c/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `npm install dsh-jev-goal-judge` and register it per the README.

## Limits and data handling

Round summaries go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit f8c7e829df31](https://github.com/kittimzhe/dsh-jev-goal-judge/tree/f8c7e829df31da65a02931cbab2723ae8081e54c). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
