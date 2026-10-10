# jevify MCP server

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local, offline MCP server that finds AI calls in your code that are really bounded decisions and plans their migration to Jev behind a shadow-mode flag.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucioamor/jevify-mcp-server) |
| Maintainer | [lucioamor](https://github.com/lucioamor). Independently curated. |
| Format | MCP server (npm `@nxlv-ai/jevify`) |
| Requirements | Node.js 20+; an MCP client such as Claude Code or Codex. No TypeSafe key needed for analysis. |
| License | [Apache-2.0](https://github.com/lucioamor/jevify-mcp-server/blob/e406c8bb7fbca9d7dd5fff3183a887b3e2500fc6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Audit a codebase for LLM calls that could become Jev decisions.
- Mismatch: static analysis only; it plans migrations but does not apply or test them.

## How it works

Tools audit files, classify individual call sites, and return a migration plan with thresholds, fallback and rollback; no model calls are made. (Summarized from the upstream [README](https://github.com/lucioamor/jevify-mcp-server/blob/e406c8bb7fbca9d7dd5fff3183a887b3e2500fc6/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Add it to your agent, e.g. `claude mcp add jevify -- npx -y @nxlv-ai/jevify`.

## Limits and data handling

Runs offline and reads only what your agent sends it. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit e406c8bb7fbc](https://github.com/lucioamor/jevify-mcp-server/tree/e406c8bb7fbca9d7dd5fff3183a887b3e2500fc6). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
