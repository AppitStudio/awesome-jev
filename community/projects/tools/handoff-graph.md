# Handoff Graph

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Issue-routing experiment that stores handoffs in FalkorDB and asks TypeSafe Jev one narrow question per candidate owner. Graph memory cut human escalations from ~two-thirds to under 10% on held-out VS Code issues in the author's study.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aashish-g03/handoff-graph) |
| Maintainer | [aashish-g03](https://github.com/aashish-g03). Independently curated. |
| Format | Python agents + FalkorDB graph memory; live demo and MCP on Railway |
| Requirements | Python env with typesafe-sdk; FalkorDB; TYPESAFE_API_KEY / JEV_MODEL for live routing. |
| License | [MIT](https://github.com/aashish-g03/handoff-graph/blob/a16aece428ec836a46e0d17893f3e247b7a06566/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/handoff_graph/decide.py`](https://github.com/aashish-g03/handoff-graph/blob/a16aece428ec836a46e0d17893f3e247b7a06566/src/handoff_graph/decide.py) at the pinned commit. |

## When to use

- Study graph-backed handoff memory with a typed decision model.
- Want each route decision tied to an inspectable graph path.
- Mismatch: research/demo stack; public MCP writes are disabled.

## How it works

`decide.py` wraps `TypeSafeClient` (default `jev-1.14.0`) for per-candidate questions. A learner records handoffs into FalkorDB; a router reads paths and either assigns, keeps, or escalates to a human. Integration evidence: [`src/handoff_graph/decide.py`](https://github.com/aashish-g03/handoff-graph/blob/a16aece428ec836a46e0d17893f3e247b7a06566/src/handoff_graph/decide.py).

## Get started

Clone the repo or open the live demo; set a TypeSafe key for local routing.

```sh
git clone https://github.com/aashish-g03/handoff-graph && cd handoff-graph
# see README for FalkorDB + TYPESAFE_API_KEY setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [handoff-graph.up.railway.app/](https://handoff-graph.up.railway.app/)
- [dev.to/aashish_g/same-ai-with-and-without-memory-a-falkordb-graph-took-issue-routing-from-18-to-74-3812](https://dev.to/aashish_g/same-ai-with-and-without-memory-a-falkordb-graph-took-issue-routing-from-18-to-74-3812)

## Limits and data handling

Study metrics are author-reported on VS Code issues. Live demo is read-mostly. Issue text goes to TypeSafe when routing live.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit a16aece428ec](https://github.com/aashish-g03/handoff-graph/tree/a16aece428ec836a46e0d17893f3e247b7a06566). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
