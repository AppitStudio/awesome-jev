# Master-JEV Hook

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local gateway and MCP server that lets Claude Code, Claude Desktop and Codex hand explicit choices to Jev (which approach, source or next action; classify, verify, score or rank a batch), with Claude Code hooks for risky-command and unverified-completion spot checks and a local query dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KeepGlide/master-jev-hook) |
| Maintainer | [KeepGlide](https://github.com/KeepGlide). Independently curated. |
| Format | TypeScript gateway with stdio MCP adapter, Python hooks and an installer |
| Requirements | Node with pnpm, Python 3; your own TypeSafe key (or OpenRouter / Vercel AI Gateway via `JEV_PROVIDER`). |
| License | [Apache-2.0](https://github.com/KeepGlide/master-jev-hook/blob/519f32de523ea54188c475c41f052ffbf4e4a9df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gateway/bin/master-jev-mcp.mjs`](https://github.com/KeepGlide/master-jev-hook/blob/519f32de523ea54188c475c41f052ffbf4e4a9df/gateway/bin/master-jev-mcp.mjs) at the pinned commit. |

## When to use

- Let a coding agent delegate choices between options it has already listed, and keep a log of every query.
- Add non-blocking checks in Claude Code before risky Bash commands and before claiming a task is done.
- Mismatch: the Claude Code plugin packaging is an early-access beta (1.3.0-beta.1).

## How it works

The MCP adapter forwards tool calls to the local gateway, which builds a Choice, Score or Noul question and posts it to `api.typesafe.ai/v1/systemone`, retrying only on 429/503/529; the API key stays in the gateway. `claude_jev.py` posts its own checks to `/master/decide` and never blocks the session. Integration evidence: [`gateway/bin/master-jev-mcp.mjs`](https://github.com/KeepGlide/master-jev-hook/blob/519f32de523ea54188c475c41f052ffbf4e4a9df/gateway/bin/master-jev-mcp.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
python3 install.py --dry-run
python3 install.py --target all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English and Brazilian Portuguese READMEs.
- Dashboard of every Jev query served by the local gateway.

## Limits and data handling

Agent context and candidates go to TypeSafe (or the chosen gateway) on your key. Jev picks between options; it does not grant permissions.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 519f32de523e](https://github.com/KeepGlide/master-jev-hook/tree/519f32de523ea54188c475c41f052ffbf4e4a9df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
