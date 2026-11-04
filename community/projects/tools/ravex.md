# Ravex (plug-and-play Socket.IO chat engine for Node.js with optional Jev message moderation)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Typed, real-time chat engine with presence, typing indicators, read receipts, reactions and rate limiting, in `@ravex/server` and `@ravex/client` packages. An optional `moderation` setting screens every sent or edited message with Jev before anyone sees it: one request asks whether the text is abusive (blocked at 0.7 by default) and whether it tries to manipulate the checker. It is off by default, the failure mode (deliver or reject when Jev is unreachable) is configurable, and Jev sees only the message text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ravex-io/ravex) |
| Maintainer | [ravex-io](https://github.com/ravex-io). Independently curated. |
| Format | TypeScript pnpm monorepo (Node.js server package and browser client package) |
| Requirements | Node.js and pnpm; a `TYPESAFE_API_KEY` only if you turn moderation on. |
| License | [MIT](https://github.com/ravex-io/ravex/blob/0a937b4cc1f70f90796df5a4ec0048068138d8fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/gs_rumana/status/2117757832363974995)). |
| Jev evidence | [`packages/server/src/middleware/JevClient.ts`](https://github.com/ravex-io/ravex/blob/0a937b4cc1f70f90796df5a4ec0048068138d8fc/packages/server/src/middleware/JevClient.ts) at the pinned commit. |

## When to use

- Add pre-delivery abuse and prompt-injection screening to a chat backend, with a threshold you set and an `onFlagged` hook for strikes or kicks.
- Mismatch: moderation is one optional feature of a general chat engine, the packages are at version 0.2.0, and every screened message is a billed Jev request.

## How it works

`JevClient.ts` posts the normalised message text to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0` pinned by default) with two yes/no questions; code turns the probabilities into a block, with `failMode` `open` (default) or `closed` for timeouts and errors. Integration evidence: [`packages/server/src/middleware/JevClient.ts`](https://github.com/ravex-io/ravex/blob/0a937b4cc1f70f90796df5a4ec0048068138d8fc/packages/server/src/middleware/JevClient.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see packages/server/README.md, section Moderation (Jev)
# new ChatEngine(httpServer, { authenticate, moderation: { apiKey: process.env.TYPESAFE_API_KEY } })
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Moderation options, blocked-message behaviour and failure modes: [github.com/ravex-io/ravex/blob/0a937b4cc1f70f90796df5a4ec0048068138d8fc/packages/server/README.md](https://github.com/ravex-io/ravex/blob/0a937b4cc1f70f90796df5a4ec0048068138d8fc/packages/server/README.md)
- Announcement post on X: [x.com/gs_rumana/status/2117757832363974995](https://x.com/gs_rumana/status/2117757832363974995)

## Limits and data handling

With a key, message text (after your middleware runs) goes to TypeSafe on your key; attachments, names, ids and room data do not. With the default `failMode: open`, a Jev outage lets messages through unscreened. Moderation tests use a fake Jev; no live scoring accuracy is published. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 0a937b4cc1f7](https://github.com/ravex-io/ravex/tree/0a937b4cc1f70f90796df5a4ec0048068138d8fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
