# model-selector (Claude Code subagent model picker)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code PreToolUse hook that sends each subagent's task text to Jev before it runs and fills in the model (haiku, sonnet or opus) and effort, for both the Agent tool and `agent()` calls inside workflows, with a cost report over your transcripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/menoncello/model-selector) |
| Maintainer | [menoncello](https://github.com/menoncello). Independently curated. |
| Format | Claude Code hook (TypeScript on Bun) |
| Requirements | Claude Code, Bun, and a TypeSafe key in `~/.claude/settings.json`. |
| License | [MIT](https://github.com/menoncello/model-selector/blob/63eddf9b11625e36c6630145c0249efaf1a86023/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`model-router/jev.ts`](https://github.com/menoncello/model-selector/blob/63eddf9b11625e36c6630145c0249efaf1a86023/model-router/jev.ts) at the pinned commit. |

## When to use

- Stop every subagent from defaulting to the most expensive model.
- Audit what subagents cost by model and effort with `report.ts`.
- Mismatch: Claude Code only; calls that already set a model or effort are left alone.

## How it works

The hook matches `Agent|Workflow` tool calls. `model-router/jev.ts` asks Jev at `https://api.typesafe.ai/v1/systemone` one Choice question for the model tier and one Score question for effort, using criteria in `config.ts`; probability and score thresholds then pick the model and effort. For workflows it rewrites the script before it runs, so the approval prompt shows each pick. Decisions and a cache go to `~/.claude/model-router/`; if Jev fails or times out, the call runs unchanged. Integration evidence: [`model-router/jev.ts`](https://github.com/menoncello/model-selector/blob/63eddf9b11625e36c6630145c0249efaf1a86023/model-router/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd model-router && bun install
ln -sfn "$PWD" ~/.claude/hooks/model-router
# add the PreToolUse hook (matcher "Agent|Workflow") and TYPESAFE_API_KEY to ~/.claude/settings.json
bun ~/.claude/hooks/model-router/report.ts --since 2026-10-01
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README settings.json snippet and delegation.md
- model-router/jev.test.ts (mocked Jev)

## Limits and data handling

Subagent task text goes to TypeSafe. The cost report reprices tokens at list prices and is a reference point, not a measured saving.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 63eddf9b1162](https://github.com/menoncello/model-selector/tree/63eddf9b11625e36c6630145c0249efaf1a86023). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
