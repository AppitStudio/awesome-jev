# rea-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that pairs REA (Reverse Engineer Anything) with TypeSafe Jev as a System 1 reflex layer — routing the target and workflow, gating risky REA calls, scoring evidence after tools and checking whether "done" was earned — plus a `jev` rank/classify/verify CLI; every hook fails open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juan-viox/rea-jev) |
| Maintainer | [juan-viox](https://github.com/juan-viox). Independently curated. |
| Format | Claude Code plugin (marketplace install) with hooks, skill, agents and a `jev` CLI |
| Requirements | Claude Code; REA (`rea-agents`, resolved via `npx`); `TYPESAFE_API_KEY` (preferred) or `OPENROUTER_API_KEY` for `typesafe/jev-1.13`. |
| License | [MIT](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Reverse-engineer native binaries, Electron/JS bundles, .NET or Android packages with REA and want cheap guardrails before and after each tool call.
- Rank, classify or verify claims from the shell with `jev rank`, `jev classify` and `jev verify`.
- Mismatch: thresholds in v0.1.0 are defaults, not calibrated on labeled data; Jev's answers are advisory.

## How it works

Hooks in [`hooks/hooks.json`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/hooks/hooks.json) call [`hook-route.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/hook-route.mjs) on prompt submit, [`hook-gate.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/hook-gate.mjs) before REA tool calls (deterministic rules first, then a Jev scope/risk gate), [`hook-evidence.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/hook-evidence.mjs) after tools and [`hook-stop.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/hook-stop.mjs) before the turn ends. The shared client [`scripts/lib/jev.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/lib/jev.mjs) validates answers; no key, timeout, error or malformed answer means the hook exits 0 and emits nothing. Decision points are documented in [`docs/decision-points.md`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/docs/decision-points.md).

## Get started

Install from the plugin marketplace, then set a key:

```sh
claude plugin marketplace add juan-viox/rea-jev
claude plugin install rea-jev@rea-jev
export TYPESAFE_API_KEY=...   # or OPENROUTER_API_KEY
# check provider, key and REA resolution:
node scripts/jev.mjs doctor --offline   # from a clone; the plugin exposes the same `jev` CLI
```

Each hook decision is a Jev request billed to your TypeSafe or OpenRouter key; REA and Claude usage are separate.

## Examples and demos

- Jev recipes for the skill: [`skills/reverse-engineer/references/jev-recipes.md`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/skills/reverse-engineer/references/jev-recipes.md).
- README *The `jev` CLI* table (ask, rank, classify, verify, doctor, stats) and *Modes*.

## Limits and data handling

Hook inputs are redacted locally before sending ([`scripts/lib/redact.mjs`](https://github.com/juan-viox/rea-jev/blob/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3/scripts/lib/redact.mjs) per upstream); route notes and gates are advisory and fail open. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b30536e8b284](https://github.com/juan-viox/rea-jev/tree/b30536e8b284ceabd8fc3a2d5bcb61630f876ff3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
