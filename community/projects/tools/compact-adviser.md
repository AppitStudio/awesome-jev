# compact-adviser

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent plugin that asks TypeSafe Jev whether the session is at a safe `/compact` boundary, then hints—or optionally auto-compacts on Pi and Claude Code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kunchenguid/compact-adviser) |
| Maintainer | [kunchenguid](https://github.com/kunchenguid). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm **compact-adviser 0.1.6** plugins for Pi, Claude Code (experimental Function Hooks), Codex CLI, and Grok Build. |
| Requirements | Node.js **22+** (22.18+ for Codex/Grok). Host: Pi ≥ 0.82, Claude Code ≥ 2.1.274, Codex ≥ 0.153, or Grok Build ≥ 1.0.34. Live judgments need `TYPESAFE_API_KEY` (env, `./.env`, or host settings). |
| License | [MIT](https://github.com/kunchenguid/compact-adviser/blob/4b7c5cf2d837e9f6ed39bb3eb8e82bf74707a362/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`packages/*/…/judge.ts`, README, LICENSE). Host install and live Jev calls were **not** executed on the review host. |

## When to use

Use it when coding-agent sessions should **hint or auto-run `/compact` only at likely checkpoints**, instead of compacting on a timer. Prefer [jev-compact](jev-compact.md) / [fast-jev-compaction](fast-jev-compaction.md) when you need to score *which* tool results to keep inside a compaction flow—this package judges *whether* to compact.

## How it works

Two one-sentence Choice questions (`done`, `shape`) go to `https://api.typesafe.ai/v1/systemone` in one request; host code composes a score and applies a context-usage-dependent hint floor. Codex and Grok are hint-only; Pi and Claude Code can opt into automatic `/compact` after first-use confirmation. Inspected shared question definitions in [`packages/pi-extension/src/judge.ts`](https://github.com/kunchenguid/compact-adviser/blob/4b7c5cf2d837e9f6ed39bb3eb8e82bf74707a362/packages/pi-extension/src/judge.ts) (mirrored in the other host packages).

## Get started

```sh
# Pi
pi install npm:compact-adviser
# Claude Code (experimental hooks)
claude plugin marketplace add kunchenguid/compact-adviser
claude plugin install compact-adviser@compact-adviser
# Codex (macOS/Linux)
codex plugin marketplace add kunchenguid/compact-adviser
codex plugin add compact-adviser@compact-adviser
```

Pin for review: [commit 4b7c5cf](https://github.com/kunchenguid/compact-adviser/tree/4b7c5cf2d837e9f6ed39bb3eb8e82bf74707a362). Supply `TYPESAFE_API_KEY` before expecting live advice.

## Examples and demos

- Status-line / hook hint screenshots in upstream `docs/`.
- Host-specific install notes in the monorepo README.

## Limits and data handling

Eligible checkpoint context is sent to TypeSafe when a key is present and product gates pass (upstream states install is consent). Wrong hints cost more when the context window is still mostly empty. Live calls and host installs were not run here.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 4b7c5cf](https://github.com/kunchenguid/compact-adviser/tree/4b7c5cf2d837e9f6ed39bb3eb8e82bf74707a362) (`compact-adviser` **0.1.6**, MIT). AI-assisted review of README, LICENSE, and judge modules. No live TypeSafe spend.

Related: [jev-compact](jev-compact.md), [fast-jev-compaction](fast-jev-compaction.md), [omp-jev-compaction](omp-jev-compaction.md).
