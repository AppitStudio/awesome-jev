# azir-dispatch

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python tool for coordinating coding agents in herdr: Jev (via OpenRouter) picks the agent, model, and reasoning effort for each task from your configured options, every dispatch goes to a local JSON Lines log, and a live terminal board shows the work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JosssphZhou/azir-dispatch) |
| Maintainer | [JosssphZhou](https://github.com/JosssphZhou). Independently curated. |
| Format | Python CLI + terminal board |
| Requirements | Python 3.11+; herdr for real dispatches; OpenRouter API key for Jev routing (configured defaults otherwise). Demo needs neither. |
| License | [MIT](https://github.com/JosssphZhou/azir-dispatch/blob/44ae133dc27290de6bb0e11909b5b60dc2f8c708/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Route parallel tasks across several coding agents with an audit trail.
- Mismatch: tied to the herdr terminal multiplexer.

## How it works

For each task Jev makes a typed choice over configured agents/models/efforts; dispatch events are appended to a JSONL log and animated on the board. (Summarized from the upstream [README](https://github.com/JosssphZhou/azir-dispatch/blob/44ae133dc27290de6bb0e11909b5b60dc2f8c708/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `python3 bin/azir-dispatch demo` to replay a run, or follow `skills/setup/SKILL.md` / INSTALL.md for real setup.

## Limits and data handling

Task descriptions are sent to OpenRouter for routing. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 44ae133dc272](https://github.com/JosssphZhou/azir-dispatch/tree/44ae133dc27290de6bb0e11909b5b60dc2f8c708). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
