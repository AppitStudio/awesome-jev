# Jev Decisions Plugin for Hermes

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin that gives the Hermes agent (and other AI agents) Jev-backed review tools: tool-risk reviews, human-approval recommendations, checking answers against their sources, and assessing whether a task is really finished. Your usual model keeps doing the work; reviews are advice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bojansandhaus/jev-decisions-hermes) |
| Maintainer | [bojansandhaus](https://github.com/bojansandhaus). Independently curated. |
| Format | Python plugin for Hermes + integration guide for other agents |
| Requirements | Python 3.10+; Hermes agent; TypeSafe API key. |
| License | [MIT](https://github.com/bojansandhaus/jev-decisions-hermes/blob/e1a3bf57220c724d73a67f78a4e8a014b8087b28/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Ask an autonomous agent to double-check risky changes, unsupported claims, and 'done' claims.
- Mismatch: advisory only; it does not block commands or replace approval settings. Automatic reviews are off by default.

## How it works

Exposes review tools whose questions are answered by Jev typed decisions; the agent supplies the evidence. (Summarized from the upstream [README](https://github.com/bojansandhaus/jev-decisions-hermes/blob/e1a3bf57220c724d73a67f78a4e8a014b8087b28/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Follow the 'Install in Hermes' section of the upstream README, then ask for a review in a normal conversation.

## Limits and data handling

Reviewed content is sent to TypeSafe under your API key. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit e1a3bf57220c](https://github.com/bojansandhaus/jev-decisions-hermes/tree/e1a3bf57220c724d73a67f78a4e8a014b8087b28). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
