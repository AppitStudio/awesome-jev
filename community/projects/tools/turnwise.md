# Turnwise by Edgar Bermudez (research project comparing Jev with schema-constrained LLMs for extracting decisions from conversations)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code for pulling reliable, reviewable structured information out of conversations. It compares Jev with schema-constrained LLMs on a reviewed synthetic pilot dataset and is preparing a dataset in Jev's format to fine-tune an open-weight decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/edgarbc/turnwise) |
| Maintainer | [edgarbc](https://github.com/edgarbc). Independently curated. |
| Format | Python CLI and library (`turnwise`, uv) |
| Requirements | Python 3.11+, uv; a TypeSafe API key only for hosted replay and benchmarks (offline validation needs none). |
| License | [MIT](https://github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/turnwise/providers/jev.py`](https://github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/src/turnwise/providers/jev.py) at the pinned commit. |

## When to use

- Study how a decision model compares with structured-output LLMs on conversation extraction.
- Mismatch: a ready-made extraction product; pilot results are exploratory.

## How it works

`src/turnwise/providers/jev.py` wraps the TypeSafe Python SDK (`TypeSafeClient`, `Choice`); `configs/experiments/jev-vs-llm.yaml` defines the Jev-versus-LLM comparison. Integration evidence: [`src/turnwise/providers/jev.py`](https://github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/src/turnwise/providers/jev.py).

## Get started

Sync and explore the CLI; offline validation and replay run without keys.

```sh
git clone https://github.com/edgarbc/turnwise.git && cd turnwise
uv sync
uv run turnwise --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/README.md](https://github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/README.md)
- Experiment config: [github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/configs/experiments/jev-vs-llm.yaml](https://github.com/edgarbc/turnwise/blob/84d1c7dafe10620260a7822a116825a0c42a8231/configs/experiments/jev-vs-llm.yaml)

## Limits and data handling

Hosted replay sends conversation text to TypeSafe and OpenAI. The pilot data is synthetic and results are not a general performance claim.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 84d1c7dafe10](https://github.com/edgarbc/turnwise/tree/84d1c7dafe10620260a7822a116825a0c42a8231). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
