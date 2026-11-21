# Parser.AI by Advaith Namboothiri (accounts payable for supplier invoices, with Jev judging fraud and intent signals)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A portfolio accounts-payable system: invoices are OCR'd locally, extracted by an LLM, checked by code (arithmetic, dates, duplicates, vendor and PO matching, tax), judged by Jev for document type, hidden instructions aimed at software, new bank details, payment pressure and unusual payment methods, and a versioned code policy approves or opens a review with every reason logged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/advaithajith-coder/parser-ai) |
| Maintainer | [advaithajith-coder](https://github.com/advaithajith-coder). Independently curated. |
| Format | Python (FastAPI) + React app |
| Requirements | uv; Groq and TypeSafe keys in `.env`; Ollama with `glm-ocr:q8_0` for scans and photos. Local runs use SQLite. |
| License | [MIT](https://github.com/advaithajith-coder/parser-ai/blob/59ec7d0f014412d5b1fb8175e9f5501966408875/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_invoice/decision/jev_client.py`](https://github.com/advaithajith-coder/parser-ai/blob/59ec7d0f014412d5b1fb8175e9f5501966408875/src/jev_invoice/decision/jev_client.py) at the pinned commit. |

## When to use

- See how Jev fits into an invoice pipeline as the judgment step for signals rules cannot catch, with code keeping the final decision.
- Mismatch: a production AP system; it uses a fictional company and approving prepares an export but never sends a payment.

## How it works

`src/jev_invoice/decision/jev_client.py` wraps the System One call; `questions.py` defines the judgment questions and `policy.py` turns Jev's calibrated probabilities plus the code checks into approve/review decisions. Jev can also pick an account from the chart of accounts when the PO line does not give one. Integration evidence: [`src/jev_invoice/decision/jev_client.py`](https://github.com/advaithajith-coder/parser-ai/blob/59ec7d0f014412d5b1fb8175e9f5501966408875/src/jev_invoice/decision/jev_client.py).

## Get started

Copy the example env, add keys, set up the demo data and start the dev server.

```sh
git clone https://github.com/advaithajith-coder/parser-ai
cd parser-ai
cp .env.example .env   # add GROQ_API_KEY and TYPESAFE_API_KEY
uv sync
uv run poe setup
uv run poe dev          # http://localhost:8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [jevai-invoice-procesing-showcase.vercel.app/](https://jevai-invoice-procesing-showcase.vercel.app/)
- README: [github.com/advaithajith-coder/parser-ai/blob/59ec7d0f014412d5b1fb8175e9f5501966408875/README.md](https://github.com/advaithajith-coder/parser-ai/blob/59ec7d0f014412d5b1fb8175e9f5501966408875/README.md)

## Limits and data handling

Extracted invoice text goes to Groq and TypeSafe; scans are OCR'd locally. The README's cost and speed figures are the author's estimates and were not reproduced.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 59ec7d0f0144](https://github.com/advaithajith-coder/parser-ai/tree/59ec7d0f014412d5b1fb8175e9f5501966408875). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
