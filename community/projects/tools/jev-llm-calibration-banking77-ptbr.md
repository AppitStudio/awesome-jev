# Jev vs LLM calibration on Banking77 PT-BR (UFMG course project: does Jev's confidence calibrate better than a local LLM's in Brazilian Portuguese intent classification?)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Final project for a UFMG LLM course (2026/2): Jev and a local generative LLM (`ministral-3:14b` via Ollama) classify the same Banking77 messages into the same 77 intents, in English and in a human-reviewed Brazilian Portuguese translation, and are compared on expected calibration error with paired bootstrap intervals, plus language shift and selective answering. Prompts are frozen and versioned; each run records model versions, hardware and input hashes. README is in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/guiinow/Jev-LLM-callibration) |
| Maintainer | [guiinow](https://github.com/guiinow). Independently curated. |
| Format | Python package and CLI (`jev-eval`) with committed outputs |
| Requirements | Python 3.12+, a `TYPESAFE_API_KEY`, and Ollama with the comparison model for the LLM arm (`--mock` for smoke runs). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_eval/clients/jev_client.py`](https://github.com/guiinow/Jev-LLM-callibration/blob/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/src/jev_eval/clients/jev_client.py) at the pinned commit. |

## When to use

- See how Jev's choice probabilities hold up as confidence scores outside English.
- Mismatch: a general benchmark; it is one dataset and one comparison model.

## How it works

`src/jev_eval/clients/jev_client.py` calls Jev through the TypeSafe Python SDK (`system_one` with a 77-option `Choice`; the final run is pinned to `jev-1.14.0`) and records the served model; `configs/final.yaml` defines the evidence run. Integration evidence: [`src/jev_eval/clients/jev_client.py`](https://github.com/guiinow/Jev-LLM-callibration/blob/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/src/jev_eval/clients/jev_client.py).

## Get started

Install, add your key, probe, then run and analyze.

```sh
git clone https://github.com/guiinow/Jev-LLM-callibration && cd Jev-LLM-callibration
python3.12 -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]"
cp .env.example .env    # TYPESAFE_API_KEY=...
jev-eval --config configs/final.yaml probe
jev-eval --config configs/final.yaml run && jev-eval --config configs/final.yaml analyze
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/guiinow/Jev-LLM-callibration/blob/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/README.md](https://github.com/guiinow/Jev-LLM-callibration/blob/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/README.md)
- Outputs: [github.com/guiinow/Jev-LLM-callibration/tree/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/outputs](https://github.com/guiinow/Jev-LLM-callibration/tree/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd/outputs)

## Limits and data handling

Banking77 messages go to TypeSafe on your key; the LLM arm runs locally. Results are the students' own; the README notes the condition used to test the main hypothesis is still a group decision. No license file, so reuse terms are not granted (the PT-BR dataset is CC BY 4.0 from its authors).

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 2d3c8b7c38e3](https://github.com/guiinow/Jev-LLM-callibration/tree/2d3c8b7c38e35dda6d6ff2379f0cf77a174364dd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
