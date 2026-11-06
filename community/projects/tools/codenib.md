# CodeNib (repo search that plans greps and reranks candidates with TypeSafe Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Cross-language source search for Claude Code, Codex and other agents: a planner proposes greps over a temporary repo copy, then OpenRouter decisions with pinned `typesafe/jev-1.13` rerank method-level candidates under a cost ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sysevol-ai/CodeNib) |
| Maintainer | [sysevol-ai](https://github.com/sysevol-ai). Independently curated. |
| Format | Python package / agent runtime (Apache-2.0) |
| Requirements | Python toolchain, repository access, and an OpenRouter key that can call TypeSafe Jev. |
| License | [Apache-2.0](https://github.com/sysevol-ai/CodeNib/blob/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`codenib/agent/runtime/grep_jev.py`](https://github.com/sysevol-ai/CodeNib/blob/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66/codenib/agent/runtime/grep_jev.py) at the pinned commit. |

## When to use

- Find source context across languages without a permanent index.
- Rerank grep hits with a decision model before showing agents.
- Mismatch: needs OpenRouter/Jev credits; not a full code intelligence graph.

## How it works

`codenib/agent/runtime/grep_jev.py` uses OpenRouterDecisions with `JEV_MODEL = "typesafe/jev-1.13"` to score candidate relevance after bounded greps. Integration evidence: [`codenib/agent/runtime/grep_jev.py`](https://github.com/sysevol-ai/CodeNib/blob/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66/codenib/agent/runtime/grep_jev.py).

## Get started

Install per README/docs.codenib.ai, configure OpenRouter, and run a search session against a bound repository.

```sh
git clone https://github.com/sysevol-ai/CodeNib.git && cd CodeNib
# follow README; configure OpenRouter for typesafe/jev-1.13
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sysevol-ai/CodeNib/blob/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66/README.md](https://github.com/sysevol-ai/CodeNib/blob/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66/README.md)

## Limits and data handling

Candidate code snippets and relevance questions are sent to OpenRouter/TypeSafe on your key. Temporary source copies are owned per request.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit c73392a396ed](https://github.com/sysevol-ai/CodeNib/tree/c73392a396ed5dd87dc7deb5ccbf4cea4202bb66). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
