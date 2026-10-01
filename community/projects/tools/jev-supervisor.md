# jev-supervisor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness macOS plugin that supervises agent execution with TypeSafe Jev decisions and budgets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ryyyzer/jev-supervisor) |
| Maintainer | [ryyyzer](https://github.com/ryyyzer). Independently curated. |
| Format | DeepSeek Harness plugin (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/ryyyzer/jev-supervisor/blob/1f6438acc3481c2ea4c0b512c9519158afe0e388/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/ryyyzer/jev-supervisor.git
cd jev-supervisor
git checkout 1f6438acc3481c2ea4c0b512c9519158afe0e388
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 1f6438acc348](https://github.com/ryyyzer/jev-supervisor/tree/1f6438acc3481c2ea4c0b512c9519158afe0e388). AI-assisted README and license inspection; install/live paths not executed.
