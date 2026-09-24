# jev-ci-pathfinder

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that asks TypeSafe Jev which **allowlisted** CI jobs should run after a change, then exports `run_jobs` / `skip_jobs` for your `if:` gates. Distinct from [jev-ci-selector](jev-ci-selector.md) (described tasks → booleans).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevForge/jev-ci-pathfinder) |
| Maintainer | [JevForge](https://github.com/JevForge). Independently curated. |
| Format | TypeScript Action + optional `composite/` wrapper. |
| Requirements | GitHub Actions; Jev provider secret; allowlist config in-repo. |
| License | [MIT](https://github.com/JevForge/jev-ci-pathfinder/blob/0684c72ea009e77ef5edd365c561a46842de5a64/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Actions/Jev not run. |

## When to use

Use it to **skip irrelevant allowlisted jobs** while keeping the job inventory in your config. Prefer path filters alone when selection is purely path-based; prefer jev-ci-selector when tasks are free-text descriptions rather than a fixed allowlist.

## How it works

Changed paths and config feed typed Jev evaluations per allowlisted job; deterministic allowlist, always-on jobs, and dependency closure cannot be bypassed. The Action never rewrites workflow files.

## Get started

```sh
git clone https://github.com/JevForge/jev-ci-pathfinder.git
cd jev-ci-pathfinder
git checkout 0684c72ea009e77ef5edd365c561a46842de5a64
npm ci
npm test
# uses: JevForge/jev-ci-pathfinder@v0  (or composite@v0)
```

## Examples and demos

- README snippets; `docs/assets/pathfinder-flow.svg`; `examples/`.

## Limits and data handling

Diff/config evidence goes to the Jev provider. Default `dry_run: true` softens step failure—set `false` to enforce. No live CI in this review.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 0684c72](https://github.com/JevForge/jev-ci-pathfinder/tree/0684c72ea009e77ef5edd365c561a46842de5a64). AI-assisted README + Action inspection.

Related: [jev-ci-selector](jev-ci-selector.md), [Moongate](moongate.md), [Metis](metis.md).
