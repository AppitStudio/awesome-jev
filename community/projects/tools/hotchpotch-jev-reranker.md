# jev-reranker (hotchpotch)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python library (PyPI) that scores and optionally filters retrieved documents for RAG with TypeSafe Jev—listwise, pointwise, and pairwise modes with concurrency, splitting, and retries.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hotchpotch/jev-reranker) |
| Maintainer | [hotchpotch](https://github.com/hotchpotch). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-reranker 0.1.2** on PyPI (`uv`/`pip`); sync and async APIs. |
| Requirements | Python **≥ 3.11**; live calls need `TYPESAFE_API_KEY` (optional `TYPESAFE_ENDPOINT`). Optional extras: `tokenizer`, `sentence-transformers`. |
| License | [MIT](https://github.com/hotchpotch/jev-reranker/blob/d58594b393b29b7ee6398cc9337dc5e9d6c6691e/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from the Rust CLI [jev-reranker (shinpr)](jev-reranker.md) and from [llama-index-jev](llama-index-jev.md). Offline `uv run pytest -q`: **206 passed, 52 skipped**. Live TypeSafe calls were not run. |

## When to use

Use it when you already have a candidate document list and want a **Python-native Jev stage** that can reorder and drop weak evidence before generation. Prefer [jev-reranker (shinpr)](jev-reranker.md) for a stdin/stdout Rust pipe; prefer [llama-index-jev](llama-index-jev.md) inside LlamaIndex pipelines.

## How it works

[`src/jev_reranker/reranker.py`](https://github.com/hotchpotch/jev-reranker/blob/d58594b393b29b7ee6398cc9337dc5e9d6c6691e/src/jev_reranker/reranker.py) posts to `https://api.typesafe.ai/v1/systemone` (override via env). `relevance_rerank()` scores usefulness as evidence and filters below a threshold; `rerank()` reorders without filtering by default. Long lists are split; httpx handles concurrency and retries. Application code owns what happens when the kept set is empty.

## Get started

```sh
pip install jev-reranker
# or: uv add jev-reranker
export TYPESAFE_API_KEY=...   # do not paste secrets into chat
```

```python
from jev_reranker import Reranker

reranker = Reranker()
kept = reranker.relevance_rerank("query", ["doc a", "doc b", "doc c"])
```

From the reviewed tip:

```sh
git clone https://github.com/hotchpotch/jev-reranker.git
cd jev-reranker
git checkout d58594b393b29b7ee6398cc9337dc5e9d6c6691e
uv run pytest -q
```

Live ranking sends query and document text to TypeSafe and can incur charges.

## Examples and demos

- Hugging Face blog walkthrough linked from the upstream README.
- Package `examples/` and unit tests under `tests/` (mocked HTTP; live tests skipped without a key).
- This listing: `uv run pytest -q` → **206 passed, 52 skipped** on the review host.

## Limits and data handling

Query and candidate document strings leave the host on live calls. Thresholds and prompt dictionaries are application policy—tune them for your corpus. Confirm TypeSafe billing separately. Unofficial community library—not affiliated with TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [commit d58594b](https://github.com/hotchpotch/jev-reranker/tree/d58594b393b29b7ee6398cc9337dc5e9d6c6691e): **0.1.2**, MIT. AI-assisted source review of README, LICENSE, `src/jev_reranker/*`, and offline pytest. No live provider calls.

Related: [jev-reranker (shinpr)](jev-reranker.md), [llama-index-jev](llama-index-jev.md), [jegrep](jegrep.md).
