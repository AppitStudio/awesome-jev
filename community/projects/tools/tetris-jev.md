# Tetris × Jev by wang-junjian (web Tetris where Jev picks each placement, with a Laya backend and seeded evals)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser Tetris with a built-in Jev player that makes one call per piece, choosing among all legal placements, plus a `window.TetrisAPI` so Playwright, Puppeteer or an LLM agent can drive the game. A local open Laya backend speaks the same protocol, every decision is logged with probabilities, confidence, timing and agreement with a classic heuristic, and a Node harness runs fixed-seed games for Jev, heuristic and random players. Docs and README are in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wang-junjian/tetris-jev) |
| Maintainer | [wang-junjian](https://github.com/wang-junjian). Independently curated. |
| Format | Static web app + Node proxy (no dependencies) |
| Requirements | Node.js; a TypeSafe API key for the Jev player (or a local Laya server). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-proxy.mjs`](https://github.com/wang-junjian/tetris-jev/blob/5da707711376b15c666d5783b58ef8b1239057a0/jev-proxy.mjs) at the pinned commit. |

## When to use

- See Jev make one Choice per move in a game, compare it with a heuristic and a local Laya model on fixed seeds, or drive the game from an agent.
- Mismatch: a strong Tetris bot; the heuristic is there for comparison.

## How it works

`jev-proxy.mjs` serves the page and forwards `/v1/systemone` calls to `https://api.typesafe.ai` with `TYPESAFE_API_KEY`, because the API's CORS allow-list blocks direct browser calls. The online GitHub Pages version has no backend and defaults to the local heuristic player. Integration evidence: [`jev-proxy.mjs`](https://github.com/wang-junjian/tetris-jev/blob/5da707711376b15c666d5783b58ef8b1239057a0/jev-proxy.mjs).

## Get started

Start the proxy with your key, open the page and start the Jev player.

```sh
git clone https://github.com/wang-junjian/tetris-jev && cd tetris-jev
TYPESAFE_API_KEY=... node jev-proxy.mjs 8787
# open http://localhost:8787 and start the Jev player
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Online version (heuristic player): [wangjunjian.com/tetris-jev/](https://wangjunjian.com/tetris-jev/)
- Research notes: [wangjunjian.com/tetris-jev/docs/](https://wangjunjian.com/tetris-jev/docs/)

## Limits and data handling

Board states go to TypeSafe through your local proxy. The hosted site runs only the heuristic. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 5da707711376](https://github.com/wang-junjian/tetris-jev/tree/5da707711376b15c666d5783b58ef8b1239057a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
