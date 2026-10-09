# memsearch

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Persistent Markdown-backed memory for coding agents (Claude Code, Codex, DeepSeek Harness, OpenClaw, OpenCode) indexed in Milvus, with optional TypeSafe Jev reranking of recalled memory chunks: one `/v1/systemone` request scores every candidate with a yes/no relevance question, off by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zilliztech/memsearch) |
| Maintainer | [zilliztech](https://github.com/zilliztech) (Zilliz). Independently curated. |
| Format | Python package + CLI + agent plugins (`memsearch` on PyPI) |
| Requirements | Python; Milvus Lite/Server/Zilliz Cloud per upstream docs; an embedding provider. Jev reranking needs `TYPESAFE_API_KEY` and an explicit `reranker.model = "jev:jev-latest"` setting. |
| License | [MIT](https://github.com/zilliztech/memsearch/blob/09e07d86b31ff81938b4f44a57099b6a9fc8723f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give several coding agents one shared, human-editable memory and improve recall ordering with an optional hosted reranker.
- Mismatch: if search queries and memory text must not leave the machine, keep the default local reranking (Jev is opt-in and remote).

## How it works

Jev is one optional reranker. [`src/memsearch/jev_reranker.py`](https://github.com/zilliztech/memsearch/blob/09e07d86b31ff81938b4f44a57099b6a9fc8723f/src/memsearch/jev_reranker.py) posts all candidates in one request to `https://api.typesafe.ai/v1/systemone`, one Noul question per candidate (adapted from TypeSafe's rerank cookbook), and surfaces errors instead of silently returning unreranked results. Enablement is documented in [`docs/home/configuration.md`](https://github.com/zilliztech/memsearch/blob/09e07d86b31ff81938b4f44a57099b6a9fc8723f/docs/home/configuration.md); project-local config cannot turn the remote provider on. The maintainers publish a [reranking evaluation](https://github.com/zilliztech/memsearch/blob/09e07d86b31ff81938b4f44a57099b6a9fc8723f/evaluation/reranking-evaluation.md) pinned to `jev-1.13.0` (their results; not reproduced here).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install "memsearch[onnx]"
export TYPESAFE_API_KEY=...   # only for Jev reranking
memsearch config set reranker.model jev:jev-latest
```

## Limits and data handling

With Jev reranking on, search queries and retrieved chunk text go to TypeSafe and are billed to your key; memories otherwise stay in local Markdown plus the configured Milvus backend. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 09e07d86b31f](https://github.com/zilliztech/memsearch/tree/09e07d86b31ff81938b4f44a57099b6a9fc8723f). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
