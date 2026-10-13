# jev-workflow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Decision contracts, adversarial testing, tracing, stability, and privacy controls for TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-workflow) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | TypeScript toolkit |
| Requirements | Node; TypeSafe API key for live Jev paths (RiskCard demo can run offline). |
| License | [MIT](https://github.com/gbesse/jev-workflow/blob/2133f0c717d97a560534b07153e1cf0a56d547f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/riskcard.ts`](https://github.com/gbesse/jev-workflow/blob/2133f0c717d97a560534b07153e1cf0a56d547f5/src/riskcard.ts) at the pinned commit. |

## When to use

- Use when you need: Decision contracts, adversarial testing, tracing, stability, and privacy control…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/riskcard.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/riskcard.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 2133f0c717d9](https://github.com/gbesse/jev-workflow/tree/2133f0c717d97a560534b07153e1cf0a56d547f5). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
