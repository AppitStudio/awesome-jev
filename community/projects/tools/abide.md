# Abide

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Enforce AGENTS.md/CLAUDE.md rules on every agent edit/turn with TypeSafe Jev (or Vercel AI Gateway) per-rule probabilities on diffs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coldteadotai/abide) |
| Maintainer | [coldteadotai](https://github.com/coldteadotai). Independently curated. |
| Format | TypeScript · agent hooks/CLI (`@coldtea/abide`, MIT) |
| Requirements | See upstream README; provider keys when using live hosted paths. |
| License | [`MIT`](https://github.com/coldteadotai/abide/blob/1a02157bbb79f19ae24864f92fc7414bd4bb5d50/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Enforce AGENTS.md/CLAUDE.md rules on every agent edit/turn with TypeSafe Jev (or Vercel AI Gateway) per-rule probabilities on diffs. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/coldteadotai/abide.git
cd abide
git checkout 1a02157bbb79f19ae24864f92fc7414bd4bb5d50
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: Jev one question per rule on diffs; hooks for Claude Code/Codex/OpenCode/Pi. ([upstream evidence](https://github.com/coldteadotai/abide/blob/1a02157bbb79f19ae24864f92fc7414bd4bb5d50/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 1a02157bbb79](https://github.com/coldteadotai/abide/tree/1a02157bbb79f19ae24864f92fc7414bd4bb5d50). AI-assisted README and license inspection; install/live paths not executed.
