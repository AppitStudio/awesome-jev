# Jev Observer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy and dashboard for TypeSafe Jev decisions (history, versions, latency/cost) with an embedded web UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LimePencil/jev-observer) |
| Maintainer | [LimePencil](https://github.com/LimePencil). Independently curated. |
| Format | Rust · local proxy + embedded dashboard (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/LimePencil/jev-observer/blob/6f76e4efc7fa08e7c0157fe58cc7e75bc2dbba6c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Independent project; name provisional per upstream. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/LimePencil/jev-observer.git
cd jev-observer
git checkout 6f76e4efc7fa08e7c0157fe58cc7e75bc2dbba6c
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 6f76e4efc7fa](https://github.com/LimePencil/jev-observer/tree/6f76e4efc7fa08e7c0157fe58cc7e75bc2dbba6c). AI-assisted README and license inspection; install/live paths not executed.
