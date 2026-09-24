# jev-git-graph

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evidence-backed TypeSafe Jev relationship graph for Git branch, worktree, and PR consolidation (read-only CLI by default).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CondorCommodore/jev-git-graph) |
| Maintainer | [CondorCommodore](https://github.com/CondorCommodore). Independently curated. |
| Format | Python CLI. |
| Requirements | Python; local Git repo; `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/CondorCommodore/jev-git-graph/blob/efa912cf6aad428a1dca969757aeb8bec5430868/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live graph build not run. |

## When to use

Use to **map** related branches/PRs with Jev evidence before consolidating. Prefer HekaJev for commit-history classification across repos.

## How it works

CLI inspects Git refs and asks Jev about relationships; default mode stays read-only (per README).

## Get started

```sh
git clone https://github.com/CondorCommodore/jev-git-graph.git
cd jev-git-graph
git checkout efa912cf6aad428a1dca969757aeb8bec5430868
# run CLI per README
```

## Examples and demos

- README consolidation workflow notes.

## Limits and data handling

Commit/PR text reaches TypeSafe. Confirm before any write/consolidation actions if you enable them.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit efa912c](https://github.com/CondorCommodore/jev-git-graph/tree/efa912cf6aad428a1dca969757aeb8bec5430868). AI-assisted README inspection; live Jev not run.
