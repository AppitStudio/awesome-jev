# Jev Decision MCP by Adrian (Polish-language MCP server with ten Choice, Score and Noul decision tools, local usage history and cost limits)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python MCP server built on the official `typesafe-sdk` that gives an agent ten advisory decision tools (make_decision, evaluate_condition, score_quality, evaluate_risk, compare_options, classify_data, validate_action, batch_decisions, get_usage and health_check), keeps a local SQLite usage history, and enforces configured cost and call limits. Docs are in Polish.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adriandabrowski444-lgtm/jev-decision-mcp) |
| Maintainer | [Adrian](https://github.com/adriandabrowski444-lgtm). Independently curated. |
| Format | Python MCP server (uv; Docker option) |
| Requirements | Python 3.12+ and uv; a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_decision/provider.py`](https://github.com/adriandabrowski444-lgtm/jev-decision-mcp/blob/97b66a43a291563a612db297287ece64f6a898dc/src/jev_decision/provider.py) at the pinned commit. |

## When to use

- Give an MCP-capable agent cheap typed decisions with spending caps and a local log.
- Mismatch: if you need English docs or an OSI licence.

## How it works

`src/jev_decision/provider.py` calls Jev through the TypeSafe SDK (`https://api.typesafe.ai/v1/systemone`); `service.py` maps each MCP tool to Choice, Score or Noul questions, and `validate_action` checks compliance and risk in one request. Results are advisory; the server never performs the actions it judges. Integration evidence: [`src/jev_decision/provider.py`](https://github.com/adriandabrowski444-lgtm/jev-decision-mcp/blob/97b66a43a291563a612db297287ece64f6a898dc/src/jev_decision/provider.py).

## Get started

Sync dependencies with uv and register the server in your MCP host.

```sh
git clone https://github.com/adriandabrowski444-lgtm/jev-decision-mcp
cd jev-decision-mcp
uv sync --python 3.12
# then add the server to your MCP host per INSTALL.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install guide: [github.com/adriandabrowski444-lgtm/jev-decision-mcp/blob/97b66a43a291563a612db297287ece64f6a898dc/INSTALL.md](https://github.com/adriandabrowski444-lgtm/jev-decision-mcp/blob/97b66a43a291563a612db297287ece64f6a898dc/INSTALL.md)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Text passed to the tools goes to TypeSafe. Polish-only documentation. Several Jev MCP servers are already listed; this one stands out for its cost limits and usage history.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 97b66a43a291](https://github.com/adriandabrowski444-lgtm/jev-decision-mcp/tree/97b66a43a291563a612db297287ece64f6a898dc). Inspected the README, INSTALL.md and the provider and service code at the pinned commit; the server was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
