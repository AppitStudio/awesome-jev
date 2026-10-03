# jev-pr-quality

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action workflow for TypeSafe Jev-assisted PR quality reviews plus a multi-repo RawTree dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rawtreedb/jev-pr-quality) |
| Maintainer | [rawtreedb](https://github.com/rawtreedb). Independently curated. |
| Format | GitHub Action + dashboard (Apache-2.0) |
| Requirements | See upstream README; provider keys when using live hosted paths. |
| License | [`Apache-2.0`](https://github.com/rawtreedb/jev-pr-quality/blob/c0a8d27cb61d183146e7e79534019a787d3498c5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

GitHub Action workflow for TypeSafe Jev-assisted PR quality reviews plus a multi-repo RawTree dashboard. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/rawtreedb/jev-pr-quality.git
cd jev-pr-quality
git checkout c0a8d27cb61d183146e7e79534019a787d3498c5
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: Jev review workflow; JEV_API_KEY; dashboard at jev-pr-quality.rawtree.tech. ([upstream evidence](https://github.com/rawtreedb/jev-pr-quality/blob/c0a8d27cb61d183146e7e79534019a787d3498c5/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit c0a8d27cb61d](https://github.com/rawtreedb/jev-pr-quality/tree/c0a8d27cb61d183146e7e79534019a787d3498c5). AI-assisted README and license inspection; install/live paths not executed.
