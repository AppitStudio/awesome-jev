# JevGuard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code / Codex plugin that turns project rules (from CLAUDE.md / AGENTS.md) into typed Jev checks on PreToolUse and Stop hooks, so the agent cannot quietly ignore them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jhonnyr97/JevGuard) |
| Maintainer | [Jhonnyr97](https://github.com/Jhonnyr97). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package **jevguard 0.1.0** — Claude Code marketplace plugin + Codex plugin hooks; bins `jevguard-hook` / `jevguard-validate`. |
| Requirements | Node.js with the bundled `dist/` binaries (or `npm run build`). TypeSafe (or compatible) System One backend via `.jevguard/config.json` + API key env (not stored in the committed config). |
| License | [MIT](https://github.com/Jhonnyr97/JevGuard/blob/ecdba7a1c9097b7512fab83db89630e3a67a390f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source + offline vitest inspected. Live Claude Code / Codex hook installs and live Jev were not run. Distinct from [jev-guard](jev-guard.md) (leepokai risk firewall). |

## When to use

Use it when CLAUDE.md / AGENTS.md keep being suggestions and you want **generated, editable rules** enforced at tool-call and stop time. Prefer [jev-guard](jev-guard.md) for multi-agent deny/ask/allow risk scoring and injection scanning; prefer [Canny](canny.md) / [clear-head](clear-head.md) for ledger- or claim-backed stop checks without a project rules JSON.

## How it works

`/jevguard:init` (and related skills) draft rules into `.jevguard/rules.json`. [`src/verify.ts`](https://github.com/Jhonnyr97/JevGuard/blob/ecdba7a1c9097b7512fab83db89630e3a67a390f/src/verify.ts) maps each applicable rule to a Jev noul/choice/score question; [`src/jev/client.ts`](https://github.com/Jhonnyr97/JevGuard/blob/ecdba7a1c9097b7512fab83db89630e3a67a390f/src/jev/client.ts) POSTs `{state, model, questions}` to a configurable `…/v1/systemone` base URL. Hooks block or warn per `.jevguard/config.json`. Pause/resume use a project flag file so hooks pick it up on the next call. Codex install path is documented as less thoroughly tested upstream.

## Get started

```sh
git clone https://github.com/Jhonnyr97/JevGuard.git
cd JevGuard
git checkout ecdba7a1c9097b7512fab83db89630e3a67a390f
npm ci
npm test
# Claude Code (upstream README):
# /plugin marketplace add Jhonnyr97/JevGuard
# /plugin install jevguard@jevguard
```

Live verification sends tool/response state to the configured System One backend and may incur charges. This listing did not install agent hooks or call live Jev.

## Examples and demos

- Offline vitest on the review host: **17 passed** (`hook`, `verify`, `pause` suites).
- Skills under `skills/` (`init`, `rule`, `pause`, `resume`).

## Limits and data handling

Tool arguments, command text, and response excerpts leave the host on live verifies. API keys must not be committed in `.jevguard/config.json` (upstream documents env-based loading). Codex end-to-end install was not verified here.

## Review and maintenance

Reviewed on **2026-09-22** at [commit ecdba7a](https://github.com/Jhonnyr97/JevGuard/tree/ecdba7a1c9097b7512fab83db89630e3a67a390f): **0.1.0**, MIT. AI-assisted source review of README, `src/jev/client.ts`, `src/verify.ts`, `package.json`, LICENSE. Offline: `npm test` → **17 passed**. No live TypeSafe or agent-hook runs.

Related: [jev-guard](jev-guard.md), [Canny](canny.md), [clear-head](clear-head.md), [agent-chaperone](agent-chaperone.md).
