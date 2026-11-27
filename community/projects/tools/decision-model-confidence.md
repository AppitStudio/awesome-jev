# When are decision models confidently wrong? by Elizabeth Hutton (study of Jev and OpenAI's Luna on 2,380 judge and logic questions, with raw outputs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Tests whether a decision model's probability can be trusted by looking at the answers each model was most sure of. Jev and Luna answered 2,380 questions from ProofWriter, JudgeBench and HaluBench, with Opus 5.5 and Sol 6.1 as references. Both held up on a faithfulness check; on multi-step logic, Luna was often confidently wrong while Jev rarely was, though Jev asserts answers where none can be derived. Raw outputs, analysis and code included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ehutt/decision-model-confidence) |
| Maintainer | [Elizabeth Hutton](https://github.com/ehutt) (ehutt). Independently curated. |
| Format | Research write-up + Python code and raw results |
| Requirements | uv; recomputing the numbers from the saved outputs needs no key; rerunning the models needs TypeSafe and OpenAI keys and a Phoenix server. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models.py`](https://github.com/ehutt/decision-model-confidence/blob/5ef7be77352471bebb12ac93ec1bd2dd01153b49/src/models.py) at the pinned commit. |

## When to use

- Builders deciding whether to auto-accept a decision model's confident answers.
- Mismatch: a general benchmark; it covers three tasks and one run per model from 26 November 2026.

## How it works

`src/models.py` asks each item as one `choice` question through the TypeSafe Python SDK (`jev-latest`, resolved to `jev-1.14.0`) and through OpenAI's Decisions API; analysis scripts compute accuracy and errors in each model's top-confidence quartile and at 0.95 and 0.99. Integration evidence: [`src/models.py`](https://github.com/ehutt/decision-model-confidence/blob/5ef7be77352471bebb12ac93ec1bd2dd01153b49/src/models.py).

## Get started

Rebuild the datasets and recompute every number from the saved outputs, without calling any model.

```sh
git clone https://github.com/ehutt/decision-model-confidence && cd decision-model-confidence
uv run python src/download.py && uv run python src/download_sources.py && uv run python src/download_halubench.py
uv run python src/build_datasets.py
uv run python src/analyze.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Reproduction steps: [github.com/ehutt/decision-model-confidence/blob/main/REPRODUCE.md](https://github.com/ehutt/decision-model-confidence/blob/main/REPRODUCE.md)
- Figures: [github.com/ehutt/decision-model-confidence/tree/main/figures](https://github.com/ehutt/decision-model-confidence/tree/main/figures)

## Limits and data handling

Author's own study from one run per model; some benchmark labels are wrong, which the author audits. No licence file, so no reuse rights are granted for the code; the datasets keep their own licences.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 5ef7be773524](https://github.com/ehutt/decision-model-confidence/tree/5ef7be77352471bebb12ac93ec1bd2dd01153b49). Inspected the README, REPRODUCE.md and `src/models.py` at the pinned commit; no licence file present. Nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
