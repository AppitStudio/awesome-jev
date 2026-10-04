# dsh-plugin-jev-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin: TypeSafe Jev scores messages for relevance-based compaction (pins constraints/tracebacks; falls back to age-based on failure; MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YYTbit/dsh-plugin-jev-compaction) |
| Maintainer | [YYTbit](https://github.com/YYTbit). Independently curated. |
| Format | DeepSeek Harness plugin: Jev-scored context compaction (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/YYTbit/dsh-plugin-jev-compaction/blob/d32b23f5c32ba923c98773ebe50b56f472238afe/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from fast-jev-compaction, jev-compaction-plus, and other non-DSH compactors—DeepSeek Harness plugin path. Live install/inference not run on the review host. |

## When to use

Use inside DeepSeek Harness when age-based compaction drops early constraints. Prefer Claude/Codex compactors for those hosts.

## How it works

Segments messages, protects system/recent/pinned text, batch-scores remaining messages with Jev Score, gates by confidence, keeps by value until budget, digests the rest.

## Get started

```sh
git clone https://github.com/YYTbit/dsh-plugin-jev-compaction.git
cd dsh-plugin-jev-compaction
git checkout d32b23f5c32ba923c98773ebe50b56f472238afe
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit d32b23f5c32b](https://github.com/YYTbit/dsh-plugin-jev-compaction/tree/d32b23f5c32ba923c98773ebe50b56f472238afe). AI-assisted README and license inspection; install/live paths not executed.
