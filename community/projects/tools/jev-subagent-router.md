# jev-router by Bender-88 (Claude Code mod that has Jev pick haiku, sonnet or opus for each subagent task)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: before a subagent starts, Jev classifies its task as trivial, standard or hard and the mod sets the subagent model to haiku, sonnet or opus. A status line shows the latest decision and an estimate of what routing saved. Forks and subagents with an explicit model are never routed, and low confidence (below 0.5), errors, timeouts or a missing key keep the default model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bender-88/jev-router) |
| Maintainer | [Bender-88](https://github.com/Bender-88). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code and a TypeSafe key in `TYPESAFE_API_KEY` or the plugin config. |
| License | [MIT](https://github.com/Bender-88/jev-router/blob/e88fc21228719e75d6c98210cb48582d4f151e0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.tsx`](https://github.com/Bender-88/jev-router/blob/e88fc21228719e75d6c98210cb48582d4f151e0f/hooks/register.tsx) at the pinned commit. |

## When to use

- Cut Claude Code cost by running simple subagent tasks on cheaper models without touching harder ones.
- Mismatch: cannot switch the main conversation's model, only suggest it; savings are estimates from configurable prices.

## How it works

`register.tsx` sends the subagent's description and prompt to `POST https://api.typesafe.ai/v1/systemone` as one Choice over `jev-latest` and sets the model when confidence clears `minConfidence`. Integration evidence: [`hooks/register.tsx`](https://github.com/Bender-88/jev-router/blob/e88fc21228719e75d6c98210cb48582d4f151e0f/hooks/register.tsx).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin install jev-router --marketplace Bender-88/jev-router
export TYPESAFE_API_KEY="<your-typesafe-api-key>"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Options table: [github.com/Bender-88/jev-router#options](https://github.com/Bender-88/jev-router#options)

## Limits and data handling

Subagent task text (and your prompt for the suggestion line) is sent to TypeSafe. Separate project from Hoppin-Sorter's jev-router already in the catalog. Independent; not affiliated with TypeSafe or Anthropic.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit e88fc2122871](https://github.com/Bender-88/jev-router/tree/e88fc21228719e75d6c98210cb48582d4f151e0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
