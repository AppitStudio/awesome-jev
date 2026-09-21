# codex-jev-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Node bridge that starts a loopback Responses API proxy for OpenAI Codex CLI, asks TypeSafe Jev which Codex model and reasoning effort fit each fresh turn, then fail-opens to the current Codex settings if Jev is unavailable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tiandee/codex-jev-router) |
| Maintainer | [tiandee](https://github.com/tiandee). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Node.js package (`codex-jev-router` 0.1.0) with `codex-jev` CLI; depends on `@typesafe-ai/sdk`. |
| Requirements | Node.js ≥ 20; OpenAI Codex CLI on `PATH` with auth; `JEV_API_KEY` or `~/.jev-codex.env` for routing (optional—wrapper still starts Codex without it). |
| License | [MIT](https://github.com/tiandee/codex-jev-router/blob/23e1de8f9b28a00ddb27f40fb77c9a003330af57/LICENSE). Codex and TypeSafe usage have separate account/cost requirements. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `npm test` → **19 passed**. Live Codex/TypeSafe routing not run. Distinct from archived [jev-codex-router](jev-codex-router.md) (Python Codex Router generic provider). |

## When to use

Use it when you want Codex CLI turns routed by Jev (model + effort) without replacing Codex itself. Prefer [jev-codex-router](jev-codex-router.md) only if you already run that archived Python Codex Router stack; prefer [jev-router](jev-router.md) for Claude Code + Codex HTTP proxies.

## How it works

[`src/jev-client.mjs`](https://github.com/tiandee/codex-jev-router/blob/23e1de8f9b28a00ddb27f40fb77c9a003330af57/src/jev-client.mjs) calls TypeSafe via `@typesafe-ai/sdk`. [`src/proxy.mjs`](https://github.com/tiandee/codex-jev-router/blob/23e1de8f9b28a00ddb27f40fb77c9a003330af57/src/proxy.mjs) rewrites model/effort on the loopback Responses proxy. [`src/effort-policy.mjs`](https://github.com/tiandee/codex-jev-router/blob/23e1de8f9b28a00ddb27f40fb77c9a003330af57/src/effort-policy.mjs) maps Jev `reasoning_required` scores to low/medium/high/max. Turn context leaves the host when a Jev key is set; without a key the wrapper prints a fallback notice and starts Codex unchanged.

## Get started

```sh
git clone https://github.com/tiandee/codex-jev-router.git
cd codex-jev-router
git checkout 23e1de8f9b28a00ddb27f40fb77c9a003330af57
npm install
npm test
npm link   # provides codex-jev
printf '%s\n' 'JEV_API_KEY=your_typesafe_api_key' > ~/.jev-codex.env
chmod 600 ~/.jev-codex.env
codex-jev
```

Live routing bills TypeSafe; Codex usage bills OpenAI.

## Examples and demos

- Upstream CI badge and `node --test` suite.
- This listing: `npm test` → **19 passed** (CLI naming, proxy rewrite, fail-open, effort policy). No live Codex or TypeSafe call.

## Limits and data handling

Routing prompts/context go to TypeSafe when configured. Automatic effort can be disabled with `JEV_CODEX_AUTO_EFFORT=0`. Not a Codex replacement. Cost/latency claims were not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 23e1de8](https://github.com/tiandee/codex-jev-router/tree/23e1de8f9b28a00ddb27f40fb77c9a003330af57): MIT; AI-assisted source review of README, LICENSE, `src/`, and offline tests. No live TypeSafe/Codex session.

Related: [jev-codex-router](jev-codex-router.md), [jev-router](jev-router.md), [pi-jev-router](pi-jev-router.md).
