# wporg-forum-triage by Hamza Ahmad Aslam (CLI where Jev sorts a plugin's WordPress.org support threads and finds the unanswered ones)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Reads a plugin's public WordPress.org support forum feed, has Jev sort each thread into bug, how-to, feature request, conflict with another plugin, praise or spam, and lists the threads still waiting for a reply. Threads it cannot place confidently go to a review list. Exit code 1 when something is unanswered, so it can run on a schedule.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/wporg-forum-triage) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam) (hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm `@hamzaahmadaslam/wporg-forum-triage`, no dependencies) |
| Requirements | Node 20+ and a TypeSafe key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/wporg-forum-triage/blob/cc6cc69d7a27f71ee5341f44fc4e78e1d35d5b79/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/wporg-forum-triage/blob/cc6cc69d7a27f71ee5341f44fc4e78e1d35d5b79/src/jev.mjs) at the pinned commit. |

## When to use

- WordPress plugin authors who answer their own support forum and want the unanswered bug reports first.
- Mismatch: private helpdesks; it reads only the public WordPress.org feeds.

## How it works

`src/jev.mjs` posts batches of up to five threads (title and first post only) to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) with a `choice` for the thread kind and `noul` questions for whether it needs a reply and whether the poster says it is solved; 429 and 529 responses are retried. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/wporg-forum-triage/blob/cc6cc69d7a27f71ee5341f44fc4e78e1d35d5b79/src/jev.mjs).

## Get started

Install from npm and point it at a plugin slug.

```sh
npm install -g @hamzaahmadaslam/wporg-forum-triage
wporg-forum-triage hello-dolly --dry-run
export TYPESAFE_API_KEY=...
wporg-forum-triage hello-dolly --unresolved
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example report: [github.com/hamzaahmadaslam/wporg-forum-triage#example](https://github.com/hamzaahmadaslam/wporg-forum-triage#example)

## Limits and data handling

Thread titles and first posts from the public forum go to TypeSafe. It reads at most the first feed page or two (WordPress.org returned the first page again for `?paged=2` when tested by the author). The bundled example uses hand-written answers, not recorded Jev output.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit cc6cc69d7a27](https://github.com/hamzaahmadaslam/wporg-forum-triage/tree/cc6cc69d7a27f71ee5341f44fc4e78e1d35d5b79). Inspected the README, LICENSE, `src/jev.mjs` and `src/triage.mjs` at the pinned commit and confirmed `@hamzaahmadaslam/wporg-forum-triage` 1.0.0 on npm; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
