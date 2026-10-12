# Callpoint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Inspectable incident decision-support demo: TypeSafe Jev judges typed questions about live incident facts, and deterministic code applies the hard rules ("the model judges, the code decides").

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rcmeadow/callpoint) |
| Maintainer | [rcmeadow](https://github.com/rcmeadow). Independently curated. |
| Format | TypeScript web app |
| Requirements | Node.js; TypeSafe key in `.env` (model pinned to `jev-1.13.0`). |
| License | [MIT](https://github.com/rcmeadow/callpoint/blob/b2054dae0e95cb90dc8f0687d12c596f5d1f5450/LICENSE) |
| Jev evidence | [`src/server/jev.ts`](https://github.com/rcmeadow/callpoint/blob/b2054dae0e95cb90dc8f0687d12c596f5d1f5450/src/server/jev.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- See a transparent pattern for keeping a model's judgments separate from decision rules.
- Mismatch: demo, not an incident-management product.

## How it works

Each new fact re-asks every question in one Jev request; the server holds all TypeSafe calls and the rules map probabilities to actions. (Summarized from the upstream [README](https://github.com/rcmeadow/callpoint/blob/b2054dae0e95cb90dc8f0687d12c596f5d1f5450/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): copy `.env.example`, set the key, and run the dev server per the README.

## Limits and data handling

Incident facts you type go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b2054dae0e95](https://github.com/rcmeadow/callpoint/tree/b2054dae0e95cb90dc8f0687d12c596f5d1f5450). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
