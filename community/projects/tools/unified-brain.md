# unified-brain (codebase memory for coding agents, with Jev selecting the evidence)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Persistent codebase memory served to coding agents over MCP: it ingests git history and tree-sitter symbols into one SQLite file with text and vector indexes, and in its Jev mode scores every stored skill against the question so the evidence set is as large as the question needs, bounded by score, count and size limits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DevLoops-ai/unified-brain) |
| Maintainer | [DevLoops-ai](https://github.com/DevLoops-ai). Independently curated. |
| Format | Python service and MCP server |
| Requirements | Python 3.11+; OpenRouter (Jev), Voyage AI or DeepInfra (embeddings) and Fireworks or Anthropic (writer) keys. |
| License | [AGPL-3.0](https://github.com/DevLoops-ai/unified-brain/blob/16e7efb4648370b4a9dbfe935a159cffb05fd3c2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. AGPL-3.0, with a commercial licence offered by the maintainer. |
| Jev evidence | [`codebase_qa_service.py`](https://github.com/DevLoops-ai/unified-brain/blob/16e7efb4648370b4a9dbfe935a159cffb05fd3c2/codebase_qa_service.py) at the pinned commit. |

## When to use

- Give Cursor, OpenCode or Claude Code a retrieval tool over a large repository's history.
- Let Jev pick relevant evidence instead of a fixed top-K vector search.
- Mismatch: cost and accuracy figures are the author's benchmarks, not verified here; the MCP tool takes 20 to 60 seconds.

## How it works

`codebase_qa_service.py` calls `typesafe/jev-1.13` through OpenRouter's Decisions route to score each active skill for the question, keeping those above `JEV_MIN_SCORE` within `JEV_MAX_SKILLS` and `JEV_MAX_CHARS`. Integration evidence: [`codebase_qa_service.py`](https://github.com/DevLoops-ai/unified-brain/blob/16e7efb4648370b4a9dbfe935a159cffb05fd3c2/codebase_qa_service.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/DevLoops-ai/unified-brain.git && cd unified-brain
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python codebase_qa_service.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DevLoops-ai/unified-brain#readme](https://github.com/DevLoops-ai/unified-brain#readme)
- DevLoops: [www.devloops.ai](https://www.devloops.ai)

## Limits and data handling

Code, commit text and questions go to OpenRouter (Jev), the embedding provider and the writer provider. The SQLite database is stored next to the indexed repository.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 16e7efb46483](https://github.com/DevLoops-ai/unified-brain/tree/16e7efb4648370b4a9dbfe935a159cffb05fd3c2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
