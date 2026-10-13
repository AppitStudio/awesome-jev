# PhonePilot

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Android task automation (Chinese docs): Codex plans and reviews, TypeSafe Jev picks the next UI action and target from the accessibility tree, and the Phone Bridge app executes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/afetmin/PhonePilot) |
| Maintainer | [afetmin](https://github.com/afetmin). Independently curated. |
| Format | Python SDK, CLI and MCP server + Android companion app |
| Requirements | Python 3.11 (uv); Android 11+ device with the Phone Bridge APK; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/afetmin/PhonePilot/blob/373c436d913353add5122614493b3fc06f97ce3f/LICENSE) |
| Jev evidence | [`src/phone_use_runner/jev.py`](https://github.com/afetmin/PhonePilot/blob/373c436d913353add5122614493b3fc06f97ce3f/src/phone_use_runner/jev.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let a coding agent drive repetitive Android tasks with fast per-step decisions.
- Mismatch: needs an unlocked device with accessibility enabled; docs are in Chinese.

## How it works

Each round, Jev receives the UI tree, flow and recent actions and selects both operation and target; verifiable completion checks run in code, others are judged by Jev. (Summarized from the upstream [README](https://github.com/afetmin/PhonePilot/blob/373c436d913353add5122614493b3fc06f97ce3f/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `uv sync`, `uv run phone-use doctor`, then `uv run phone-use-mcp`; build/install the Android app from `android/`.

## Limits and data handling

Screen UI text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 373c436d9133](https://github.com/afetmin/PhonePilot/tree/373c436d913353add5122614493b3fc06f97ce3f). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
