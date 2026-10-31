# FinDoc (loan-file copilot that checks a mortgage packet against its documents, with Jev classifying and splitting pages)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app for mortgage loan officers: upload a borrower's PDFs, get an automatic review of the application against pay slips, statements and title documents, record a decision on every flag and ask follow-ups with page citations. Jev labels each page's document type and detects document boundaries during ingestion; the app never approves or rejects loans.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VIVPM/document-retrieval-system) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/VIVPM/document-retrieval-system#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you pay for AWS, Pinecone, Neon, Gemini/Cloudflare and TypeSafe usage. Checked 2026-10-31. |
| Jev evidence | [`backend/core/document_classifier_jev.py`](https://github.com/VIVPM/document-retrieval-system/blob/fce403506cdab26f2c096a9266cdaf142424ebff/backend/core/document_classifier_jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/VIVEKPM99/status/2116387186828615716)). |
| Maintainer | [VIVPM](https://github.com/VIVPM). Independently curated. |
| Format | Web app (FastAPI backend + worker, React frontend) |
| Platform and availability | Self-hosted web app (browser); no hosted instance verified. |
| Jev's role | Classifies each page's document type and detects document boundaries during ingestion. |
| Requirements | AWS Textract (or local PyMuPDF), Pinecone, Neon Postgres, a Gemini or Cloudflare Workers AI key, and a TypeSafe key for ingestion. |
| License | [MIT](https://github.com/VIVPM/document-retrieval-system/blob/fce403506cdab26f2c096a9266cdaf142424ebff/LICENSE) |

## When to use

- Split merged loan packets into logical documents before retrieval and cross-checking.
- Mismatch: answers and field extraction run on Gemini; Jev only handles page labels and boundaries.

## How it works

`backend/core/document_classifier_jev.py` sends page text to `api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`) as a closed-set choice for document type and a yes/no for 'does a new document start here'; unknown labels are logged and handled in code. Integration evidence: [`backend/core/document_classifier_jev.py`](https://github.com/VIVPM/document-retrieval-system/blob/fce403506cdab26f2c096a9266cdaf142424ebff/backend/core/document_classifier_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
cd backend && pip install -r requirements.txt   # then fill backend/.env incl. TYPESAFE_API_KEY
cd frontend && npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo post on X: [x.com/VIVEKPM99/status/2116387186828615716](https://x.com/VIVEKPM99/status/2116387186828615716)

## Limits and data handling

Borrower documents are sent to AWS Textract, Gemini/Cloudflare and TypeSafe; treat the setup as handling sensitive financial PII. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit fce403506cda](https://github.com/VIVPM/document-retrieval-system/tree/fce403506cdab26f2c096a9266cdaf142424ebff). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
