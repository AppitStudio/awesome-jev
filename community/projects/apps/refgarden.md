# RefGarden

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local spatial gallery that finds image and short-video references from a prompt. Jev chooses search phrases and highlights which catalog items fit; The Met, NASA, Cosmos, and Internet Archive supply the media.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlbionaHoti/refgarden) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/AlbionaHoti/refgarden#refgarden) |
| Pricing and access | [Run locally from MIT source](https://github.com/AlbionaHoti/refgarden#run-locally); no app purchase fee. Bring a TypeSafe API key (`TYPESAFE_AI_API_KEY`). A separate [hosted preview](https://jev-curator.vercel.app) uses keyword retrieval without Jev. Reviewed 2026-09-20. |
| Jev evidence | [`src/jev-client.ts`](https://github.com/AlbionaHoti/refgarden/blob/cd27f332632f9522173eb66df3a42470a917d47e/src/jev-client.ts) posts to `https://api.typesafe.ai/v1/systemone`; [`src/decision.ts`](https://github.com/AlbionaHoti/refgarden/blob/cd27f332632f9522173eb66df3a42470a917d47e/src/decision.ts) builds choice questions (default model `jev-latest`). |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. Source and offline tests inspected; live Explore runs and the hosted preview were not exercised. |
| Maintainer | [AlbionaHoti](https://github.com/AlbionaHoti). Independently curated; not an upstream submission. |
| Format | TypeScript local web app (Node/Bun server + browser gallery), package **0.1.0**. |
| Platform and availability | Self-host on Node.js 22+ at `http://127.0.0.1:4318`. Hosted preview is keyword-only (no Jev). |
| Jev's role | Chooses search phrases and which reference IDs to highlight from titles/descriptions. Application code owns collection balance, dedupe, and UI. Jev receives no image pixels, video frames, or audio. |
| Requirements | Node.js 22+; TypeSafe account and API key for local Explore. |
| License | [MIT](https://github.com/AlbionaHoti/refgarden/blob/cd27f332632f9522173eb66df3a42470a917d47e/LICENSE). |

## When to use

Use it to explore visual references (artwork, science imagery, design, short archive clips) while keeping Jev decisions limited to text metadata. Prefer ordinary search UIs when you already know exact collection IDs. Do not treat gallery results as rights-cleared assets for commercial reuse without checking each source's terms.

## How it works

1. Local Explore sends prompt and style settings into decision helpers that ask Jev which phrases and reference IDs fit.
2. [`requestJev`](https://github.com/AlbionaHoti/refgarden/blob/cd27f332632f9522173eb66df3a42470a917d47e/src/jev-client.ts) calls TypeSafe System One with Bearer auth; code validates choices against the offered candidate set before spending another call.
3. Deterministic collectors pull Met/NASA/Cosmos images and Prelinger short videos under source-balance and duration/size caps; the 3D gallery renders cards and keeps pins locally.

Keys are stored in a local ignored `.env` after Connect Jev. Upstream documents that Jev never sees media bytes.

## Get started

```sh
git clone https://github.com/AlbionaHoti/refgarden.git
cd refgarden
git checkout cd27f332632f9522173eb66df3a42470a917d47e
npm ci
npm run build
npm start
```

Open `http://127.0.0.1:4318`, connect a TypeSafe key, then Explore. Live runs send metadata-derived prompts/state to TypeSafe and can incur charges.

## Examples and demos

- Offline unit suite under `tests/` (decision boundaries, discovery, source balance, connection helpers).
- Upstream README prompt examples (toy commercials, botanical moon observatory, etc.) were not re-run live for this listing.

## Limits and data handling

Hosted preview ≠ local Jev path. Collection percentages can be uneven when sources fail. Duplicate filtering is metadata-based, not pixel matching. Video streaming hits Internet Archive; clips are capped at three minutes / 80 MB. Provider 401/429/5xx paths surface in the UI with retries documented in the client.

## Review and maintenance

Reviewed on **2026-09-20** at [commit cd27f33](https://github.com/AlbionaHoti/refgarden/tree/cd27f332632f9522173eb66df3a42470a917d47e): MIT, package 0.1.0. AI-assisted source review of `jev-client.ts`, `decision.ts`, README, and license. After installing the pinned Bun binary, **`npm test`**: **74 pass / 0 fail**. No live TypeSafe Explore run and no hosted-preview validation.

Related: [Jev Radar](jev-radar.md), [Jev Search](jev-search.md).
