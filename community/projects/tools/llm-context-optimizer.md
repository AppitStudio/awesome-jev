# LLM Context Optimizer

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript SDK for choosing which document chunks to send with an OpenAI, Anthropic, or Google Gemini request. The core runs a local deterministic heuristic; TypeSafe Jev is an optional relevance backend. Initial source release; no npm registry release claimed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enigma49/llm-context-optimizer) |
| Maintainer | [enigma49](https://github.com/enigma49). Independently curated. |
| Format | TypeScript library (build from source / `npm pack`) |
| Requirements | Node.js 24; optional TypeSafe API key. |
| License | [MIT](https://github.com/enigma49/llm-context-optimizer/blob/40da093e6f6305eef59a6666b34df5a890c64796/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Cut prompt size on retrieval-heavy requests while pinning essential documents.
- Mismatch: Early release; selection can drop needed evidence, as the upstream README warns.

## How it works

Documents are chunked, protected or atomic chunks are kept, and the remaining chunks are ranked locally or by Jev under a reduction policy. (Summarized from the upstream [README](https://github.com/enigma49/llm-context-optimizer/blob/40da093e6f6305eef59a6666b34df5a890c64796/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `npm ci && npm run check`, then `npm pack` and install the archive in your application.

## Limits and data handling

Local mode sends nothing; the Jev backend sends chunk text to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 40da093e6f63](https://github.com/enigma49/llm-context-optimizer/tree/40da093e6f6305eef59a6666b34df5a890c64796). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
