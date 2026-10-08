# pi-watcher

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that watches long-running builds, tests, training jobs, CI and deadlines from durable evidence and keeps the session quiet until a fact needs a decision; optionally, TypeSafe Jev answers six bounded questions about a sanitized evidence window (progress, blocker, needs a decision, repeating, claim vs evidence, enough context) that can raise or annotate an episode but never override hard facts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Maolon/pi-watcher) |
| Maintainer | [Maolon](https://github.com/Maolon). Independently curated. |
| Format | Pi extension (`pi install npm:@maolon/pi-watcher`), recommended with `@maolon/pi-relay` |
| Requirements | Pi with `/login` → TypeSafe credentials for the optional Jev review (off by default). |
| License | [MIT](https://github.com/Maolon/pi-watcher/blob/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Stop an agent from polling `sleep` loops on long tasks.
- Catch a stalled run, a repeating fix loop or a log that claims success while showing errors.
- Mismatch: Jev is optional; without it only code-level facts (exit markers, deadlines, silence) trigger wakes.

## How it works

Code decides terminal states, exit markers, deadlines and silence; [`src/jev/questions.ts`](https://github.com/Maolon/pi-watcher/blob/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7/src/jev/questions.ts) defines the six questions, [`src/jev/sanitizer.ts`](https://github.com/Maolon/pi-watcher/blob/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7/src/jev/sanitizer.ts) redacts the evidence window and [`src/jev/consent.ts`](https://github.com/Maolon/pi-watcher/blob/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7/src/jev/consent.ts) gates sending it; [`src/jev/client.ts`](https://github.com/Maolon/pi-watcher/blob/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7/src/jev/client.ts) uses Pi's registered TypeSafe credentials.

## Get started

Install both packages in Pi (README):

```sh
pi install npm:@maolon/pi-relay      # wake transport (recommended)
pi install npm:@maolon/pi-watcher
```

With semantic review on, each check is a Jev request billed to your TypeSafe account.

## Examples and demos

- npm packages: [`@maolon/pi-watcher`](https://www.npmjs.com/package/@maolon/pi-watcher) (0.1.3) and [`@maolon/pi-relay`](https://www.npmjs.com/package/@maolon/pi-relay) (0.2.1).
- README *Usage* and *Semantic review (Jev, optional)*.

## Limits and data handling

Only a sanitized evidence window goes to TypeSafe, and only after consent when review is enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit ccbfe5be6d85](https://github.com/Maolon/pi-watcher/tree/ccbfe5be6d859b6cf02b0b1168ecb2f49f06c3f7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
