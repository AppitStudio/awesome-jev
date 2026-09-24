# HekaJev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ask reproducible Git-history analytics questions across one or many repositories; TypeSafe Jev filters and classifies commits with saved evidence and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zurk/hekajev) |
| Maintainer | [zurk](https://github.com/zurk). Independently curated. |
| Format | Python CLI/package (`hekajev`). |
| Requirements | Python 3.14+; Git; `TYPESAFE_API_KEY` for live analysis. |
| License | [MIT](https://github.com/zurk/hekajev/blob/9b62c615c580aa5663548e5d77a67c35b99ab189/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live multi-repo analysis not run. |

## When to use

Use to **measure** commit history with typed Jev labels and exportable evidence. Prefer jev-git-graph for branch/worktree consolidation graphs.

## How it works

YAML filters/categories drive commit selection; Jev judges labels; results land in JSONL/JSON/logs/HTML (per README).

## Get started

```sh
git clone https://github.com/zurk/hekajev.git
cd hekajev
git checkout 9b62c615c580aa5663548e5d77a67c35b99ab189
# follow README / AGENTS.md; export TYPESAFE_API_KEY
```

## Examples and demos

- README agent prompt and CLI sections; research notes.

## Limits and data handling

Commit messages and selected diffs reach TypeSafe. Large histories incur provider cost—use filters and resume.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 9b62c61](https://github.com/zurk/hekajev/tree/9b62c615c580aa5663548e5d77a67c35b99ab189). AI-assisted README inspection; live Jev not run.
