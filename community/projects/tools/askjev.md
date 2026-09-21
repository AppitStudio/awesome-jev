# askjev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial MCP server for TypeSafe Jev: agents ask plain questions about material they already have; Jev returns calibrated Noul/Choice/Score probabilities (hosted Cloudflare Worker or local stdio).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pZacca/askjev) |
| Maintainer | [pZacca](https://github.com/pZacca). Independently curated; this page is not an upstream submission or endorsement. Not affiliated with TypeSafe. |
| Format | TypeScript MCP server published as npm `askjev` **0.2.0**; local stdio via `npx -y askjev` or hosted `https://jev.zacca.dev/mcp`. |
| Requirements | Node.js **≥ 22**; `TYPESAFE_API_KEY` (local) or `x-api-key` / bearer on the hosted endpoint. |
| License | [MIT](https://github.com/pZacca/askjev/blob/77b6d79ca8a4bd52386564309f1b45ac81310f9c/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline vitest passed; live MCP clients and live TypeSafe calls were **not** run. Distinct from [ask-jev-skill](ask-jev-skill.md) (Hermes skill) and [jev-mcp](jev-mcp.md) (multi-tool MCP pack). |

## When to use

Use it when Claude Code, Cursor, Codex, or Claude Desktop should get a fast second opinion from Jev over context the agent already holds, without spinning a generative sub-agent. Prefer [ask-jev-skill](ask-jev-skill.md) for a Hermes-only skill path, or [jev-mcp](jev-mcp.md) for a broader set of purpose-built judgment tools.

## How it works

[`src/jev.ts`](https://github.com/pZacca/askjev/blob/77b6d79ca8a4bd52386564309f1b45ac81310f9c/src/jev.ts) and the router assemble typed questions and forward them to TypeSafe System One. The hosted Worker builds a client from the key you send and keeps nothing durable. Application/agent code owns acting on the returned probabilities. Question text and state leave the host when Jev is called.

## Get started

```sh
# Local stdio (Claude Code / Cursor / Codex)
export TYPESAFE_API_KEY=...
npx -y askjev
```

Pinned offline tests:

```sh
git clone https://github.com/pZacca/askjev.git
cd askjev
git checkout 77b6d79ca8a4bd52386564309f1b45ac81310f9c
npm ci --ignore-scripts
npm test
```

Live MCP sessions call TypeSafe (or the hosted forwarder) and can incur charges.

## Examples and demos

- Upstream README demo GIF and client install snippets (Claude Code, Desktop, Cursor, Codex).
- Offline vitest on the review host: **35 passed** across 5 files. No live TypeSafe or hosted MCP session.

## Limits and data handling

Questions and state go to TypeSafe (directly or via the Worker). Keys should stay in env/headers—never in chat. Upstream latency/cost anecdotes are author claims, not catalog benchmarks. Hosted mode still requires you to supply a TypeSafe key per request.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 77b6d79](https://github.com/pZacca/askjev/tree/77b6d79ca8a4bd52386564309f1b45ac81310f9c): **0.2.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `src/router.ts`, and tests. **`npm test` (vitest): 35 passed**. No live TypeSafe or MCP client session.

Related: [ask-jev-skill](ask-jev-skill.md), [jev-mcp](jev-mcp.md), [Jev Review](jev-review.md).
