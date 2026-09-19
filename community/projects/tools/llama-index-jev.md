# llama-index-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Add Jev judgments at two points in a LlamaIndex workflow: ranking retrieved passages and selecting the query engine that should handle a question.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WiktorB2004/llama-index-jev) |
| Maintainer | [WiktorB2004](https://github.com/WiktorB2004). Independent of TypeSafe and LlamaIndex. |
| Format | Two Python integration packages. |
| Requirements | Python 3.10+, a LlamaIndex application, and a key for the selected provider. |
| License | [MIT](https://github.com/WiktorB2004/llama-index-jev/blob/main/LICENSE). |

## When to use

- You already retrieve candidate passages and want a semantic relevance step before answering.
- You have several query engines/tools and need a typed selection among them.
- You want an integration with LlamaIndex's existing interfaces instead of a separate application.

Retrieval, embeddings, answer generation, and tool execution remain responsibilities of your application.

## How it works

`JevRerank` evaluates query/passage pairs and orders the candidates. `JevSingleSelector` picks one option; `JevMultiSelector` evaluates options with Nouls. The [reranker guide](https://github.com/WiktorB2004/llama-index-jev/blob/main/packages/llama-index-postprocessor-jev/README.md) and [selector guide](https://github.com/WiktorB2004/llama-index-jev/blob/main/packages/llama-index-selectors-jev/README.md) describe their settings and failure behavior.

## Get started

Install only the integration you need in your project's Python environment:

```sh
python -m pip install llama-index-postprocessor-jev
```

For selection instead, install `llama-index-selectors-jev`. Configure `TYPESAFE_API_KEY` privately for the TypeSafe provider. OpenRouter is an alternative with its own key and provider setting.

In an existing LlamaIndex application, attach a reranker to your query engine:

```python
from llama_index.postprocessor.jev import JevRerank

# `index` is your application's already-configured LlamaIndex index.
query_engine = index.as_query_engine(
    node_postprocessors=[JevRerank(top_n=3, mode="score")],
)
```

This is an integration fragment, not a standalone demo. Querying the engine makes provider requests and may also call your embedding or answering models.

## Examples and demos

- [Runnable walkthroughs](https://github.com/WiktorB2004/llama-index-jev/blob/main/examples/README.md) — prerequisites and expected outputs.
- [Passage reranking](https://github.com/WiktorB2004/llama-index-jev/blob/main/examples/basic_rerank.py).
- [Single selection](https://github.com/WiktorB2004/llama-index-jev/blob/main/examples/basic_selector.py).
- [Query-engine routing](https://github.com/WiktorB2004/llama-index-jev/blob/main/examples/router_query_engine.py).

These upstream walkthroughs use **OpenRouter** and need `OPENROUTER_API_KEY`. Their mock embeddings/answering components do not make the Jev calls offline. Provider-reported benchmark results have not been reproduced by this catalog.

## Limits and data handling

Queries/passages or tool descriptions go to the selected provider. In the default reranker configuration, a failed pass returns the original retrieval order; `raise_on_error=True` surfaces it instead. A low-confidence flag does not remove a passage. Score mode uses a 0–3 rubric, not cosine similarity. Multi-selection can still select a best option when none clears its threshold; inspect policy before relying on abstention. See the [security guidance](https://github.com/WiktorB2004/llama-index-jev/blob/main/docs/security.md).

## Review and maintenance

Documentation was rechecked on 2026-09-19 at [72c73dc](https://github.com/WiktorB2004/llama-index-jev/tree/72c73dc50bca4b7ea6928ef65ea09f1a7ee4a01e). The catalog's 2026-09-18 review passed 52 mocked reranker/selector tests on Python 3.12. No live behavior or task quality was evaluated. See [validation scope](../../../docs/validation.md#community-project-checks).

Related: [RAG triage](../../../examples/rag-triage/README.md) for a smaller example without LlamaIndex.
