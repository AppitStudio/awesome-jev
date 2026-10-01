# evidence-referee

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that checks "done" claims and small judgment calls with TypeSafe Jev and keeps receipts (distinct from claude-referee).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ismaildasci/evidence-referee) |
| Maintainer | [ismaildasci](https://github.com/ismaildasci). Independently curated. |
| Format | Claude Code plugin (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/ismaildasci/evidence-referee/blob/235ebd8b06e7fc477a25578d33bb8e5cc679a141/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/ismaildasci/evidence-referee.git
cd evidence-referee
git checkout 235ebd8b06e7fc477a25578d33bb8e5cc679a141
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 235ebd8b06e7](https://github.com/ismaildasci/evidence-referee/tree/235ebd8b06e7fc477a25578d33bb8e5cc679a141). AI-assisted README and license inspection; install/live paths not executed.
