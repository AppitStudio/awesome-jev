# Milvus Model

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Use a Python reranker interface to score candidate documents with Jev and return their original indices in score order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milvus-io/milvus-model) |
| Maintainer | Milvus team; the contributor works at Zilliz and contributes to the Milvus ecosystem. |
| Format | Python library adapter, `JevRerankFunction`. |
| Jev's role | Optional document scoring with Noul; Python sorts the scores and applies `top_k`. |
| Requirements | Python, the source version linked below, `requests`, and a TypeSafe account with `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/milvus-io/milvus-model/blob/a5c59e849db2875cfe91d0e59438958f5ec9d54e/LICENSE). |
| Availability | Merged source integration; inclusion in a published package version was not verified. |

## When to use

Use it after retrieving candidate text from Milvus when your application needs scored documents and their original positions. The current prompt frames the query as a scientific claim and asks whether each document provides relevant evidence; evaluate that wording before using it for a different domain.

## How it works

The [adapter](https://github.com/milvus-io/milvus-model/blob/a5c59e849db2875cfe91d0e59438958f5ec9d54e/src/pymilvus/model/reranker/jev.py) sends the claim and all candidate documents to the TypeSafe System One endpoint in one HTTP request. Each document has a Noul question. The default model is `jev-latest`; the constructor also accepts a model name. Python sorts the returned scores in descending order and returns up to `top_k` results with text, score, and original index. This adapter does not retrieve documents or generate an answer.

## Get started

The following is a live integration fragment, not an offline demo. It sends the query and document text to TypeSafe and can incur API charges. Configure `TYPESAFE_API_KEY` privately in your environment.

To use the reviewed source revision in an existing uv project:

```sh
uv add "pymilvus.model @ git+https://github.com/milvus-io/milvus-model.git@a5c59e849db2875cfe91d0e59438958f5ec9d54e" requests
```

Then run a Python file containing:

```python
from pymilvus.model.reranker.jev import JevRerankFunction

rerank = JevRerankFunction()
results = rerank(
    query="0-dimensional biomaterials lack inductive properties.",
    documents=[
        "We study 0-dimensional biomaterials and find they lack inductive properties.",
        "We study 3-dimensional biomaterials for tissue engineering.",
        "This paper reviews inductive properties of various materials.",
    ],
    top_k=2,
)
for result in results:
    print(result.index, result.score, result.text)
```

The output contains up to two scored documents. No fixed live score or ordering is promised. See the [upstream installation instructions](https://github.com/milvus-io/milvus-model#installation) for the broader library.

## Examples and demos

The [upstream unit tests](https://github.com/milvus-io/milvus-model/blob/a5c59e849db2875cfe91d0e59438958f5ec9d54e/tests/test_jev_reranker.py) use synthetic documents and mocked API responses to check missing-key handling, the request shape, sorting, and top-k selection. These are interface checks, not measurements of Jev quality. There is no separate adapter demo linked here.

## Limits and data handling

The query and complete candidate documents leave the application for `api.typesafe.ai`. Keep private records out unless that transfer is authorized. The open-source license does not include free inference.

At the reviewed revision, a response without `answers` raises an error, while individual missing answers or missing Noul scores are skipped. The HTTP call has no explicit timeout or retry policy; callers should account for service failures. Scores are used for ordering, without a calibrated acceptance threshold. The adapter neither enforces a context-size budget nor performs downstream actions.

## Review and maintenance

Reviewed on 2026-09-24 at [commit `a5c59e849db2`](https://github.com/milvus-io/milvus-model/commit/a5c59e849db2875cfe91d0e59438958f5ec9d54e). Source, package metadata, license, and unit tests were inspected. The source installation and live API example were not executed as part of this listing review. No latency, cost-saving, or quality claim is made.
