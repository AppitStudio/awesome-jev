# Jevs

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Bun/TypeScript MCP server (Codex plugin) that exposes TypeSafe Jev classify/score/check/batch tools over stdio via the official JavaScript SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nshcr/jevs) |
| Maintainer | [nshcr](https://github.com/nshcr). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript · Bun MCP server / Codex plugin **0.1.0**. |
| Requirements | Bun **≥ 1.4.2** on PATH for Codex plugin install. Offline `bun test` needs no key. Live tools need `TYPESAFE_API_KEY` (optional `TYPESAFE_BASE_URL` / model). |
| License | [MIT](https://github.com/nshcr/jevs/blob/a25321054bcc5cda296516f57dfc9cfe927b3170/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `bun test`: **42 passed**. Live TypeSafe / Codex plugin sessions not run. Distinct from [TypeSafe MCP](typesafe-mcp.md), [jev-mcp](jev-mcp.md), and [askjev](askjev.md). |

## When to use

Use it when you want Codex (or another MCP host) to call Jev through a small stdio tool surface with concurrency/queue controls and provider adapters documented upstream. Prefer [TypeSafe MCP](typesafe-mcp.md) for a Go general-purpose evaluator, or [jev-mcp](jev-mcp.md) for a larger purpose-built tool pack.

## How it works

[`src/server.ts`](https://github.com/nshcr/jevs/blob/a25321054bcc5cda296516f57dfc9cfe927b3170/src/server.ts) builds an MCP server around `@typesafe-ai/sdk` `TypeSafeClient`. Tools map to Choice/Score/Noul (and batch/structure helpers); `jev_guide` / `jev_list_models` avoid evaluation. [`src/provider.ts`](https://github.com/nshcr/jevs/blob/a25321054bcc5cda296516f57dfc9cfe927b3170/src/provider.ts) documents TypeSafe, OpenRouter Decisions, and gateway endpoint shaping. Live calls send state/questions to the configured provider.

## Get started

```sh
git clone https://github.com/nshcr/jevs.git
cd jevs
git checkout a25321054bcc5cda296516f57dfc9cfe927b3170
bun install
bun test
# Codex plugin install per upstream README (release branch marketplace); export TYPESAFE_API_KEY
```

## Examples and demos

- Offline **`bun test`**: **42 passed** across contracts, provider adapters, scheduler, batch, and runtime suites (mocked HTTP; no live key).

## Limits and data handling

Queue/concurrency defaults are documented upstream. Provider errors are shaped for MCP clients; do not treat check probabilities as booleans. Live inference incurs provider charges. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit a253210](https://github.com/nshcr/jevs/tree/a25321054bcc5cda296516f57dfc9cfe927b3170): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/server.ts` / `provider.ts` / tests. **`bun test`: 42 passed**. No live TypeSafe.

Related: [TypeSafe MCP](typesafe-mcp.md), [jev-mcp](jev-mcp.md), [askjev](askjev.md), [TypeSafe-as-a-Judge](typesafe-as-a-judge.md).
