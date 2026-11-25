# Veya by Tobias Gundhus (local decision engine forked from Laya that serves Jev's /v1/systemone wire protocol on your own hardware)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local engine for classification, scoring and yes/no questions that runs through Python or ONNX Runtime with HTTP and local MCP interfaces. A fork of the open Laya engine that adds configurable decision retention, replay across devices and precision modes, and framework integrations (LangChain, LlamaIndex, CrewAI, Agno); it uses upstream Laya checkpoints, not TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tgundhus/Veya) |
| Maintainer | [Tobias Gundhus](https://github.com/tgundhus). Independently curated. |
| Format | Python package with ONNX, TypeScript, Java and .NET clients |
| Requirements | Python 3.10 to 3.13; optional `serve` and `mcp` extras. |
| License | [Apache-2.0](https://github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`veya/serve.py`](https://github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/veya/serve.py) at the pinned commit. |

## When to use

- Keep routing and guardrail decisions on your own hardware with a Jev-compatible API.
- Mismatch: if you need Jev-level accuracy; on the author's 64-case Chinese diagnostic Veya scored 20/64 versus Jev's 64/64.

## How it works

`veya/serve.py` exposes Veya over TypeSafe Jev's `/v1/systemone` wire protocol so Jev clients can point at a local server. No TypeSafe calls are needed; the README's Jev numbers are recorded comparison calls. Integration evidence: [`veya/serve.py`](https://github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/veya/serve.py).

## Get started

Install from GitHub with the serve and MCP extras.

```sh
python -m pip install "veya[serve,mcp] @ git+https://github.com/tgundhus/Veya.git"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Limits: [github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/docs/limits.md](https://github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/docs/limits.md)
- Upstream review: [github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/docs/reports/upstream-review-2026-11-25.md](https://github.com/tgundhus/Veya/blob/b15114b187b6d11fce3e0e58cd94d08321a25db9/docs/reports/upstream-review-2026-11-25.md)

## Limits and data handling

Measurements are the author's own on synthetic cases and do not establish general accuracy. Replay improves repeatability, not accuracy.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit b15114b187b6](https://github.com/tgundhus/Veya/tree/b15114b187b6d11fce3e0e58cd94d08321a25db9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
