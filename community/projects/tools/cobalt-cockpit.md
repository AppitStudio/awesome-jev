# Cobalt Cockpit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: cyberpunk HUD, orchestration telemetry, verification gates and a local Run Ledger, with an optional per-session decision router that can use TypeSafe Jev for advisory routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/echelong/cobalt-cockpit) |
| Maintainer | [echelong](https://github.com/echelong). Independently curated. |
| Format | Claude Code plugin |
| Requirements | Claude Code; TypeSafe key only if you switch a session's router to JEV mode. |
| License | [MIT](https://github.com/echelong/cobalt-cockpit/blob/ae3a17018ca1f668b2d4b2ee82b71b0e5dca19fc/LICENSE) |
| Jev evidence | [`hooks/router.ts`](https://github.com/echelong/cobalt-cockpit/blob/ae3a17018ca1f668b2d4b2ee82b71b0e5dca19fc/hooks/router.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Observe and gate Claude Code orchestration locally, and optionally try Jev routing recommendations per session.
- Mismatch: Jev is optional and advisory (router OFF by default; deterministic rules stay authoritative).

## How it works

Hooks record observed milestones and verification into a local ledger; `/cockpit router jev` starts a decision router that asks Jev for advisory routing in that session only. (Summarized from the upstream [README](https://github.com/echelong/cobalt-cockpit/blob/ae3a17018ca1f668b2d4b2ee82b71b0e5dca19fc/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `claude plugin marketplace add echelong/cobalt-cockpit` then `claude plugin install cobalt-cockpit@cobalt-cockpit`; open `/cockpit`.

## Limits and data handling

No network calls of its own; in JEV router mode, routing context goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit ae3a17018ca1](https://github.com/echelong/cobalt-cockpit/tree/ae3a17018ca1f668b2d4b2ee82b71b0e5dca19fc). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
