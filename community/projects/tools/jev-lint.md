# jev-lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Natural-language semantic linter: [ast-grep](https://ast-grep.github.io) selects subjects locally; each rule’s one-sentence question is answered by TypeSafe Jev (Noul) with calibrated cutoffs. Distinct from catalog [JevLint](jevlint.md) (`huntedman/JevLint` / `@jevlint/cli`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mizchi/jev-lint) |
| Maintainer | [mizchi](https://github.com/mizchi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI/library **jev-lint 0.4.1** (npm; `bin` `jev-lint`). |
| Requirements | Node.js **≥ 20**; `@ast-grep/cli`. Live checks need `TYPESAFE_API_KEY` or `TYPESAFEAI_API_KEY`. |
| License | [MIT](https://github.com/mizchi/jev-lint/blob/e088fe3bda01ea4cbf0539ea1d82b9e01bd6ce5f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live TypeSafe lint runs were not executed. |

## When to use

Use it when you want **meaning-level** checks (name↔body drift, stale comments, tests that would pass if the claim were broken) that parsers and ESLint cannot decide, with subject selection kept local via ast-grep. Prefer [JevLint](jevlint.md) for file-level convention plugins (`@jevlint/cli`). Prefer [patdown](patdown.md) for fuzzy markdown rule trees; prefer [Moongate](moongate.md) for PR-diff semantic CI rules.

## How it works

[`src/jev.ts`](https://github.com/mizchi/jev-lint/blob/e088fe3bda01ea4cbf0539ea1d82b9e01bd6ce5f/src/jev.ts) posts typed Noul questions to `https://api.typesafe.ai/v1/systemone`. Rules under [`rules/`](https://github.com/mizchi/jev-lint/tree/e088fe3bda01ea4cbf0539ea1d82b9e01bd6ce5f/rules) pair an ast-grep matcher with `ask` / `criteria` / cutoff. Matching is free and local; only selected subject text is sent to TypeSafe. Caching, dry-run, and calibration tooling are included.

## Get started

```sh
npm i -g jev-lint
# or from the reviewed tip:
git clone https://github.com/mizchi/jev-lint.git
cd jev-lint
git checkout e088fe3bda01ea4cbf0539ea1d82b9e01bd6ce5f
npm ci --ignore-scripts
npm test
npm run dry   # dry-run check without live TypeSafe calls
```

Set `TYPESAFE_API_KEY` before live `jev-lint check`. Live runs send selected code subjects to TypeSafe and can incur charges; this listing ran offline tests only.

## Examples and demos

- Offline `npm test` — **188 passed** on the review host.
- Upstream README sample findings (`fn-name-promises`, `test-name-verifies-claim`, `comment-describes-declaration`) and `npm run dry` / `eval:replay` paths.

## Limits and data handling

Selected subject text leaves the machine on live checks. Upstream token/cost/latency figures in the README were not independently measured. Not a replacement for compilers, typecheckers, or ESLint API-knowledge rules.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e088fe3](https://github.com/mizchi/jev-lint/tree/e088fe3bda01ea4cbf0539ea1d82b9e01bd6ce5f): **0.4.1**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `package.json`, and rules layout. Ran `npm ci --ignore-scripts` and `npm test` (188 pass). No live TypeSafe calls.

Related: [JevLint](jevlint.md), [patdown](patdown.md), [Moongate](moongate.md).
