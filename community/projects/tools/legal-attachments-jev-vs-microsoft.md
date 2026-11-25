# Legal attachment classification by Gabriel Sales (Brazilian court-filing types sorted by Jev and Microsoft-Decision-1, with time and cost per document)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experiment that asks Jev and Microsoft-Decision-1 the same Choice question to label 256 synthetic Brazilian court attachments (petição inicial, contestação, sentença, certidão and others, 22 options), with OCR for scanned PDFs, a confidence cut-off for human review, and measured latency and cost. Both models labelled all 256 correctly; the README compares where each was unsure. In Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gabsalles/teste-anexos-class) |
| Maintainer | [Gabriel Sales](https://github.com/gabsalles). Independently curated. |
| Format | Python scripts with test PDFs, results and charts |
| Requirements | Python 3, the TypeSafe Python SDK and a TypeSafe key; an OpenRouter key for the Microsoft comparison. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classificar.py`](https://github.com/gabsalles/teste-anexos-class/blob/08316c7f0e9a24a8e57e2f6272ee6294a2fd7bf1/classificar.py) at the pinned commit. |

## When to use

- Estimate whether a decision model can triage document types in a legal workflow, and what it costs.
- Mismatch: production legal use; the data are synthetic and the author says thresholds must be calibrated on real labelled documents.

## How it works

`classificar.py` sends each document's text, page count and OCR flag to `AsyncTypeSafeClient.system_one` with one Choice question whose 22 options each carry a description, then writes per-document results with tokens and cost; `classificar_microsoft.py` runs the same question through OpenRouter. Integration evidence: [`classificar.py`](https://github.com/gabsalles/teste-anexos-class/blob/08316c7f0e9a24a8e57e2f6272ee6294a2fd7bf1/classificar.py).

## Get started

Install the requirements, set your key, and run the classifier over the test PDFs.

```sh
git clone https://github.com/gabsalles/teste-anexos-class
cd teste-anexos-class
pip install -r requirements.txt
export TYPESAFE_API_KEY=...
python classificar.py anexos_juridicos_teste/pdfs --gabarito anexos_juridicos_teste/manifest.csv
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and charts: [github.com/gabsalles/teste-anexos-class/tree/08316c7f0e9a24a8e57e2f6272ee6294a2fd7bf1/docs](https://github.com/gabsalles/teste-anexos-class/tree/08316c7f0e9a24a8e57e2f6272ee6294a2fd7bf1/docs)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. The 256 PDFs are synthetic. Microsoft-Decision-1 (non-TypeSafe) is reached through OpenRouter, so its timings include OpenRouter. Jev cost is computed from list price, not billed. Results are the author's own.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 08316c7f0e9a](https://github.com/gabsalles/teste-anexos-class/tree/08316c7f0e9a24a8e57e2f6272ee6294a2fd7bf1). Inspected the README and classifier scripts at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
