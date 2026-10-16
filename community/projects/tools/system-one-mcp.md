# system-one-mcp

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small MCP server that gives agents two tools, evaluate typed Choice/Score/Noul questions and list models, against any System One backend: TypeSafe Jev, local Ollama System One models, Kev or Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/es11225599/system-one-mcp) |
| Maintainer | [es11225599](https://github.com/es11225599). Independently curated. |
| Format | Node.js MCP server (stdio, TypeScript) |
| Requirements | Node.js; a System One backend (TypeSafe key for Jev, or a local Ollama model). |
| License | [MIT](https://github.com/es11225599/system-one-mcp/blob/ec34c51ce1d6188d6e8ca6539cf66e52e78a2e5a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.ts`](https://github.com/es11225599/system-one-mcp/blob/ec34c51ce1d6188d6e8ca6539cf66e52e78a2e5a/src/client.ts) at the pinned commit. |

## When to use

- Let Claude Code or another MCP client ask Jev a typed question mid-task.
- Switch the same agent tool between TypeSafe Jev and a local System One model by changing two env vars.
- Mismatch: thin passthrough; defaults to a local Ollama backend, so point `SYSTEMONE_BASE_URL` at TypeSafe for Jev.

## How it works

The MCP tools validate arguments with Zod and forward them to `{SYSTEMONE_BASE_URL}/v1/systemone` with an optional Bearer key; `model` is free-form, and HTTP errors are surfaced with status and retry-after. Integration evidence: [`src/client.ts`](https://github.com/es11225599/system-one-mcp/blob/ec34c51ce1d6188d6e8ca6539cf66e52e78a2e5a/src/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/es11225599/system-one-mcp.git && cd system-one-mcp
npm install && npm run build
SYSTEMONE_BASE_URL=https://api.typesafe.ai SYSTEMONE_API_KEY=... SYSTEMONE_MODEL=jev node dist/index.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Claude Code MCP config example in the README.
- Copy-paste env: `.env.example`.

## Limits and data handling

Tool arguments go to the backend you configure; with TypeSafe, on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit ec34c51ce1d6](https://github.com/es11225599/system-one-mcp/tree/ec34c51ce1d6188d6e8ca6539cf66e52e78a2e5a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
