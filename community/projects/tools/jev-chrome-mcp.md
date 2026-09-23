# jev-chrome-mcp

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP adapter that runs the jev-browser-use click loop inside Google Chrome for Cursor/Codex (and any local-process MCP client).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Pioneer113/jev-chrome-mcp) |
| Maintainer | [Pioneer113](https://github.com/Pioneer113). Independently curated. Not an endorsement. Not an official part of jev-browser-use. |
| Format | Node.js MCP server (`jev-chrome-mcp`). |
| Requirements | Node; installed [jev-browser-use](https://github.com/wy-coliney/jev-browser-use) `bridge.mjs`; Google Chrome; MCP client config. |
| License | [MIT](https://github.com/Pioneer113/jev-chrome-mcp/blob/b12f9178855b1892402aca10e4c98f0e1d8d351b/LICENSE). Upstream skill is MIT; provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live Chrome/Jev **not** run. Adapter imports installed skill—does not vendor its code. |

## When to use

Use it when Cursor/Codex should drive Chrome clicks via MCP while Jev chooses the next click through jev-browser-use. Prefer full browser SDKs when you need Playwright APIs beyond this click loop.

## How it works

MCP server starts a local process, loads the installed jev-browser-use bridge, and exposes task/type/check tools; Jev selects clicks inside Chrome.

## Get started

```sh
# Install jev-browser-use + Chrome first (upstream README)
git clone https://github.com/Pioneer113/jev-chrome-mcp.git
cd jev-chrome-mcp
git checkout b12f9178855b1892402aca10e4c98f0e1d8d351b
# .cursor/mcp.json → node /absolute/path/to/jev-chrome-mcp/src/server.mjs
```

## Examples and demos

- README Cursor MCP JSON snippet.
- Russian README (`README.ru.md`).

## Limits and data handling

Page content and task text reach the browser-use/Jev path when live. Requires a separate skill install. Click-loop quality was not measured here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit b12f917](https://github.com/Pioneer113/jev-chrome-mcp/tree/b12f9178855b1892402aca10e4c98f0e1d8d351b) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [Jev Browser Skill](jev-browser-skill.md), [jev-ra](jev-ra.md), [Footwork](footwork.md).
