# decision-server

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Cloudflare Worker that answers Jev-format decision calls on free Workers AI Clef models first and falls back to Jev, with REST, a remote MCP server, budgets and a stats dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PrashamTrivedi/decision-server) |
| Maintainer | [PrashamTrivedi](https://github.com/PrashamTrivedi). Independently curated. |
| Format | Self-hosted Cloudflare Worker (TypeScript) |
| Requirements | Cloudflare account, Bun, TypeSafe API key for fallback. |
| License | [MIT](https://github.com/PrashamTrivedi/decision-server/blob/14a3651e94211e50dbbeac24415405cf783a5ac9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/jev.ts`](https://github.com/PrashamTrivedi/decision-server/blob/14a3651e94211e50dbbeac24415405cf783a5ac9/src/providers/jev.ts) at the pinned commit. |

## When to use

- Serve one Jev-compatible endpoint that prefers free Clef models and escalates important questions to Jev.
- Expose decisions to agents through a remote MCP server with call logs.
- Mismatch: requires your own Cloudflare deployment behind Access.

## How it works

A router chooses a tier per request (free Clef first, Jev on budget exhaustion, failure or importance) and records `servedBy` and `routeReason`; the Jev provider passes the request to TypeSafe. Integration evidence: [`src/providers/jev.ts`](https://github.com/PrashamTrivedi/decision-server/blob/14a3651e94211e50dbbeac24415405cf783a5ac9/src/providers/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp .dev.vars.example .dev.vars
bun run test:run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Routes: `/v1/systemone`, `/v1/budget`, `/v1/stats`, `/mcp` (documented upstream).

## Limits and data handling

Call logs with full payloads are stored in your D1 database; fallback calls go to TypeSafe and are billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 14a3651e9421](https://github.com/PrashamTrivedi/decision-server/tree/14a3651e94211e50dbbeac24415405cf783a5ac9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
