# pi-session-name by akirousnow (pi coding-agent extension where Jev decides when a session title has gone stale)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small extension for the pi coding agent. Instead of renaming a session every few turns, at the start of a user turn it asks Jev whether the main topic has changed enough that the current title is misleading; at or above a threshold it writes a new title with the session's model, otherwise it does nothing. Titles set by hand always win, the first title comes from the first prompt without Jev, and the work never delays the agent's first token.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akirousnow/pi-session-name) |
| Maintainer | [akirousnow](https://github.com/akirousnow). Independently curated. |
| Format | pi extension (TypeScript) |
| Requirements | pi 1.4+ and a TypeSafe key for `typesafe/jev-latest` (or another configured classifier model) in `TYPESAFE_API_KEY` or pi's auth store. |
| License | [MIT](https://github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/session-name/classifier.ts`](https://github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/extensions/session-name/classifier.ts) at the pinned commit. |

## When to use

- Keep pi session titles accurate as a conversation drifts, without renaming on a fixed schedule.
- Mismatch: other coding agents; it uses pi's extension and classifier APIs.

## How it works

`extensions/session-name/classifier.ts` runs the stale-title question through pi's classifier registry, preferring `typesafe/jev-latest` (default in `extensions/session-name/config.ts`) and reading the yes probability against `autoThreshold`. Integration evidence: [`extensions/session-name/classifier.ts`](https://github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/extensions/session-name/classifier.ts).

## Get started

Install it with pi, add your TypeSafe key, and tune `sessionName` in pi's settings.

```sh
pi install git:github.com/akirousnow/pi-session-name
export TYPESAFE_API_KEY=...
pi
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/README.md](https://github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/README.md)
- Changelog: [github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/CHANGELOG.md](https://github.com/akirousnow/pi-session-name/blob/cebfe2a57423aed11c83070444b7dccfe43e5a57/CHANGELOG.md)

## Limits and data handling

Recent turn text and the current title are sent to TypeSafe on each check (rate-limited by `minTurnsBetweenChecks`); new titles are written by the session's own model.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit cebfe2a57423](https://github.com/akirousnow/pi-session-name/tree/cebfe2a57423aed11c83070444b7dccfe43e5a57). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
