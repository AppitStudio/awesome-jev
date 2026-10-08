# jev-netlify-mcp

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Two parts for using TypeSafe Jev from Claude Code, Codex CLI, Claude Desktop or any MCP client: a key-locked Netlify function that exposes `POST /v1/systemone` and `GET /v1/models` through Netlify AI Gateway (which injects the gateway credentials, so no TypeSafe key is needed), and an MCP server with `jev_evaluate` / `jev_models` tools plus question-writing instructions; it also works directly against TypeSafe with your own key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NighCross/jev-netlify-mcp) |
| Maintainer | [NighCross](https://github.com/NighCross). Independently curated. |
| Format | Netlify function (`proxy/`) and Python MCP server (`jev-netlify-mcp`) |
| Requirements | A Netlify account with AI Gateway (credit-based plan) and Python for the MCP server; or a TypeSafe API key to skip the proxy. |
| License | [MIT](https://github.com/NighCross/jev-netlify-mcp/blob/545a8928df195cc28d5f16b881a668e5ff80f4e9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give an MCP client Jev without managing a TypeSafe balance, using Netlify AI Gateway credits.
- Lock a personal endpoint so requests without your key never reach the model.
- Mismatch: Netlify credit limits and terms apply; usage counts against your Netlify plan.

## How it works

[`proxy/netlify/functions/jev.mjs`](https://github.com/NighCross/jev-netlify-mcp/blob/545a8928df195cc28d5f16b881a668e5ff80f4e9/proxy/netlify/functions/jev.mjs) checks a SHA-256 of your key and forwards to the gateway's TypeSafe route; [`src/jev_netlify_mcp/server.py`](https://github.com/NighCross/jev-netlify-mcp/blob/545a8928df195cc28d5f16b881a668e5ff80f4e9/src/jev_netlify_mcp/server.py) exposes the tools and guidance (atomic questions, the three types, translate non-English input).

## Get started

Follow README *Setup* to deploy the proxy, then connect your agent:

```sh
git clone https://github.com/NighCross/jev-netlify-mcp.git && cd jev-netlify-mcp
# README Setup: scripts/setup.py builds proxy/dist with your key hash → deploy to Netlify
# README Connect your agent: register the MCP server with Claude Code / Codex / Desktop
```

Calls consume Netlify AI Gateway credits (or your TypeSafe balance when used directly).

## Examples and demos

- README *Tools* and *Security notes*; Turkish README available.

## Limits and data handling

Questions and state pass through Netlify to TypeSafe. Independent project; not affiliated with Netlify or TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 545a8928df19](https://github.com/NighCross/jev-netlify-mcp/tree/545a8928df195cc28d5f16b881a668e5ff80f4e9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
