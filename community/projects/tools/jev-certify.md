# jev-certify

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Finite-sample routing certificates and prediction-powered audits for TypeSafe Jev probabilities: conformal risk control for thresholds, PPI for cheap live audits, plus measured failure modes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nikkoxgonzales/jev-certify) |
| Maintainer | [nikkoxgonzales](https://github.com/nikkoxgonzales). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package / CLI **`jev-certify` 0.1.0** (MIT); zero runtime dependencies (numpy optional for plots). |
| Requirements | Python ≥ 3.10. Live collection uses OpenRouter Decisions (`OPENROUTER_API_KEY`) with model `typesafe/jev-1.13` — not a chat-completions path. Offline math/tests need no key. |
| License | [MIT](https://github.com/nikkoxgonzales/jev-certify/blob/5dfe58226f07a7ccbafc71aa0f54fcb792cc2e72/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, journalled results, and offline pytest inspected. Live OpenRouter/Jev collection was not re-run. Author-reported experiment cost and accuracy tables are upstream measurements. |

## When to use

Use it when a hand-picked confidence threshold is not enough and you need a **provable bound** on silently misrouted queries (or an affordable audit of that bound on live traffic). Prefer [jev-calibrate](jev-calibrate.md) for labelled tune/holdout verdicts without conformal guarantees, or [Typed Evals](typed-evals.md) for general LLM/RAG judge harnesses.

## How it works

Offline modules implement split-conformal / conformal risk control and prediction-powered inference over stored Jev `choice`/`noul` answers (CLINC150-style intent + in-scope tasks). [`client.py`](https://github.com/nikkoxgonzales/jev-certify/blob/5dfe58226f07a7ccbafc71aa0f54fcb792cc2e72/jev_certify/client.py) talks to `POST https://openrouter.ai/api/alpha/decisions` with `typesafe/jev-1.13`. Calling code still owns deployment intents, thresholds, and escalation. Shipped `results/` journals support offline re-analysis without new API spend.

## Get started

```sh
git clone https://github.com/nikkoxgonzales/jev-certify.git
cd jev-certify
git checkout 5dfe58226f07a7ccbafc71aa0f54fcb792cc2e72
python3 -m pip install -e '.[dev]'
python3 -m pytest -q
```

Live collection (charges on OpenRouter; not run for this listing):

```sh
# see upstream README / .env.example for OPENROUTER_API_KEY
jev-certify --help
```

## Examples and demos

- README risk/coverage tables and SVG figures under `docs/`.
- [`results/REPORT.md`](https://github.com/nikkoxgonzales/jev-certify/blob/5dfe58226f07a7ccbafc71aa0f54fcb792cc2e72/results/REPORT.md) and JSON journals for the published experiment.
- Offline unit tests covering conformal/PPI/cascade helpers.

## Limits and data handling

Live collection sends queries and intent criteria to OpenRouter’s Decisions API. Certificates assume exchangeability; upstream documents prevalence shift and out-of-scope breakage. Do not treat README percentages as your production error rate without your own labels. References to third-party awesome lists are author commentary, not catalog endorsements.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 5dfe582](https://github.com/nikkoxgonzales/jev-certify/tree/5dfe58226f07a7ccbafc71aa0f54fcb792cc2e72): **0.1.0**, MIT. AI-assisted source review of README, `jev_certify/`, LICENSE, and tests. On the review host: **`pytest -q` → 43 passed**. No live OpenRouter/TypeSafe spend.

Related: [jev-calibrate](jev-calibrate.md), [Typed Evals](typed-evals.md), [jeval](jeval.md).
