# jev-rag

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Vector-free local RAG: SQLite BM25 retrieval, TypeSafe Jev evidence reranking, optional grounded LLM answers (no embeddings).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aifabrice/jev-rag) |
| Maintainer | [aifabrice](https://github.com/aifabrice). Independently curated. |
| Format | Python local RAG library/CLI/web UI. |
| Requirements | Python 3.9+; TYPESAFE_API_KEY for Jev rerank; optional OpenRouter/chat model for answers; pypdf optional for PDF. |
| License | [MIT](https://github.com/aifabrice/jev-rag/blob/78b6c10982316290cfcbf6ed3ba22af7a7209388/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for **local, embedding-free search** where BM25 finds candidates and Jev scores evidence usefulness. Prefer vector RAG when semantic paraphrase search is the main need.

## How it works

Indexes a folder into SQLite FTS5/BM25, batches Jev relevance questions over candidates, and optionally sends selected passages to a chat model for cited streaming answers.

## Get started

```sh
git clone https://github.com/aifabrice/jev-rag.git
cd jev-rag
git checkout 78b6c10982316290cfcbf6ed3ba22af7a7209388
# See README for index/query/UI; needs TYPESAFE_API_KEY for live Jev rerank
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 78b6c10](https://github.com/aifabrice/jev-rag/tree/78b6c10982316290cfcbf6ed3ba22af7a7209388). AI-assisted README and license inspection; install/live paths not executed.
