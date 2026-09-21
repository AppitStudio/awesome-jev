# jev-debtgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered technical-debt gate for coding agents and CI: collects local git/file metrics, asks TypeSafe Jev typed questions, then applies confidence policy (allow / review / block) with optional fail-open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smlayero/jev-debtgate) |
| Maintainer | [smlayero](https://github.com/smlayero). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Node.js CLI/MCP (`jev-debtgate` / `debtgate` **0.3.0**); GitHub Action via `action.yml`; Cursor skill under `skills/`. |
| Requirements | Node.js **≥ 20**; `TYPESAFE_API_KEY` for live assessments (collect-only mode needs no key). |
| License | [MIT](https://github.com/smlayero/jev-debtgate/blob/105e39bcbfb16fa261809ef6b87fb019c3439a2b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline `npm test` passed; live TypeSafe and full CI Action runs were **not** executed. Distinct from [jev-ci-selector](jev-ci-selector.md) (which CI jobs apply) and [jev-linter-action](jev-linter-action.md) (file Q&A gates). |

## When to use

Use it when agents or CI should gate merges on technical-debt risk scored by Jev over local metrics, with explicit confidence floors and fail-open. Prefer [jev-ci-selector](jev-ci-selector.md) to choose which jobs run; prefer [is-malicious](is-malicious.md) for deceptive-code scanning.

## How it works

Local collectors gather diff/file metrics. [`src/jev.ts`](https://github.com/smlayero/jev-debtgate/blob/105e39bcbfb16fa261809ef6b87fb019c3439a2b/src/jev.ts) POSTs to `https://api.typesafe.ai/v1/systemone` (`jev-latest`). [`src/assess.ts`](https://github.com/smlayero/jev-debtgate/blob/105e39bcbfb16fa261809ef6b87fb019c3439a2b/src/assess.ts) combines question packs with policy thresholds into allow/review/block. Secrets are scanned before commit (`scripts/check-secrets.mjs`). Metrics and derived state leave the host when Jev is called.

## Get started

```sh
git clone https://github.com/smlayero/jev-debtgate.git
cd jev-debtgate
git checkout 105e39bcbfb16fa261809ef6b87fb019c3439a2b
npm ci --ignore-scripts
npm test
# Live (charges): export TYPESAFE_API_KEY=... && npx jev-debtgate doctor
```

CI template: upstream `templates/github-workflow.yml` and `action.yml`.

## Examples and demos

- Offline **`npm test`**: TypeScript build + **24** Node test cases + secret-scan (no committed TypeSafe keys) on the review host.
- Examples and skill docs under `examples/` and `skills/debtgate/`.

## Limits and data handling

Bring your own TypeSafe key. Fail-open can skip Jev on errors—know your CI posture. Collect-only reports metrics without calling Jev. Not a substitute for human architecture review.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 105e39b](https://github.com/smlayero/jev-debtgate/tree/105e39bcbfb16fa261809ef6b87fb019c3439a2b): **0.3.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `src/assess.ts`, and tests. **`npm test`: 24 passed** + secret-scan clean. No live TypeSafe or Action run.

Related: [jev-ci-selector](jev-ci-selector.md), [jev-linter-action](jev-linter-action.md), [is-malicious](is-malicious.md).
