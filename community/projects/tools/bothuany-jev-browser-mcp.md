# jev-browser-mcp (bothuany)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP browser for coding agents: your model states intent; TypeSafe Jev chooses clicks; a cheap reader model sees the page; only the answer returns—not the DOM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bothuany/jev-browser-mcp) |
| Maintainer | [bothuany](https://github.com/bothuany). Independently curated. |
| Format | Node.js MCP server (`npx -y jev-browser-mcp`) on Playwright. |
| Requirements | Node 20+; Chrome via Playwright; TypeSafe/Jev credentials; Gemini Flash (or configured reader) for page reads. |
| License | [MIT](https://github.com/bothuany/jev-browser-mcp/blob/5234a08e356670ebd8f64509ed8dba3e64a62af7/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream token-savings table not re-measured. Live MCP browser session not run. Distinct from Pioneer113/jev-chrome-mcp and other browser MCP listings. |

## When to use

Use when an agent should **browse without stuffing the DOM into context**. Prefer full Playwright MCP when the host model must see raw page structure.

## How it works

Tools such as `browse_ask` / `browse_goal` / `browse_replay` compress page state for Jev step choice, use a reader model for extraction, and can record/replay/heal recipes or export Playwright tests (per README).

## Get started

```sh
claude mcp add --scope user jev-browser -- npx -y jev-browser-mcp
# Configure TypeSafe + reader keys per upstream README
```

Pin review tip: `5234a08e356670ebd8f64509ed8dba3e64a62af7`.

## Examples and demos

- README Wikipedia/GitHub/MDN/HN token comparison table.
- Recipe replay and Playwright export flow.

## Limits and data handling

Page content is processed on the MCP host; Jev receives compressed state; the reader model may see page text. Credentials stay in the MCP server environment.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 5234a08](https://github.com/bothuany/jev-browser-mcp/tree/5234a08e356670ebd8f64509ed8dba3e64a62af7). AI-assisted README and LICENSE inspection; live browse not run.

Related: [jev-chrome-mcp](jev-chrome-mcp.md), [Jev Ultrafast](jev-ultrafast.md).
