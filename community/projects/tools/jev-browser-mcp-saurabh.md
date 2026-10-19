# Jev Browser MCP (saurabhgangurde)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Local MCP server that lets a coding agent run bounded browser tasks in a dedicated Chrome window: `browser_task` follows a goal through Jev-selected page actions drawn only from the request and live page evidence, with the full Chrome DevTools MCP operation set also exposed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saurabhgangurde/jev-browser-mcp) |
| Maintainer | [saurabhgangurde](https://github.com/saurabhgangurde). Independently curated. |
| Format | MCP server (TypeScript, Node.js 22+) |
| Requirements | Node.js 22+, Chrome, and `TYPESAFE_API_KEY` in the MCP host environment. |
| License | [MIT](https://github.com/saurabhgangurde/jev-browser-mcp/blob/aef86ce7f903b50e8c2b490a2a5e793352314486/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision.ts`](https://github.com/saurabhgangurde/jev-browser-mcp/blob/aef86ce7f903b50e8c2b490a2a5e793352314486/src/decision.ts) at the pinned commit. |

## When to use

- Let a coding agent click through a web flow without writing selectors.
- Inspect pages, tabs, console and network through DevTools MCP from the same server.
- Mismatch: HTTP(S) pages and `about:blank` only for Jev actions; build from source.

## How it works

The server snapshots the page text, URL, title, visible controls and recent actions, and `src/decision.ts` asks Jev (via `@typesafe-ai/sdk`) to choose the next action among concrete options; the loop in `src/index.ts` executes it through Chrome DevTools MCP. Jev chooses actions and does not write answers; discovery, tabs and inspect tools do not call Jev. Integration evidence: [`src/decision.ts`](https://github.com/saurabhgangurde/jev-browser-mcp/blob/aef86ce7f903b50e8c2b490a2a5e793352314486/src/decision.ts).

## Get started

From the upstream README: install, build, then register the server with your MCP client.

```sh
git clone https://github.com/saurabhgangurde/jev-browser-mcp && cd jev-browser-mcp
npm install
npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README tool list (browser_discover, browser_task, browser_devtools)

## Limits and data handling

The goal and page evidence go to TypeSafe on each `browser_task` step. The browser acts with whatever sessions it holds.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit aef86ce7f903](https://github.com/saurabhgangurde/jev-browser-mcp/tree/aef86ce7f903b50e8c2b490a2a5e793352314486). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
