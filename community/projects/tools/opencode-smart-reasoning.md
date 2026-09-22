# opencode-smart-reasoning

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin: TypeSafe Jev (via OpenCode Zen SystemOne) picks per-request **reasoning effort** before the model call—cheap prompts stay cheap; high-stakes work can bump effort—fail-open without a key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d0nj/opencode-smart-reasoning) |
| Maintainer | [d0nj](https://github.com/d0nj). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with TypeSafe or OpenCode. |
| Format | TypeScript OpenCode plugin **`opencode-smart-reasoning` 0.2.0** (`@opencode/plugin`); installs via `opencode.jsonc` plugins list. |
| Requirements | OpenCode with Zen/`@opencode/plugin`. Auth: `OPENCODE_API_KEY` or `JEV_API_KEY`. Default endpoint `https://opencode.ai/zen/v1/systemone`; model default `jev-1.13-free` (paid `jev-1.13`). |
| License | [MIT](https://github.com/d0nj/opencode-smart-reasoning/blob/6fb18a17ebb0dfea574265435f722f42a1813435/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `bun test` **36 passed** after `npm install --legacy-peer-deps`. Live OpenCode/Zen sessions not run. Distinct from [fast-jev-opencode](fast-jev-opencode.md) (prunes tool context) and [pi-jev-effort](pi-jev-effort.md) (Pi thinking levels). |

## When to use

Use it when OpenCode agents should **route reasoning effort per prompt** with typed Jev Choice/Noul rather than a fixed variant. Prefer [fast-jev-opencode](fast-jev-opencode.md) to prune stale tool results; prefer [Agent Router](agent-router.md) / [codex-jev-router](codex-jev-router.md) when choosing models across harnesses.

## How it works

[`src/jev.ts`](https://github.com/d0nj/opencode-smart-reasoning/blob/6fb18a17ebb0dfea574265435f722f42a1813435/src/jev.ts) calls SystemOne (`reasoning_effort` Choice + `high_stakes` Noul). [`src/index.ts`](https://github.com/d0nj/opencode-smart-reasoning/blob/6fb18a17ebb0dfea574265435f722f42a1813435/src/index.ts) hooks OpenCode `prompt`/`context`: one decision per new user prompt (retry-safe stash), then applies a model variant via `event.options`. Fail-open on missing key, timeout, or errors. Prompt text leaves the host when live.

## Get started

```sh
git clone https://github.com/d0nj/opencode-smart-reasoning.git
cd opencode-smart-reasoning
git checkout 6fb18a17ebb0dfea574265435f722f42a1813435
npm install --legacy-peer-deps
bun test
# Wire into opencode.jsonc plugins (see README / opencode.jsonc.example)
```

Live routing uses your Zen/OpenCode key and may incur charges. This listing did not run a live OpenCode session.

## Examples and demos

- Offline `bun test`: **36 passed** on the review host.
- README documents effort bump/clamp rules and endpoint override order.

## Limits and data handling

Fail-open leaves model defaults when Jev is unavailable. Endpoint may be Zen rather than `api.typesafe.ai` depending on config—still TypeSafe SystemOne-shaped decisions per upstream docs. No live spend here.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 6fb18a1](https://github.com/d0nj/opencode-smart-reasoning/tree/6fb18a17ebb0dfea574265435f722f42a1813435): **0.2.0**, MIT. AI-assisted review of README, LICENSE, `src/jev.ts`, `src/index.ts`, and tests. **`bun test`: 36 passed** (deps with `--legacy-peer-deps`). No live TypeSafe/Zen.

Related: [fast-jev-opencode](fast-jev-opencode.md), [pi-jev-effort](pi-jev-effort.md), [Agent Router](agent-router.md), [codex-jev-router](codex-jev-router.md).
