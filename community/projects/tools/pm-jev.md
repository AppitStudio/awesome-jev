# pm-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

pm-cli extension and library for typed, local-first System One decisions about project items, built on the official TypeSafe JavaScript SDK. Defaults to local Ollama with `tev1:4b`; code keeps ranking, thresholds, retries, and history. The README calls it an unpublished v0 development slice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/unbraind/pm-jev) |
| Maintainer | [unbraind](https://github.com/unbraind). Independently curated. |
| Format | pm-cli extension + npm/Bun library |
| Requirements | Node 22.18+ (or Bun), pm-cli 2026.10.5+, Ollama with a decision-capable model and `/v1/systemone` API; hosted TypeSafe optional. |
| License | [MIT](https://github.com/unbraind/pm-jev/blob/0f0c0cb7eff8e722d88acaa29046908da7b3427c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Ask typed questions about pm-cli items (choices, scores) without leaving the CLI.
- Mismatch: not yet published; install is from a local build.

## How it works

Supplies item state to System One typed questions through the TypeSafe JS SDK and keeps authorization and arithmetic in code. (Summarized from the upstream [README](https://github.com/unbraind/pm-jev/blob/0f0c0cb7eff8e722d88acaa29046908da7b3427c/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Build locally, `npm pack`, install into a pm project, then `pm jev doctor`.

## Limits and data handling

Local-first by default (Ollama); hosted TypeSafe only if configured. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 0f0c0cb7eff8](https://github.com/unbraind/pm-jev/tree/0f0c0cb7eff8e722d88acaa29046908da7b3427c). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
