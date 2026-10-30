# systemone-mcp-server (MCP server exposing System One decision tools over files and gated commands to Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server with six tools built from levels 8-10 of ten-levels-of-jev: ask one typed question over a short state, up to 20 files and one gated read-only command, ask the same questions across many files in parallel, pick which file to open first, and single-file yes/no, choice and score checks. Commands pass a bash safety gate inside the tool. Calls go through a local cc-router relay by default, or directly to OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/paulrobello/systemone-mcp-server) |
| Maintainer | [paulrobello](https://github.com/paulrobello). Independently curated. |
| Format | MCP server (TypeScript, Bun) |
| Requirements | Bun; Claude Code or another MCP client; a local cc-router relay or an OpenRouter key (an offline mock backend is included for tests). |
| License | [MIT](https://github.com/paulrobello/systemone-mcp-server/blob/66b8c02629b2a13bf33b43d70ba74656f768a4e6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone/core/client.ts`](https://github.com/paulrobello/systemone-mcp-server/blob/66b8c02629b2a13bf33b43d70ba74656f768a4e6/src/systemone/core/client.ts) at the pinned commit. |

## When to use

- Let Claude Code triage many files or command output with typed answers instead of reading everything itself.
- Mismatch: install path in the README is the author's local checkout; adjust paths yourself.

## How it works

`src/systemone.ts` resolves the backend (relay, OpenRouter or mock) and `core/client.ts` posts `/v1/systemone` requests with `~typesafe/jev-latest` as the OpenRouter model. Integration evidence: [`src/systemone/core/client.ts`](https://github.com/paulrobello/systemone-mcp-server/blob/66b8c02629b2a13bf33b43d70ba74656f768a4e6/src/systemone/core/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
make test
claude mcp add -s user systemone-mcp-server -- bun /path/to/systemone-mcp-server/src/index.ts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Upstream ten-levels-of-jev: [github.com/disler/ten-levels-of-jev](https://github.com/disler/ten-levels-of-jev)

## Limits and data handling

File contents and command output you pass are sent to the relay or OpenRouter. Vendors code from ten-levels-of-jev. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 66b8c02629b2](https://github.com/paulrobello/systemone-mcp-server/tree/66b8c02629b2a13bf33b43d70ba74656f768a4e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
