# jev-libero

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Fine-grained robot-manipulation study loop: TypeSafe Jev chooses layered intents/actions while local physics previews candidate effects on configurable LIBERO tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dimweaker/jev-libero) |
| Maintainer | [Dimweaker](https://github.com/Dimweaker). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-libero 0.1.0** (CLI `jev-libero`; optional `[robot]` extras for MuJoCo/robosuite/LIBERO). |
| Requirements | Python ≥ 3.10,<3.12 for the core package; live episodes need `TYPESAFE_API_KEY` or OpenRouter credentials plus a LIBERO/MuJoCo environment (`LIBERO_ROOT`, renderer). Recorded demos can be inspected without the simulator. |
| License | [MIT](https://github.com/Dimweaker/jev-libero/blob/667b3bbeb0e40594e6a9993356ce84e70afc936d/LICENSE). |

## When to use

Use it to study typed decision chains for tabletop manipulation with inspectable records (requests, controls, costs, media). Prefer [jev-drone](jev-drone.md) for flight-style MuJoCo experiments, or [TypeSafe Mario](typesafe-mario.md) for emulator action choice. This is a research/simulation package, not a production robot stack.

## How it works

[`src/jev_libero/client.py`](https://github.com/Dimweaker/jev-libero/blob/667b3bbeb0e40594e6a9993356ce84e70afc936d/src/jev_libero/client.py) calls TypeSafe `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or OpenRouter’s decisions path. Policy layers pick intent, contact/motion family, and one of 27 fine-grained inputs; reversible simulator branches preview effects before commit. Task JSON configures objects, goals, and prompts. Example records under `examples/records/` ship microwave/top-drawer demos.

## Get started

```sh
git clone https://github.com/Dimweaker/jev-libero.git
cd jev-libero
git checkout 667b3bbeb0e40594e6a9993356ce84e70afc936d
pip install -e .
jev-libero tasks
jev-libero inspect examples/records/top_drawer_seed1
# Live episodes: install '[robot]', set LIBERO_ROOT / TYPESAFE_API_KEY (or OpenRouter), see docs/setup.md
```

Live control sends observations/questions to the chosen provider and needs a heavyweight simulator. This listing did not run live episodes.

## Examples and demos

- GIF/MP4 demos linked from the README (`docs/media/`).
- Offline unit tests under [`tests/`](https://github.com/Dimweaker/jev-libero/tree/667b3bbeb0e40594e6a9993356ce84e70afc936d/tests) (client mocking, config, geometry).
- Architecture/setup docs under `docs/`.

## Limits and data handling

Episode state and prompts leave the machine for TypeSafe/OpenRouter when live. Simulator extras pin specific MuJoCo/robosuite/torch versions. Alpha package (`Development Status :: 3 - Alpha`). Recorded results are illustrative, not a performance claim for all LIBERO tasks.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 667b3bb](https://github.com/Dimweaker/jev-libero/tree/667b3bbeb0e40594e6a9993356ce84e70afc936d): **0.1.0**, MIT. AI-assisted source review of README, `client.py`, policy/CLI surfaces, tests layout, and license. No `pytest` and no live simulator/TypeSafe run on the review host.

Related: [jev-drone](jev-drone.md), [TypeSafe Mario](typesafe-mario.md).
