# Jev RAG Chinese Benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible Chinese RAG reranking benchmark for TypeSafe Jev on C-MTEB/T2Reranking with a frozen protocol, pinned model, cost caps and full per-call logs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vicfei/jev-rag-zh-benchmark) |
| Maintainer | [vicfei](https://github.com/vicfei). Independently curated. |
| Format | Python benchmark (uv) |
| Requirements | Python (uv); TypeSafe key; small cost cap per run. |
| License | [MIT](https://github.com/vicfei/jev-rag-zh-benchmark/blob/27ec0b9b07df21b2c0914456cd153c45911faf5f/LICENSE) |
| Jev evidence | [`scripts/run_bench.py`](https://github.com/vicfei/jev-rag-zh-benchmark/blob/27ec0b9b07df21b2c0914456cd153c45911faf5f/scripts/run_bench.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Check Jev Score/Noul reranking quality on Chinese queries before adopting it.
- Mismatch: 100-query stage-1 sample; author reports limitations next to results.

## How it works

Prepares a deterministic sample, runs Score and Noul variants with runtime cost breakers, and analyzes nDCG against BM25; logs mirrored on Hugging Face and ModelScope. (Summarized from the upstream [README](https://github.com/vicfei/jev-rag-zh-benchmark/blob/27ec0b9b07df21b2c0914456cd153c45911faf5f/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `uv run python scripts/prepare_data.py --n 100 --out s1` then `scripts/run_bench.py` per the README.

## Limits and data handling

Benchmark text goes to TypeSafe; results are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 27ec0b9b07df](https://github.com/vicfei/jev-rag-zh-benchmark/tree/27ec0b9b07df21b2c0914456cd153c45911faf5f). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
