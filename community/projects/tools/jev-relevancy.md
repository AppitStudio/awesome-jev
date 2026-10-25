# jev-relevancy (search relevance evaluation with Jev as the judge, turbopuffer and DuckDB)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Search evaluation framework that calibrates Jev as a relevance judge against Amazon's human-graded ESCI queries, then grades your own retrievers and rerankers with a rubric: turbopuffer runs retrieval and hosted reranking, DuckDB stores every run and computes nDCG, recall and confidence intervals in SQL; also benchmarks Jev as a reranker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rickcrawford/jev-relevancy) |
| Maintainer | [rickcrawford](https://github.com/rickcrawford). Independently curated. |
| Format | Python scripts (uv) with a DuckDB warehouse |
| Requirements | uv (Python 3.12); turbopuffer and TypeSafe API keys; about 2 GB of disk; optional OpenRouter key for LLM judges. |
| License | [MIT](https://github.com/rickcrawford/jev-relevancy/blob/23ff36a7c1f0f552c23e403cdfc346e8e2e5d0a6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/relevancy/jev.py`](https://github.com/rickcrawford/jev-relevancy/blob/23ff36a7c1f0f552c23e403cdfc346e8e2e5d0a6/src/relevancy/jev.py) at the pinned commit. |

## When to use

- Tell whether a search change made results better without human labels for your data.
- Compare Jev with LLM judges and hosted rerankers on the same queries.
- Mismatch: results and agreement figures are the author's measurements, not verified here.

## How it works

`src/relevancy/jev.py` grades (query, result) pairs through TypeSafe's API with a rubric from `rubrics/*.toml` (default `jev-1.13.0`); grades land in DuckDB beside the human labels. Integration evidence: [`src/relevancy/jev.py`](https://github.com/rickcrawford/jev-relevancy/blob/23ff36a7c1f0f552c23e403cdfc346e8e2e5d0a6/src/relevancy/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/rickcrawford/jev-relevancy.git && cd jev-relevancy
cp .env.example .env   # turbopuffer + TypeSafe keys
uv sync
uv run scripts/00_check_setup.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/rickcrawford/jev-relevancy/blob/main/docs/results.md](https://github.com/rickcrawford/jev-relevancy/blob/main/docs/results.md)
- Sample run: [github.com/rickcrawford/jev-relevancy/blob/main/sample/README.md](https://github.com/rickcrawford/jev-relevancy/blob/main/sample/README.md)

## Limits and data handling

Queries and result text go to TypeSafe for grading and to turbopuffer for retrieval. The DuckDB warehouse stays local.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 23ff36a7c1f0](https://github.com/rickcrawford/jev-relevancy/tree/23ff36a7c1f0f552c23e403cdfc346e8e2e5d0a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
