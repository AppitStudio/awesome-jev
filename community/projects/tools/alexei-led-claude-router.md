# claude-router (alexei-led)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Claude Code plugin: local gateway rewrites `jev-router` requests after TypeSafe Jev picks micro/low/medium/high tier and continuation—distinct from [jev-claude-router](jev-claude-router.md) hooks and [Jev Model Router](jev-model-router.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexei-led/claude-router) |
| Maintainer | [alexei-led](https://github.com/alexei-led). Independently curated. Not an endorsement. |
| Format | npm package `@alexeiled/claude-router`; local gateway on `127.0.0.1`. |
| Requirements | Node ≥ 22; Claude Code; TypeSafe key; Anthropic API path via Claude Code. |
| License | [MIT](https://github.com/alexei-led/claude-router/blob/f6b8aed9815d98bd33864f46e86cda95d89218dd/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live gateway/Jev **not** run. Author marks status experimental. |

## When to use

Use it when you want model/effort routing via a local Anthropic-proxy gateway rather than Claude Code function-hook plugins. Prefer [jev-claude-router](jev-claude-router.md) for cost-aware hook routing forks.

## How it works

Claude Code `--model jev-router` hits a local gateway that asks Jev Choice (tier) + Noul (continuation?), applies stickiness/escalation policy, rewrites model/effort/thinking, and forwards to Anthropic. Continuations keep the turn's route; other models pass through.

## Get started

Follow upstream npm/install docs at [commit f6b8aed](https://github.com/alexei-led/claude-router/tree/f6b8aed9815d98bd33864f46e86cda95d89218dd); configure `~/.claude/router.json` tiers.

## Examples and demos

- README architecture diagram and CI badge.
- `docs/architecture.md` module map.

## Limits and data handling

Experimental. Prompts go to TypeSafe for routing and to Anthropic for completion. No live spend here.

## Review and maintenance

Reviewed **2026-09-23** at [commit f6b8aed](https://github.com/alexei-led/claude-router/tree/f6b8aed9815d98bd33864f46e86cda95d89218dd) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [jev-claude-router](jev-claude-router.md), [jev-model-router](jev-model-router.md).
