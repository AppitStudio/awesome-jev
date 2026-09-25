# System One Connector

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go MCP connector (`evaluate`) that gives agents typed System One judgments (TypeSafe Jev, optional local Laya/CLM) with probabilities instead of prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsmostafa/system-one-connector) |
| Maintainer | [itsmostafa](https://github.com/itsmostafa). Independently curated. Distinct from catalogued [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp). |
| Format | Static Go binary CLI + MCP registration for Claude Code/Desktop, Codex, Hermes, pi. |
| Requirements | macOS/Linux installer; `TYPESAFE_API_KEY` and/or OpenRouter; optional `TYPESAFE_BASE_URL` for local System One hosts. |
| License | [MIT](https://github.com/itsmostafa/system-one-connector/blob/349f981773d0b0a31257bfe0e886fb99da0dae04/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live MCP/TypeSafe paths not run on the review host. |

## When to use

Use when an agent needs **branchable Noul/Choice/Score answers** via MCP. Prefer library SDKs when you want an in-process API instead of an MCP tool.

## How it works

`evaluate setup mcp` registers the connector; agents send `state` plus typed `questions` and receive calibrated probabilities. Supports batched `items` and custom System One hosts.

## Get started

```sh
curl -fsSL https://raw.githubusercontent.com/itsmostafa/system-one-connector/main/install.sh | sh
TYPESAFE_API_KEY=your-key evaluate setup mcp
git clone https://github.com/itsmostafa/system-one-connector.git
cd system-one-connector
git checkout 349f981773d0b0a31257bfe0e886fb99da0dae04
```

## Examples and demos

- README ticket urgency/department example JSON request/response.
- Docs for local CLM/Laya hosts under `docs/configuration.md`.

## Limits and data handling

Prompt/state text goes to the configured TypeSafe, OpenRouter, or local endpoint.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 349f981](https://github.com/itsmostafa/system-one-connector/tree/349f981773d0b0a31257bfe0e886fb99da0dae04). AI-assisted README and LICENSE inspection; installer and live MCP not executed.
