# Light Decision MCP by Light Cheng (multi-backend System One MCP server and Magpie plugin, with Jev as one provider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A zero-dependency MCP server and Magpie plugin that turns System One decision models into agent tools (`noul` yes/no, `choice`, `score`), routing to TypeSafe Jev, Google Gemini Decision, Perplexity Decisions, OpenAI or local OpenDecider/Ollama/MLX, either through a Magpie gateway (no keys in the plugin) or standalone over stdio.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/light-cheng/Light-Decision-MCP) |
| Maintainer | [light-cheng](https://github.com/light-cheng). Independently curated. |
| Format | Node.js MCP server + Magpie plugin |
| Requirements | Node.js and an MCP client (Claude Desktop/Code, Cursor and others) or Magpie; a TypeSafe key for the Jev backend (other providers or a local model otherwise). |
| License | [MIT](https://github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config/load.mjs`](https://github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/src/config/load.mjs) at the pinned commit. |

## When to use

- Give an agent one set of decision tools that can switch between Jev, other hosted decision models and local ones.
- Mismatch: a Jev-only integration; Jev is one of several backends and the default differs by setup.

## How it works

`src/config/load.mjs` registers a `systemone` backend for TypeSafe at `TYPESAFE_BASE_URL` (default `https://api.typesafe.ai`) when `TYPESAFE_API_KEY` is set, alongside the other providers; the tools expose the three question types and return typed answers. Integration evidence: [`src/config/load.mjs`](https://github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/src/config/load.mjs).

## Get started

Install as a Magpie plugin, or run standalone over stdio from your MCP client config.

```sh
git clone https://github.com/light-cheng/Light-Decision-MCP
# Magpie: magpie plugin add /absolute/path/to/Light-Decision-MCP
# standalone MCP: command "node", args ["/absolute/path/to/Light-Decision-MCP/bin/stdio.mjs"],
#   env { "TYPESAFE_API_KEY": "..." }
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/README.md](https://github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/README.md)
- Chinese README: [github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/README.zh-CN.md](https://github.com/light-cheng/Light-Decision-MCP/blob/84ae697175dc8f079cb530bbf66591af19c494d8/README.zh-CN.md)

## Limits and data handling

Prompts and context the agent passes go to whichever provider is selected, with that provider's costs. Early project.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 84ae697175dc](https://github.com/light-cheng/Light-Decision-MCP/tree/84ae697175dc8f079cb530bbf66591af19c494d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
