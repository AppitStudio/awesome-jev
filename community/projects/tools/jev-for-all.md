# jev-for-all

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shared TypeSafe Jev (System One) decision contract for OpenCode, Claude Code, and Hermes: skill routing, tool subset, and browser moves without an LLM deliberating each step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emirbartu/jev-for-all) |
| Maintainer | [emirbartu](https://github.com/emirbartu). Independently curated. Not an endorsement. Not affiliated with the OpenCode team. |
| Format | TypeScript OpenCode plugin + adapters (`jev-for-all`). |
| Requirements | Bun/Node for the plugin path; OpenRouter API key (`sk-or-…`) for Decisions/`~typesafe/jev-latest`. |
| License | [MIT](https://github.com/emirbartu/jev-for-all/blob/dd8137d81c5121c554311685fb6e5cdac69a60eb/LICENSE). OpenRouter/TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, `src/jev.ts`). Live OpenRouter/Jev **not** run. |

## When to use

Use it when one coding harness should get the same fast typed decisions (skill load, tool subset, browser step) from Jev instead of another prompt. Prefer harness-specific routers when you only need model/effort selection without this shared contract.

## How it works

`createJev` in [`src/jev.ts`](https://github.com/emirbartu/jev-for-all/blob/dd8137d81c5121c554311685fb6e5cdac69a60eb/src/jev.ts) calls OpenRouter Decisions with typed Choice/Noul questions. OpenCode plugin wiring and Claude Code / Hermes adapters reuse that contract. Mock helpers support offline paths.

## Get started

```sh
git clone https://github.com/emirbartu/jev-for-all.git
cd jev-for-all
git checkout dd8137d81c5121c554311685fb6e5cdac69a60eb
# OpenCode: point plugins.package at this checkout; options.apiKey = sk-or-...
bun test && bun run typecheck   # offline when documented
```

## Examples and demos

- README OpenCode `opencode.jsonc` snippet.
- Design notes under `docs/superpowers/`.

## Limits and data handling

Agent state and question text go to OpenRouter/TypeSafe when live. Failures and uncertain answers must be handled by harness policy—do not treat a plugin load as a quality guarantee.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit dd8137d](https://github.com/emirbartu/jev-for-all/tree/dd8137d81c5121c554311685fb6e5cdac69a60eb) (MIT). AI-assisted source review. No live TypeSafe/OpenRouter spend.

Related: [opencode-jev-guard](opencode-jev-guard.md), [Hermes Jev Skills](hermes-jev-skills.md), [Intent-Router](intent-router.md).
