# tax-doc-classifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript library that classifies tax-document PDF pages into IRS forms and page kinds with TypeSafe Jev Choice questions over a shipped JSON criteria file (261 forms)—no fine-tuned model hosted by the project.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kyotofin/tax-doc-classifier) |
| Maintainer | [kyotofin](https://github.com/kyotofin). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm/pnpm package **tax-doc-classifier 0.1.0** (`classifyPage`, `jevBackend`, PDF helpers; ships `data/criteria.json`). |
| Requirements | Node ≥ 20; live classification needs `TYPESAFE_API_KEY`. PDF helpers need poppler (`pdftotext` / `pdfinfo`) on `PATH`. |
| License | [Apache-2.0](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/LICENSE) (criteria data has a separate [DATA-LICENSE.md](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/DATA-LICENSE.md)). |

## When to use

Use it to map extracted page text to a fixed IRS form id and page kind with calibrated probabilities and an optional confidence gate (default ≥ 0.95). Prefer [doc-router](doc-router.md) when the problem is OCR vs local extraction routing rather than tax-form identity. Upstream corpus accuracy and cost figures are vendor-reported; this listing does not restate them as measured here.

## How it works

[`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/src/backend.ts) implements `jevBackend()` against `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with bearer `TYPESAFE_API_KEY`. [`classifyPage`](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/src/classify.ts) builds Choice questions from `data/criteria.json` (kind, then form list, then optional schedule sub-question for a few parents). Application code owns gating and fallbacks from `formConfidence`.

## Get started

```sh
# as a dependency (see upstream README for pnpm add github:…), or:
git clone https://github.com/kyotofin/tax-doc-classifier.git
cd tax-doc-classifier
git checkout 6afcf701395466d7c936ec8178daf017b9d96b0c
pnpm install
pnpm typecheck
pnpm test
export TYPESAFE_API_KEY=…   # required for live classifyPage via jevBackend()
```

Every classified page is a billable System One call (and may recurse for schedule families). Page text leaves the host for TypeSafe. This listing ran no live eval.

## Examples and demos

- README `classifyPage` + `jevBackend` TypeScript snippet.
- `pnpm eval` / `eval/` scripts for reproducible corpus runs (need credentials and data download).
- Offline unit tests via `pnpm test` (Vitest).

## Limits and data handling

Tax page text is sent to TypeSafe. Blank pages may skip a call. Upstream “100% strict” / cost claims were not reproduced on the review host. Keep API keys in the environment; do not commit `.env`.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 6afcf701](https://github.com/kyotofin/tax-doc-classifier/tree/6afcf701395466d7c936ec8178daf017b9d96b0c): **0.1.0**, Apache-2.0. AI-assisted source review of README, `src/backend.ts`, `src/classify.ts`, `package.json`, and license. `pnpm test` / live TypeSafe eval were not run on the review host.

Related: [doc-router](doc-router.md), [Advocaat](advocaat.md).
