# vulnwash (Snyk Labs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Snyk Labs triage harness that runs every Snyk CLI finding — SCA (`snyk test`) and SAST (`snyk code test`) — through TypeSafe Jev for contextual, tunable prioritization of dependency vulnerabilities and true-positive filtering of code findings, without touching Snyk's detection; cached and re-triageable at a new confidence bar with no new calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snyk-labs/vulnwash-cli) |
| Maintainer | [Snyk Labs](https://github.com/snyk-labs). Independently curated. |
| Format | Node/TypeScript CLI (pnpm) with live terminal dashboard or `--plain` report |
| Requirements | Node.js with pnpm, the Snyk CLI with a Snyk account able to scan the target, and a `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut the list of Snyk findings to the ones worth fixing first in a given project context.
- Re-triage cached results at a different `--min-confidence` without re-calling Jev.
- Mismatch: requires Snyk; it reclassifies Snyk output and does not detect anything itself.

## How it works

[`src/sca.ts`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/src/sca.ts) and [`src/sast.ts`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/src/sast.ts) run or replay Snyk output; [`src/jev-client.ts`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/src/jev-client.ts) classifies each finding; results cache in `data/cache/` by finding id. The exact instructions given to Jev per label are in [`docs/jev-integration.md`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/docs/jev-integration.md); full write-up in [`docs/README.md`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/docs/README.md).

## Get started

Quickstart (README):

```sh
git clone https://github.com/snyk-labs/vulnwash-cli.git && cd vulnwash-cli
pnpm install
cp .env.schema .env    # set TYPESAFE_API_KEY
pnpm sca ../nodejs-goof
pnpm sast ../nodejs-goof
```

Each uncached finding is classified by Jev on your TypeSafe key; Snyk usage follows your Snyk plan.

## Examples and demos

- README demo video and [`docs/demo.md`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/docs/demo.md).
- Spec: [`docs/spec.md`](https://github.com/snyk-labs/vulnwash-cli/blob/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18/docs/spec.md) (confidence is a dial, not a verdict).

## Limits and data handling

Finding details (and code context for SAST) go to TypeSafe. Vendor-lab project; AppitStudio has no affiliation with Snyk. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit efbf69fcc5a5](https://github.com/snyk-labs/vulnwash-cli/tree/efbf69fcc5a5bbc8a6439a9e9bcb7efcd4e7ce18). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
