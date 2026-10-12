# Lintel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Change gate for AI coding agents: the agent proposes a choice, TypeSafe Jev reviews it, and you approve or reject before any code is written; works with Claude Code, Codex, Cursor and Gemini CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Capzay/Lintel) |
| Maintainer | [Capzay](https://github.com/Capzay). Independently curated. |
| Format | Go CLI (`lintel`) + agent hooks |
| Requirements | Go build or release binary; TypeSafe key; supported coding agent. |
| License | [MIT](https://github.com/Capzay/Lintel/blob/1c1dbb57d8a22e61b86c4ac4ee05869be80fd64e/LICENSE) |
| Jev evidence | [`internal/gate/gate.go`](https://github.com/Capzay/Lintel/blob/1c1dbb57d8a22e61b86c4ac4ee05869be80fd64e/internal/gate/gate.go) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Insert a fast typed review plus human approval into agent coding loops.
- Mismatch: adds a blocking approval step per proposal.

## How it works

`lintel wait` runs in the same agent turn; Jev's verdict card appears in the tool's permission prompt (or a window for Codex) for approval. (Summarized from the upstream [README](https://github.com/Capzay/Lintel/blob/1c1dbb57d8a22e61b86c4ac4ee05869be80fd64e/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the `lintel` command per the README and enable the hooks for your agent.

## Limits and data handling

Proposals go to TypeSafe for review. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 1c1dbb57d8a2](https://github.com/Capzay/Lintel/tree/1c1dbb57d8a22e61b86c4ac4ee05869be80fd64e). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
