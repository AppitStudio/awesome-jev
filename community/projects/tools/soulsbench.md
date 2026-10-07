# SoulsBench

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Dark Souls III realtime combat benchmark for decision models: TypeSafe Jev, OpenAI Decisions, Perplexity's decider and local Kev / Laya each fight Iudex Gundyr through the same harness, state, 16 actions and 200 ms budget on the live game; the author's 50-seed results table reports wins, damage, latency and cost per fight.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AWoLnik/SoulsBench) |
| Maintainer | [AWoLnik](https://github.com/AWoLnik). Independently curated. |
| Format | Python package run from WSL with a native Windows bridge (SoulsGym) driving the game |
| Requirements | Windows with WSL, an owned Steam copy of Dark Souls III 1.15.2 with both DLCs, uv, and a TypeSafe key for the Jev adapter (other adapters need their own keys or local servers). |
| License | [MIT](https://github.com/AWoLnik/SoulsBench/blob/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- See how Jev's latency and choices hold up in a realtime control loop against other decision models.
- Add your own adapter to the same harness.
- Mismatch: upstream warns the project is entirely AI-written and not carefully reviewed; use a throwaway offline save.

## How it works

[`soulsbench/adapters/jev.py`](https://github.com/AWoLnik/SoulsBench/blob/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf/soulsbench/adapters/jev.py) turns each `CombatState` into one Jev request for the next action; other adapters (OpenAI Decisions, rules, HTTP) share [`base.py`](https://github.com/AWoLnik/SoulsBench/blob/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf/soulsbench/adapters/base.py). Results and caveats (prompt tuned on Jev) are in [`docs/results_full50.md`](https://github.com/AWoLnik/SoulsBench/blob/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf/docs/results_full50.md).

## Get started

Start the Windows bridge, then run a short benchmark (README):

```sh
uv run python -m soulsbench.bridge start
uv run python -m soulsbench.run --backend souls_gym --scenario gundyr_full --adapter openai,jev --seeds 10
```

One Jev request per decision (upstream reports about $0.024 per fight), billed to your TypeSafe key.

## Examples and demos

- README *Results* table.
- [Full 50-seed results](https://github.com/AWoLnik/SoulsBench/blob/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf/docs/results_full50.md).

## Limits and data handling

Game state summaries go to each provider; the bridge reads and writes game memory and sends keystrokes. Results are upstream measurements. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 08ed40fdc21e](https://github.com/AWoLnik/SoulsBench/tree/08ed40fdc21e6b0341f7087f55994a3c1e3f40cf). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
