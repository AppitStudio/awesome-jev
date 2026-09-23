# opencode-jev-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode Responses API proxy: TypeSafe Jev picks reasoning effort per request, then pins execution to the resolved Astra/Luna/Sol model while preserving historical effort updates for cache lineage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/robertn702/opencode-jev-router) |
| Maintainer | [robertn702](https://github.com/robertn702). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node CLI / proxy **`@robertn702/opencode-jev-router` 0.1.0** (npm). |
| Requirements | Node.js **24.x**; CLIProxyAPI with Codex OAuth **or** an OpenAI API key for the selected GPT-6 model; `JEV_API_KEY` (TypeSafe or Vercel AI Gateway with `JEV_BASE_URL=https://ai-gateway.vercel.sh/typesafe`). |
| License | [MIT](https://github.com/robertn702/opencode-jev-router/blob/869486c74e58d2535763b2e156a53d8853611edd/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `src/jev.ts`, `src/router.ts`). Live OpenCode/Jev proxy runs were **not** executed on the review host. Distinct from [opencode-jev-guard](opencode-jev-guard.md). |

## When to use

Use it when OpenCode should adapt reasoning effort on a fixed GPT-6 Responses upstream without abandoning cache lineage. Prefer [opencode-jev-guard](opencode-jev-guard.md) for shell preflight rather than effort routing; prefer [Astra-Ares](astra-ares.md) for Codex CLI effort adaptation.

## How it works

For each `POST /v1/responses`, the proxy asks Jev how much reasoning the next step needs ([`src/jev.ts`](https://github.com/robertn702/opencode-jev-router/blob/869486c74e58d2535763b2e156a53d8853611edd/src/jev.ts)), may emit a `configuration_update` for effort, and forwards to the Responses upstream ([`src/router.ts`](https://github.com/robertn702/opencode-jev-router/blob/869486c74e58d2535763b2e156a53d8853611edd/src/router.ts)). Request-level `reasoning.effort` stays at a stable base so reported effort is the base setting.

## Get started

```sh
npm install -g @robertn702/opencode-jev-router
# configure upstream + JEV_API_KEY per README
opencode-jev-router --help
opencode-jev-router
```

Pin for review: [commit 869486c](https://github.com/robertn702/opencode-jev-router/tree/869486c74e58d2535763b2e156a53d8853611edd). Live traffic sends bounded classification context to Jev and model tokens to the upstream; both may incur charges.

## Examples and demos

- `examples/opencode.jsonc`.
- Upstream CI and smoke scripts (not re-run here). README notes end-to-end task benchmarks vs fixed effort are not yet established.

## Limits and data handling

Node 24-only engines range. Adaptive effort’s effect on task success is not proven by a published task benchmark in this review. No live proxy spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 869486c](https://github.com/robertn702/opencode-jev-router/tree/869486c74e58d2535763b2e156a53d8853611edd) (**0.1.0**, MIT). AI-assisted source review. No live OpenCode or TypeSafe spend.

Related: [opencode-jev-guard](opencode-jev-guard.md), [Astra-Ares](astra-ares.md), [jev-effort-router](jev-effort-router.md).
