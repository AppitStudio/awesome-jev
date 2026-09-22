# jev-pref

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turn AGENTS.md / project preferences into a Jev-powered semantic linter for coding-agent diffs, with setup, review, tune commands and an optional GitHub Action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doeixd/jev-pref) |
| Maintainer | [doeixd](https://github.com/doeixd). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`jev-pref` 0.4.1** (`npx jev-pref`); monorepo under `packages/jev-pref`. |
| Requirements | Node.js ≥ 20; `TYPESAFE_API_KEY` (or `AI_GATEWAY_API_KEY` / `VERCEL_OIDC_TOKEN` / `JEV_API_KEY`) for live review/tune. |
| License | [MIT](https://github.com/doeixd/jev-pref/blob/9d77ea6069123a0b3eedf465ec39781842722b0a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline package tests inspected; live TypeSafe review not run on the review host. Distinct from [patdown](patdown.md) (fuzzy markdown rules) and [JevGuard](jevguard.md) (hook-enforced CLAUDE.md/AGENTS.md rules). |

## When to use

Use it when you want **evidence-grounded semantic prefs** on a git diff (mutable state, API breaks, secrets gates) decided by TypeSafe Jev, then acted on by your coding agent. Prefer [patdown](patdown.md) for fuzzy markdown-rule linting, or [JevGuard](jevguard.md) for PreToolUse/Stop hooks derived from CLAUDE.md/AGENTS.md.

## How it works

`npx jev-pref setup` teaches the agent to write preference checks. `review` collects a diff, builds typed questions, and calls TypeSafe Jev (via advocaat / Gateway cascade) through [`packages/jev-pref/src/commands/review.js`](https://github.com/doeixd/jev-pref/blob/9d77ea6069123a0b3eedf465ec39781842722b0a/packages/jev-pref/src/commands/review.js). Code owns thresholding, secrets gates, and agent-facing outcomes. Optional GitHub Action under `actions/review/`.

## Get started

```sh
git clone https://github.com/doeixd/jev-pref.git
cd jev-pref
git checkout 9d77ea6069123a0b3eedf465ec39781842722b0a
cd packages/jev-pref
npm install --ignore-scripts
npm test
# Live (not run here): npx jev-pref setup / review with TYPESAFE_API_KEY
```

Live review/tune send diffs to TypeSafe/Gateway and may incur charges.

## Examples and demos

- Offline on the review host: `npm test` in `packages/jev-pref` → **86 passed**.
- Upstream explainer GIF and Action examples under `actions/review/examples/`.

## Limits and data handling

Diff text leaves the host on live review. Prefer change-scoped, evidence-grounded prefs per upstream `docs/principles.md`. Auth cascade is documented in the package README.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 9d77ea6](https://github.com/doeixd/jev-pref/tree/9d77ea6069123a0b3eedf465ec39781842722b0a): **`jev-pref` 0.4.1**, MIT. AI-assisted source review of README, `packages/jev-pref/src/commands/review.js`, LICENSE. Offline: `npm test` → 86 passed. No live TypeSafe on the review host.

Related: [patdown](patdown.md), [JevGuard](jevguard.md), [jev-preflight](jev-preflight.md), [Discern](discern.md).
