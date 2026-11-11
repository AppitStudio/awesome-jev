# llm-rankers Jev experiments (pointwise to listwise reranking with Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Document-ranking research repo from ielab with Jev experiments as a pointwise, pairwise, setwise and listwise reranker, including scoring all 100 candidates in one request, with scripts and result tables.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ielab/llm-rankers) |
| Maintainer | [ielab](https://github.com/ielab). Independently curated. |
| Format | Research code (Python, Apache-2.0) |
| Requirements | Python, the TREC DL data from `prepare_data.sh`, and a TypeSafe key to rerun live. |
| License | [Apache-2.0](https://github.com/ielab/llm-rankers/blob/bf7911d91a9304bf331ad49c99cc5e09bf2d354e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/jev_rankers.py`](https://github.com/ielab/llm-rankers/blob/bf7911d91a9304bf331ad49c99cc5e09bf2d354e/jev/jev_rankers.py) at the pinned commit. |

## When to use

- Compare Jev reranking modes on standard IR benchmarks.
- Reuse the ranker code in a retrieval pipeline.
- Mismatch: research results are the authors' claims; not independently rerun here.

## How it works

`jev/jev_rankers.py` implements the four ranking modes on `/v1/systemone`; `run_jev.py`, `eval_run.py` and `make_table.py` reproduce the runs and tables described in `jev/README.md`. Integration evidence: [`jev/jev_rankers.py`](https://github.com/ielab/llm-rankers/blob/bf7911d91a9304bf331ad49c99cc5e09bf2d354e/jev/jev_rankers.py).

## Get started

Prepare the data, check access with `check_access.py`, then run `run_jev.py`.

```sh
git clone https://github.com/ielab/llm-rankers.git && cd llm-rankers/jev
pip install -r requirements.txt
python check_access.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev experiments README: [github.com/ielab/llm-rankers/blob/bf7911d91a9304bf331ad49c99cc5e09bf2d354e/jev/README.md](https://github.com/ielab/llm-rankers/blob/bf7911d91a9304bf331ad49c99cc5e09bf2d354e/jev/README.md)

## Limits and data handling

Query and passage text goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit bf7911d91a93](https://github.com/ielab/llm-rankers/tree/bf7911d91a9304bf331ad49c99cc5e09bf2d354e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
