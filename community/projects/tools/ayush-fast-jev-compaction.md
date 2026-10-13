# fast-jev-compaction (Ayush)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that replaces compaction summaries with Jev decisions over tool calls and results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AyushChauhan9389/fast-jev-compaction) |
| Maintainer | [AyushChauhan9389](https://github.com/AyushChauhan9389). Independently curated. |
| Format | Claude Code plugin |
| Requirements | Claude Code; TypeSafe API key. |
| License | [MIT](https://github.com/AyushChauhan9389/fast-jev-compaction/blob/ac0cc4df43497ea2f49d7cb7bf9cd0bdca1561ab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`hooks/fast-jev.ts`](https://github.com/AyushChauhan9389/fast-jev-compaction/blob/ac0cc4df43497ea2f49d7cb7bf9cd0bdca1561ab/hooks/fast-jev.ts) at the pinned commit. |

## When to use

- Use when you need: Claude Code plugin that replaces compaction summaries with Jev decisions over to…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `hooks/fast-jev.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: hooks/fast-jev.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit ac0cc4df4349](https://github.com/AyushChauhan9389/fast-jev-compaction/tree/ac0cc4df43497ea2f49d7cb7bf9cd0bdca1561ab). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
