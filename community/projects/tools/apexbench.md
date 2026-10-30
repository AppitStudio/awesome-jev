# ApexBench (benchmark for forecasting Apex Legends team placements from replay data, Jev by default)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Open benchmark that loads a historical ALGS Apex Legends replay, rebuilds the match state at a chosen time and asks a model to forecast one team's final placement, then compares forecasts with the result. Jev is the default model through OpenRouter's Decisions API; GPT, Claude, Gemini, DeepSeek and other OpenRouter models can be swapped in. Includes terminal playback, caching and export.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cyanxiao/apex-bench) |
| Maintainer | [cyanxiao](https://github.com/cyanxiao). Independently curated. |
| Format | Python CLI benchmark |
| Requirements | Python 3.12+, uv, a replay JSON in the documented format, and an OpenRouter key for new predictions (inspect, playback and evaluation work without one). |
| License | [Apache-2.0](https://github.com/cyanxiao/apex-bench/blob/dc2f7d0b06cc099091296d4aa431aed01ee19119/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/apexbench/jev.py`](https://github.com/cyanxiao/apex-bench/blob/dc2f7d0b06cc099091296d4aa431aed01ee19119/src/apexbench/jev.py) at the pinned commit. |

## When to use

- Compare how Jev and chat models forecast outcomes from partial, timestamped game telemetry.
- Mismatch: you need your own replay files; no published leaderboard of results in the repo.

## How it works

`jev.py` sends the reconstructed match state with fixed placement instructions to `openrouter.ai/api/alpha/decisions` (default `typesafe/jev-1.13`) and turns the answer into a placement forecast; results are cached. Integration evidence: [`src/apexbench/jev.py`](https://github.com/cyanxiao/apex-bench/blob/dc2f7d0b06cc099091296d4aa431aed01ee19119/src/apexbench/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run apexbench inspect "$REPLAY"
export OPENROUTER_API_KEY="your-openrouter-api-key"
uv run apexbench predict "$REPLAY" --team "$TEAM" --at 60
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Replay format: [github.com/cyanxiao/apex-bench/blob/dc2f7d0b06cc099091296d4aa431aed01ee19119/docs/replay-format.md](https://github.com/cyanxiao/apex-bench/blob/dc2f7d0b06cc099091296d4aa431aed01ee19119/docs/replay-format.md)

## Limits and data handling

Replay data you load is sent to OpenRouter and the chosen model provider. Not affiliated with EA, Respawn or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit dc2f7d0b06cc](https://github.com/cyanxiao/apex-bench/tree/dc2f7d0b06cc099091296d4aa431aed01ee19119). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
