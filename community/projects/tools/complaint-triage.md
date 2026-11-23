# Pharmaceutical complaint triage by Alinme (tutorial that classifies product complaints with decision models such as Jev and routes them with fixed rules)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

A small runnable tutorial: one request per complaint asks ten bounded questions (category, subcategory, multi-label tags, enough detail, adverse event, severity), hard rules on the raw text decide what is urgent, and a QA reviewer confirms every result. A benchmark on 40 synthetic complaints compares Jev 1.14 with other decision models; the web demo defaults to another model with Jev as fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Alinme-Co/ComplaintTriage) |
| Maintainer | [Alinme-Co](https://github.com/Alinme-Co). Independently curated. |
| Format | Python scripts (standard library) + local web demo |
| Requirements | Python 3.10+; an OpenRouter API key (the self-test runs offline). |
| License | [All rights reserved (view-only)](https://github.com/Alinme-Co/ComplaintTriage/blob/36059892c6ede30e77ec1a2309ebb9bcee8b1c09/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classify.py`](https://github.com/Alinme-Co/ComplaintTriage/blob/36059892c6ede30e77ec1a2309ebb9bcee8b1c09/classify.py) at the pinned commit. |

## When to use

- Learn a pattern where a decision model suggests and fixed rules plus a person decide, on a regulated-domain example.
- Mismatch: real pharmacovigilance; the model never decides batch safety, recalls or reporting.

## How it works

`classify.py` posts to OpenRouter's `https://openrouter.ai/api/alpha/decisions`; `JEV_MODEL` selects the decision model, and Jev 1.14 results are in `benchmarks/typesafe_jev-1.14.json`. Integration evidence: [`classify.py`](https://github.com/Alinme-Co/ComplaintTriage/blob/36059892c6ede30e77ec1a2309ebb9bcee8b1c09/classify.py).

## Get started

Run the offline self-test, then the benchmark with your key.

```sh
git clone https://github.com/Alinme-Co/ComplaintTriage && cd ComplaintTriage
python classify.py --selftest
export OPENROUTER_API_KEY=...
JEV_MODEL=typesafe/jev-1.14 python classify.py complaints.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark results: [github.com/Alinme-Co/ComplaintTriage/blob/36059892c6ede30e77ec1a2309ebb9bcee8b1c09/report.md](https://github.com/Alinme-Co/ComplaintTriage/blob/36059892c6ede30e77ec1a2309ebb9bcee8b1c09/report.md)

## Limits and data handling

Complaints and photos are sent to OpenRouter. Benchmarks are the author's run on 40 synthetic complaints. The licence is view-only: no rights to use, modify or redistribute the code are granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 36059892c6ed](https://github.com/Alinme-Co/ComplaintTriage/tree/36059892c6ede30e77ec1a2309ebb9bcee8b1c09). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
