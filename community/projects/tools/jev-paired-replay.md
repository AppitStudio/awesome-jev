# Jev Paired-Replay Study

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pre-registered study of whether identical replays flip Jev 1.13's action at shipped thresholds: 12,705 calls on 847 near-threshold items from Banking77, CLINC150 and HelpSteer2 found about 18.5% flips at 0.5 and 0.6 and 5.3% at 0.9, with flips nearly cancelling out.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/poisson-labs/jev-replay) |
| Maintainer | [poisson-labs](https://github.com/poisson-labs). Independently curated. |
| Format | Python replication data (Parquet), harness and an offline verification script |
| Requirements | Python 3 with numpy, scipy and pyarrow to verify; a TypeSafe key and Poisson's `proofload` runner to re-run the sweeps. |
| License | [MIT](https://github.com/poisson-labs/jev-replay/blob/aeaba514ec54e69fd6c6ba847623172614cfee80/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_harness.py`](https://github.com/poisson-labs/jev-replay/blob/aeaba514ec54e69fd6c6ba847623172614cfee80/jev_harness.py) at the pinned commit. |

## When to use

- Size how much threshold-based automation built on Jev may change its action on a re-run before you ship it.
- Recompute every published table from the raw rows without any API calls.
- Mismatch: items were picked near each threshold, so the rates are higher than on ordinary traffic; one model version.

## How it works

`jev_harness.py` sends each frozen item to `jev-1.13.0` in five arms across three replicate sweeps with zero retries; `recompute.py` rebuilds the flip counts, item-clustered intervals and McNemar checks from `data/store/` using only numpy, scipy and pyarrow. Integration evidence: [`jev_harness.py`](https://github.com/poisson-labs/jev-replay/blob/aeaba514ec54e69fd6c6ba847623172614cfee80/jev_harness.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install "numpy>=2.0.0" "scipy>=1.14.0" "pyarrow>=17.0.0"
python3 recompute.py     # offline, reproduces the tables
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Research note: [poissonlabs.ai/research/jev-paired-replay](https://poissonlabs.ai/research/jev-paired-replay)
- Study and dataset specs in `docs/`.

## Limits and data handling

Verification is fully offline. Re-running the sweeps sends public benchmark text to TypeSafe on your key. Published by a company that sells evaluation tooling.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit aeaba514ec54](https://github.com/poisson-labs/jev-replay/tree/aeaba514ec54e69fd6c6ba847623172614cfee80). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
