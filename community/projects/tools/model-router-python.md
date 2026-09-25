# model-router-python

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Python library: filter models by context/budget limits, then ask TypeSafe Jev which remaining model should handle the prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheCoder30ec4/model_router_python) |
| Maintainer | [TheCoder30ec4](https://github.com/TheCoder30ec4). Independently curated. |
| Format | Python library on PyPI (`model-router-python`). |
| Requirements | Python 3; TypeSafe/Jev API access for live routing. |
| License | [MIT](https://github.com/TheCoder30ec4/model_router_python/blob/64f1b3e7a008f5ad467a8e0264890ab16b906ab2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live routing spend not run on the review host. |

## When to use

Use to **pick a model id** for each prompt after hard limit filters, without embedding an LLM-as-judge.

## How it works

Code drops models that cannot fit context/output/budget; Jev chooses among survivors using live price/limit metadata; your app calls the returned model id.

## Get started

```sh
pip install model-router-python
# Docs: https://thecoder30ec4.github.io/model_router_python/
# Pin: https://github.com/TheCoder30ec4/model_router_python/tree/64f1b3e7a008f5ad467a8e0264890ab16b906ab2
```

## Examples and demos

- README `router.route(...)` examples and project docs site.

## Limits and data handling

Prompt summaries/features used for routing go to TypeSafe. The library returns a model id only—it does not call the chat model for you.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 64f1b3e](https://github.com/TheCoder30ec4/model_router_python/tree/64f1b3e7a008f5ad467a8e0264890ab16b906ab2). AI-assisted README and LICENSE inspection; live Jev not run.
