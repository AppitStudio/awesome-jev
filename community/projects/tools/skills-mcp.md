# skills-mcp (MCP server that keeps agent skills out of context and suggests the right one with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bun/TypeScript MCP server that stores a skill catalog outside the model context: the agent calls `find`, gets one suggestion, then `load`s that skill. Classification uses `@ai-sdk/typesafe-ai` against TypeSafe; measured fixed tool overhead targets ~300 tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/heliowap/skills-mcp) |
| Maintainer | [heliowap](https://github.com/heliowap). Independently curated. |
| Format | TypeScript MCP server for Bun (MIT) |
| Requirements | Bun, skill sources (GitHub/local/CLI), and a TypeSafe key for the classifier path. |
| License | [MIT](https://github.com/heliowap/skills-mcp/blob/ea61589a0acb25b5b683414326ebb54d2a0f783d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/ai-sdk.ts`](https://github.com/heliowap/skills-mcp/blob/ea61589a0acb25b5b683414326ebb54d2a0f783d/src/decision/ai-sdk.ts) at the pinned commit. |

## When to use

- Stop paying native skill-list tokens on every step.
- Serve one suggested skill on demand over MCP.
- Mismatch: classifier accuracy is measured on one labeled set; thresholds were fitted on the same set.

## How it works

`src/decision/ai-sdk.ts` creates a TypeSafe AI client against `https://api.typesafe.ai/v1` to score which skill fits a task. Integration evidence: [`src/decision/ai-sdk.ts`](https://github.com/heliowap/skills-mcp/blob/ea61589a0acb25b5b683414326ebb54d2a0f783d/src/decision/ai-sdk.ts).

## Get started

Install with Bun, point at skill sources, and connect any MCP harness (OpenCode scripts included).

```sh
git clone https://github.com/heliowap/skills-mcp.git && cd skills-mcp
bun install
export TYPESAFE_API_KEY=...
# see README Connect a harness
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/heliowap/skills-mcp/blob/ea61589a0acb25b5b683414326ebb54d2a0f783d/README.md](https://github.com/heliowap/skills-mcp/blob/ea61589a0acb25b5b683414326ebb54d2a0f783d/README.md)

## Limits and data handling

Task text used for `find` is sent to TypeSafe on your key. Skills themselves are never executed by the server.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit ea61589a0acb](https://github.com/heliowap/skills-mcp/tree/ea61589a0acb25b5b683414326ebb54d2a0f783d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
