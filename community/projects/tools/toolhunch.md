# toolhunch

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python library for agents with too many tools: hybrid search narrows a tool catalog, then a fast decider — TypeSafe Jev, Cloudflare Clef, or Jev-compatible local servers (Strands Decider, rizzo-flow, Laya) — or an LLM picks one tool or answers 'none'; maintainer benchmarks on 40–101-tool catalogs and ToolRet's 44,453 tools, with Pydantic AI integration.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dfm88/toolhunch) |
| Product homepage | [pypi.org](https://pypi.org/project/toolhunch/) |
| Maintainer | [dfm88](https://github.com/dfm88). Independently curated. |
| Format | Python library (PyPI 0.2.0 at review) with optional Pydantic AI extra and benchmark package |
| Requirements | Python with pip/uv; `TYPESAFE_API_KEY` for Jev (or a Clef / local Jev-compatible endpoint). |
| License | [MIT](https://github.com/dfm88/toolhunch/blob/9e8a450f0bd0c29136581c0685da7e5e9d440c66/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Expose hundreds of MCP tools to an agent without sending every definition on every call.
- Let the decider answer 'none' when no tool fits.
- Mismatch: at 40–101 tools upstream found GPT agents did about as well with every tool loaded; search earns its place at larger catalogs.

## How it works

A BM25/hybrid retriever builds candidates; [`decision/decider.py`](https://github.com/dfm88/toolhunch/blob/9e8a450f0bd0c29136581c0685da7e5e9d440c66/src/toolhunch/decision/decider.py) asks the decider to pick among them with an abstain option, using the Jev wire format in [`jev_wire.py`](https://github.com/dfm88/toolhunch/blob/9e8a450f0bd0c29136581c0685da7e5e9d440c66/src/toolhunch/decision/jev_wire.py). [`examples/jev_compatible_server.py`](https://github.com/dfm88/toolhunch/blob/9e8a450f0bd0c29136581c0685da7e5e9d440c66/examples/jev_compatible_server.py) shows a local endpoint.

## Get started

Install (README *Quickstart*):

```sh
pip install toolhunch                  # or: uv add toolhunch
pip install "toolhunch[pydantic-ai]"   # Pydantic AI integration
export TYPESAFE_API_KEY=...
```

Each decision is a request to the chosen decider billed to your key (local deciders are free to run).

## Examples and demos

- README *Results* (precision with confidence intervals, cost and latency per decider).

## Limits and data handling

Requests and candidate tool cards go to the chosen decider. Benchmarks are the maintainer's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 9e8a450f0bd0](https://github.com/dfm88/toolhunch/tree/9e8a450f0bd0c29136581c0685da7e5e9d440c66). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
