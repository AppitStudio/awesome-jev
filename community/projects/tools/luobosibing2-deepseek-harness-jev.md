# deepseek-harness-jev (luobosibing2)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Native DeepSeek Harness plugin integrating TypeSafe Jev as a System One decision layer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luobosibing2/deepseek-harness-jev) |
| Maintainer | [luobosibing2](https://github.com/luobosibing2). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | DeepSeek Harness (DSH) Cordis plugin. |
| Requirements | DeepSeek Harness (~0.1.7-rc.2 tested upstream); TypeSafe credentials via plugin settings. |
| License | [MIT](https://github.com/luobosibing2/deepseek-harness-jev/blob/59f9edf5decea41f6bbbe76a58e936178af46cd4/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from wjw66/deepseek-harness-jev-pre-compaction. |

## When to use

Use when DeepSeek Harness should optionally consult TypeSafe Jev at selection/supervision/approval points.

## How it works

Eleven independently disabled features invoke Jev at DSH extension points for ranking, supervision, corrections, and approvals while the main model keeps planning/tools. Distinct from wjw66/deepseek-harness-jev-pre-compaction. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/luobosibing2/deepseek-harness-jev.git
cd deepseek-harness-jev
git checkout 59f9edf5decea41f6bbbe76a58e936178af46cd4
# follow upstream README for DSH plugin install; enable features intentionally
```

Pin revision `59f9edf5decea41f6bbbe76a58e936178af46cd4` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Early-stage; features off by default. Live DSH/Jev paths not run on the review host. Distinct from wjw66/deepseek-harness-jev-pre-compaction.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 59f9edf](https://github.com/luobosibing2/deepseek-harness-jev/tree/59f9edf5decea41f6bbbe76a58e936178af46cd4). AI-assisted README and LICENSE inspection; install/live paths not executed.
