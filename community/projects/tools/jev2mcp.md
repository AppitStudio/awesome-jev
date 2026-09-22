# jev2mcp

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Local companion server plus Chrome extension that uses TypeSafe Jev to choose which configured ChatGPT MCP servers, plugins, or tools to mention for the current prompt—without generating tool names or rewriting the prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/n8mirai/jev2mcp) |
| Maintainer | [n8mirai](https://github.com/n8mirai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js local HTTP companion **`jev2mcp` 0.2.1** + unpacked Chrome extension under `extension/`. |
| Requirements | Node.js ≥ 22.13; `TYPESAFE_API_KEY` (or Keychain helper on macOS per README). No production npm runtime dependencies. ChatGPT signed-in browser for the documented path. |
| License | [MIT](https://github.com/n8mirai/jev2mcp/blob/42ca77eddad9acd79d3c4d1f79738678ea7555d1/LICENSE). TypeSafe usage billed separately from ChatGPT. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `npm test` after `npm ci`: **21 passed**. Experimental; ChatGPT Work/desktop paths partially unverified upstream. No live TypeSafe or ChatGPT session here. |

## When to use

Use it when ChatGPT should attach the right MCP/plugin mention from a **you-configured** catalog based on prompt context. Prefer [jev-mcp](jev-mcp.md) / [typesafe-mcp](typesafe-mcp.md) when you want MCP tools that *are* Jev judgments, not a ChatGPT picker router.

## How it works

The companion exposes a local typed schema; Jev selects among enabled tools you listed. The extension pairs via a copied package and injects the chosen native mention. It does not discover account-installed tools by itself or connect directly to MCP servers.

## Get started

```sh
git clone https://github.com/n8mirai/jev2mcp.git
cd jev2mcp
git checkout 42ca77eddad9acd79d3c4d1f79738678ea7555d1
npm ci
npm test
# Live (charges TypeSafe): export TYPESAFE_API_KEY; npm start  # http://127.0.0.1:4328
# Then load extension/ unpacked and pair per README.
```

## Examples and demos

- README ChatGPT Chat path (author-reported Google Drive mention demo; not re-run here).
- `test/*.test.mjs` — offline Node test suite.

## Limits and data handling

Experimental. Prompt text and tool catalog descriptions may be sent to TypeSafe. Failures should keep credentials out of responses (covered in offline tests). Desktop/Work support is limited per upstream. This listing did not run live ChatGPT or TypeSafe.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 42ca77e](https://github.com/n8mirai/jev2mcp/tree/42ca77eddad9acd79d3c4d1f79738678ea7555d1) (`0.2.1`, MIT). AI-assisted review of README, LICENSE, and offline tests. **`npm test` 21 passed**. No live TypeSafe/ChatGPT.

Related: [jev-mcp](jev-mcp.md), [typesafe-mcp](typesafe-mcp.md), [Prompt Rejector](prompt-rejector.md).
