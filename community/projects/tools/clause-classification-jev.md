# Clause classification with Jev (measures how much CUAD contract text Jev can discard before an expensive model reads it)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment on the CUAD license-agreement corpus: Jev answers yes/no per clause and rule, clauses below a cutoff are binned before an expensive model ever reads them, and the report weighs the saving against lawyer-marked provisions lost. The author's run binned 77.3% of 3,246 clauses at the 0.5 cutoff while losing 44 of 429 marked provisions (10.3%).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MuhammedTech/clause-classification-with-jev) |
| Maintainer | [MuhammedTech](https://github.com/MuhammedTech). Independently curated. |
| Format | Python experiment with report generator (uv; no license file) |
| Requirements | Python with uv, a local copy of CUAD v1 (`CUAD_DIR`), and a TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_cascade/typesafe.py`](https://github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/src/jev_cascade/typesafe.py) at the pinned commit. |

## When to use

- Estimate how much contract text a cheap Jev gate can drop before LLM review, and at what recall cost.
- Mismatch: production contract review; the dataset is not bundled and the numbers are one author run.

## How it works

`src/jev_cascade/typesafe.py` posts to `https://api.typesafe.ai/v1/systemone`; the reported run used `jev-1.14.0` and cost $0.085 in Jev usage. The estimated ~91% saving against Claude Sonnet comes from token counts at list prices; the expensive model was never run. Integration evidence: [`src/jev_cascade/typesafe.py`](https://github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/src/jev_cascade/typesafe.py).

## Get started

Point `CUAD_DIR` at your CUAD copy, sync dependencies and run the cascade report.

```sh
export CUAD_DIR=/path/to/CUAD_v1
uv sync --extra dev
uv run jev-cascade --out out
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/README.md](https://github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/README.md)
- Glossary: [github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/GLOSSARY.md](https://github.com/MuhammedTech/clause-classification-with-jev/blob/5569ec361bc15419e8e9fa9c826bd0c69be19e4e/GLOSSARY.md)

## Limits and data handling

Contract clauses from your CUAD copy go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 5569ec361bc1](https://github.com/MuhammedTech/clause-classification-with-jev/tree/5569ec361bc15419e8e9fa9c826bd0c69be19e4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
