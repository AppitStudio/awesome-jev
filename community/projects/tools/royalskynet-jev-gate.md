# Jev Gate (royalskynet)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server and Claude Code/Codex plugin that uses Jev to keep only the parts of logs and tool output that matter, shorten long conversations, and give task-classification and review advice; an optional local Laya pilot handles simple classifications first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royalskynet/jev-gate-mcp) |
| Maintainer | [royalskynet](https://github.com/royalskynet). Independently curated. |
| Format | Node.js MCP server + Claude Code/Codex plugin |
| Requirements | Node.js 22 or 24; a Jev credential; optional local Laya bundle (~540 MB). |
| License | [MIT](https://github.com/royalskynet/jev-gate-mcp/blob/a9dadedce0ce3e57f3e545120f5bfbbad0f08003/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Cut noisy tool output before it reaches Claude Code or Codex.
- Get advisory task classification and completion review (not authorization).
- Mismatch: Savings not measured by the maintainer; judgments cannot authorize actions. Distinct from other listed "jev-gate" projects.

## How it works

Hooks and the gateway call Jev to judge relevance of passages and to classify/review; with `JEV_PROVIDER=laya`, short schema-matched classifications go to local Laya first and fall back to Jev. Jev integration: [`hooks/jev.js`](https://github.com/royalskynet/jev-gate-mcp/blob/a9dadedce0ce3e57f3e545120f5bfbbad0f08003/hooks/jev.js). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/royalskynet/jev-gate-mcp.git
cd jev-gate-mcp
npm install
# then follow gateway/README.md for Claude Code or Codex
```

## Limits and data handling

Text sent for pruning/classification goes to Jev (may be billed). Local classifications are logged for review by default (`JEV_ROUTING_LOG=off` disables). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit a9dadedce0ce](https://github.com/royalskynet/jev-gate-mcp/tree/a9dadedce0ce3e57f3e545120f5bfbbad0f08003). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
