# jev-zork

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

TypeSafe Jev plays Zork I: Jericho supplies valid actions; Jev answers one Choice (plus danger/intent questions) per turn; code owns memory, anti-loop, and the French terminal/replay dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Resadan-dev/jev-zork) |
| Maintainer | [Resadan-dev](https://github.com/Resadan-dev). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package / CLI **`jev-zork` 0.1.0** plus browser replay (`replay/`) and optional video renderer. |
| Requirements | Python ≥ 3.10; Linux/macOS (or Windows via WSL) for Jericho + Zork I ROM; `typesafe-sdk` 0.7.x; `TYPESAFE_API_KEY` for live Jev (random judge available for keyless harness tests). |
| License | [MIT](https://github.com/Resadan-dev/jev-zork/blob/981451ba8adc076fd4058d20a37c8bef2739c0ae/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline unit tests (non-Jericho) inspected. Live Zork play and live TypeSafe not run on the review host. Dashboard UI language is French. |

## When to use

Use it when you want a **visible text-adventure lab** for calibrated Choices over legal actions, with anti-loop policy in code. Prefer [Jev 2048](../apps/jev-2048.md) / [Jev Lab](jev-lab.md) / [TypeSafe Mario](typesafe-mario.md) for other simulation demos.

## How it works

Each turn builds state from the last moves and Jericho’s valid-action list (capped at 255). [`judges.py`](https://github.com/Resadan-dev/jev-zork/blob/981451ba8adc076fd4058d20a37c8bef2739c0ae/src/jev_zork/judges.py) calls TypeSafe System One (`POST https://api.typesafe.ai/v1/systemone` via the SDK). [`policy.py`](https://github.com/Resadan-dev/jev-zork/blob/981451ba8adc076fd4058d20a37c8bef2739c0ae/src/jev_zork/policy.py) halves probabilities for actions already tried in the same world state. Departures from Jev’s top choice are logged for the French dashboard and replay player.

## Get started

```sh
git clone https://github.com/Resadan-dev/jev-zork.git
cd jev-zork
git checkout 981451ba8adc076fd4058d20a37c8bef2739c0ae
# Follow upstream README / scripts/setup_wsl.sh for Jericho + ROM
python3 -m pip install -e '.[dev]'   # or uv sync per upstream
PYTHONPATH=src pytest -q -m 'not jericho'
```

Live play sends game state and questions to TypeSafe and may incur charges. This listing did not start a live game.

## Examples and demos

- Offline unit tests (no Jericho marker) on the review host: **123 passed**.
- Browser replay: open `replay/index.html` on a recorded JSONL log.
- Optional `video/render_video.py` for MP4/GIF (not run here).

## Limits and data handling

Observation text and action catalogs leave the host on live turns. Jericho/Zork assets follow upstream licensing; dashboard strings are French. Anti-loop and option capping are application policy, not model guarantees.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 981451b](https://github.com/Resadan-dev/jev-zork/tree/981451ba8adc076fd4058d20a37c8bef2739c0ae): **0.1.0**, MIT. AI-assisted source review of README, `judges.py`, `policy.py`, `questions.py`, LICENSE, tests. Offline: `pytest -q -m 'not jericho'` → **123 passed**. No live TypeSafe or Jericho play on the review host.

Related: [Jev Lab](jev-lab.md), [Jev 2048](../apps/jev-2048.md), [TypeSafe Mario](typesafe-mario.md), [JevPokerBench](jev-poker-bench.md).
