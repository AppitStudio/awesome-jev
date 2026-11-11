# RAG-Fusion Jev experiments (Jev as reranker, fusion weights and router)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

The RAG-Fusion reference repo's experiments that put Jev inside the pipeline as a calibrated reranker and evidence gate, a source of fusion weights and a query-kind router, with result files and a narrated walkthrough.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Raudaschl/rag-fusion) |
| Maintainer | [Raudaschl](https://github.com/Raudaschl). Independently curated. |
| Format | Research code (Python, MIT) |
| Requirements | Python, the NFCorpus setup in the replication folder, and a TypeSafe key to rerun live (answers are cached per run). |
| License | [MIT](https://github.com/Raudaschl/rag-fusion/blob/1a2a820d1150fc1b9b95dee91f56fd73353ef730/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`eval/jev.py`](https://github.com/Raudaschl/rag-fusion/blob/1a2a820d1150fc1b9b95dee91f56fd73353ef730/eval/jev.py) at the pinned commit. |

## When to use

- See how a decision model changes RAG-Fusion's lift over a plain reranker.
- Reuse a Jev relevance gate in retrieval experiments.
- Mismatch: experiments in a research repo, n=200 NFCorpus sample.

## How it works

`eval/jev.py` makes one Jev call each for relevance per document, intent weights per query variant and the query kind, caching answers on disk keyed by `JEV_RUN`; `experiments/jev-in-the-pipeline/README.md` reports the results. Integration evidence: [`eval/jev.py`](https://github.com/Raudaschl/rag-fusion/blob/1a2a820d1150fc1b9b95dee91f56fd73353ef730/eval/jev.py).

## Get started

Read the Jev write-up, then rerun the evals with your key.

```sh
git clone https://github.com/Raudaschl/rag-fusion.git && cd rag-fusion
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev write-up: [github.com/Raudaschl/rag-fusion/blob/1a2a820d1150fc1b9b95dee91f56fd73353ef730/experiments/jev-in-the-pipeline/README.md](https://github.com/Raudaschl/rag-fusion/blob/1a2a820d1150fc1b9b95dee91f56fd73353ef730/experiments/jev-in-the-pipeline/README.md)
- Video walkthrough: [youtu.be/SzfGTXWZf4o](https://youtu.be/SzfGTXWZf4o)

## Limits and data handling

Queries and document text go to TypeSafe on your key when rerun.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 1a2a820d1150](https://github.com/Raudaschl/rag-fusion/tree/1a2a820d1150fc1b9b95dee91f56fd73353ef730). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
