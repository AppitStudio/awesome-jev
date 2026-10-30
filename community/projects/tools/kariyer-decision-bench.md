# kariyer-decision-bench (Turkish job-posting benchmark of Jev, tau-4b and prompted LLMs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark harness from Kariyer.net R&D that asks the same seven typed questions (seniority, department, work mode and others) of Turkish decision models and prompted LLMs over 600 real job postings. Reported results: Jev 1.13.0 had the best accuracy (71.5%) and seniority error, while the open tau-4b model was better calibrated (ECE 0.093 against 0.156); a hand check of 40 errors found most were label or taxonomy problems. README in Turkish.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kubrakrcn/kariyer-decision-bench) |
| Maintainer | [kubrakrcn](https://github.com/kubrakrcn). Independently curated. |
| Format | Python benchmark scripts |
| Requirements | Python 3 with the listed requirements; a Jev API key for the Jev run; a GPU or 16 GB RAM for tau-4b; your own postings file and taxonomy. |
| License | [Apache-2.0](https://github.com/kubrakrcn/kariyer-decision-bench/blob/043eb7cfb4816fa47a9a046333e7750cc50bace2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench_decisions.py`](https://github.com/kubrakrcn/kariyer-decision-bench/blob/043eb7cfb4816fa47a9a046333e7750cc50bace2/bench_decisions.py) at the pinned commit. |

## When to use

- Compare a hosted decision model with open ones and prompted LLMs on your own extraction questions.
- Mismatch: the 600 Kariyer.net postings are not published; you bring your own data.

## How it works

`bench_decisions.py` sends each posting and question to TypeSafe `POST /v1/systemone` with exponential backoff on 429/529, resumes where it stopped, and `report.py` computes accuracy, MAE, ECE and risk-coverage. Integration evidence: [`bench_decisions.py`](https://github.com/kubrakrcn/kariyer-decision-bench/blob/043eb7cfb4816fa47a9a046333e7750cc50bace2/bench_decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
export JEV_API_KEY=...
python jev_probe.py
python bench_decisions.py --system jev --file kariyer_set.jsonl --out-dir results --limit 20
python report.py results/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results folder: [github.com/kubrakrcn/kariyer-decision-bench/tree/043eb7cfb4816fa47a9a046333e7750cc50bace2/results](https://github.com/kubrakrcn/kariyer-decision-bench/tree/043eb7cfb4816fa47a9a046333e7750cc50bace2/results)

## Limits and data handling

Posting text is sent to TypeSafe on the Jev run. Results come from the author's private set and cannot be reproduced exactly from the repo. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 043eb7cfb481](https://github.com/kubrakrcn/kariyer-decision-bench/tree/043eb7cfb4816fa47a9a046333e7750cc50bace2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
