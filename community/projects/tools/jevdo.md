# JevDo

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-first DeepSeek Harness agent loop that reuses validated Actions before calling a frontier model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yinhong-zhou/jevdo) |
| Maintainer | [yinhong-zhou](https://github.com/yinhong-zhou). Independently curated. |
| Format | TypeScript · DeepSeek Harness agent loop (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/yinhong-zhou/jevdo/blob/0a2e116b5737449f141ad2a03b83ff792092b4a9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/yinhong-zhou/jevdo.git
cd jevdo
git checkout 0a2e116b5737449f141ad2a03b83ff792092b4a9
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 0a2e116b5737](https://github.com/yinhong-zhou/jevdo/tree/0a2e116b5737449f141ad2a03b83ff792092b4a9). AI-assisted README and license inspection; install/live paths not executed.
