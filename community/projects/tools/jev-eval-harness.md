# jev-eval-harness

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pre-registered research harness testing whether Jev's typed market judgments beat trivial baselines on hourly BTC/USD, with sealed holdout, purge, deflated Sharpe and bootstrap CIs; the measured answer was no.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Joshua7792/jev-eval-harness) |
| Maintainer | [Joshua7792](https://github.com/Joshua7792). Independently curated. |
| Format | Python research harness |
| Requirements | Python; `TYPESAFE_API_KEY` (or Vercel AI Gateway) for live replays; mock mode needs no key. |
| License | [MIT](https://github.com/Joshua7792/jev-eval-harness/blob/0e494c0fc1f650f4ff07de263be6fa39681fcbbc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevloop/client.py`](https://github.com/Joshua7792/jev-eval-harness/blob/0e494c0fc1f650f4ff07de263be6fa39681fcbbc/jevloop/client.py) at the pinned commit. |

## When to use

- Evaluate a decision model on a forecasting task with bars fixed in advance.
- Reuse the metering, caching and replay tooling for honest evals.
- Mismatch: not trading software; places no orders.

## How it works

`jevloop/client.py` calls `https://api.typesafe.ai/v1/systemone` with `jev-latest`, or the Vercel AI Gateway route. The lab fetches public bars, snapshots what the model sees each hour, replays the scored window with caching and metering, and scores direction and regime calls against pre-registered bars. Integration evidence: [`jevloop/client.py`](https://github.com/Joshua7792/jev-eval-harness/blob/0e494c0fc1f650f4ff07de263be6fa39681fcbbc/jevloop/client.py).

## Get started

From the upstream README: run the public-data lab and the mock replay first, then a real replay with `--limit`.

```sh
python -m jevloop lab fetch --symbol BTC/USD --source alpaca
python -m jevloop jevtest replay --mock --limit 24 --interval-s 1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/results.md
- docs/preregistration.md

## Limits and data handling

Market snapshots go to TypeSafe on real replays, which cost money. Result covers one model, task, dataset and period.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 0e494c0fc1f6](https://github.com/Joshua7792/jev-eval-harness/tree/0e494c0fc1f650f4ff07de263be6fa39681fcbbc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
