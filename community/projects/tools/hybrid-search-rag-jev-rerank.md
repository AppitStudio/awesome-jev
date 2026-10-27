# hybrid-search-rag (measured RAG ablation over near-duplicate docs, with Jev as a reranker)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Small local RAG pipeline (BM25 plus dense vectors fused with RRF, an LLM reranker, cited answers and a deterministic citation checker) measured stage by stage on a synthetic corpus full of near-duplicate documents; one experiment swaps the slow LLM reranker for Jev, asking one yes/no question per passage, and reports quality, latency and cost with confidence intervals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Guilherme-pxt/hybrid-search-rag) |
| Maintainer | [Guilherme-pxt](https://github.com/Guilherme-pxt). Independently curated. |
| Format | Python (numpy) with a local Ollama server |
| Requirements | Python 3.11+, numpy, requests and Ollama; a TypeSafe API key only for the Jev experiment. |
| License | [MIT](https://github.com/Guilherme-pxt/hybrid-search-rag/blob/120e3e7058471ebd83883b2bfe532127deffb751/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hybridrag/jev.py`](https://github.com/Guilherme-pxt/hybrid-search-rag/blob/120e3e7058471ebd83883b2bfe532127deffb751/hybridrag/jev.py) at the pinned commit. |

## When to use

- See what each retrieval stage buys when wrong-entity look-alikes are the main failure.
- Compare Jev against an LLM reranker on latency and accuracy.
- Mismatch: synthetic corpus, one laptop; numbers are the author's.

## How it works

`hybridrag/jev.py` posts each question with its fused top 20 passages as Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0` pinned) and sorts by Jev's probability. Integration evidence: [`hybridrag/jev.py`](https://github.com/Guilherme-pxt/hybrid-search-rag/blob/120e3e7058471ebd83883b2bfe532127deffb751/hybridrag/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Guilherme-pxt/hybrid-search-rag && cd hybrid-search-rag
python3 -m unittest discover -s tests -t .
python3 -m hybridrag run-all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/Guilherme-pxt/hybrid-search-rag#readme](https://github.com/Guilherme-pxt/hybrid-search-rag#readme)

## Limits and data handling

Questions and candidate passages go to TypeSafe during `jev-eval`; everything else runs locally.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 120e3e705847](https://github.com/Guilherme-pxt/hybrid-search-rag/tree/120e3e7058471ebd83883b2bfe532127deffb751). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
