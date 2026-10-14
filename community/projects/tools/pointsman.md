# Pointsman

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered model and task routing for Claude Code and Codex: structured decisions become dependency DAGs that dispatch ready tasks to coding workers (formerly Jev Router).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kai-Leee/pointsman) |
| Maintainer | [Kai-Leee](https://github.com/Kai-Leee). Independently curated. |
| Format | Node.js CLI, MCP integration and evaluation tools |
| Requirements | Node.js 22+; TypeSafe (or compatible) API key for live routing. |
| License | [Apache-2.0](https://github.com/Kai-Leee/pointsman/blob/7310cc4cdffbd905015e32cd54e6a4ca654d3e7c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/jev.mjs`](https://github.com/Kai-Leee/pointsman/blob/7310cc4cdffbd905015e32cd54e6a4ca654d3e7c/bin/jev.mjs) at the pinned commit. |

## When to use

- Let Jev pick model and effort for coding-agent tasks before dispatch.
- Record routing decisions against scoped artifacts and outcomes for evaluation.
- Mismatch: advanced DAG experiments live on a separate research branch.

## How it works

A Jev client sends task descriptions with typed routing questions; the runner turns answers into dependency DAGs and dispatches ready tasks, with a usage dashboard and offline evaluation records. Integration evidence: [`bin/jev.mjs`](https://github.com/Kai-Leee/pointsman/blob/7310cc4cdffbd905015e32cd54e6a4ca654d3e7c/bin/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Kai-Leee/pointsman.git
cd pointsman
npm test
npm run eval:demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline evaluation demo: `npm run eval:demo`.

## Limits and data handling

Task descriptions are sent to the configured Jev provider and billed to your key; tests use fake keys and mock HTTP.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 7310cc4cdffb](https://github.com/Kai-Leee/pointsman/tree/7310cc4cdffbd905015e32cd54e6a4ca654d3e7c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
