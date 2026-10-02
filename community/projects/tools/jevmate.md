# jevmate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shell/CLI, Claude Code plugin, and MCP server for coding-agent triage, test selection, and risk review via TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GastonGelhorn/jevmate) |
| Maintainer | [GastonGelhorn](https://github.com/GastonGelhorn). Independently curated. |
| Format | Python · CLI + Claude Code plugin + MCP (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/GastonGelhorn/jevmate/blob/a664659e41e5a28815e7b0fabc1908cdca39fd35/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/GastonGelhorn/jevmate.git
cd jevmate
git checkout a664659e41e5a28815e7b0fabc1908cdca39fd35
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit a664659e41e5](https://github.com/GastonGelhorn/jevmate/tree/a664659e41e5a28815e7b0fabc1908cdca39fd35). AI-assisted README and license inspection; install/live paths not executed.
