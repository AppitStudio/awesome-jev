# Jev CodeGuard by undowhai113 (MCP server and PreToolUse hook that has Jev and local linters vet coding agents' shell commands and diffs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source MCP server, `PreToolUse` hook and local dashboard for Claude Code, Codex, Cursor, Windsurf and Antigravity. A command firewall (`jev_guard_action` and the `jev-gate` hook) asks Jev about a literal shell command's blast radius, destructiveness and secret exfiltration before it runs; an auditor combines local AST and lint engines (ts-morph, oxlint, ruff) with OWASP-style rubrics; and a git diff verifier checks changes locally without model tokens. A local page at 127.0.0.1:4399 shows decisions live.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/undowhai113/jev-codeguard) |
| Maintainer | [undowhai113](https://github.com/undowhai113). Independently curated. |
| Format | MCP server and CLI hook (TypeScript, Node.js, MIT) |
| Requirements | Node.js 20+, a coding agent with MCP or hooks, and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/undowhai113/jev-codeguard/blob/ab95631970684b132b0b6426a7a9b72a90779212/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/jev-client.ts`](https://github.com/undowhai113/jev-codeguard/blob/ab95631970684b132b0b6426a7a9b72a90779212/src/core/jev-client.ts) at the pinned commit. |

## When to use

- Put a fast Jev check in front of an agent's shell commands and code changes.
- Mismatch: a replacement for sandboxing or code review; treat its verdicts as one layer.

## How it works

`src/core/jev-client.ts` posts the command and code questions to `https://api.typesafe.ai/v1/systemone`; `src/mcp/server.ts` exposes the tools to the agent. Integration evidence: [`src/core/jev-client.ts`](https://github.com/undowhai113/jev-codeguard/blob/ab95631970684b132b0b6426a7a9b72a90779212/src/core/jev-client.ts).

## Get started

Clone, build and register the MCP server and hook with your agent as the README describes.

```sh
git clone https://github.com/undowhai113/jev-codeguard && cd jev-codeguard
npm install && npm run build
export TYPESAFE_API_KEY=...
claude mcp add jev-codeguard -- node "$PWD/dist/src/cli/index.js" serve   # Claude Code; other agents per the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/undowhai113/jev-codeguard/blob/ab95631970684b132b0b6426a7a9b72a90779212/README.md](https://github.com/undowhai113/jev-codeguard/blob/ab95631970684b132b0b6426a7a9b72a90779212/README.md)

## Limits and data handling

Commands and code snippets it checks go to TypeSafe on your key. The README's speed and cost figures are the author's; the firewall's catch rate is not independently measured.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit ab9563197068](https://github.com/undowhai113/jev-codeguard/tree/ab95631970684b132b0b6426a7a9b72a90779212). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
