# contextleleo

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Carry a coding agent's session to the next agent (Claude Code → Antigravity and others) trimmed to what the next task needs: TypeSafe Jev scores what matters, rules shrink the rest, originals stay untouched. Built on Skillsync's txcript.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Adityakk9031/contextleleo) |
| Maintainer | [Adityakk9031](https://github.com/Adityakk9031). Independently curated. |
| Format | Rust CLI |
| Requirements | Rust toolchain; TypeSafe key for Jev scoring. |
| License | [Apache-2.0](https://github.com/Adityakk9031/contextleleo/blob/b6e169420cf1d5a8d8cf3be908f52f32aaea8a89/LICENSE) |
| Jev evidence | [`src/jev.rs`](https://github.com/Adityakk9031/contextleleo/blob/b6e169420cf1d5a8d8cf3be908f52f32aaea8a89/src/jev.rs) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Switch agents mid-task without dragging the full transcript, with Jev yes/no search and relevance scoring.
- Mismatch: if you only need format conversion, upstream txcript is simpler.

## How it works

Reads agent session formats (txcript), asks Jev to score turns/items for the next task, applies shrink rules, and writes a traceable trimmed handoff. (Summarized from the upstream [README](https://github.com/Adityakk9031/contextleleo/blob/b6e169420cf1d5a8d8cf3be908f52f32aaea8a89/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): clone and build with Cargo per the README.

## Limits and data handling

Session excerpts go to TypeSafe for scoring. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b6e169420cf1](https://github.com/Adityakk9031/contextleleo/tree/b6e169420cf1d5a8d8cf3be908f52f32aaea8a89). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
