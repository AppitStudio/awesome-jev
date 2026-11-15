# jevchain (typed TypeScript framework for composing Jev calls into decision graphs, with a studio that shows every branch taken and not taken)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Zero-dependency TypeScript framework for building chains of Jev decisions: `choice`, `score` and `noul` questions are typed end to end, and nodes such as `route`, `gate`, `parallel` and `cascade` pick the path from Jev's answers, with low-confidence fallbacks checked at compile time. Every run leaves a JSON trace with the full probability distributions, the branches not taken, latency and cost; same-state asks are merged into one request automatically. A Next.js studio runs chains live, explains each decision in plain English, compares inputs, shares runs as links and builds chains visually.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aj604/jev-chain) |
| Maintainer | [aj604](https://github.com/aj604). Independently curated. |
| Format | TypeScript library (npm `jevchain` 0.1.0) and Next.js studio (pnpm monorepo, MIT) |
| Requirements | Node.js with pnpm and a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/jevchain/src/client.ts`](https://github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/packages/jevchain/src/client.ts) at the pinned commit. |

## When to use

- Build multi-step Jev routing, gating and cascades in TypeScript with a full trace of why each path was taken.
- Mismatch: text generation; jevchain only composes typed decisions.

## How it works

`packages/jevchain/src/client.ts` posts to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) with retries, timeouts, concurrency limits and same-tick batching; the studio calls it through a server-side `/api/jev` proxy that keeps the key off the browser and rate-limits per IP. Integration evidence: [`packages/jevchain/src/client.ts`](https://github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/packages/jevchain/src/client.ts).

## Get started

Install the monorepo, add your key, then open the studio or run an example chain in the terminal.

```sh
git clone https://github.com/aj604/jev-chain && cd jev-chain
pnpm install
echo "TYPESAFE_API_KEY=..." > .env
pnpm dev    # studio at http://localhost:3000
pnpm example haunted-desk "my kettle is screaming in latin"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/README.md](https://github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/README.md)
- Framework reference: [github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/packages/jevchain/README.md](https://github.com/aj604/jev-chain/blob/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577/packages/jevchain/README.md)
- Hosted studio: [jev-chain.vercel.app](https://jev-chain.vercel.app)

## Limits and data handling

States and questions go to TypeSafe on your key. The maker's hosted studio (jev-chain.vercel.app) runs chains through its own proxy with a per-IP rate limit, or forwards your own key per request without storing it. Version 0.1.0; the five bundled examples are deliberately playful.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit ce749f53e1c7](https://github.com/aj604/jev-chain/tree/ce749f53e1c7f7f368ac97c21c8ed32ace1d9577). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
