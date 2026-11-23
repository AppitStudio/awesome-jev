# Phoenix MCP by Linus Lee (Home Assistant MCP server with per-key permissions and an optional Jev decision provider for command routing)

[All projects](../README.md) · [Home automation](README.md#home-automation)

A Home Assistant integration that gives AI agents scoped, least-privilege access through MCP: one access key per agent, a permissions tree down to single entities, approvals, audit log and 178 tools. A typed decision provider (TypeSafe Jev, an OpenCode decision endpoint or a local System One server) can route Assist commands to targets and answer Home Assistant's Evaluate action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leecaochang/Phoenix-MCP) |
| Maintainer | [leecaochang](https://github.com/leecaochang). Independently curated. |
| Format | Home Assistant custom integration (Python) with a web panel |
| Requirements | Home Assistant 2026.7+; install via the Marketplace or HACS; a TypeSafe API key only if you pick the TypeSafe / JEV decision provider. |
| License | [MIT](https://github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`custom_components/phoenix_mcp/routing/decision_provider.py`](https://github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/custom_components/phoenix_mcp/routing/decision_provider.py) at the pinned commit. |

## When to use

- Give Claude Code, Cursor or other agents tightly scoped Home Assistant access, with Jev as an optional typed router for commands.
- Mismatch: users who want an unrestricted agent; Phoenix is built around approvals and narrow permissions.

## How it works

`routing/decision_provider.py` implements bounded, non-executing adapters for typed decision APIs; `llm/accounts.py` registers a `TypeSafe / JEV` provider using the `systemone` adapter, alongside OpenCode and local System One options. Decisions pick routes and entities from closed lists; execution stays behind Phoenix's permission checks. Integration evidence: [`custom_components/phoenix_mcp/routing/decision_provider.py`](https://github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/custom_components/phoenix_mcp/routing/decision_provider.py).

## Get started

Add the repository in Home Assistant's Marketplace (or HACS), install, then pick a decision provider under Phoenix MCP settings.

```sh
# Home Assistant 2026.11+: Settings > Marketplace > Add from link
https://github.com/leecaochang/Phoenix-MCP
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/README.md](https://github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/README.md)
- Provider accounts: [github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/custom_components/phoenix_mcp/llm/accounts.py](https://github.com/leecaochang/Phoenix-MCP/blob/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe/custom_components/phoenix_mcp/llm/accounts.py)

## Limits and data handling

With the TypeSafe provider, command text and candidate target summaries are sent to TypeSafe. The Jev provider is one optional part of a large integration; the review inspected the provider code, not a live Home Assistant install.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 37f322817e6e](https://github.com/leecaochang/Phoenix-MCP/tree/37f322817e6ee993bb73bc15bd29bdb8ef6cf2fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
