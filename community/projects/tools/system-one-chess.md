# system-one-chess

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser chess against TypeSafe Jev (Vercel AI Gateway or OpenRouter System One): legal moves as Choice options, live confidence, and in-browser Stockfish analysis. Optional local Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dperezcabrera/system-one-chess) |
| Maintainer | [dperezcabrera](https://github.com/dperezcabrera). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python ≥ 3.11 web app (`system-one-chess` 0.5.0): pico/FastAPI + chessground UI; Docker image on GHCR. |
| Requirements | Python **≥ 3.11** or Docker. Offline `pytest` needs no key. Live play needs `AI_GATEWAY_API_KEY` or `OPENROUTER_API_KEY` (optional Laya extras for local play). |
| License | [GPL-3.0](https://github.com/dperezcabrera/system-one-chess/blob/a9d4e39b6c1d00666017e205228a114d4ad7682e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline **pytest 50 passed**. Live gateway/OpenRouter games not run. Distinct from [Jev Chess](../apps/jevchess.md). |

## When to use

Use it to **measure how Jev picks among legal chess moves** with Stockfish percentile/centipawn breakdowns and optional LLM opponents on the same board. Prefer [Jev Chess](../apps/jevchess.md) for a hosted one-page demo with site-lent keys; prefer [Jev Lab](jev-lab.md) for Shogi/NPC labs. Do not treat demo games as a general Jev strength claim.

## How it works

[`system_one_chess/jev.py`](https://github.com/dperezcabrera/system-one-chess/blob/a9d4e39b6c1d00666017e205228a114d4ad7682e/system_one_chess/jev.py) POSTs one Choice question per turn to `{gateway}/v1/systemone` (Vercel `typesafe-ai/jev` or OpenRouter `jev-latest`). Chess.js/python-chess own legality; Stockfish WASM analyses locally; optional chat models share the same legal-move list. Optional Laya path runs locally without a key. Live Jev mode sends position/move descriptions to the gateway.

## Get started

```sh
git clone https://github.com/dperezcabrera/system-one-chess.git
cd system-one-chess
git checkout a9d4e39b6c1d00666017e205228a114d4ad7682e
python3 -m pip install -e '.[dev]'
python3 -m pytest -q
# Docker (no build): docker pull ghcr.io/dperezcabrera/system-one-chess:latest
# docker run --rm -p 127.0.0.1:8000:8000 -e OPENROUTER_API_KEY=... ghcr.io/dperezcabrera/system-one-chess:latest
```

## Examples and demos

- Offline `pytest`: **50 passed**.
- README includes analysis screenshots and random-mover baselines; `experiments/` documents option-order/legality studies (upstream-reported spend; not re-run here).

## Limits and data handling

Jev is a fast classifier, not a chess engine. Laya uses shorter move labels (token budget). Live calls incur gateway/OpenRouter usage. GPL-3.0 applies to this project. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit a9d4e39](https://github.com/dperezcabrera/system-one-chess/tree/a9d4e39b6c1d00666017e205228a114d4ad7682e): **0.5.0**, GPL-3.0. AI-assisted review of README, LICENSE, `system_one_chess/jev.py`, settings/provider. **`pytest`: 50 passed**. No live TypeSafe/OpenRouter/Vercel play.

Related: [Jev Chess](../apps/jevchess.md), [Jev Lab](jev-lab.md), [jev-zork](jev-zork.md), [System One Playground](system-one-playground.md).
