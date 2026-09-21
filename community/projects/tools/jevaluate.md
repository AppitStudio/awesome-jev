# Jevaluate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Confidence-gated web-app walkthroughs and related eval helpers for TypeSafe Jev: Jev picks the next UI step and stops under an 80% confidence gate; an optional vision model reviews screenshots; field notes and an agent skill are included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ElshinQ/jevaluate) |
| Maintainer | [ElshinQ](https://github.com/ElshinQ) / Maykana. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js + Python scripts, Playwright walk loop, and agent skill (field-notes kit). |
| Requirements | Node 18+; Python 3.9+ for some scripts; Playwright for browser loops; `TYPESAFE_API_KEY`; walk mode also needs `DEEPSEEK_API_KEY`. |
| License | [MIT](https://github.com/ElshinQ/jevaluate/blob/9f1b9272a9ac797fae6bfba54d141d2953a62991/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live TypeSafe/DeepSeek walks were not run on the review host. Upstream calibration anecdotes were not independently reproduced. |

## When to use

Use it when you want a cheap, confidence-gated agent to click through a test app and hand off when unsure, plus reusable Jev eval/judge scripts. Prefer [jeval](jeval.md) for calibration curves over already-recorded confidences, or [Typed Evals](typed-evals.md) for library judges. Do not treat the author's 60-request calibration write-up as catalog-measured accuracy on your app.

## How it works

[`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/9f1b9272a9ac797fae6bfba54d141d2953a62991/scripts/jev.mjs) calls `https://api.typesafe.ai/v1/systemone` with pinned `jev-1.13.0` by default. The walk loop asks Jev for the next step from a short list and refuses to act below the confidence gate; DeepSeek vision optionally flags visual defects from screenshots. Application code owns Playwright actions and reports.

## Get started

```sh
git clone https://github.com/ElshinQ/jevaluate.git
cd jevaluate
git checkout 9f1b9272a9ac797fae6bfba54d141d2953a62991
# Offline-ish helpers (still need a key for live Jev scripts):
# python3 scripts/eval.py --questions examples/questions.json --cases examples/cases.json
node scripts/tree-test.mjs --tree examples/tree.json --tasks examples/tasks.json
# Live walk (TypeSafe + DeepSeek charges):
# npm i -D @playwright/test@1 && npx playwright install chromium
# export TYPESAFE_API_KEY=… DEEPSEEK_API_KEY=…
# node scripts/walk.mjs --spec examples/walk-watch.json --watch
```

## Examples and demos

- README GIF and `assets/` walk demo artifacts.
- `examples/walk.json` / `walk-watch.json` specs; `article/` write-up of methods and mistakes.
- Review host ran `tree-test.mjs` without a key (no live Jev decisions). Live walk not executed.

## Limits and data handling

Page context and screenshots leave the machine on live walks (TypeSafe for steps; DeepSeek for vision). Use disposable test apps and throwaway logins. The confidence gate is policy, not a proof of correctness. Costs in the README are author-reported for their demo.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9f1b927](https://github.com/ElshinQ/jevaluate/tree/9f1b9272a9ac797fae6bfba54d141d2953a62991): MIT. AI-assisted source review of README, `scripts/jev.mjs`, walk/judge scripts, and LICENSE. No live TypeSafe or DeepSeek calls.

Related: [jeval](jeval.md), [Typed Evals](typed-evals.md), [Jev Score](jev-score.md).
