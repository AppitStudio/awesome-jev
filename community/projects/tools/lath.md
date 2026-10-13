# Lath

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent loops that pay for model calls over a Tempo payment channel with every call recorded on Solana; a separate TypeSafe Jev decision answers continue vs achieved after each step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lath-agents/lath) |
| Maintainer | [lath-agents](https://github.com/lath-agents). Independently curated. |
| Format | TypeScript SDK + web demo |
| Requirements | Node.js; Tempo/Solana devnet setup per README; OpenRouter and TypeSafe keys. |
| License | [MIT](https://github.com/lath-agents/lath/blob/805d45cce3ec6fddce90a299ca498ed4c010819f/LICENSE) |
| Jev evidence | [`sdk/src/verify.ts`](https://github.com/lath-agents/lath/blob/805d45cce3ec6fddce90a299ca498ed4c010819f/sdk/src/verify.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let users audit what an agent spent while an independent model judges completion.
- Mismatch: devnet/mainnet crypto setup; experimental.

## How it works

Each loop step pays OpenRouter through a capped channel and commits a record on Solana; after the step Jev answers continue or achieved. (Summarized from the upstream [README](https://github.com/lath-agents/lath/blob/805d45cce3ec6fddce90a299ca498ed4c010819f/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow the README to fund the demo keys and run the loop.

## Limits and data handling

Step summaries go to TypeSafe; payments and records are public on-chain. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 805d45cce3ec](https://github.com/lath-agents/lath/tree/805d45cce3ec6fddce90a299ca498ed4c010819f). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
