# jev-rerank-bench

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Reproducible experiments comparing TypeSafe Jev rubric/Choice reranking recipes against Cohere, ZeroEntropy, and open rerankers on shared BM25 candidate sets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anessbelbati/jev-rerank-bench) |
| Maintainer | [anessbelbati](https://github.com/anessbelbati). Independently curated. |
| Format | Python experiment suite + saved responses/scoring; public write-up and evidence viewer. |
| Requirements | Python toolchain per README; API keys for live Jev/Cohere/etc. legs you choose to re-run. |
| License | [MIT](https://github.com/anessbelbati/jev-rerank-bench/blob/54a1efbddd0171c5c63d3337967d790ee22ecf5b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream nDCG/cost tables are author-reported; live spend not run on the review host. |

## When to use

Use to **inspect or reproduce** whether Jev is a competitive passage reranker on the published English/BRIGHT/NevIR/MIRACL setups before adopting a recipe.

## How it works

Models start from the same BM25 top-30 (truncated) candidates; Jev is prompted with rubric, batch yes/no, Choice+none, cascade, and other recipes; scoring code computes nDCG@10 and related metrics.

## Get started

```sh
git clone https://github.com/anessbelbati/jev-rerank-bench.git
cd jev-rerank-bench
git checkout 54a1efbddd0171c5c63d3337967d790ee22ecf5b
# See README + https://anessbelbati.com/blog/i-gave-jev-a-rerankers-job
```

## Examples and demos

- Evidence viewer: [anessbelbati.com/lab/jev-reranking](https://anessbelbati.com/lab/jev-reranking/)
- Blog write-up linked from the README.

## Limits and data handling

Re-running cloud legs sends queries/passages to providers. Saved responses allow offline inspection without new spend.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 54a1efb](https://github.com/anessbelbati/jev-rerank-bench/tree/54a1efbddd0171c5c63d3337967d790ee22ecf5b). AI-assisted README and LICENSE inspection; live benches not run.
