# jev-router (hectorj2f)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Route Claude Code subagents by Jev depth/breadth/noul scores; publishes where the idea fails (distinct from other jev-router*).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hectorj2f/jev-router) |
| Maintainer | [hectorj2f](https://github.com/hectorj2f). Independently curated. |
| Format | Claude Code subagent model router with published findings (Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/hectorj2f/jev-router/blob/c43e1c0b8823f4587e3384aea644d12de0664aa1/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from gargpratyush/jev-router and other listed jev-router* entries. Upstream Findings document failure modes. Live install/inference not run on the review host. |

## When to use

Use when routing Claude Code subagent model tiers from typed scores, and you want measured failure modes published alongside the router.

## How it works

Five atomic Jev questions (depth/breadth scores; mechanical/irreversible/ambiguous nouls) combine in code; upgrades ungated, downgrades need earned confidence.

## Get started

```sh
git clone https://github.com/hectorj2f/jev-router.git
cd jev-router
git checkout c43e1c0b8823f4587e3384aea644d12de0664aa1
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit c43e1c0b8823](https://github.com/hectorj2f/jev-router/tree/c43e1c0b8823f4587e3384aea644d12de0664aa1). AI-assisted README and license inspection; install/live paths not executed.
