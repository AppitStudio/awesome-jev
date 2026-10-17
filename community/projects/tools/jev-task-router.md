# Jev Task Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

npm CLI that asks Jev, through the AI SDK and Vercel AI Gateway, which eligible coding model should handle a task, then hands the task to your local Codex or GitHub Copilot CLI session after you confirm.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hainalstefan-coder/Jev_Router) |
| Maintainer | [hainalstefan-coder](https://github.com/hainalstefan-coder). Independently curated. |
| Format | Node.js CLI (`jev-task-router` on npm) |
| Requirements | Node.js 22.14+, a Vercel AI Gateway key, and Codex CLI and/or Copilot CLI signed in. |
| License | [MIT](https://github.com/hainalstefan-coder/Jev_Router/blob/baa05a38d86e9afa84cd829ec0f093aabc6954e7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/router.ts`](https://github.com/hainalstefan-coder/Jev_Router/blob/baa05a38d86e9afa84cd829ec0f093aabc6954e7/src/router.ts) at the pinned commit. |

## When to use

- Pick a coding model per task across your existing Codex and Copilot subscriptions.
- Preview the recommendation with `jev route` before anything runs.
- Mismatch: only routes between models those CLIs expose; if Jev or the provider fails, the command stops.

## How it works

`src/router.ts` calls `gateway.decisionModel("typesafe-ai/jev")` with the task and the discovered eligible model catalog (optionally enriched with Artificial Analysis data); `jev run` shows the choice and rationale, asks before dispatch, and runs Codex with `--ephemeral`. Integration evidence: [`src/router.ts`](https://github.com/hainalstefan-coder/Jev_Router/blob/baa05a38d86e9afa84cd829ec0f093aabc6954e7/src/router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --global jev-task-router
export AI_GATEWAY_API_KEY=...
jev doctor
jev route "Add pagination to the users endpoint"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Command reference and cost notes in the README.

## Limits and data handling

The task prompt goes to Jev for the routing choice and to the chosen provider for execution; repository files are not sent to Jev and prompts are not saved.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit baa05a38d86e](https://github.com/hainalstefan-coder/Jev_Router/tree/baa05a38d86e9afa84cd829ec0f093aabc6954e7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
