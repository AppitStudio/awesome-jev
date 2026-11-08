# inbox-sweep (local Gmail triage in batches with TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Local web app that works through Gmail 10–50 emails at a time: TypeSafe Jev archives clear junk and turns uncertain emails into quick 1/2/3 review cards; nothing is filed until you approve. Includes a no-account fake mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Meerav29/inbox-sweep) |
| Maintainer | [Meerav29](https://github.com/Meerav29). Independently curated. |
| Format | Node.js local web app (MIT) |
| Requirements | Node 22.12+, your own Google OAuth client, and a TypeSafe API key. |
| License | [MIT](https://github.com/Meerav29/inbox-sweep/blob/e518652b5256a2642d1f99a84c018043796da424/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev/client.ts`](https://github.com/Meerav29/inbox-sweep/blob/e518652b5256a2642d1f99a84c018043796da424/server/jev/client.ts) at the pinned commit. |

## When to use

- Get a backlogged Gmail inbox to zero with human approval.
- Review only the emails Jev is unsure about.
- Mismatch: you must create your own Google OAuth client.

## How it works

`server/jev/client.ts` wraps `@typesafe-ai/sdk` `TypeSafeClient`; `server/jev/questions.ts` builds `choice`/`noul` questions per email. Integration evidence: [`server/jev/client.ts`](https://github.com/Meerav29/inbox-sweep/blob/e518652b5256a2642d1f99a84c018043796da424/server/jev/client.ts).

## Get started

Clone, run `npm run dev:fake` to try it, then add Google and TypeSafe keys to `.env` for your real inbox.

```sh
git clone https://github.com/Meerav29/inbox-sweep.git && cd inbox-sweep
export TYPESAFE_API_KEY=...
npm install && npm run dev:fake
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Meerav29/inbox-sweep/blob/e518652b5256a2642d1f99a84c018043796da424/README.md](https://github.com/Meerav29/inbox-sweep/blob/e518652b5256a2642d1f99a84c018043796da424/README.md)

## Limits and data handling

Email content is sent to TypeSafe on your key; it runs on your machine and nothing is hosted.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit e518652b5256](https://github.com/Meerav29/inbox-sweep/tree/e518652b5256a2642d1f99a84c018043796da424). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
