# DecideBench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of decision models (Jev and open alternatives) and LLMs measuring accuracy, cost per task and latency together on 400 contrastive decisions, with Pareto frontiers instead of a single ranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/choyiny/decidebench) |
| Maintainer | [choyiny](https://github.com/choyiny). Independently curated. |
| Format | Python benchmark, dataset and leaderboard |
| Requirements | Python with uv; provider keys for live re-runs. |
| License | [MIT](https://github.com/choyiny/decidebench/blob/bbf8f2c77b544952b42be555866729a22c33980d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decidebench/systems/jev.py`](https://github.com/choyiny/decidebench/blob/bbf8f2c77b544952b42be555866729a22c33980d/decidebench/systems/jev.py) at the pinned commit. |

## When to use

- Compare Jev against open decision models on accuracy, cost and latency.
- Rebuild the published tables from stored results.
- Mismatch: results are the author's measurements.

## How it works

Each system adapter (including the Jev adapter calling TypeSafe) answers the same 400 items; reports rebuild tables and Pareto frontiers from `results/v1`. Integration evidence: [`decidebench/systems/jev.py`](https://github.com/choyiny/decidebench/blob/bbf8f2c77b544952b42be555866729a22c33980d/decidebench/systems/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run python -m decidebench.report
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Leaderboard: [huggingface.co/spaces/choyiny/decidebench-leaderboard](https://huggingface.co/spaces/choyiny/decidebench-leaderboard)

## Limits and data handling

Live re-runs send benchmark items to providers and bill your keys; the stored results need no key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit bbf8f2c77b54](https://github.com/choyiny/decidebench/tree/bbf8f2c77b544952b42be555866729a22c33980d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
