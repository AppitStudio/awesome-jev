# jev-claude-router (Flam1ngFir3ball)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin fork: TypeSafe Jev picks model tier and effort per turn with cost-aware switch checks and optional Jev compaction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Flam1ngFir3ball/jev-claude-router) |
| Maintainer | [Flam1ngFir3ball](https://github.com/Flam1ngFir3ball). Fork of satviksinha/jev-model-router; independently curated. Not an endorsement. |
| Format | Claude Code plugin (hooks + policy). |
| Requirements | Claude Code with function hooks; TypeSafe API key (recommended) or Vercel AI Gateway key. |
| License | [MIT](https://github.com/Flam1ngFir3ball/jev-claude-router/blob/3ebe3360d5b389f714cd840885d1b1925b9894a4/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, hooks/policy). Live Claude Code/Jev **not** run. Distinct from [alexei-led/claude-router](https://github.com/alexei-led/claude-router) and catalog [Jev Model Router](jev-model-router.md). |

## When to use

Use it when Claude Code should auto-route haiku/sonnet/opus/fable tiers with stickiness and price ceilings. Prefer the davila7 [Jev Model Router](jev-model-router.md) for the upstream mod path, or [alexei-led-claude-router](https://github.com/alexei-led/claude-router) for a local gateway rewrite approach.

## How it works

On `turn.start`, Jev answers tier + effort; policy in `hooks/policy.ts` applies window/confidence/price ceilings before rewriting requests. Optional compaction uses Jev (credit: tamaratran/fast-jev-compaction). Status lines show tier, confidence, and cost.

## Get started

Follow upstream README: add TypeSafe or Gateway key to `~/.claude/settings.json`, enable function hooks, install the plugin from the repo at [commit 3ebe336](https://github.com/Flam1ngFir3ball/jev-claude-router/tree/3ebe3360d5b389f714cd840885d1b1925b9894a4).

## Examples and demos

- README routing diagram and sample status lines.
- Upstream credits and fork delta sections.

## Limits and data handling

Model switches can invalidate prompt cache and cost money; the fork's checks exist to reduce thrash. Prompt context goes to TypeSafe (and Anthropic). No live spend here.

## Review and maintenance

Reviewed **2026-09-23** at [commit 3ebe336](https://github.com/Flam1ngFir3ball/jev-claude-router/tree/3ebe3360d5b389f714cd840885d1b1925b9894a4) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [jev-model-router](jev-model-router.md), [alexei-led-claude-router](https://github.com/alexei-led/claude-router), [jev-effort-router](jev-effort-router.md).
