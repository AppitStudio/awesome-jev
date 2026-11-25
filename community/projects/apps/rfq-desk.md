# RFQ Desk by 1Beyond1 (self-hosted B2B quoting workbench where Jev triages the inquiry inbox before human-approved quotes)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted workbench that turns incoming request-for-quotation emails (body text, spreadsheets and text PDFs) into traceable quotes. Jev sorts each inbox message into new RFQ, revision, other or suspicious; an agent extracts line items with source citations and checks stock and history, while acceptance, pricing, approval and export stay with a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/1Beyond1/rfq-desk) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/1Beyond1/rfq-desk#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-25. |
| Jev evidence | [`apps/api/aux_models.py`](https://github.com/1Beyond1/rfq-desk/blob/74886ef3a5009fb465f085a652cc6503b54ad27b/apps/api/aux_models.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [1Beyond1](https://github.com/1Beyond1). Independently curated. |
| Format | Python web app with a JavaScript frontend |
| Platform and availability | Self-hosted Python web app (local SQLite by default, optional MatrixOne). Chinese and English READMEs. |
| Jev's role | Jev (`jev-latest`) answers a four-way Choice for each inbox email; low confidence (below 0.8), a narrow top-two margin or a suspicious label forces human review. Without Jev it falls back to a reranker, then to local rules. |
| Requirements | Python 3.12+ (Node.js 20+ for frontend tests); a TypeSafe key in `RFQ_JEV_KEY` with `RFQ_ENABLE_MODEL_REQUESTS=1` to turn Jev on; optional reranker and MatrixOne accounts. |
| License | [MIT](https://github.com/1Beyond1/rfq-desk/blob/74886ef3a5009fb465f085a652cc6503b54ad27b/LICENSE) |

## When to use

- Triage a supplier or distributor's RFQ inbox and flag prompt-injection attempts before an agent reads them.
- Keep quoting auditable with line-level evidence and human approval.
- Mismatch: if you need a hosted service; this is a self-hosted workbench.

## How it works

`apps/api/aux_models.py` sends the email to `https://api.typesafe.ai/v1/systemone` as a single Choice question with instructions to treat the content as data; `apps/api/inbox.py` applies the confidence and margin thresholds and the fallbacks. Integration evidence: [`apps/api/aux_models.py`](https://github.com/1Beyond1/rfq-desk/blob/74886ef3a5009fb465f085a652cc6503b54ad27b/apps/api/aux_models.py).

## Get started

Install the Python dependencies and start the API with the bundled demo data (see the English README for platform commands).

```sh
git clone https://github.com/1Beyond1/rfq-desk
cd rfq-desk
python -m pip install -r requirements.txt
# see README.en.md for the start commands and the optional Jev settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/1Beyond1/rfq-desk/blob/74886ef3a5009fb465f085a652cc6503b54ad27b/README.en.md](https://github.com/1Beyond1/rfq-desk/blob/74886ef3a5009fb465f085a652cc6503b54ad27b/README.en.md)

## Limits and data handling

Model calls are off until you enable them. Email content goes to TypeSafe for triage and, if configured, to the reranker provider and MatrixOne cloud. The Jev prompt in the code describes the inbox as synthetic demo data, so treat it as a reference build rather than production software.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 74886ef3a500](https://github.com/1Beyond1/rfq-desk/tree/74886ef3a5009fb465f085a652cc6503b54ad27b). Inspected the English README and the Jev client and inbox triage code at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
