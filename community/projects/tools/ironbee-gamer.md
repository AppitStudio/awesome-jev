# IronBee Gamer

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Plays browser games live (2D canvas, Phaser, PixiJS, Cocos, HTML): a perception adapter turns what the page draws into a small JSON state and a decision engine picks every input — hosted TypeSafe Jev with your key, or Laya fine-tuned per game and run locally — with a web UI showing each state, action and probability, a coding-agent trainer for new games, and a shared Hugging Face library.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ironbee-ai/ironbee-gamer) |
| Maintainer | [ironbee-ai](https://github.com/ironbee-ai). Independently curated. |
| Format | Node CLI `ibgamer` with local web UI (`npm run ui`, `http://127.0.0.1:1986`) and a Python environment for Laya |
| Requirements | Node, Python 3 for Laya; `TYPESAFE_API_KEY` to play with Jev; a logged-in Claude Code (or similar) CLI to train/add games. |
| License | [Elastic License 2.0](https://github.com/ironbee-ai/ironbee-gamer/blob/286127993d79deebe8d969ca2a58996e0e53ace4/LICENSE) — source available, not an OSI open-source license (restricts offering it as a managed service). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- See how a System One model plays real-time-ish games from structured state.
- Compare hosted Jev against a small fine-tuned Laya on the same game.
- Mismatch: real-time play with hosted Jev is described upstream as not good enough yet; Laya is the default engine.

## How it works

[`src/engine/jev.ts`](https://github.com/ironbee-ai/ironbee-gamer/blob/286127993d79deebe8d969ca2a58996e0e53ace4/src/engine/jev.ts) and [`src/engine/systemone.ts`](https://github.com/ironbee-ai/ironbee-gamer/blob/286127993d79deebe8d969ca2a58996e0e53ace4/src/engine/systemone.ts) send the extracted state and typed action questions; [`src/engine/laya.ts`](https://github.com/ironbee-ai/ironbee-gamer/blob/286127993d79deebe8d969ca2a58996e0e53ace4/src/engine/laya.ts) uses the local Laya server ([`laya/serve.py`](https://github.com/ironbee-ai/ironbee-gamer/blob/286127993d79deebe8d969ca2a58996e0e53ace4/laya/serve.py)). The trainer writes per-game extract rules and fine-tunes Laya.

## Get started

Build the CLI and open the UI (README *Quick start*):

```sh
git clone https://github.com/ironbee-ai/ironbee-gamer.git && cd ironbee-gamer
npm install && npm run build && npm link
ibgamer laya setup   # local engine
npm run ui           # http://127.0.0.1:1986
```

Jev play bills your TypeSafe key; Laya runs locally.

## Examples and demos

- Per-game Laya models: [ironbee-ai/ironbee-gamer-library on Hugging Face](https://huggingface.co/ironbee-ai/ironbee-gamer-library).

## Limits and data handling

With Jev, game state JSON goes to TypeSafe. Elastic License 2.0 terms apply. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 286127993d79](https://github.com/ironbee-ai/ironbee-gamer/tree/286127993d79deebe8d969ca2a58996e0e53ace4). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
