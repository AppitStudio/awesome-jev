# pi-jev-thinking-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi/omp extension that keeps the model fixed and lets TypeSafe Jev pick the thinking effort for each turn via a local daemon, preserving the prompt cache (distinct from [pi-jev-thinking](pi-jev-thinking.md)).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brzewVCE/pi-jev-thinking-router) |
| Maintainer | [brzewVCE](https://github.com/brzewVCE). Independently curated. |
| Format | Pi extension with embedded Python daemon |
| Requirements | Pi or omp; Python 3 (stdlib); TypeSafe key. |
| License | [Apache-2.0](https://github.com/brzewVCE/pi-jev-thinking-router/blob/490b8fd962af8507b0ca8e6ae25a2813b6461722/LICENSE) |
| Jev evidence | [`adapters/pi/core/jev_core.py`](https://github.com/brzewVCE/pi-jev-thinking-router/blob/490b8fd962af8507b0ca8e6ae25a2813b6461722/adapters/pi/core/jev_core.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Spend more reasoning on hard turns and less on easy ones while keeping cache continuity.
- Mismatch: never turns thinking off; thin README.

## How it works

Before each turn the extension calls a local daemon (`POST /decide`) that asks Jev for the effort level; failures fail open to the current level. (Summarized from the upstream [README](https://github.com/brzewVCE/pi-jev-thinking-router/blob/490b8fd962af8507b0ca8e6ae25a2813b6461722/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the extension in Pi per the README; it spawns the daemon on demand.

## Limits and data handling

Prompt summaries go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 490b8fd962af](https://github.com/brzewVCE/pi-jev-thinking-router/tree/490b8fd962af8507b0ca8e6ae25a2813b6461722). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
