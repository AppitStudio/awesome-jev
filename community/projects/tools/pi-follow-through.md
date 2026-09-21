# pi-follow-through

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that asks TypeSafe Jev whether useful work remains after a run settles, and only nudges the agent when Jev cites verifiable unfinished evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nabsku/pi-follow-through) |
| Maintainer | [Nabsku](https://github.com/Nabsku). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension (`pi-follow-through` npm package / `pi install npm:pi-follow-through`). |
| Requirements | Pi coding agent with extension support; `TYPESAFE_API_KEY` (or `TYPESAFE_AI_API_KEY`) in the environment that starts Pi. |
| License | [MIT](https://github.com/Nabsku/pi-follow-through/blob/52b541f9af2d6be00b793a167517819e43d412a0/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `tsx --test` **5 passed**; live TypeSafe smoke not run. |

## When to use

Use it when Pi should continue unfinished user-requested work after `agent_settled`, without inventing new follow-ups. Prefer [pi-heed](pi-heed.md) for conversational constraint ledgers; prefer [pi-jev](pi-jev.md) / [pi-jev-permit](pi-jev-permit.md) for per-call gates.

## How it works

After a run settles (TUI/RPC modes only), [`extensions/follow-through.ts`](https://github.com/Nabsku/pi-follow-through/blob/52b541f9af2d6be00b793a167517819e43d412a0/extensions/follow-through.ts) sends bounded recent requests, optional tool data, transcript, and final output to TypeSafe Jev. It requires a probability above a configured threshold (default `0.8`) plus typed answers that cite IDs present in the submitted state before posting a fixed continuation prompt. Missing keys, errors, and timeouts skip the nudge.

## Get started

```sh
git clone https://github.com/Nabsku/pi-follow-through.git
cd pi-follow-through
git checkout 52b541f9af2d6be00b793a167517819e43d412a0
npm ci
npm test
# install into Pi (review source first):
# pi install npm:pi-follow-through
export TYPESAFE_API_KEY=…
```

Optional `~/.pi/agent/settings.json` / `.pi/settings.json` keys: `followThrough.threshold`, `followThrough.includeToolData`.

## Examples and demos

- Upstream README documents the nudge prompt and data caps.
- This listing ran `npm test`: **5 passed**. No live TypeSafe call.

## Limits and data handling

User prompts, code, tool args/results, and assistant text may reach TypeSafe when enabled (caps documented upstream). Skips print/JSON modes, failed/aborted runs, and identical progress after a prior nudge. Not a substitute for explicit user direction.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 52b541f](https://github.com/Nabsku/pi-follow-through/tree/52b541f9af2d6be00b793a167517819e43d412a0): MIT; AI-assisted source review of README, LICENSE, extension, and tests; offline tests **5 pass**. No live TypeSafe call.

Related: [pi-heed](pi-heed.md), [pi-jev](pi-jev.md), [pi-jev-context](pi-jev-context.md).
