# Covel (modular agentic AI RPG framework with an optional TypeSafe Jev evaluation provider)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Open-source AI role-playing framework and studio (plugins, world packs, stage mode) whose provider layer can call TypeSafe Jev for System One evaluations used by plugins such as the jev-choice-demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ackness/covel) |
| Maintainer | [ackness](https://github.com/ackness). Independently curated. |
| Format | TypeScript/Tauri desktop studio + web demo (MIT, early access) |
| Requirements | Covel desktop build or source checkout, your chat model keys, and a TypeSafe (or OpenRouter/Vercel AI Gateway) key for Jev evaluations. |
| License | [MIT](https://github.com/ackness/covel/blob/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/ai-provider/src/adapters/evaluation.ts`](https://github.com/ackness/covel/blob/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891/packages/ai-provider/src/adapters/evaluation.ts) at the pinned commit. |

## When to use

- Let typed Jev judgments drive RPG mechanics (choices, checks).
- Mix LLM storytelling with System One evaluations.
- Mismatch: Jev is optional; the demo plugin lives in covel-plugins.

## How it works

`evaluation.ts` adds `typesafe-systemone-v1` and `openrouter-decisions-v1` protocols that post to `/v1/systemone`; `llm.toml.example` shows a `jev-latest` evaluation connection that plugins consume (the Jev demo plugin lives in the separate covel-plugins repo). Integration evidence: [`packages/ai-provider/src/adapters/evaluation.ts`](https://github.com/ackness/covel/blob/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891/packages/ai-provider/src/adapters/evaluation.ts).

## Get started

Install Covel from releases or build from source (`pnpm install --frozen-lockfile`), then add a TypeSafe evaluation connection as in `llm.toml.example` and enable an evaluation plugin.

```sh
git clone https://github.com/ackness/covel.git && cd covel
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- llm.toml.example: [github.com/ackness/covel/blob/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891/llm.toml.example](https://github.com/ackness/covel/blob/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891/llm.toml.example)
- Plugin directory: [github.com/covel-ai/covel-plugins](https://github.com/covel-ai/covel-plugins)

## Limits and data handling

Story state sent to evaluation plugins goes to TypeSafe on your key. Early-access builds are unsigned.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 013ee2ccb7f5](https://github.com/ackness/covel/tree/013ee2ccb7f58fdfb3f05157cf408ccb3e90d891). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
