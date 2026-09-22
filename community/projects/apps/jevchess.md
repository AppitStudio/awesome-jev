# Jev Chess

[All projects](../README.md) · [Web apps](README.md#web-apps)

One-page web app where TypeSafe Jev plays chess against OpenRouter LLMs, Stockfish, or you—with live move probabilities, clocks, saved games, and an optional hosted key-lending demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/choxos/jevchess) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Hosted demo](https://jevchess.xera.ac) — site-lent keys with daily caps, or bring your own TypeSafe/OpenRouter keys. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Hosted play can use the site’s lent keys (capped) or your own keys. TypeSafe/OpenRouter usage can incur charges when using paid keys. |
| Jev evidence | Inspected [`server.mjs`](https://github.com/choxos/jevchess/blob/602190f963e9b04def959b8519e6a2f2513590e0/server.mjs): proxies Jev to `https://api.typesafe.ai/v1/systemone` and optionally OpenRouter Decisions; chess.js owns legality, clocks, persistence, and Stockfish/LLM opponent lanes. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source and offline unit tests inspected; live TypeSafe/OpenRouter games not run on the review host. |
| Maintainer | [choxos](https://github.com/choxos). Independently curated. |
| Format | Node ≥ 20.3 zero-dependency server (`server.mjs`) + static UI; npm package name `jev-chess` **0.1.0** (private). |
| Platform and availability | Local `npm start` or hosted [jevchess.xera.ac](https://jevchess.xera.ac) (HTTP 200 checked). |
| Jev's role | Chooses among legal chess moves via typed System One questions with calibrated probabilities (arrows/UI). Application code owns board state, legality, clocks, Stockfish/LLM opponents, voice parsing policy, and saved games. |
| Requirements | Node ≥ 20.3; optional `TYPESAFE_API_KEY` / OpenRouter keys (or hosted lending). |
| License | [MIT](https://github.com/choxos/jevchess/blob/602190f963e9b04def959b8519e6a2f2513590e0/LICENSE). |

## When to use

Use it when you want a **watchable Jev-vs-machine (or you-vs-Jev) chess demo** with probability arrows and saved replays. Prefer [Jev 2048](jev-2048.md) for a simpler Choice-every-move puzzle, or [jev-zork](../tools/jev-zork.md) for text-adventure action choice. Do not treat win rates on the hosted tour as a general Jev strength claim.

## How it works

The Node server serves the UI and proxies typed Jev requests (TypeSafe System One or OpenRouter Decisions). Opponents are Stockfish-in-page and/or OpenRouter chat models. Finished games are stored after move replay validation; stats aggregate Jev’s record by opponent class.

## Get started

```sh
git clone https://github.com/choxos/jevchess.git
cd jevchess
git checkout 602190f963e9b04def959b8519e6a2f2513590e0
npm test
npm start
# Open the printed local URL, or use https://jevchess.xera.ac
```

Live games send positions/move options to TypeSafe and/or OpenRouter and may incur charges. This listing did not start a live game.

## Examples and demos

- Offline on the review host: `npm test` → **12 passed**.
- Hosted demo: [jevchess.xera.ac](https://jevchess.xera.ac) (HTTP 200).
- Upstream tour assets under `documentation/`.

## Limits and data handling

Board states and chosen moves leave the host on live Jev/LLM calls. Site-lent keys are capped per upstream README; BYOK lifts caps. Voice mode may send audio to the browser’s speech service (e.g. Google in Chrome).

## Review and maintenance

Reviewed on **2026-09-22** at [commit 602190f](https://github.com/choxos/jevchess/tree/602190f963e9b04def959b8519e6a2f2513590e0): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `server.mjs`. Offline `npm test` 12 passed. No live TypeSafe/OpenRouter play on the review host.

Related: [Jev 2048](jev-2048.md), [Jev Grand Prix](jev-grand-prix.md), [jev-zork](../tools/jev-zork.md).
