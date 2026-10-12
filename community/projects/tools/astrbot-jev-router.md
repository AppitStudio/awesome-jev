# astrbot_plugin_jev_router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin that routes each message to the best-matching sub-agent with TypeSafe Jev, overriding only this turn's model, persona and tool allowlist while AstrBot's history and memory stay native.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maolbsMd/astrbot_plugin_jev_router) |
| Maintainer | [maolbsMd](https://github.com/maolbsMd). Independently curated. |
| Format | AstrBot plugin |
| Requirements | AstrBot; TypeSafe key. |
| License | [MIT](https://github.com/maolbsMd/astrbot_plugin_jev_router/blob/2180ec072061455ef8740047047e408694802cc1/LICENSE) |
| Jev evidence | [`main.py`](https://github.com/maolbsMd/astrbot_plugin_jev_router/blob/2180ec072061455ef8740047047e408694802cc1/main.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Route chatbot turns to specialised sub-agents without changing AstrBot's main flow.
- Mismatch: Chinese-language docs; AstrBot-specific.

## How it works

On each message the plugin calls the Jev SystemOne endpoint (optionally with recent context and last agent) and overrides the turn's settings. (Summarized from the upstream [README](https://github.com/maolbsMd/astrbot_plugin_jev_router/blob/2180ec072061455ef8740047047e408694802cc1/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install through AstrBot's plugin manager or copy the repo per the README.

## Limits and data handling

Messages (and optional summaries) go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 2180ec072061](https://github.com/maolbsMd/astrbot_plugin_jev_router/tree/2180ec072061455ef8740047047e408694802cc1). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
