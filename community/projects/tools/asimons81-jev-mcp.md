# Jev MCP (asimons81)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small community MCP server that exposes three bounded Jev decision tools (yes/no, choose and score) over stdio or authenticated loopback HTTP, with text-only inputs, no search or action execution, and credentials read only from the environment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asimons81/jev-mcp) |
| Maintainer | [asimons81](https://github.com/asimons81). Independently curated. |
| Format | MCP server (Node.js 22+) |
| Requirements | Node.js 22+ and npm; `TYPESAFE_API_KEY` (optional `TYPESAFE_MODEL`, default `jev-latest`). |
| License | [MIT](https://github.com/asimons81/jev-mcp/blob/fc4d4bef26af92d1d5a3b9e05bffb46d90a37eae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions.js`](https://github.com/asimons81/jev-mcp/blob/fc4d4bef26af92d1d5a3b9e05bffb46d90a37eae/src/decisions.js) at the pinned commit. |

## When to use

- Give an MCP client (Codex, ChatGPT developer mode or another host) typed Jev judgments without letting it call arbitrary HTTP.
- Keep criteria and answers small and auditable: labels, probabilities and a confidence.
- Mismatch: live TypeSafe calls and client registration are untested per the README; tests use mocked responses.

## How it works

Each tool builds a System One request from `state`, `instructions` and the criteria and sends it to TypeSafe (`src/decisions.js`); the server returns the probability, chosen label or fractional score. Integration evidence: [`src/decisions.js`](https://github.com/asimons81/jev-mcp/blob/fc4d4bef26af92d1d5a3b9e05bffb46d90a37eae/src/decisions.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/asimons81/jev-mcp.git && cd jev-mcp
npm ci --ignore-scripts
npm test
export TYPESAFE_API_KEY=your-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tool table and status notes in the README: [github.com/asimons81/jev-mcp#readme](https://github.com/asimons81/jev-mcp#readme)

## Limits and data handling

The text you pass is sent to TypeSafe. No hosted endpoint or npm release; `private: true` in package.json. Community project, not affiliated with TypeSafe or OpenAI.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit fc4d4bef26af](https://github.com/asimons81/jev-mcp/tree/fc4d4bef26af92d1d5a3b9e05bffb46d90a37eae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
