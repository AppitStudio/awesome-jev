# Jev 따라하기 example code by ady95 (Korean book companion: runnable Jev examples chapter by chapter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Example code for the Korean book "Jev 따라하기 (LLM과 다른 의사결정 AI 시작하기)". Each chapter has standalone Python scripts: first calls, Choice, Noul, Score and parallel questions, calibration charts, routing and rule-engine comparisons, guardrails, RAG reranking, agent risk, a four-way benchmark, abstention and reliability statistics, a LangChain tax-advice agent and a Laya comparison, plus a 120-case labelled dataset.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ady95/jev_tutorial) |
| Maintainer | [ady95](https://github.com/ady95). Independently curated. |
| Format | Python example scripts (Korean) |
| Requirements | Python with the listed requirements; a TypeSafe API key (an OpenAI key only for the LLM comparison examples). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The companion book is a commercial publication sold separately; this listing covers only the public example code. |
| Jev evidence | [`ch03/choice.py`](https://github.com/ady95/jev_tutorial/blob/5c2894cece5ebb7ccdf72866e56848516e56e5f2/ch03/choice.py) at the pinned commit. |

## When to use

- Learn Jev step by step in Korean, with code matched to each chapter of the book.
- Mismatch: English readers; the README and comments are in Korean.

## How it works

`ch03/choice.py` and the other chapters use the official `typesafe_sdk` (`TypeSafeClient`, `Choice`), with `_common.py` checking `TYPESAFE_API_KEY`. Chapter 12 also runs a local Laya server that speaks the same `/v1/systemone` interface for comparison. Integration evidence: [`ch03/choice.py`](https://github.com/ady95/jev_tutorial/blob/5c2894cece5ebb7ccdf72866e56848516e56e5f2/ch03/choice.py).

## Get started

Install requirements, add your key and run a chapter script from the repository root.

```sh
git clone https://github.com/ady95/jev_tutorial.git && cd jev_tutorial
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # TYPESAFE_API_KEY
python ch02/first_call.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Book on WikiDocs: [wikidocs.net/book/21376](https://wikidocs.net/book/21376)
- Chapter map: [github.com/ady95/jev_tutorial/blob/5c2894cece5ebb7ccdf72866e56848516e56e5f2/README.md](https://github.com/ady95/jev_tutorial/blob/5c2894cece5ebb7ccdf72866e56848516e56e5f2/README.md)

## Limits and data handling

The book itself is sold separately (YES24, Kyobo, WikiDocs); prices were not checked and this listing covers the public example code only. Scripts send examples to TypeSafe and, for comparisons, OpenAI. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 5c2894cece5e](https://github.com/ady95/jev_tutorial/tree/5c2894cece5ebb7ccdf72866e56848516e56e5f2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
