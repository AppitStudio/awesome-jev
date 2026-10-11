# Jev Harness (Apixly)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Agent-loop runtime where Jev chooses the next tool and arguments while code executes, refreshes state and checks completion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/apixly-ai/jev-harness) |
| Maintainer | [apixly-ai](https://github.com/apixly-ai). Independently curated. |
| Format | Python library and CLI (`apixly-jev-harness`) |
| Requirements | Python; Jev access via TypeSafe. |
| License | [MIT](https://github.com/apixly-ai/jev-harness/blob/4253a52404050a9b758447e6b8e9105ae63671e4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let Jev explore routes through unfamiliar catalogs, files or repos inside AI-defined tools and bounds.
- Mismatch: you already know the exact route; a plain script is simpler. Install from the Git URL, not the unrelated PyPI `jev-harness` package.

## How it works

The primary AI writes task scripts defining tool capabilities, parameter providers, observation and completion checks; Jev picks the next step from the goal, admitted conversation, state and history; code executes and verifies within permission and resource bounds. (Summarized from the upstream [README](https://github.com/apixly-ai/jev-harness/blob/4253a52404050a9b758447e6b8e9105ae63671e4/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pip install 'git+https://github.com/apixly-ai/jev-harness.git@v0.1.17'`.

## Limits and data handling

Goal, admitted conversation and observed state are sent to the hosted Jev API on each step. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 4253a5240405](https://github.com/apixly-ai/jev-harness/tree/4253a52404050a9b758447e6b8e9105ae63671e4). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
