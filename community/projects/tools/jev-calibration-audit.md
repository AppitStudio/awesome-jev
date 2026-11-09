# jev-calibration-audit (independent calibration audit of Jev vs eight LLMs on WorkflowEvals data)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Recomputes TypeSafe's published WorkflowEvals runs to measure how well Jev's probabilities are calibrated versus eight LLMs; no model calls or API key needed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mohith26/jev-calibration-audit) |
| Maintainer | [Mohith26](https://github.com/Mohith26). Independently curated. |
| Format | Python analysis (MIT) |
| Requirements | Python 3 and `pip install -r requirements.txt`; data comes from public Hugging Face datasets. |
| License | [MIT](https://github.com/Mohith26/jev-calibration-audit/blob/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_all.py`](https://github.com/Mohith26/jev-calibration-audit/blob/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83/run_all.py) at the pinned commit. |

## When to use

- Check Jev calibration before setting thresholds.
- Reuse the audit method for other decision models.
- Mismatch: agreement with reference models, not human ground truth.

## How it works

`run_all.py` and the `calaudit` package reproduce the published scores, then compute ECE, selective agreement and Learn-then-Test gates; tables are in `results/RESULTS.md`. Integration evidence: [`run_all.py`](https://github.com/Mohith26/jev-calibration-audit/blob/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83/run_all.py).

## Get started

Create a venv, install requirements and run `python run_all.py`.

```sh
git clone https://github.com/Mohith26/jev-calibration-audit.git && cd jev-calibration-audit
python -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/python run_all.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/Mohith26/jev-calibration-audit/blob/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83/results/RESULTS.md](https://github.com/Mohith26/jev-calibration-audit/blob/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83/results/RESULTS.md)

## Limits and data handling

Uses only public datasets; nothing is sent to any model.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 8ca6ec1fd80e](https://github.com/Mohith26/jev-calibration-audit/tree/8ca6ec1fd80e1215733e22b66f8864b29ec6dd83). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
