# jev Claude Code plugin (yinjs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that hands small frequent decisions to Jev at six points — permission requests, prompt-injection warnings on fetched content, a 'done' re-check, prompt nudges, and jev-route effort/model routing — each one ~1 s call that changes nothing when Jev is unsure; Jev via OpenRouter (default), TypeSafe or Vercel AI Gateway.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yinjs/claude-jev) |
| Maintainer | [yinjs](https://github.com/yinjs). Independently curated. |
| Format | Claude Code plugin from the `yinjs` marketplace |
| Requirements | Claude Code and one provider key: `OPENROUTER_API_KEY` (default), `TYPESAFE_API_KEY` with `JEV_PROVIDER=typesafe`, or `AI_GATEWAY_API_KEY`. |
| License | [MIT](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Auto-approve clearly safe, on-task Bash/WebFetch/MCP calls and deny clearly destructive ones.
- Warn Claude when fetched content addresses the agent; re-check claims that tests pass.
- Mismatch: upstream warns commands not on the static never-approve list run on Jev's judgment alone — read *Limits* before enabling.

## How it works

Hook scripts: [`permission.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/permission.ts) (approve at high safe/on-task probability, deny at high destructive probability, static never-approve list), [`injection.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/injection.ts), [`done-check.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/done-check.ts), [`prompt-nudge.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/prompt-nudge.ts) and [`turn.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/turn.ts) for jev-route; [`lib.ts`](https://github.com/yinjs/claude-jev/blob/a2bc77425d608d5865847986d6760736f21de26c/scripts/lib.ts) holds the shared client.

## Get started

Install from the marketplace (README *Install*):

```sh
claude plugin marketplace add yinjs/claude-jev
claude plugin install jev@yinjs
export OPENROUTER_API_KEY=sk-or-...    # or JEV_PROVIDER=typesafe + TYPESAFE_API_KEY
```

Each hook decision is one Jev call billed by the chosen provider (OpenRouter, TypeSafe or Vercel).

## Examples and demos

- README hook table, *Provider*, *Cost* and *What leaves the machine*.

## Limits and data handling

Commands, tool results (head/tail) and prompts go to the chosen Jev provider. Approval thresholds are tuned, not guaranteed; use at your own risk (upstream). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit a2bc77425d60](https://github.com/yinjs/claude-jev/tree/a2bc77425d608d5865847986d6760736f21de26c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
