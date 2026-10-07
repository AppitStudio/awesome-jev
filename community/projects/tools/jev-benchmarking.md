# Evaluating and Benchmarking the System One Model Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code for the arXiv paper by Deußer, Sparrenberg and Sifa (arXiv:2609.37647, 2026) benchmarking TypeSafe Jev (pinned `jev-1.13.0`) zero-shot on 37 public datasets against two open-weight LLMs scored on identical requests; raw responses are on Zenodo so every number can be recomputed offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking) |
| Maintainer | [AppliedMachineLearning-Lab](https://github.com/AppliedMachineLearning-Lab). Independently curated. |
| Format | Python package and scripts; responses dataset on Zenodo |
| Requirements | Python 3.10+ (uv or pip); Hugging Face access for datasets (one gated); a TypeSafe key only to rerun Jev; a GPU for open-model scoring. |
| License | [MIT](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/87562114d23597f610754f057e5e0da8659dbcfb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check independent accuracy and calibration results for Jev across many task types.
- Rerun or extend the benchmark on your own datasets.
- Mismatch: results are for `jev-1.13.0`; newer versions may differ.

## How it works

[`jev_benchmarking/runner.py`](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/87562114d23597f610754f057e5e0da8659dbcfb/jev_benchmarking/runner.py) builds requests from Hugging Face datasets and caches responses keyed by request hash; [`scripts/evaluate.py`](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/87562114d23597f610754f057e5e0da8659dbcfb/scripts/evaluate.py) scores them. Dataset selection and API cost are documented in [`docs/datasets.md`](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/87562114d23597f610754f057e5e0da8659dbcfb/docs/datasets.md).

## Get started

Install, download the Zenodo responses into `cache/`, and recompute offline (README):

```sh
git clone https://github.com/AppliedMachineLearning-Lab/jev-benchmarking.git && cd jev-benchmarking
uv venv && source .venv/bin/activate && uv pip install -e ".[dev,paper]"
python scripts/evaluate.py all --split eval
```

Offline recomputation makes no Jev calls; rerunning Jev is billed by TypeSafe.

## Examples and demos

- [Paper on arXiv](https://arxiv.org/abs/2609.37647).
- [Raw responses on Zenodo](https://doi.org/10.5281/zenodo.23039006).

## Limits and data handling

Reported results are the authors'; not rerun on the review host. Datasets keep their own licences.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 87562114d235](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/tree/87562114d23597f610754f057e5e0da8659dbcfb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
