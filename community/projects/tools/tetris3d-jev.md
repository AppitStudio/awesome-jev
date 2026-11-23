# TETRIS·3D by wang-junjian (Three.js 3D Tetris where Jev can play, falling back to a built-in heuristic)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

A 3D Tetris in React and Three.js with glowing voxels and line-clear animations, playable by hand on keyboard or touch, or by AI. In AI mode each step sends the board and candidate placements to Jev's Choice and plays the best one with its confidence; if Jev fails, times out or is unsure, a Dellacherie-style heuristic takes over so the game never stops. README in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wang-junjian/tetris3d) |
| Maintainer | [wang-junjian](https://github.com/wang-junjian). Independently curated. |
| Format | Web app (React + Three.js + Hono proxy) |
| Requirements | Node.js (or Docker); a TypeSafe API key entered in the page settings. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/game/jev.ts`](https://github.com/wang-junjian/tetris3d/blob/1fd1380f9eebb6628158c638948632c3d0780bc2/src/game/jev.ts) at the pinned commit. |

## When to use

- Watch Jev play a 3D game move by move with a visible decision log and a safe fallback.
- Mismatch: the hosted demo for Jev play; online it uses the heuristic only.

## How it works

`src/game/jev.ts` sends each decision to the same-origin proxy `/api/jev/systemone`, and `api/jev-proxy.ts` forwards it to `https://api.typesafe.ai/v1/systemone`. The key is set in the page and kept in the browser's localStorage. The GitHub Pages build has no proxy, so Jev mode falls back to the heuristic there. Integration evidence: [`src/game/jev.ts`](https://github.com/wang-junjian/tetris3d/blob/1fd1380f9eebb6628158c638948632c3d0780bc2/src/game/jev.ts).

## Get started

Install and run the dev server, then set your key in Settings and switch to the Jev engine.

```sh
git clone https://github.com/wang-junjian/tetris3d && cd tetris3d
npm install
npm run dev   # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Online version: [wangjunjian.com/tetris3d/](https://wangjunjian.com/tetris3d/)

## Limits and data handling

Board states go to TypeSafe through the local proxy; the key sits in browser localStorage. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 1fd1380f9eeb](https://github.com/wang-junjian/tetris3d/tree/1fd1380f9eebb6628158c638948632c3d0780bc2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
