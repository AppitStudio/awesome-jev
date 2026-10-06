# Coding Router Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript/Bun launchers `codex-jev` and `claude-jev` plus a Pi `jev/auto` virtual model that route each coding-agent user turn through TypeSafe Jev to pick a model tier (Fast, Balanced, Strong, Long) and reasoning effort, with confidence-capped local policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/guanghuang/coding-router-jev) |
| Maintainer | [guanghuang](https://github.com/guanghuang). Independently curated. |
| Format | CLI launchers + local proxy + Pi extension (release v0.1.0) |
| Requirements | Codex CLI, Claude Code CLI or Pi installed and authenticated; `TYPESAFE_API_KEY` and `TYPESAFE_BASE_URL` (TypeSafe or OpenRouter). |
| License | [MIT](https://github.com/guanghuang/coding-router-jev/blob/367e4d99245980ce433ac12fd4ee77cf48a12687/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Jev choose model and effort per Codex or Claude Code turn while you keep explicit control (`--model`, “use Strong”).
- Select `jev/auto` in Pi to resolve a physical model per request.
- Mismatch: without a TypeSafe key routing is disabled; tier changes can affect prompt-cache reuse.

## How it works

For Codex, a temporary local proxy forwards Responses API requests and sends Jev a bounded routing context (latest message, current tier/model/effort, tier catalogue, capped excerpts, cache observations); three score questions plus a tier choice drive [`src/router.ts`](https://github.com/guanghuang/coding-router-jev/blob/367e4d99245980ce433ac12fd4ee77cf48a12687/src/router.ts). Failed or invalid Jev answers keep the current tier (3-second deadline); low confidence refuses downgrades and caps upgrades.

## Get started

Install release binaries and configure Jev:

```sh
curl -fsSL https://raw.githubusercontent.com/guanghuang/coding-router-jev/main/install.sh | sh
export TYPESAFE_API_KEY=...
export TYPESAFE_BASE_URL="https://openrouter.ai/api"   # or TypeSafe's API
codex-jev    # or claude-jev
```

Each routed turn is a Jev request billed by TypeSafe/OpenRouter; model usage bills through your agent provider.

## Examples and demos

- README *Routing*, *Local policy* and *Routing history* (`jev-logs`) sections.
- Claude Code plugin and Pi package install paths.

## Limits and data handling

Latest user message and capped excerpts are sent to the Jev provider. The installer pipes a remote script to `sh` (review it first). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 367e4d992459](https://github.com/guanghuang/coding-router-jev/tree/367e4d99245980ce433ac12fd4ee77cf48a12687). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
