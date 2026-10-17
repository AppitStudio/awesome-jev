# System One Arcade and @system-one/ai

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Bun workspace with one typed TypeScript API over System One decision providers (TypeSafe Jev, OpenRouter, OpenAI, Cloudflare Clef, Vercel AI Gateway) and a React arcade where those models play games against each other while a server logs every call and ranks them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/desplega-ai/system-one) |
| Maintainer | [desplega-ai](https://github.com/desplega-ai). Independently curated. |
| Format | TypeScript library (`@system-one/ai`) and React arcade app (Bun workspace; Fly.io and Docker deploy notes) |
| Requirements | Bun; keys for the providers you want to compare (for Jev: `TYPESAFE_API_KEY`, or OpenRouter/AI Gateway keys). |
| License | [MIT](https://github.com/desplega-ai/system-one/blob/fa3ca6327651f85eafed2f324d1617e73266001b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/voidisomorphism/status/2111432319429218779)). |
| Jev evidence | [`packages/ai/src/providers.ts`](https://github.com/desplega-ai/system-one/blob/fa3ca6327651f85eafed2f324d1617e73266001b/packages/ai/src/providers.ts) at the pinned commit. |

## When to use

- Compare how Jev, Clef and other decision models behave on the same live game state, with cost and latency per call.
- Call several System One providers through one typed `decide()` API and swap models without changing the call.
- Mismatch: a playful benchmark of a few games, not a rigorous evaluation; a public deploy spends your provider keys unless you set budgets.

## How it works

`typesafe("jev-latest")` and the other provider factories return the same `DecisionModel`; `decide()` sends a state (text, JSON, images, audio where supported) and typed boolean, choice and score questions, then returns typed answers with probabilities, refusals and token usage. The arcade server stores every call (tokens, cost, latency, error code) and scores each model per game. Integration evidence: [`packages/ai/src/providers.ts`](https://github.com/desplega-ai/system-one/blob/fa3ca6327651f85eafed2f324d1617e73266001b/packages/ai/src/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp .env.example .env   # fill in the keys you have
bun test               # unit tests, no network
bun run dev            # the arcade on http://localhost:3300
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted arcade linked by the author: [system-one-arcade.fly.dev/](https://system-one-arcade.fly.dev/) (creator-funded, with a daily spend cap).
- Author's X thread with game videos: [x.com/voidisomorphism/status/2111432319429218779](https://x.com/voidisomorphism/status/2111432319429218779)

## Limits and data handling

Game state (including webcam frames in the Attention game) goes to each provider you enable, on your keys. The database keeps images and audio only as a hash and size. Cost figures for TypeSafe are list-price estimates, not provider-reported.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit fa3ca6327651](https://github.com/desplega-ai/system-one/tree/fa3ca6327651f85eafed2f324d1617e73266001b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
