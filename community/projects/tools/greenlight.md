# Greenlight (Pi risky-command checks by Jev, escalated to the orchestrator agent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that builds on the listed pi-jev: Jev checks each risky command in about a third of a second, and a flagged command is paused and sent up the chain to the orchestrating agent (Traycer, a parent Pi or any A2A orchestrator) to approve, deny or ask a human; warn-only by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KHAEntertainment/greenlight) |
| Maintainer | [KHAEntertainment](https://github.com/KHAEntertainment). Independently curated. |
| Format | Pi extension (TypeScript, npm) |
| Requirements | Pi coding agent; a TypeSafe key (`/login typesafe` or `TYPESAFE_API_KEY`) or Jev through OpenRouter, Cloudflare, Vercel or OpenCode. |
| License | [MIT](https://github.com/KHAEntertainment/greenlight/blob/a6dda67448f7393c3e26877d532d4d23e42d2fdb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classifier.ts`](https://github.com/KHAEntertainment/greenlight/blob/a6dda67448f7393c3e26877d532d4d23e42d2fdb/src/classifier.ts) at the pinned commit. |

## When to use

- Run Pi helpers under an orchestrator and have flagged commands answered by the agent that knows the plan.
- Keep pi-jev-style risky-command and password-leak warnings while you step away.
- Mismatch: starts in warn-only mode; it never blocks the agent if the check itself fails.

## How it works

`src/classifier.ts` defaults to `typesafe/jev-latest` and splits the provider from the model id so the same check can run through TypeSafe or a gateway; flagged commands go to the orchestrator over the supported channels, with a timeout that falls back to asking you. Integration evidence: [`src/classifier.ts`](https://github.com/KHAEntertainment/greenlight/blob/a6dda67448f7393c3e26877d532d4d23e42d2fdb/src/classifier.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:@khaentertainment/pi-greenlight
# then in Pi: /login typesafe   (or set TYPESAFE_API_KEY)
# /greenlight log shows what it caught
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KHAEntertainment/greenlight#readme](https://github.com/KHAEntertainment/greenlight#readme)
- Upstream pi-jev: [github.com/y0usaf/pi-jev](https://github.com/y0usaf/pi-jev)

## Limits and data handling

Command text goes to the Jev provider you choose, and flagged commands go to your orchestrator. Warn-only by default; enable pausing deliberately.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit a6dda67448f7](https://github.com/KHAEntertainment/greenlight/tree/a6dda67448f7393c3e26877d532d4d23e42d2fdb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
