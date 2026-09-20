# Jev Score

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local CLI and web workspace that scores document revisions against your criteria with TypeSafe Jev (via OpenRouter Decisions), keeping history so agents can see whether drafts improve.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/a-Fig/jev-score) |
| Maintainer | [a-Fig](https://github.com/a-Fig). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI (`jev-score` 1.0.0) plus local web UI and agent skill. |
| Requirements | Node.js ≥ 22.13. Live scoring needs `OPENROUTER_API_KEY` (default model `typesafe/jev-1.13` on OpenRouter Decisions). Offline tests need no key. |
| License | [MIT](https://github.com/a-Fig/jev-score/blob/7ab7bfd19ee2cd2de3456decb0726f306e44d347/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests inspected. Live OpenRouter/TypeSafe calls were not run. Uses OpenRouter's Decisions API rather than `api.typesafe.ai` directly. |

## When to use

Use it when a coding agent is iterating on a resume, essay, spec, or landing page and you want a persistent scoreboard tied to explicit questions. Prefer one-off Jev Score/Choice scripts when you do not need workspace history or a UI.

## How it works

[`src/jev.mjs`](https://github.com/a-Fig/jev-score/blob/7ab7bfd19ee2cd2de3456decb0726f306e44d347/src/jev.mjs) posts typed score questions to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13` by default. Local code stores revisions, aggregates scores, and serves the workspace UI—Jev does not edit the document.

## Get started

```sh
git clone https://github.com/a-Fig/jev-score.git
cd jev-score
git checkout 7ab7bfd19ee2cd2de3456decb0726f306e44d347
npm ci --ignore-scripts
npm test
# Live (OpenRouter/TypeSafe charges): export OPENROUTER_API_KEY=… && follow README "Try it locally"
```

## Examples and demos

- `examples/resume/` sample document, job posting, and questions.
- Offline `test/*.mjs` covering scorer aggregation and server behavior.

## Limits and data handling

Document text, context, and criteria are sent to OpenRouter (TypeSafe Jev behind Decisions) on live runs. Scores are rubric indices mapped to a 0–100 display—not proof of hiring/editorial quality. Confirm OpenRouter account terms and model availability separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 7ab7bfd](https://github.com/a-Fig/jev-score/tree/7ab7bfd19ee2cd2de3456decb0726f306e44d347): **1.0.0**, MIT. AI-assisted source review of README, `src/jev.mjs`, and tests. **`npm test`**: **8 passed**. No live OpenRouter/TypeSafe calls.

Related: [jeval](jeval.md), [Supercov](supercov.md).
