# Jev Fraud Shield

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted, explainable card-fraud triage using per-factor Jev judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jonny5isalive5/jev-fraud-shield) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/jonny5isalive5/jev-fraud-shield#readme) |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-27**. Live triage needs a TypeSafe key; usage separate. |
| Jev evidence | README and library describe per-factor TypeSafe Jev API calls for triage ([README](https://github.com/jonny5isalive5/jev-fraud-shield/blob/eeb4fc6ebb8435fcfda87b3544fd1f41c6c55e7f/README.md)). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |
| Maintainer | [jonny5isalive5](https://github.com/jonny5isalive5). Independently curated. |
| Format | Python library + static dashboard from a recorded run. |
| Platform and availability | Self-hosted source library + static `dashboard.html` sample. Early research demo. |
| Jev's role | Scores/triages individual fraud factors with typed questions; code aggregates policy. |
| Requirements | Python; `TYPESAFE_API_KEY` for live triage. |
| License | [MIT](https://github.com/jonny5isalive5/jev-fraud-shield/blob/eeb4fc6ebb8435fcfda87b3544fd1f41c6c55e7f/LICENSE). |

## When to use

Use to explore explainable Jev-based fraud feature decomposition. Prefer certified vendor systems for production card decisions.

## How it works

Decomposes fraud signals into typed Jev questions rather than one opaque score; application code owns approve/decline policy.

## Get started

```sh
git clone https://github.com/jonny5isalive5/jev-fraud-shield.git
cd jev-fraud-shield
git checkout eeb4fc6ebb8435fcfda87b3544fd1f41c6c55e7f
# open dashboard.html; follow README for live runs with TYPESAFE_API_KEY
```

Pin revision `eeb4fc6ebb8435fcfda87b3544fd1f41c6c55e7f` when reproducing this review.

## Examples and demos

Open committed `dashboard.html` from a recorded 60-transaction run. Live API not executed on the review host.

## Limits and data handling

Sends transaction details to TypeSafe's hosted API. README documents earlier flawed versions—treat claims carefully. Not a production fraud engine certification. Live API not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit eeb4fc6](https://github.com/jonny5isalive5/jev-fraud-shield/tree/eeb4fc6ebb8435fcfda87b3544fd1f41c6c55e7f). AI-assisted README and LICENSE inspection; live paths not executed.
