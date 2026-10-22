# dsh-work-planner (GitHub issue work packages for DSH)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin (Japanese docs) that groups open GitHub issues into ordered work packages for the agent's next session, using a decision model such as Jev for size and priority estimates and deterministic rules for dependency order, with no chat LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lifwsp/dsh-work-planner) |
| Maintainer | [lifwsp](https://github.com/lifwsp). Independently curated. |
| Format | DeepSeek Harness (dsh) plugin (TypeScript) |
| Requirements | DeepSeek Harness; a decision-model key such as `TYPESAFE_API_KEY` (Liquid, OpenRouter and custom endpoints are also supported). |
| License | [MIT](https://github.com/lifwsp/dsh-work-planner/blob/3e785d4ea0ed2fbd14dd18007e135a983e93808d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/client.ts`](https://github.com/lifwsp/dsh-work-planner/blob/3e785d4ea0ed2fbd14dd18007e135a983e93808d/src/decision/client.ts) at the pinned commit. |

## When to use

- Decide what the agent should work on next from a pile of issues.
- Re-rank the plan every hour in the background.
- Mismatch: the provider defaults to none (deterministic only); Jev is one of several options.

## How it works

`src/decision/client.ts` calls the configured System One endpoint; with `decisionProvider: typesafe` it uses Jev with `TYPESAFE_API_KEY` (see `src/config.ts`). The plugin never writes to GitHub itself. Integration evidence: [`src/decision/client.ts`](https://github.com/lifwsp/dsh-work-planner/blob/3e785d4ea0ed2fbd14dd18007e135a983e93808d/src/decision/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile web add github:lifwsp/dsh-work-planner
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage in the README: [github.com/lifwsp/dsh-work-planner#readme](https://github.com/lifwsp/dsh-work-planner#readme)

## Limits and data handling

Issue titles and bodies are sent to the decision provider you configure.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 3e785d4ea0ed](https://github.com/lifwsp/dsh-work-planner/tree/3e785d4ea0ed2fbd14dd18007e135a983e93808d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
