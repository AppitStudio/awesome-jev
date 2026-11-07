# jev-flap (TypeSafe Jev plays OpenGames Flap from browser screenshots)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experiment harness that has TypeSafe Jev (and optionally a local LiquidAI d1-3B) play OpenGames Flap using only browser screenshots, with evaluation scripts that compare Jev against the local model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ARCS-inc/jev-game-blog) |
| Maintainer | [ARCS-inc](https://github.com/ARCS-inc). Independently curated. |
| Format | Python experiment harness (MIT) |
| Requirements | Python, browser/game setup per README, and a TypeSafe API key for the Jev path (optional local d1 model). |
| License | [MIT](https://github.com/ARCS-inc/jev-game-blog/blob/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_flap/model.py`](https://github.com/ARCS-inc/jev-game-blog/blob/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d/src/jev_flap/model.py) at the pinned commit. |

## When to use

- Benchmark Jev on a visual flap-or-not control loop.
- Compare hosted Jev against a local decision model on the same frames.
- Mismatch: research harness; not a polished consumer game.

## How it works

`src/jev_flap/model.py` and eval scripts call TypeSafe with `api:jev-latest` / `TYPESAFE_API_KEY` to answer flap decisions from screenshot state. Integration evidence: [`src/jev_flap/model.py`](https://github.com/ARCS-inc/jev-game-blog/blob/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d/src/jev_flap/model.py).

## Get started

Clone, set TYPESAFE_API_KEY, and run the uv/python scripts in README.

```sh
git clone https://github.com/ARCS-inc/jev-game-blog.git && cd jev-game-blog
export TYPESAFE_API_KEY=...
uv run --env-file .env python scripts/06_eval_frames_ep0_jev_vs_d1.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ARCS-inc/jev-game-blog/blob/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d/README.md](https://github.com/ARCS-inc/jev-game-blog/blob/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d/README.md)

## Limits and data handling

Screenshot-derived state is sent to TypeSafe on your key. Local d1 path stays on-machine.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit b0d3ca4c9260](https://github.com/ARCS-inc/jev-game-blog/tree/b0d3ca4c92608dabcb52e9c32608f2e027d6a05d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
