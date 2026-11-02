# FirstCare (grounded medical-triage research demo where Jev reranks cases and checks each claim's support)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

ECIR 2027 demo-track system for low-hallucination medical triage over the Chinese Clinical Case Repository: hybrid BM25/TF-IDF retrieval, Jev reranking, and a two-question Jev check (mentioned? supported?) for every candidate statement, so unsupported ones are removed before the answer is written. Includes a single-file browser demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SumTHU/FirstCare) |
| Maintainer | [SumTHU](https://github.com/SumTHU). Independently curated. |
| Format | Python research pipeline + static browser demo |
| Requirements | Python 3; a Jev key (TypeSafe direct or a compatible gateway) and an LLM key for the end-to-end evaluation; the browser demo needs nothing. |
| License | [MIT](https://github.com/SumTHU/FirstCare/blob/778bebd7cd8ac0f0dc28bc09af48246b01f32e56/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/verification/jev_client.py`](https://github.com/SumTHU/FirstCare/blob/778bebd7cd8ac0f0dc28bc09af48246b01f32e56/src/verification/jev_client.py) at the pinned commit. |

## When to use

- Study a retrieve, rerank and verify pipeline that drops unsupported claims.
- Mismatch: research demo, not medical advice; its QA set has not had expert review.

## How it works

`src/verification/jev_client.py` is a shared client for TypeSafe's System One API (`api.typesafe.ai/v1/systemone`, or a configured gateway); `stage2_jev_reranker.py` scores the top 50 candidates and `jev_fact_verifier.py` asks a mention and a support question per statement with a 0.7 threshold. Integration evidence: [`src/verification/jev_client.py`](https://github.com/SumTHU/FirstCare/blob/778bebd7cd8ac0f0dc28bc09af48246b01f32e56/src/verification/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/SumTHU/FirstCare.git
cd FirstCare
python compare_backend_frontend.py
python smoke_test_pipeline.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Interactive demo: [sumthu.github.io/FirstCare/medir_triage_ui_real.html](https://sumthu.github.io/FirstCare/medir_triage_ui_real.html)
- Demo video page: [sumthu.github.io/FirstCare/](https://sumthu.github.io/FirstCare/)

## Limits and data handling

Not a medical device or medical advice. Queries and case text go to TypeSafe or the configured gateway. The end-to-end evaluation uses 30 samples and the README warns against citing results as proven. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 778bebd7cd8a](https://github.com/SumTHU/FirstCare/tree/778bebd7cd8ac0f0dc28bc09af48246b01f32e56). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
