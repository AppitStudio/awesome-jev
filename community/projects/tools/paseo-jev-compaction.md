# paseo-jev-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Separate Paseo provider for Codex that tries Jev history compaction first on manual and context-limit compaction, falling back to Codex when Jev fails or saves too few tokens, while the standard Codex provider stays available.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hakilee/paseo-jev-compaction) |
| Maintainer | [hakilee](https://github.com/hakilee). Independently curated. |
| Format | Paseo provider wrapper + pinned patched engine |
| Requirements | macOS, Node.js 22+, Python 3.11+, Git, Rust 1.95.0; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/hakilee/paseo-jev-compaction/blob/3450cd8981a991009d673896ddb17fdb6184ab4b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Use Jev to drop stale file-read and search results from long Codex sessions in Paseo.
- Mismatch: macOS and Paseo only; some models (per README) are not supported by the pinned engine.

## How it works

Jev decides which complete, older read/grep/list tool results can be removed; the wrapper verifies source revision and binary hashes before launch. (Summarized from the upstream [README](https://github.com/hakilee/paseo-jev-compaction/blob/3450cd8981a991009d673896ddb17fdb6184ab4b/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Build per the README, run `node bin/paseo-jev-compaction.mjs provider-config`, and add `agents.providers.codex-jev` to your Paseo config.

## Limits and data handling

Session history is sent to TypeSafe for compaction decisions; the key is kept in the engine environment only. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 3450cd8981a9](https://github.com/hakilee/paseo-jev-compaction/tree/3450cd8981a991009d673896ddb17fdb6184ab4b). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
