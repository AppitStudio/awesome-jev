# ci-triage (samiulhuda360)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that reads a failed CI run, uses TypeSafe Jev to decide flaky vs infrastructure vs real failure, re-runs the first two once, and leaves one short PR comment for real failures. Distinct from criguex/jev-ci-triage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samiulhuda360/ci-triage) |
| Maintainer | [samiulhuda360](https://github.com/samiulhuda360). Independently curated. |
| Format | Python · GitHub Action |
| Requirements | GitHub Actions; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/samiulhuda360/ci-triage/blob/bb7d13172cf7ddb1ce8079c78f4dbfd11fcae34f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Noisy CI where flaky/infra noise buries real regressions.
- Mismatch: Still needs human follow-up for real failures.

## How it works

Log excerpts go to Jev for typed classification; code re-runs or comments accordingly. Backend: [`ci_triage/backends/jev.py`](https://github.com/samiulhuda360/ci-triage/blob/bb7d13172cf7ddb1ce8079c78f4dbfd11fcae34f/ci_triage/backends/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
Uses: samiulhuda360/ci-triage@main
# secrets + workflow per upstream README
```

## Limits and data handling

CI log slices are sent to TypeSafe; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit bb7d13172cf7](https://github.com/samiulhuda360/ci-triage/tree/bb7d13172cf7ddb1ce8079c78f4dbfd11fcae34f). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
