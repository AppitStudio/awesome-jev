# automodel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code proxy where Jev (via OpenRouter) picks the model and effort for each prompt, subagent and workflow step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/moukrea/automodel) |
| Maintainer | [moukrea](https://github.com/moukrea). Independently curated. |
| Format | Local proxy + Claude Code integration |
| Requirements | Claude Code; OpenRouter API key for Jev decisions. |
| License | [MIT](https://github.com/moukrea/automodel/blob/0e2c4b89ec759e5ee0ce4c2e8e274018204c4d2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Cut Claude Code cost by sending simple turns to smaller models.
- Mismatch: Claude Code only.

## How it works

Selecting "Jev (auto)" in `/model` routes each prompt through a local proxy; Jev answers a typed choice over models/efforts and the request continues on your own Claude subscription. (Summarized from the upstream [README](https://github.com/moukrea/automodel/blob/0e2c4b89ec759e5ee0ce4c2e8e274018204c4d2e/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install script from the upstream README (`install.sh` into `~/.local/bin`), then pick Jev (auto) in `/model`.

## Limits and data handling

Prompt content is sent to OpenRouter for the routing decision. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 0e2c4b89ec75](https://github.com/moukrea/automodel/tree/0e2c4b89ec759e5ee0ce4c2e8e274018204c4d2e). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
