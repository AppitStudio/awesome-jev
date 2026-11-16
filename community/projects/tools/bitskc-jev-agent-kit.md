# Honest Jev (by bitskc)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One Cloudflare Worker exposing 16 Jev-backed MCP tools, plus 10 agent skills and an optional guard hook, for the judgment calls coding agents make all day: is this shell command safe, is this sub-agent the right size, did the agent really verify before saying done. Builds on jkudish/jev-mcp and jonathanavis96/jev-kit; deterministic rules handle what a model shouldn't guess.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bitskc/honest-jev) |
| Maintainer | [bitskc](https://github.com/bitskc). Independently curated. |
| Format | Cloudflare Worker MCP server (Node.js) with agent skills |
| Requirements | A Cloudflare account and a TypeSafe (or Vercel AI Gateway) key. |
| License | [MIT](https://github.com/bitskc/honest-jev/blob/953d9d9eb593700bc9c530e0baffe7dc964604fe/LICENSE) |
| Disclosure | Rename update self-submitted by the maintainer (bitskc) with AI assistance; checked by an AI-assisted catalog review. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/src/kit/jev.mjs`](https://github.com/bitskc/honest-jev/blob/953d9d9eb593700bc9c530e0baffe7dc964604fe/server/src/kit/jev.mjs) at the pinned commit. |

## When to use

- Give omp or Claude Code fast safety and sizing checks over MCP.
- Mismatch: distinct from the other kits named jev-agent-kit in this catalog.

## How it works

`server/src/kit/jev.mjs` resolves the upstream (TypeSafe or Vercel AI Gateway's TypeSafe-compatible API) and sends `{model, state, questions}` for each `kit_*` tool. Integration evidence: [`server/src/kit/jev.mjs`](https://github.com/bitskc/honest-jev/blob/953d9d9eb593700bc9c530e0baffe7dc964604fe/server/src/kit/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bitskc/honest-jev && ./honest-jev/install.sh --both
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bitskc/honest-jev#readme](https://github.com/bitskc/honest-jev#readme)

## Limits and data handling

Commands, tasks and evidence checked by the tools go through your Worker to TypeSafe or the gateway. Logs stay in your Cloudflare account.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia; maintainer rename update pinned 2026-11-14) at [commit 953d9d9](https://github.com/bitskc/honest-jev/tree/953d9d9eb593700bc9c530e0baffe7dc964604fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
