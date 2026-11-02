# dsh-jev-mcp by NingYuanLee (DeepSeek Harness plugin that runs jkudish/jev-mcp and registers its Jev tools)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness plugin that reads a key from the DSH credential store, starts the pinned `@jkudish/jev-mcp` server on stdio and registers its judgment tools (verify, screen, find, rerank and more) plus a `jev` skill, so the agent can call Jev without a separate MCP config. Providers: TypeSafe, OpenRouter, Cloudflare, Vercel AI Gateway or a compatible endpoint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NingYuanLee/dsh-jev-mcp) |
| Maintainer | [NingYuanLee](https://github.com/NingYuanLee). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript) |
| Requirements | DeepSeek Harness; a TypeSafe or other supported provider key saved in the DSH credential store. |
| License | [MIT](https://github.com/NingYuanLee/dsh-jev-mcp/blob/456fc956805bf0bc200e52030368091805c6d78c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/client.js`](https://github.com/NingYuanLee/dsh-jev-mcp/blob/456fc956805bf0bc200e52030368091805c6d78c/lib/client.js) at the pinned commit. |

## When to use

- Give a DeepSeek Harness agent Jev tools with one plugin install.
- Mismatch: thin launcher; tool behaviour comes from jkudish/jev-mcp.

## How it works

`src/launch.js` resolves the pinned `@jkudish/jev-mcp` binary and spawns it with the chosen provider credential; `lib/client.js` is the settings panel that maps providers to key names. Integration evidence: [`lib/client.js`](https://github.com/NingYuanLee/dsh-jev-mcp/blob/456fc956805bf0bc200e52030368091805c6d78c/lib/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile web add github:NingYuanLee/dsh-jev-mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Upstream MCP server: [github.com/jkudish/jev-mcp](https://github.com/jkudish/jev-mcp)

## Limits and data handling

Tool inputs are sent to the selected Jev provider. Separate from the listed bojansandhaus dsh-jev-mcp. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 456fc956805b](https://github.com/NingYuanLee/dsh-jev-mcp/tree/456fc956805bf0bc200e52030368091805c6d78c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
