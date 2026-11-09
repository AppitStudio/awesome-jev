# PayRecover Jev (rules-first failed-payment diagnosis for Razorpay with typed Jev decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Detects failed Razorpay one-time payments and diagnoses the cause with a rules → Jev → Gemini cascade, then recovers revenue through bounded, audited actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nish344/payrecover-jev) |
| Maintainer | [Nish344](https://github.com/Nish344). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python, Razorpay test credentials, and an OpenRouter or TypeSafe key for Jev. |
| License | [MIT](https://github.com/Nish344/payrecover-jev/blob/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/payrecover/diagnosis.py`](https://github.com/Nish344/payrecover-jev/blob/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4/src/payrecover/diagnosis.py) at the pinned commit. |

## When to use

- Triage failed payments with typed causes.
- Study a rules-first cascade with a fair eval.
- Mismatch: built for Razorpay test mode.

## How it works

`diagnosis.py` runs rules first and calls `JevClient.decide_payment_failure` (model `typesafe/jev-1.14`) when keyed; `eval.py` compares the cascade on a fixed set. Integration evidence: [`src/payrecover/diagnosis.py`](https://github.com/Nish344/payrecover-jev/blob/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4/src/payrecover/diagnosis.py).

## Get started

Install with `pip install -e ".[dev]"`, copy `.env.example` and set the Jev key.

```sh
git clone https://github.com/Nish344/payrecover-jev.git && cd payrecover-jev
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Nish344/payrecover-jev/blob/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4/README.md](https://github.com/Nish344/payrecover-jev/blob/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4/README.md)

## Limits and data handling

Payment failure metadata is sent to the Jev provider.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit d1fe4a1a635c](https://github.com/Nish344/payrecover-jev/tree/d1fe4a1a635c1e3e472fcf711ee14ce8c027d6d4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
