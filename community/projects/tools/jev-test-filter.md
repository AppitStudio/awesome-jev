# jev-test-filter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that scores each repository test against a `git diff` with TypeSafe Jev and emits filter arguments for vitest, Jest, `node:test`, Playwright, `cargo test`, and `go test` so runners cover the tests a change could plausibly break.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mizchi/jev-test-filter) |
| Maintainer | [mizchi](https://github.com/mizchi). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript · npm CLI (`jev-test-filter` 0.1.0) plus Agent Skills / Claude Code plugin docs. |
| Requirements | Node.js ≥ 24; `git`; `TYPESAFE_API_KEY` unless `--dry-run` / `--replay`; optional `cargo` / `go` for those formats. |
| License | [MIT](https://github.com/mizchi/jev-test-filter/blob/01319cdc2bb897a91b90c5c1685359332a66bc21/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline node tests **107 passed**; live TypeSafe smoke not run. |

## When to use

Use it to shrink CI or local test runs to the subset Jev scores as impacted by the current diff. Prefer full suites when coverage risk is high. `--dry-run` extracts tests without calling Jev.

## How it works

One shared `state` (the diff) and one question per test go to TypeSafe `/v1/systemone` via [`src/jev.ts`](https://github.com/mizchi/jev-test-filter/blob/01319cdc2bb897a91b90c5c1685359332a66bc21/src/jev.ts). Code maps scores into runner-native filter flags; `--exec` can invoke the runner. Diff and test titles leave the host on live runs.

## Get started

```sh
git clone https://github.com/mizchi/jev-test-filter.git
cd jev-test-filter
git checkout 01319cdc2bb897a91b90c5c1685359332a66bc21
npm install
npm test
npm run build
# live (billed): export TYPESAFE_API_KEY=... && npx jev-test-filter --base main --dry-run
```

Or `pnpm add -D jev-test-filter` / `npx jev-test-filter ...`. Skill install is separate from the CLI (`npx skills add mizchi/jev-test-filter`).

## Examples and demos

- Upstream README runner examples and skill docs under `skills/`.
- This listing: `npm test` → **107 passed**. No live TypeSafe call.

## Limits and data handling

Diff text and test metadata reach TypeSafe on live runs. Selection quality was not measured on a representative corpus here. Node 24+ is required.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 01319cd](https://github.com/mizchi/jev-test-filter/tree/01319cdc2bb897a91b90c5c1685359332a66bc21): MIT; AI-assisted source review of README, LICENSE, `src/`, build, and offline tests. No live TypeSafe call.

Related: [jev-ci-selector](jev-ci-selector.md), [Supercov](supercov.md), [jev-lint](jev-lint.md).
