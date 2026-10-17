# PokéSurvivor x Jev learning bot

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experimental bot for the browser survival game PokéSurvivor: a Chrome extension handles 60 FPS dodging locally, and a local bridge asks Jev for level-up cards, items and tactics, learning only from what it sees on screen (README in Cantonese).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/skyhilam/pokesurvivor) |
| Maintainer | [skyhilam](https://github.com/skyhilam). Independently curated. |
| Format | Chrome MV3 extension plus local Python bridge (port 8765) |
| Requirements | Chrome, Python 3, a TypeSafe API key in `~/.config/typesafe/api_key`. |
| License | [Apache-2.0](https://github.com/skyhilam/pokesurvivor/blob/8150dfebe7bcd1b53fd86008ebc8280d209b07c7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bridge/jev_bridge.py`](https://github.com/skyhilam/pokesurvivor/blob/8150dfebe7bcd1b53fd86008ebc8280d209b07c7/bridge/jev_bridge.py) at the pinned commit. |

## When to use

- Study a split between a fast local reflex loop and slower Jev strategy calls in a real-time game.
- Follow a self-learning loop with a player journal instead of hand-tuned knowledge.
- Mismatch: work in progress; the author says there is no evidence yet that Jev can clear the full 31-minute run, and early clear results were from a simplified simulation.

## How it works

`bridge/jev_bridge.py` serves `/decide/levelup`, `/decide/item` and `/decide/tactics` and forwards each to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default). The extension's page agent does potential-field avoidance and WASD input every frame and calls the bridge only at decision points. Logs in `logs/LEARNING_REPORT.md` record real runs. Integration evidence: [`bridge/jev_bridge.py`](https://github.com/skyhilam/pokesurvivor/blob/8150dfebe7bcd1b53fd86008ebc8280d209b07c7/bridge/jev_bridge.py).

## Get started

From the upstream README (not run on the review host):

```sh
./run_bridge.sh   # starts the local Jev bridge on :8765
# then load extension/ as an unpacked extension in chrome://extensions and open the game
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Learning report: `logs/LEARNING_REPORT.md`.
- Offline tests: `python3 bridge/test_learning.py`, `bridge/test_pure_mode.py`.

## Limits and data handling

Game observations go to TypeSafe on your key. Use it only where the game's rules allow automated play; the extension injects into the game page.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 8150dfebe7bc](https://github.com/skyhilam/pokesurvivor/tree/8150dfebe7bcd1b53fd86008ebc8280d209b07c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
