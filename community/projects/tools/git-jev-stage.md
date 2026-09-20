# git-jev-stage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that classifies Git hunks against a one-sentence staging intent with TypeSafe Jev, shows a plan, and stages only the confirmed blocks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ibrahemid/git-jev-stage) |
| Maintainer | [ibrahemid](https://github.com/ibrahemid). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI (`git-jev-stage` 0.1.1) plus an agent skill folder. |
| Requirements | Node.js; a Git working tree; `TYPESAFE_API_KEY` for live classification. Offline Vitest needs no key. |
| License | [MIT](https://github.com/ibrahemid/git-jev-stage/blob/9cab2c11fdd333bb94cf1c742103bea71c763dc0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests inspected. Live TypeSafe calls and interactive staging sessions were not run. |

## When to use

Use it when a messy working tree mixes several intents and you want hunk-level staging guided by a plain-language description, with an explicit confirm step. Prefer ordinary `git add -p` when you already know which hunks belong together.

## How it works

[`src/core/jevClient.ts`](https://github.com/ibrahemid/git-jev-stage/blob/9cab2c11fdd333bb94cf1c742103bea71c763dc0/src/core/jevClient.ts) uses `@typesafe-ai/sdk` (`jev-latest` by default) to classify hunks. Application code builds the plan, prompts for confirmation, and runs Git staging—Jev does not execute Git commands by itself.

## Get started

```sh
git clone https://github.com/ibrahemid/git-jev-stage.git
cd git-jev-stage
git checkout 9cab2c11fdd333bb94cf1c742103bea71c763dc0
npm ci --ignore-scripts
npm test
# Live (charges TypeSafe): export TYPESAFE_API_KEY=… && npx git-jev-stage "fix login validation"
```

## Examples and demos

- Unit and integration Vitest suites under `test/` (mocked provider paths).
- `skills/git-jev-stage/SKILL.md` for agent-hosted usage.

## Limits and data handling

Hunk text and the intent sentence are sent to TypeSafe during live classification. Mis-staged hunks remain possible—always read the plan before confirming. Network/provider failures surface as provider errors; offline tests cover client and CLI shapes without live calls.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9cab2c1](https://github.com/ibrahemid/git-jev-stage/tree/9cab2c11fdd333bb94cf1c742103bea71c763dc0): **0.1.1**, MIT. AI-assisted source review of README, `jevClient.ts`, and tests. **`npm test`**: **330 passed**, 2 skipped. No live TypeSafe calls.

Related: [Jev Review Action](jev-review-action.md), [Moongate](moongate.md).
