# JevPolicy

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript decision runtime that turns Jev probabilities (via Vercel AI Gateway) into versioned, replayable YAML-policy decisions with audit traces.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sanoy24/jevpolicy) |
| Maintainer | [sanoy24](https://github.com/sanoy24). Independently curated. |
| Format | npm library + CLI |
| Requirements | Node.js 22.18+; Vercel AI Gateway key for live evaluation. |
| License | [Apache-2.0](https://github.com/sanoy24/jevpolicy/blob/79abbbee060eeccf3111dde68a9fb69061b29718/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Approval gates, moderation or routing that need replayable decisions.
- Mismatch: requires Vercel AI Gateway for live calls.

## How it works

Deterministic preconditions run first, Jev answers typed questions, then ordered YAML rules map the signals to a decision plus trace. (Summarized from the upstream [README](https://github.com/sanoy24/jevpolicy/blob/79abbbee060eeccf3111dde68a9fb69061b29718/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `npm install @sanoy24/jevpolicy`, then `npx jevpolicy validate ./policy.yaml`.

## Limits and data handling

State/facts are sent to Jev through Vercel AI Gateway; the host app executes any action. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 79abbbee060e](https://github.com/sanoy24/jevpolicy/tree/79abbbee060eeccf3111dde68a9fb69061b29718). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
