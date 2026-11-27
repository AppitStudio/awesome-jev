# Intent routing with Jev by Vinicius Finger (customer-support intent classifier with an OpenAI fallback and deepeval evals)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Small Python example that classifies a customer-support message into one of 12 e-commerce intents (order status, delivery delay, refund, return and so on) with one Jev `choice` question, returns the probability for every intent and flags answers under 0.8 for clarification. Supports earlier turns as context, an optional OpenAI fallback when the Jev call fails, and a deepeval suite that compares both systems.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/viniciusfinger/jev-intent-classification) |
| Maintainer | [Vinicius Finger](https://github.com/viniciusfinger) (viniciusfinger). Independently curated. |
| Format | Python example + eval suite |
| Requirements | Python with uv, an OpenRouter key for Jev; optional OpenAI key for the fallback and the eval judge. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classifier.py`](https://github.com/viniciusfinger/jev-intent-classification/blob/d9f15a0b7d31aa9a998da4aa50b84b6878287409/classifier.py) at the pinned commit. |

## When to use

- Developers building support routing who want a compact starting point with evals.
- Mismatch: a production router; intents and thresholds are examples.

## How it works

`classifier.py` builds a `Choice` question with per-intent criteria and calls `TypeSafeClient.system_one()` from `typesafe-sdk`, configured in `main.py` to reach Jev through OpenRouter. If the call raises and a fallback is configured, `classifier_fallback.py` asks an OpenAI model for a structured answer. The README's expansion of JEV is the author's own, not TypeSafe's. Integration evidence: [`classifier.py`](https://github.com/viniciusfinger/jev-intent-classification/blob/d9f15a0b7d31aa9a998da4aa50b84b6878287409/classifier.py).

## Get started

Set the keys in `.env` and run the example.

```sh
git clone https://github.com/viniciusfinger/jev-intent-classification && cd jev-intent-classification
cp .env.example .env   # OPENROUTER_API_KEY=...
uv run python main.py
uv run python -m evals.run_evals --systems jev --no-judge --limit 10
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evals: [github.com/viniciusfinger/jev-intent-classification/tree/main/evals](https://github.com/viniciusfinger/jev-intent-classification/tree/main/evals)

## Limits and data handling

Messages go to OpenRouter (and to OpenAI when the fallback or judge is used). No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit d9f15a0b7d31](https://github.com/viniciusfinger/jev-intent-classification/tree/d9f15a0b7d31aa9a998da4aa50b84b6878287409). Inspected the README, `classifier.py`, `main.py` and the evals folder at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
