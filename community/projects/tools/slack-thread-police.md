# Slack Thread Police (self-hosted Slack bot that uses Jev to nudge people to reply in threads)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Free, self-hosted Slack bot: when a top-level message looks like it belongs in the thread of a recent message, it sends the poster a private nudge. The decision goes to TypeSafe's hosted Jev by default, or to a decision model you host yourself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seanparkross/slack-thread-police) |
| Maintainer | [seanparkross](https://github.com/seanparkross). Independently curated. |
| Format | TypeScript Slack bot (pnpm) |
| Requirements | Node.js and pnpm, a Slack app, and a TypeSafe API key (or a self-hosted decision model). |
| License | [MIT](https://github.com/seanparkross/slack-thread-police/blob/371729cceafa3f01c25cbeedb0d964efb8e32e83/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision.ts`](https://github.com/seanparkross/slack-thread-police/blob/371729cceafa3f01c25cbeedb0d964efb8e32e83/src/decision.ts) at the pinned commit. |

## When to use

- Keep busy Slack channels threaded without manual moderation.
- Mismatch: needs a Slack app with message access.

## How it works

`src/decision.ts` uses `@typesafe-ai/sdk` to ask whether the new message is a reply to one in the recent window; `src/detector.ts` turns the answer into a private nudge. Integration evidence: [`src/decision.ts`](https://github.com/seanparkross/slack-thread-police/blob/371729cceafa3f01c25cbeedb0d964efb8e32e83/src/decision.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see the README for Slack app setup, then add TYPESAFE_API_KEY to .env and start the bot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/seanparkross/slack-thread-police#readme](https://github.com/seanparkross/slack-thread-police#readme)

## Limits and data handling

New messages and the recent channel window are sent to TypeSafe (unless self-hosted). Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 371729cceafa](https://github.com/seanparkross/slack-thread-police/tree/371729cceafa3f01c25cbeedb0d964efb8e32e83). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
