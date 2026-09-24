# firefox-jev-mcp

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server that lets Claude drive Firefox: Claude plans; TypeSafe Jev chooses which page element to act on; Claude resumes when Jev is unsure or the action is sensitive.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kitoutou999/firefox-jev-mcp) |
| Maintainer | [kitoutou999](https://github.com/kitoutou999). Independently curated. |
| Format | TypeScript MCP server + Firefox WebExtension (WebSocket bridge). |
| Requirements | Firefox; Node/TypeScript toolchain; Claude Code; TypeSafe Jev API access. |
| License | [MIT](https://github.com/kitoutou999/firefox-jev-mcp/blob/49a31d1f3dc0f9b92495351eca174e04ba6ca110/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream Wikipedia race / MCP latency tables not re-measured. Live Firefox MCP session not run. French-primary README. |

## When to use

Use when Claude should **pilot Firefox** with Jev picking routine clicks. Prefer Chrome-oriented MCP listings when your stack is Chromium-only.

## How it works

`browse_goal` loops snapshot → Jev Choice/Noul → extension action until the goal is met, Jev hesitates, or a sensitive action appears; then control returns to Claude with top candidates (per README).

## Get started

```sh
git clone https://github.com/kitoutou999/firefox-jev-mcp.git
cd firefox-jev-mcp
git checkout 49a31d1f3dc0f9b92495351eca174e04ba6ca110
# Follow upstream README: build server/, load extension/, configure Claude MCP + TypeSafe key
```

## Examples and demos

- README Wikipedia Titanic→Tour Eiffel race charts under `bench/`.
- Base-action latency table vs other browser MCP servers (upstream-reported).

## Limits and data handling

Page element text reaches Jev; the extension talks only to the local MCP server over WebSocket. Sensitive actions (pay/delete/send) escalate to Claude.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 49a31d1](https://github.com/kitoutou999/firefox-jev-mcp/tree/49a31d1f3dc0f9b92495351eca174e04ba6ca110). AI-assisted README and LICENSE inspection; live race not re-run.

Related: [bothuany jev-browser-mcp](bothuany-jev-browser-mcp.md), [legostin jev-mcp](legostin-jev-mcp.md).
