# claude-referee

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code referee/guard plugin that asks TypeSafe Jev before risky tool actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ismaildasci/claude-referee) |
| Maintainer | [ismaildasci](https://github.com/ismaildasci). Independently curated. |
| Format | TypeScript · Claude Code plugin (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/ismaildasci/claude-referee/blob/5cc24b1eb3590b69493dadc1f904939f4af5abb7/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/ismaildasci/claude-referee.git
cd claude-referee
git checkout 5cc24b1eb3590b69493dadc1f904939f4af5abb7
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 5cc24b1eb359](https://github.com/ismaildasci/claude-referee/tree/5cc24b1eb3590b69493dadc1f904939f4af5abb7). AI-assisted README and license inspection; install/live paths not executed.
