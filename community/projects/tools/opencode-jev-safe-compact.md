# opencode-jev-safe-compact (Jev-guided compaction for OpenCode)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin whose `/jev-compact` command prunes a session's tool history with a decision model instead of an LLM summary: needed tool calls stay verbatim, stale outputs are shortened with a re-run marker, and the keep cut-off adapts because Jev's noul calibration drifts with state shape.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lewistouchtech/opencode-jev-safe-compact) |
| Maintainer | [lewistouchtech](https://github.com/lewistouchtech). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode with the V2 plugin API; any System One endpoint (TypeSafe, self-hosted or OpenCode Zen); `TYPESAFE_API_KEY` for the hosted API. |
| License | [MIT](https://github.com/lewistouchtech/opencode-jev-safe-compact/blob/3c428b9ee13386d456e37baf1bdb4770d310d830/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/lewistouchtech/opencode-jev-safe-compact/blob/3c428b9ee13386d456e37baf1bdb4770d310d830/src/jev.ts) at the pinned commit. |

## When to use

- Shrink long OpenCode sessions without losing the record of what was run.
- Use a local decision model for compaction at no API cost.
- Mismatch: only acts when you run `/jev-compact`; native `/compact` is untouched.

## How it works

`src/jev.ts` sends each tool output with the session goal to the configured endpoint (`jev-latest` by default) for a noul keep score; outputs are ranked and the lowest are shortened or, below `dropFloor`, removed. Integration evidence: [`src/jev.ts`](https://github.com/lewistouchtech/opencode-jev-safe-compact/blob/3c428b9ee13386d456e37baf1bdb4770d310d830/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
// opencode.json
{ "plugins": [ { "package": "github:lewistouchtech/opencode-jev-safe-compact" } ] }
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Options table and findings in the README: [github.com/lewistouchtech/opencode-jev-safe-compact#readme](https://github.com/lewistouchtech/opencode-jev-safe-compact#readme)
- Inspired by: [github.com/tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)

## Limits and data handling

Tool outputs are sent to whichever decision endpoint you configure. Calibration findings are the author's.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 3c428b9ee133](https://github.com/lewistouchtech/opencode-jev-safe-compact/tree/3c428b9ee13386d456e37baf1bdb4770d310d830). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
