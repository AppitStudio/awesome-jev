# opencode-history (searchable OpenCode session history with an optional Jev recall judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that makes earlier sessions searchable from OpenCode's own database (SQLite FTS5 over prompts, replies and compaction summaries), adds a frozen recent-work block to each session, and optionally asks Jev before each message which earlier passages would actually help, adding up to three of them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/StevenJPx2/opencode-history) |
| Maintainer | [StevenJPx2](https://github.com/StevenJPx2). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode; a TypeSafe API key only for the optional per-turn recall judge. |
| License | [MIT](https://github.com/StevenJPx2/opencode-history/blob/67b228a25857b3f38be7e71412eeaf292ba548c7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/recall.ts`](https://github.com/StevenJPx2/opencode-history/blob/67b228a25857b3f38be7e71412eeaf292ba548c7/src/recall.ts) at the pinned commit. |

## When to use

- Find what you or the agent said in an earlier OpenCode session.
- Bring relevant past work into a new turn without a separate memory store.
- Mismatch: without a key, search and the recent-work block still work and recall is off.

## How it works

`src/recall.ts` sends the new message and up to eight candidate passages to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`, configurable with `TYPESAFE_BASE_URL` and `TYPESAFE_DEFAULT_MODEL`) and admits only the passages Jev accepts. Integration evidence: [`src/recall.ts`](https://github.com/StevenJPx2/opencode-history/blob/67b228a25857b3f38be7e71412eeaf292ba548c7/src/recall.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# add the plugin to your OpenCode config as described in the README
export TYPESAFE_API_KEY=...   # optional, enables recall
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/StevenJPx2/opencode-history#readme](https://github.com/StevenJPx2/opencode-history#readme)

## Limits and data handling

OpenCode's database is opened read-only; a derived index stays on your machine. With recall on, your message and candidate passages go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 67b228a25857](https://github.com/StevenJPx2/opencode-history/tree/67b228a25857b3f38be7e71412eeaf292ba548c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
