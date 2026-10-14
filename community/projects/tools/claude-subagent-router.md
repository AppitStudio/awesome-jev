# Claude Subagent Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin with seven subagent workers, a review skill and a Codex CLI bridge; optional model routing sends Agent-call briefs to Jev and switches model when it is confident.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/robertanton81/claude-subagent-router) |
| Maintainer | [robertanton81](https://github.com/robertanton81). Independently curated. |
| Format | Claude Code plugin (Node.js scripts) |
| Requirements | Claude Code; optional TypeSafe API key (Jev routing off by default). |
| License | [MIT](https://github.com/robertanton81/claude-subagent-router/blob/2d9858bfa5548eab6d59c07307e30cb628251a23/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/lib/typesafe.mjs`](https://github.com/robertanton81/claude-subagent-router/blob/2d9858bfa5548eab6d59c07307e30cb628251a23/scripts/lib/typesafe.mjs) at the pinned commit. |

## When to use

- Spread subagent work across Claude models and Codex to stay within plan limits.
- Let Jev choose the model for Agent tool calls when it is confident.
- Mismatch: Jev routing and Codex are both off by default.

## How it works

With routing enabled, each Agent tool call's brief is sent to Jev as a choice question; above the confidence threshold the plugin changes the call's model (and worker for its own workers). Integration evidence: [`scripts/lib/typesafe.mjs`](https://github.com/robertanton81/claude-subagent-router/blob/2d9858bfa5548eab6d59c07307e30cb628251a23/scripts/lib/typesafe.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add robertanton81/claude-subagent-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- See 'What leaves your machine' in the upstream README.

## Limits and data handling

With routing on, subagent briefs are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 2d9858bfa554](https://github.com/robertanton81/claude-subagent-router/tree/2d9858bfa5548eab6d59c07307e30cb628251a23). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
