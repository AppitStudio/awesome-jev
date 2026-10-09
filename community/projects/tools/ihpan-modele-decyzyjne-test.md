# Decision models on Polish historical gazetteer entries (IHPAN)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small evaluation from the Institute of History of the Polish Academy of Sciences: 250 human-labelled fragments of the 19th-century Polish geographical dictionary (SGKP) with a topic and query, scored by three decision models — TypeSafe Jev (via OpenRouter Decisions), TEV1 and Basal — against the human relevance judgment, with data, scripts and raw outputs published. Polish documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IHPAN/modele-decyzyjne-test) |
| Maintainer | [IHPAN](https://github.com/IHPAN) (Instytut Historii PAN). Independently curated. |
| Format | Python scripts + CSV/XLSX dataset + result CSVs |
| Requirements | Python; `OPENROUTER_API_KEY` to re-run the Jev script. |
| License | [Apache-2.0](https://github.com/IHPAN/modele-decyzyjne-test/blob/e1b2976d4f5847bcdbbf91b7a26b587564685cb6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- See how Jev compares with other decision models on a historical-text relevance task in Polish.
- Mismatch: 250 items from one corpus; not a general benchmark.

## How it works

[`src/evaluate_jev.py`](https://github.com/IHPAN/modele-decyzyjne-test/blob/e1b2976d4f5847bcdbbf91b7a26b587564685cb6/src/evaluate_jev.py) reuses the shared evaluator with OpenRouter Decisions (`https://openrouter.ai/api/alpha/decisions`, `typesafe/jev-1.13`). The README reports agreement with human judgment of 244/250 for Jev, 223/250 for TEV1 and 197/250 for Basal (maintainers' results; not reproduced here).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/IHPAN/modele-decyzyjne-test.git
cd modele-decyzyjne-test
python src/evaluate_jev.py   # needs OPENROUTER_API_KEY
```

## Limits and data handling

Re-running sends the dataset fragments to OpenRouter/TypeSafe. Result CSVs from the authors' run are included. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit e1b2976d4f58](https://github.com/IHPAN/modele-decyzyjne-test/tree/e1b2976d4f5847bcdbbf91b7a26b587564685cb6). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
