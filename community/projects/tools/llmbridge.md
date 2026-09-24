# llmbridge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenAI-compatible LLM routing gateway: L1 rules, L2 TypeSafe Jev task/complexity judgments, then L3 fallback—observable, degradable, and billable before the first token.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dragonlin-ai/llmbridge) |
| Maintainer | [dragonlin-ai](https://github.com/dragonlin-ai). Independently curated. |
| Format | Python FastAPI gateway + Vue admin (`llmbridge`). |
| Requirements | Python 3.11+; downstream LLM provider keys; TypeSafe Jev for L2 routing. |
| License | [Apache-2.0](https://github.com/dragonlin-ai/llmbridge/blob/7bf7aa8d76cef4512f4466c1c62c843cb5cc845d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live routing not run. Docs primarily Chinese with English README_EN.md. |

## When to use

Use when apps need **one OpenAI-compatible endpoint** with Jev-informed model routing. Prefer RLCD Gateway for coding-agent login forwarding and System One audit.

## How it works

Requests hit the gateway; rules and TypeSafe Jev classify task type/complexity; traffic is forwarded to the chosen downstream model with observability and fallback (per README).

## Get started

```sh
git clone https://github.com/dragonlin-ai/llmbridge.git
cd llmbridge
git checkout 7bf7aa8d76cef4512f4466c1c62c843cb5cc845d
# follow README / README_EN.md deploy steps
```

## Examples and demos

- README architecture and API overview; Vue admin UI.

## Limits and data handling

Prompts reach both Jev (for routing) and the selected LLM provider. Gateway does not execute tools—`tools`/`tool_calls` pass through.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 7bf7aa8](https://github.com/dragonlin-ai/llmbridge/tree/7bf7aa8d76cef4512f4466c1c62c843cb5cc845d). AI-assisted README inspection; live deploy not run.

Related: [hono-jev-router](hono-jev-router.md).
