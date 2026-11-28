# Jev vs Laya by encorp.ai (browser app that runs Jev and Laya side by side on a document classifier and two games, with live cost counters)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Frontend-only Next.js app that sends identical decisions to TypeSafe Jev and the Laya decision model and shows the answers, latency, probabilities and running cost side by side: a document classifier with labelled samples, Snake and a side-scroller called Glide. Without keys each engine runs a clearly labelled simulation; keys stay in the browser. Includes a Jev model-router skill plugin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/martin-key/jev-vs-laya) |
| Maintainer | [Martin Kuvandzhiev](https://github.com/martin-key) ([encorp.ai](https://encorp.ai)). Independently curated. |
| Format | Next.js static web app |
| Requirements | Node.js 20.9+; a TypeSafe key for live Jev, and a Laya key or local Laya server. |
| License | [MIT](https://github.com/martin-key/jev-vs-laya/blob/460d6aeb1a47a62b7b71c5e9dc9189da43638857/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/engines/client.ts`](https://github.com/martin-key/jev-vs-laya/blob/460d6aeb1a47a62b7b71c5e9dc9189da43638857/src/lib/engines/client.ts) at the pinned commit. |

## When to use

- Developers comparing a hosted and a local decision model on speed, cost and answers before choosing one.
- Mismatch: rigorous accuracy benchmarks; the demos are small and illustrative.

## How it works

`src/lib/engines/client.ts` posts `{model, state, questions}` to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) and the same body to the configured Laya endpoint, then times and prices each call. Integration evidence: [`src/lib/engines/client.ts`](https://github.com/martin-key/jev-vs-laya/blob/460d6aeb1a47a62b7b71c5e9dc9189da43638857/src/lib/engines/client.ts).

## Get started

Run it locally in simulation mode, then add keys under API keys.

```sh
git clone https://github.com/martin-key/jev-vs-laya && cd jev-vs-laya
npm ci
npm run dev   # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted copy: [jev-vs-laya.encorp.ai](https://jev-vs-laya.encorp.ai)

## Limits and data handling

With keys set, the browser calls TypeSafe and the Laya endpoint directly. Costs shown are computed from published prices, not billing data. A hosted copy is at jev-vs-laya.encorp.ai.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 460d6aeb1a47](https://github.com/martin-key/jev-vs-laya/tree/460d6aeb1a47a62b7b71c5e9dc9189da43638857). Inspected the README, LICENSE and the engine client at the pinned commit and confirmed the hosted copy loads (HTTP 200); nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
