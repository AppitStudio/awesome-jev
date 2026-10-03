# jev-compaction-plus

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code compaction via TypeSafe Jev keep/drop; retained text stays verbatim and dropped tool outputs move to a drawer file (fork of fast-jev-compaction).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cth9191/jev-compaction-plus) |
| Maintainer | [cth9191](https://github.com/cth9191). Independently curated. |
| Format | TypeScript · Claude Code plugin (MIT) |
| Requirements | See upstream README; provider keys when using live hosted paths. |
| License | [`MIT`](https://github.com/cth9191/jev-compaction-plus/blob/e2ca81cdb71c709b5f5a2f07a15e5f3a700f884a/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from tamaratran/fast-jev-compaction (adds drawer retention). Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Claude Code compaction via TypeSafe Jev keep/drop; retained text stays verbatim and dropped tool outputs move to a drawer file (fork of fast-jev-compaction). Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/cth9191/jev-compaction-plus.git
cd jev-compaction-plus
git checkout e2ca81cdb71c709b5f5a2f07a15e5f3a700f884a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: Jev yes/no per tool result; drawer path; fork of tamaratran/fast-jev-compaction. ([upstream evidence](https://github.com/cth9191/jev-compaction-plus/blob/e2ca81cdb71c709b5f5a2f07a15e5f3a700f884a/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit e2ca81cdb71c](https://github.com/cth9191/jev-compaction-plus/tree/e2ca81cdb71c709b5f5a2f07a15e5f3a700f884a). AI-assisted README and license inspection; install/live paths not executed.
