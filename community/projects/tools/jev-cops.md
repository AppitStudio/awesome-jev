# jev-cops

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-aware tool-call policing for coding agents with graduated Jev-backed verdicts (allow→kill).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FrancoisChastel/jev-cops) |
| Maintainer | [FrancoisChastel](https://github.com/FrancoisChastel). Independently curated. |
| Format | TypeScript/Bun · npm (`jev-cops`, Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/FrancoisChastel/jev-cops/blob/9dd371ba73a1e8d4b7ffb0aaf353da0becb1d64f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/FrancoisChastel/jev-cops.git
cd jev-cops
git checkout 9dd371ba73a1e8d4b7ffb0aaf353da0becb1d64f
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 9dd371ba73a1](https://github.com/FrancoisChastel/jev-cops/tree/9dd371ba73a1e8d4b7ffb0aaf353da0becb1d64f). AI-assisted README and license inspection; install/live paths not executed.
