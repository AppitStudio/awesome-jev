# jev-test-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Mutation-test triage: Jev helps rank which surviving mutants deserve a new test.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cdubiel08/jev-test-triage) |
| Maintainer | [cdubiel08](https://github.com/cdubiel08). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI with Python mutator and Stryker JSON ingest. |
| Requirements | Python; `uv tool install`; `TYPESAFE_API_KEY`; optional Stryker for JS/TS. |
| License | [MIT](https://github.com/cdubiel08/jev-test-triage/blob/a71a46bbe36ec9cfb178bab6fa449c2d47d24486/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use after mutation testing when you need to prioritize real test gaps over equivalent mutants.

## How it works

Code prefilters survivors; one request asks ~12 narrow Jev questions; composite score in code routes act/review/ignore. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
uv tool install git+https://github.com/cdubiel08/jev-test-triage
export TYPESAFE_API_KEY=…
jtt mutate-py --module src/pkg/pricing.py --cmd \"pytest -x -q tests/test_pricing.py\" --out mutants.jsonl
jtt triage mutants.jsonl
```

Pin revision `a71a46bbe36ec9cfb178bab6fa449c2d47d24486` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live mutation/Jev paths not run on the review host. Reported metrics are upstream claims.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit a71a46b](https://github.com/cdubiel08/jev-test-triage/tree/a71a46bbe36ec9cfb178bab6fa449c2d47d24486). AI-assisted README and LICENSE inspection; install/live paths not executed.
