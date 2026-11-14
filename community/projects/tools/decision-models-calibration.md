# Decision models calibration (Vikawork) (measurement of Jev 1.14, gpt-6-luna Decisions and Gemini Decision 1 on BANKING77, BoolQ and SST-5: accuracy, calibration, speed and cost)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent comparison of three typed-decision APIs on the same 400 items from each of three public test sets (intent routing, yes/no over a passage, 5-level sentiment), checking accuracy, how often a ≥90%-confident answer is right, calibration error, latency and cost, with a generative-model baseline. Code, per-item outputs and a full report are in the repository.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vikawork/decision-models-calibration) |
| Maintainer | [vikawork](https://github.com/vikawork). Independently curated. |
| Format | Python scripts, results and report (MIT) |
| Requirements | Python 3; `JEV_API_KEY`, `OPENAI_API_KEY` and `GEMINI_API_KEY` to rerun all arms. |
| License | [MIT](https://github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`common.py`](https://github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/common.py) at the pinned commit. |

## When to use

- Compare calibration and latency of Jev with other decision APIs before choosing one.
- Mismatch: your own domain; three public sets and 400 items each are a narrow sample.

## How it works

`common.py` maps the `jev` provider to `https://api.typesafe.ai/v1/systemone` with model `jev-1.14.0` and its published input price; `run.py` sends each item once per provider and `write_report.py` builds `REPORT.md`. Integration evidence: [`common.py`](https://github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/common.py).

## Get started

Read the report, or rerun after fetching the SST-5 inputs.

```sh
git clone https://github.com/vikawork/decision-models-calibration && cd decision-models-calibration
python3 -I fetch_sst5.py
./run-all.sh    # needs the three provider keys
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Report: [github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/REPORT.md](https://github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/REPORT.md)
- README: [github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/README.md](https://github.com/vikawork/decision-models-calibration/blob/c92d83daa4d789af2db98133bb54bd312e6d5f63/README.md)

## Limits and data handling

Reruns send benchmark items to TypeSafe, OpenAI and Google on your keys. Results are the maintainer's single measurement on 14 November 2026.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit c92d83daa4d7](https://github.com/vikawork/decision-models-calibration/tree/c92d83daa4d789af2db98133bb54bd312e6d5f63). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
