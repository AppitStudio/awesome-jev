# Jev for Claude

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dependency-free Claude Code plugin with nine user-invoked engineering skills (safety preflight, rule rubric, browser QA, evidence completion and more), conservative local hooks, and an explicit opt-in typed TypeSafe Jev judge adapter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VoidLight00/jev-for-claude) |
| Maintainer | [VoidLight00](https://github.com/VoidLight00). Independently curated. |
| Format | Claude Code plugin |
| Requirements | Claude Code; TypeSafe key only for the opt-in `jev-judge` skill. |
| License | [MIT](https://github.com/VoidLight00/jev-for-claude/blob/5e119b53f724340360274ae2d8a15b1d82685778/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add guardrail skills to Claude Code with optional typed Jev checks.
- Mismatch: most features work without Jev; hooks are not a safety proof.

## How it works

See the upstream [README](https://github.com/VoidLight00/jev-for-claude/blob/5e119b53f724340360274ae2d8a15b1d82685778/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/VoidLight00/jev-for-claude.git   # install per README
```

## Limits and data handling

Only the opt-in judge skill sends content to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 5e119b53f724](https://github.com/VoidLight00/jev-for-claude/tree/5e119b53f724340360274ae2d8a15b1d82685778). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
