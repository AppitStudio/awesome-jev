# Jev for Claude Code (brookcs3)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial Claude Code plugin exposing TypeSafe Jev typed judgments (noul/choice/score) plus corpus→eval loops.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brookcs3/jev--system-one-for-claude) |
| Maintainer | [brookcs3](https://github.com/brookcs3). Independently curated. |
| Format | Claude Code plugin `jev` (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/brookcs3/jev--system-one-for-claude/blob/ff9c3a6e7438a85647edcd3a25c2a9e06ad46c2a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Unofficial; not affiliated with TypeSafe. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/brookcs3/jev--system-one-for-claude.git
cd jev--system-one-for-claude
git checkout ff9c3a6e7438a85647edcd3a25c2a9e06ad46c2a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit ff9c3a6e7438](https://github.com/brookcs3/jev--system-one-for-claude/tree/ff9c3a6e7438a85647edcd3a25c2a9e06ad46c2a). AI-assisted README and license inspection; install/live paths not executed.
