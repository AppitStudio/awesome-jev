# Kassad

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

.NET LLM guardrails: TypeSafe Jev typed checks return Allow/Flag/Review/Block with calibrated confidence (ASP.NET middleware).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jacob-berendsohn/kassad) |
| Maintainer | [jacob-berendsohn](https://github.com/jacob-berendsohn). Independently curated. |
| Format | C# · .NET guardrails library (Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/jacob-berendsohn/kassad/blob/39b68901ca0565443337174354c58d8ef37250cc/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Early 0.1.0 release; middleware/handler maturity per upstream README. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/jacob-berendsohn/kassad.git
cd kassad
git checkout 39b68901ca0565443337174354c58d8ef37250cc
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 39b68901ca05](https://github.com/jacob-berendsohn/kassad/tree/39b68901ca0565443337174354c58d8ef37250cc). AI-assisted README and license inspection; install/live paths not executed.
