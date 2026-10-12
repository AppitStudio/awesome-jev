# fast-compact

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

`/fc` for Claude Code: TypeSafe Jev picks which old tool outputs are still needed and keeps them whole, other outputs are cut to head/tail with every cut saved to a file; built-in `/compact` stays untouched.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NodarDavituri/fast-compact) |
| Maintainer | [NodarDavituri](https://github.com/NodarDavituri). Independently curated. |
| Format | Claude Code plugin / slash command |
| Requirements | Claude Code; TypeSafe key (falls back to keeping newest outputs without one). |
| License | [MIT](https://github.com/NodarDavituri/fast-compact/blob/e1ab729a1a483819f985927b4006393f22df3dde/LICENSE) |
| Jev evidence | [`src/jev.ts`](https://github.com/NodarDavituri/fast-compact/blob/e1ab729a1a483819f985927b4006393f22df3dde/src/jev.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Shrink bloated tool output in about a second without a lossy LLM summary.
- Mismatch: only trims older long tool outputs; does not summarize conversation text.

## How it works

Ranks older outputs over ~2,000 characters with one Jev request; kept outputs stay verbatim and cut ones keep start/end with full text saved to a file. (Summarized from the upstream [README](https://github.com/NodarDavituri/fast-compact/blob/e1ab729a1a483819f985927b4006393f22df3dde/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the plugin per the README and run `/fc` (or `/fast-compact`).

## Limits and data handling

Tool output excerpts go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e1ab729a1a48](https://github.com/NodarDavituri/fast-compact/tree/e1ab729a1a483819f985927b4006393f22df3dde). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
