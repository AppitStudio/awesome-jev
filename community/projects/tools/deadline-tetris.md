# Deadline Tetris

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Live benchmark where Jev, Clef, Laya, Strands Decider and LLMs play the same Tetris game while pieces keep falling: over four games Jev landed about 119 pieces per game with a 289 ms median answer and won all four, while slower models placed better moves but too late.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jagadeeswara-reddy-p/jev-demos) |
| Maintainer | [jagadeeswara-reddy-p](https://github.com/jagadeeswara-reddy-p). Independently curated. |
| Format | Bun + TypeScript web app with model adapters and recorded runs |
| Requirements | Bun; a TypeSafe key for Jev plus keys for any other models you add (Cloudflare, Bedrock); optional AWS GPU for the self-hosted models. |
| License | [MIT](https://github.com/jagadeeswara-reddy-p/jev-demos/blob/1d7cebc40540b3627012b3a2548475a2ea8b1997/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/adapters/decision.ts`](https://github.com/jagadeeswara-reddy-p/jev-demos/blob/1d7cebc40540b3627012b3a2548475a2ea8b1997/server/adapters/decision.ts) at the pinned commit. |

## When to use

- Show how speed and judgment trade off when a decision has a deadline.
- Add your own models to the line-up from the page and race them on the same seed.
- Mismatch: one game and one prompt; the author's measured runs are from India, so latency includes network.

## How it works

Each piece becomes a decision request listing the candidate placements; `decision.ts` calls decision models (Jev through the TypeSafe API) and other adapters handle LLMs. An answer that arrives after the piece lands does not count, and the results screen splits speed from move quality. Integration evidence: [`server/adapters/decision.ts`](https://github.com/jagadeeswara-reddy-p/jev-demos/blob/1d7cebc40540b3627012b3a2548475a2ea8b1997/server/adapters/decision.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp .env.example .env   # add the keys for the models you want
bun dev                # http://localhost:5317
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Six-model recording: `docs/media/demo-six-models.mp4`.
- Mock models (no API calls) are built in for trying it offline.

## Limits and data handling

Board states go to each model provider on your keys. Exposing the server on a network lets others run models on your keys.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 1d7cebc40540](https://github.com/jagadeeswara-reddy-p/jev-demos/tree/1d7cebc40540b3627012b3a2548475a2ea8b1997). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
