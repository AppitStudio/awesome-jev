# jev-backend-qa

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Backend QA agent: audits DB/API/auth/secrets/payments/observability, then PAL/Jev adjudication yields BLOCK/WARN/PASS — CLI and GitHub Action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/diamitani/jev-backend-qa) |
| Maintainer | [diamitani](https://github.com/diamitani). Independently curated. Not an endorsement. |
| Format | Python package / CLI (`jev-backend-qa`) + Node bridge + GitHub Action. |
| Requirements | Python; `agent/` Node bridge (`npm install`); AI Gateway / TypeSafe credentials for live adjudication. |
| License | [MIT](https://github.com/diamitani/jev-backend-qa/blob/3fd47ba557f4582b6f677fa01ae196e37af823a9/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, `agent/jev_bridge.mjs`). Live QA/Jev **not** run. |

## When to use

Use it when a Jev-powered backend needs a whole-system audit with risk probabilities rather than heuristic lint alone. Prefer narrower linters when you only need one surface (SQL, auth, etc.).

## How it works

Static/backend checks emit findings; the PAL loop asks Jev boolean/score/choice/false-positive questions via `experimental_evaluate` through the Node bridge, then maps to BLOCK/WARN/PASS. Optional Rostr upload is documented upstream.

## Get started

```sh
git clone https://github.com/diamitani/jev-backend-qa.git
cd jev-backend-qa
git checkout 3fd47ba557f4582b6f677fa01ae196e37af823a9
pip install -e '.[agent]'   # or follow README pip install path
cd agent && npm install && cd ..
# export AI_GATEWAY_API_KEY / TypeSafe creds per README
# jev-qa …   # live — not run on review host
```

## Examples and demos

- README one-command download→upload path.
- `references/jev-questions.md` question set.

## Limits and data handling

Finding text and context go to the configured AI Gateway/TypeSafe path when live. Verdict quality was not measured here. Rostr upload is optional and separate.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3fd47ba](https://github.com/diamitani/jev-backend-qa/tree/3fd47ba557f4582b6f677fa01ae196e37af823a9) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [agent-evals](agent-evals.md), [Jev WCAG Auditor](jev-wcag-auditor.md).
