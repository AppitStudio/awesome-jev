# similarity-ts-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that runs `similarity-ts` and `fallow` duplicate detection on TypeScript, then asks TypeSafe Jev which reported pairs are worth refactoring—printing only those families.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kongyo2/similarity-ts-jev) |
| Maintainer | [kongyo2](https://github.com/kongyo2). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI / npm package (`@kongyo2/similarity-ts-jev` 0.1.0). |
| Requirements | Node.js **≥ 22**; `TYPESAFE_API_KEY` for live judging (`npx @kongyo2/similarity-ts-jev .`). |
| License | [MIT](https://github.com/kongyo2/similarity-ts-jev/blob/90e41c2a65dddddd86b807af7f5765c14a46e93e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `npm test` **39 pass** on the review host; upstream CI success cited. No live TypeSafe spend. |

## When to use

Use it when mechanical clone detectors flood you with lookalikes and you want **Jev to filter for merge-worthy pairs**. Prefer [sgrep](sgrep.md) / [jegrep](jegrep.md) for intent search, or [Supercov](supercov.md) for per-file quality scores. This is not a proof that reported pairs must be merged.

## How it works

Detection merges `similarity-ts` and `fallow` findings into pairs. [`judge.ts`](https://github.com/kongyo2/similarity-ts-jev/blob/90e41c2a65dddddd86b807af7f5765c14a46e93e/src/judge.ts) batches pairs through `@typesafe-ai/sdk` System One questions (`refactor` score, `same_logic`, `same_concept`). Code groups survivors into families above `--min-score` (default 1.9). Fixture/cache paths support offline verification.

## Get started

```sh
git clone https://github.com/kongyo2/similarity-ts-jev.git
cd similarity-ts-jev
git checkout 90e41c2a65dddddd86b807af7f5765c14a46e93e
npm ci --ignore-scripts
npm test
# Live (charges): export TYPESAFE_API_KEY=... && npx @kongyo2/similarity-ts-jev .
```

Live judging sends declaration snippets to TypeSafe. This listing did not run a live scan.

## Examples and demos

- Offline suite under `test/` — **39 pass** on the review host.
- Upstream CI: [Actions run](https://github.com/kongyo2/similarity-ts-jev/actions/runs/35701513090) **success** on main.
- README documents a date-fns sample (pairs in → families out); treat as upstream illustration, not re-measured here.

## Limits and data handling

Requires a TypeSafe key for live judging. Snippet text leaves the machine. Thresholds and detectors are configurable; empty output means nothing cleared the score, not that the repo has no duplication. npm package available as `@kongyo2/similarity-ts-jev`.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 90e41c2](https://github.com/kongyo2/similarity-ts-jev/tree/90e41c2a65dddddd86b807af7f5765c14a46e93e): MIT **0.1.0**. AI-assisted source review of README, LICENSE, `src/judge.ts`, `src/questions.ts`, and tests. Offline `npm test` **39 pass**. No live TypeSafe spend.

Related: [sgrep](sgrep.md), [jegrep](jegrep.md), [jgrep](jgrep.md), [Supercov](supercov.md).
