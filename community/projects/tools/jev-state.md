# jev-state

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript helpers that turn raw app and game state into state TypeSafe Jev reads well; author benchmark reports 74% → 100% accuracy with 43% fewer tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suranjaychandra/jev-state) |
| Maintainer | [suranjaychandra](https://github.com/suranjaychandra). Independently curated. |
| Format | TypeScript library |
| Requirements | Node.js; TypeSafe key for benchmarks. |
| License | [MIT](https://github.com/suranjaychandra/jev-state/blob/71be2a5442d597a8c80f87e322c6dfb2d04166f5/LICENSE) |
| Jev evidence | [`playground/2-jev-state.ts`](https://github.com/suranjaychandra/jev-state/blob/71be2a5442d597a8c80f87e322c6dfb2d04166f5/playground/2-jev-state.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Improve Jev accuracy and token use by restructuring the state you send.
- Mismatch: benchmark numbers are the author's scenarios.

## How it works

Composable formatters convert objects into compact labelled state; `bench/` compares raw vs shaped state on Jev. (Summarized from the upstream [README](https://github.com/suranjaychandra/jev-state/blob/71be2a5442d597a8c80f87e322c6dfb2d04166f5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README and try `examples/quickstart.ts`.

## Limits and data handling

Shaped state goes to TypeSafe when you call Jev. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 71be2a5442d5](https://github.com/suranjaychandra/jev-state/tree/71be2a5442d597a8c80f87e322c6dfb2d04166f5). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
