# Thorkell (Valheim companion)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Research project: a Valheim companion that joins your world as a real second player, reads its own game screen, takes chat requests like "make us an axe" or "follow me", and uses Jev for fast typed decisions under a deadline while a larger model plans and talks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lofcgi/thorkell) |
| Maintainer | [lofcgi](https://github.com/lofcgi). Independently curated. |
| Format | Game agent (Python brain + game client on macOS) |
| Requirements | macOS with a specific Valheim build; `GEMINI_API_KEY` for the main model and `TYPESAFE_API_KEY` for Jev. |
| License | [MIT](https://github.com/lofcgi/thorkell/blob/f5c71d3199f816a1ee5c7be6da950f69ed618a77/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`brain/thorkell/decide/points.py`](https://github.com/lofcgi/thorkell/blob/f5c71d3199f816a1ee5c7be6da950f69ed618a77/brain/thorkell/decide/points.py) at the pinned commit. |

## When to use

- Experiment with an embodied game agent that sees, decides and acts like a first-time player.
- Study splitting fast in-fight choices (Jev) from slower planning.
- Mismatch: research work in progress; macOS and one Valheim build only.

## How it works

The brain reads screenshots and chat, keeps memory, and plans with a generative model. Time-critical typed choices, such as how to respond to a hit, go to Jev in about 0.2 seconds; `brain/thorkell/decide/points.py` and `config.py` wire the Jev backend at `https://api.typesafe.ai`. The README plans a fine-tuned local Laya later. Integration evidence: [`brain/thorkell/decide/points.py`](https://github.com/lofcgi/thorkell/blob/f5c71d3199f816a1ee5c7be6da950f69ed618a77/brain/thorkell/decide/points.py).

## Get started

From the upstream README: put `GEMINI_API_KEY` and `TYPESAFE_API_KEY` in the repo-root secrets file, then follow the setup for the supported Valheim build.

```sh
git clone https://github.com/lofcgi/thorkell
# then follow the README setup for the supported Valheim build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo captions (axe crafting, house building, Eikthyr fight)

## Limits and data handling

Screenshots and chat go to the configured model providers. See the README Status section for what has been verified in the real game.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit f5c71d3199f8](https://github.com/lofcgi/thorkell/tree/f5c71d3199f816a1ee5c7be6da950f69ed618a77). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
