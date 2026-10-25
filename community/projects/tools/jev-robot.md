# JEV robot (Unitree G1 in MuJoCo with Jev motor decisions and Gemini planning)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Simulation-only demo of a Unitree G1 humanoid in MuJoCo: Jev chooses velocities and bounded joint offsets (full control) or named movements (primitives) while Gemini plans from the live camera frame, all shown in a browser control room; an offline mode runs without keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arterialist/jev-robot) |
| Maintainer | [arterialist](https://github.com/arterialist). Independently curated. |
| Format | Python app with a web control room (uv) |
| Requirements | Python 3.12+, uv and Git; OpenRouter and Gemini keys for live mode. |
| License | [MIT](https://github.com/arterialist/jev-robot/blob/0fbe40cd75127b23fdc366989ac79defd0509883/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_robot/brains.py`](https://github.com/arterialist/jev-robot/blob/0fbe40cd75127b23fdc366989ac79defd0509883/src/jev_robot/brains.py) at the pinned commit. |

## When to use

- Experiment with Jev as a fast low-level controller under a slower planner.
- Try the full setup offline first with local fallback decisions.
- Mismatch: simulation only; no real hardware control.

## How it works

`brains.py` calls `~typesafe/jev-latest` through OpenRouter's Decisions API for motor decisions, and `gemini-3.8-flash` plans from camera frames; missing keys or failed requests fall back to local decisions. Integration evidence: [`src/jev_robot/brains.py`](https://github.com/arterialist/jev-robot/blob/0fbe40cd75127b23fdc366989ac79defd0509883/src/jev_robot/brains.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/arterialist/jev-robot.git && cd jev-robot
uv sync --python 3.12
uv run jev-robot-web --offline   # no keys
# live: add OPENROUTER_API_KEY and GEMINI_API_KEY to .env, then uv run jev-robot-web
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Running guide: [github.com/arterialist/jev-robot/blob/main/docs/running.md](https://github.com/arterialist/jev-robot/blob/main/docs/running.md)
- Architecture: [github.com/arterialist/jev-robot/blob/main/docs/architecture.md](https://github.com/arterialist/jev-robot/blob/main/docs/architecture.md)

## Limits and data handling

In live mode, simulation state goes to OpenRouter and TypeSafe, and camera frames go to Google Gemini when the planner runs.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 0fbe40cd7512](https://github.com/arterialist/jev-robot/tree/0fbe40cd75127b23fdc366989ac79defd0509883). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
