# dsh-auto-review-jev (sperictao)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness Auto-permission plugin: TypeSafe Jev reviews each tool call, with inline usage and API-key settings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sperictao/dsh-auto-review-jev) |
| Maintainer | [sperictao](https://github.com/sperictao). Independently curated. |
| Format | TypeScript · DeepSeek Harness plugin (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/sperictao/dsh-auto-review-jev/blob/996aba6e1d218656f7227c029b7e0b149438742d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from xlennart/dsh-auto-review-jev. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/sperictao/dsh-auto-review-jev.git
cd dsh-auto-review-jev
git checkout 996aba6e1d218656f7227c029b7e0b149438742d
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 996aba6e1d21](https://github.com/sperictao/dsh-auto-review-jev/tree/996aba6e1d218656f7227c029b7e0b149438742d). AI-assisted README and license inspection; install/live paths not executed.
