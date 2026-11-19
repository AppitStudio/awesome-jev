# Lakewood Creek HOA Q&A (cited answers from one HOA's documents, with Jev gating, retrieving and checking support)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Unofficial one-box Q&A for an Illinois homeowners' association: answers come only from the HOA's published documents and two Illinois statutes, every claim must be backed by a verbatim quote, and off-topic or unanswerable questions are refused.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lostcol0ny/lwc-hoa-qa) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://lwc-hoa-qa.vercel.app) |
| Pricing and access | Free public page with a monthly spending budget and per-IP rate limits; the MIT source can be deployed with your own TypeSafe, LLM, Vercel and Upstash accounts. Checked 2026-11-20. |
| Jev evidence | [`src/hoa_qa/retrieval/jev.py`](https://github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/src/hoa_qa/retrieval/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [lostcol0ny](https://github.com/lostcol0ny). Independently curated. |
| Format | Python FastAPI app on Vercel (MIT) |
| Platform and availability | Web (Vercel); Python CLI for local use. |
| Jev's role | Gate (is this about the HOA?), sweep (scores every corpus chunk and keeps the top 8) and support check (does each quote support the claim?), plus matching against a curated answer cache. |
| Requirements | Python and uv; `TYPESAFE_API_KEY` and an LLM key for answers; Vercel and Upstash Redis for the hosted budget and rate limits. |
| License | [MIT](https://github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/LICENSE) |

## When to use

- See a pattern for a small, citation-strict document Q&A where a cheap decision model does scope, retrieval and verification.
- Mismatch: legal advice or other communities' documents without rebuilding the corpus; it covers one HOA.

## How it works

`src/hoa_qa/retrieval/jev.py` asks Jev (pinned to `jev-1.13.0`, the version the thresholds were tuned on) whether a question is in scope, then scores all ~678 chunks for relevance; an LLM writes the answer and each quoted claim is checked in code and by a Jev support question before it is shown. Integration evidence: [`src/hoa_qa/retrieval/jev.py`](https://github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/src/hoa_qa/retrieval/jev.py).

## Get started

Use the public page, or run the QA core locally.

```sh
git clone https://github.com/lostcol0ny/lwc-hoa-qa
cd lwc-hoa-qa
uv sync
# set TYPESAFE_API_KEY and the LLM key (see README configuration table)
# build the corpus (docs/ingest.md), then ask from the CLI
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live page: [lwc-hoa-qa.vercel.app](https://lwc-hoa-qa.vercel.app)
- QA design: [github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/docs/qa-core.md](https://github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/docs/qa-core.md)
- Web ops and budget: [github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/docs/web-ops.md](https://github.com/lostcol0ny/lwc-hoa-qa/blob/8bb19f26c27dd6ca735da94c6bf058c302e043ca/docs/web-ops.md)

## Limits and data handling

Questions are sent to TypeSafe and the answering LLM; the README says answers are not legal advice and the Board's documents are authoritative. The author's cost and latency figures were not reproduced.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 8bb19f26c27d](https://github.com/lostcol0ny/lwc-hoa-qa/tree/8bb19f26c27dd6ca735da94c6bf058c302e043ca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
