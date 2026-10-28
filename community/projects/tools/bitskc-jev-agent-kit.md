# jev-agent-kit by bitskc (self-hosted Jev MCP toolbox and skills for oh-my-pi and Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One Cloudflare Worker exposing 15 Jev-backed MCP tools, plus 7 agent skills and an optional guard hook, for the judgment calls coding agents make all day: is this shell command safe, is this sub-agent the right size, did the agent really verify before saying done. Builds on jkudish/jev-mcp and jonathanavis96/jev-kit; deterministic rules handle what a model shouldn't guess.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bitskc/jev-agent-kit) |
| Maintainer | [bitskc](https://github.com/bitskc). Independently curated. |
| Format | Cloudflare Worker MCP server (Node.js) with agent skills |
| Requirements | A Cloudflare account and a TypeSafe (or Vercel AI Gateway) key. |
| License | [MIT](https://github.com/bitskc/jev-agent-kit/blob/c7181c04970e4f80cdfa308f3ae935b824caa9c3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/src/kit/jev.mjs`](https://github.com/bitskc/jev-agent-kit/blob/c7181c04970e4f80cdfa308f3ae935b824caa9c3/server/src/kit/jev.mjs) at the pinned commit. |

## When to use

- Give omp or Claude Code fast safety and sizing checks over MCP.
- Mismatch: distinct from the other kits named jev-agent-kit in this catalog.

## How it works

`server/src/kit/jev.mjs` resolves the upstream (TypeSafe or Vercel AI Gateway's TypeSafe-compatible API) and sends `{model, state, questions}` for each `kit_*` tool. Integration evidence: [`server/src/kit/jev.mjs`](https://github.com/bitskc/jev-agent-kit/blob/c7181c04970e4f80cdfa308f3ae935b824caa9c3/server/src/kit/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bitskc/jev-agent-kit && ./jev-agent-kit/install.sh --both
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bitskc/jev-agent-kit#readme](https://github.com/bitskc/jev-agent-kit#readme)

## Limits and data handling

Commands, tasks and evidence checked by the tools go through your Worker to TypeSafe or the gateway. Logs stay in your Cloudflare account.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit c7181c04970e](https://github.com/bitskc/jev-agent-kit/tree/c7181c04970e4f80cdfa308f3ae935b824caa9c3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
