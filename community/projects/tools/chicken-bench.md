# Chicken Bench (decision APIs playing Crossy Road)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Playful benchmark of how far, fast and cheaply decision APIs can play Crossy Road, comparing jev-latest and jev-preview with GPT and Clef models on score, latency, tokens and cost per game, with best-run videos.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mohsen1/chicken-bench) |
| Maintainer | [mohsen1](https://github.com/mohsen1). Independently curated. |
| Format | Python benchmark (uv) |
| Requirements | Python with uv; a TypeSafe API key for Jev runs (and keys for any other models you compare). |
| License | [MIT](https://github.com/mohsen1/chicken-bench/blob/d3ca68e219f107e02e7438a7992b8a7f66b6dad4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`deciders.py`](https://github.com/mohsen1/chicken-bench/blob/d3ca68e219f107e02e7438a7992b8a7f66b6dad4/deciders.py) at the pinned commit. |

## When to use

- Compare decision-model latency and cost in a real-time loop.
- Use as a template for game-playing decision benchmarks.
- Mismatch: a toy benchmark; the author labels the code and write-up AI-generated.

## How it works

`deciders.py` defines a TypeSafe decider that sends each game frame to `https://api.typesafe.ai/v1` with `jev-latest` (or `jev-preview`) using `TYPESAFE_API_KEY`, alongside other providers. Integration evidence: [`deciders.py`](https://github.com/mohsen1/chicken-bench/blob/d3ca68e219f107e02e7438a7992b8a7f66b6dad4/deciders.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv run bench.py --games 10
uv run report.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table and videos in the README: [github.com/mohsen1/chicken-bench#readme](https://github.com/mohsen1/chicken-bench#readme)

## Limits and data handling

Results are a 10-game snapshot from the author's runs.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit d3ca68e219f1](https://github.com/mohsen1/chicken-bench/tree/d3ca68e219f107e02e7438a7992b8a7f66b6dad4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
