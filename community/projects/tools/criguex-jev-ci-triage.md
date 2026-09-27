# jev-ci-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rules-first CI failure triage with Jev for ambiguous Playwright/JUnit failures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/criguex/jev-ci-triage) |
| Maintainer | [criguex](https://github.com/criguex). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI/report generator with GitHub Pages sample. |
| Requirements | Node toolchain; `TYPESAFE_API_KEY` when Jev is consulted. |
| License | [MIT](https://github.com/criguex/jev-ci-triage/blob/42e6f8f907ab8f94a05c5d0cb52ff52f121c9aac/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to sort a red pipeline before humans dig in. Prefer flake quarantine tooling if you need automatic retries.

## How it works

Rules classify clear cases; remaining failures become Choice questions to Jev; outputs labels only. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/criguex/jev-ci-triage.git
cd jev-ci-triage
git checkout 42e6f8f907ab8f94a05c5d0cb52ff52f121c9aac
# follow upstream README; sample report: https://criguex.github.io/jev-ci-triage/
```

Pin revision `42e6f8f907ab8f94a05c5d0cb52ff52f121c9aac` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Does not rerun or skip tests. Sends failure text to TypeSafe when rules cannot decide. Live triage not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 42e6f8f](https://github.com/criguex/jev-ci-triage/tree/42e6f8f907ab8f94a05c5d0cb52ff52f121c9aac). AI-assisted README and LICENSE inspection; install/live paths not executed.
