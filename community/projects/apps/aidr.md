# AI;DR

[All projects](../README.md) · [Web apps](README.md#web-apps)

Ranked daily AI-news site and digest whose importance scoring can use Jev through AnyRouter, with a chat-model rubric as backup.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/duyet/aidr) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://aidr.today) |
| Pricing and access | Hosted site free to read without an account (checked 2026-10-14). Self-hosting incurs your own Cloudflare and AnyRouter/TypeSafe costs. |
| Jev evidence | [`apps/web/worker/importance-rubric.ts`](https://github.com/duyet/aidr/blob/f3c4ac58edff41de58454514919dd144beb4502f/apps/web/worker/importance-rubric.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [duyet](https://github.com/duyet). Independently curated. |
| Format | Hosted web app + Cloudflare Worker source (TypeScript monorepo) |
| Platform and availability | Web (hosted) · Chrome extension · Telegram · RSS |
| Jev's role | Jev is one importance-scoring path for ranking stories; a chat-model rubric is the backup. |
| Requirements | Hosted site needs no account; self-hosting needs Cloudflare, pnpm, and AnyRouter/TypeSafe BYOK configuration. |
| License | No LICENSE file (all rights reserved by default) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Read a ranked AI-news digest (English/Vietnamese) on the web, Telegram, RSS, or Chrome extension.
- Study how a news ranker shares one 1–10 importance scale between Jev and a chat-model rubric.
- Mismatch: the repository has no LICENSE file; reuse terms are not granted.

## How it works

The worker scores story importance on anchored 1–10 bands shared by every scoring path. Configuration tries a decision model first, then Jev (`typesafe/jev` via AnyRouter BYOK), with the chat chain as backup. Code handles ingestion, ranking, translation QA and publishing. Integration evidence: [`apps/web/worker/importance-rubric.ts`](https://github.com/duyet/aidr/blob/f3c4ac58edff41de58454514919dd144beb4502f/apps/web/worker/importance-rubric.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [aidr.today](https://aidr.today) (checked 2026-10-14).
- Importance bands: `apps/web/worker/importance-rubric.ts`.

## Limits and data handling

Hosted reading is free and needs no account (checked 2026-10-14). Self-hosted scoring sends story text to AnyRouter/TypeSafe. Which provider scored a given hosted story is not shown to readers.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit f3c4ac58edff](https://github.com/duyet/aidr/tree/f3c4ac58edff41de58454514919dd144beb4502f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
