# Jev Atlas (independent, evidence-first Jev field guide with build blueprints, a claim tracker and a read-only MCP server)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent research site about Jev: 31 build blueprints grouped by the Jev property they rely on, a fit checker that finds Choice, Score and yes/no decision points in a described workflow, a claims page that keeps vendor claims labelled as vendor claims, and located community builds. Coding agents can query it through a read-only MCP server or `llms.txt`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gorock007/jev-atlas) |
| Maintainer | [gorock007](https://github.com/gorock007). Independently curated. |
| Format | Next.js site, hosted at jev.gorock.sh, with a read-only MCP endpoint (MIT) |
| Requirements | None to browse or connect the hosted MCP. Locally: Node.js and npm; the fit checker uses an LLM via Vercel AI Gateway when `AI_GATEWAY_API_KEY` is set and falls back to rules otherwise. |
| License | [MIT](https://github.com/gorock007/jev-atlas/blob/d7e0b44517ef7448466b88b02182ece7a9e265cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/app/mcp/route.ts`](https://github.com/gorock007/jev-atlas/blob/d7e0b44517ef7448466b88b02182ece7a9e265cd/src/app/mcp/route.ts) at the pinned commit. |

## When to use

- Give a coding agent sourced context on what Jev can and cannot do before you build.
- Mismatch: official documentation; it is independent research, not affiliated with TypeSafe.

## How it works

`src/app/mcp/route.ts` serves five read-only tools (`search_jev_knowledge`, `get_jev_context_pack`, `assess_jev_fit`, `get_build_blueprint`, `trace_jev_claim`) over the bundled research. It does not call Jev or accept a TypeSafe key; it is a knowledge resource about Jev, not a Jev integration. Integration evidence: [`src/app/mcp/route.ts`](https://github.com/gorock007/jev-atlas/blob/d7e0b44517ef7448466b88b02182ece7a9e265cd/src/app/mcp/route.ts).

## Get started

Browse jev.gorock.sh, point your coding agent at the MCP URL, or run it locally.

```sh
# MCP client config:
{"mcpServers":{"jev-atlas":{"url":"https://jev.gorock.sh/mcp"}}}
# local:
git clone https://github.com/gorock007/jev-atlas && cd jev-atlas && npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [jev.gorock.sh](https://jev.gorock.sh)
- README: [github.com/gorock007/jev-atlas/blob/d7e0b44517ef7448466b88b02182ece7a9e265cd/README.md](https://github.com/gorock007/jev-atlas/blob/d7e0b44517ef7448466b88b02182ece7a9e265cd/README.md)

## Limits and data handling

Hosted MCP queries go to the maintainer's site. Refreshing the research costs X API credits and is capped by spend limits. Not affiliated with or endorsed by TypeSafe.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit d7e0b44517ef](https://github.com/gorock007/jev-atlas/tree/d7e0b44517ef7448466b88b02182ece7a9e265cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
