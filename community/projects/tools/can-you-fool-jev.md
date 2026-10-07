# Can you fool Jev?

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

1,000 English trick questions sent as identical `/v1/systemone` requests to Jev, Nimble 9B, tev1 4B and Strands Decider 2B, with the dataset, every request body, per-model answers, a runner for any `/v1/systemone` endpoint and a video walkthrough.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huseyinbabal/can-you-fool-jev) |
| Maintainer | [huseyinbabal](https://github.com/huseyinbabal). Independently curated. |
| Format | Dataset (`data/questions.csv`) + Python runner and summary/chart scripts + committed results |
| Requirements | Python 3; a TypeSafe key for Jev, or any model behind a `/v1/systemone` endpoint (the maintainer used Ollama and `strands-decider serve` for local models). |
| License | [MIT](https://github.com/huseyinbabal/can-you-fool-jev/blob/1072daa0438d4bb787430c9ea980792c6debc44e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Probe failure modes (customer messages, agent tool calls, code and commits) with adversarial questions before trusting a decision model.
- Rerun the exact same 1,000 requests against a self-hosted `/v1/systemone` model to compare with the committed Jev answers.
- Mismatch: the maintainer says it is not a benchmark — one author, some debatable labels, one run per model.

## How it works

Each CSV row becomes one request: the `input` is the `state`, and the question is a `choice`, `noul` (yes/no) or `score` over 1–10 ([`examples/request.json`](https://github.com/huseyinbabal/can-you-fool-jev/blob/1072daa0438d4bb787430c9ea980792c6debc44e/examples/request.json)). [`scripts/run_systemone.py`](https://github.com/huseyinbabal/can-you-fool-jev/blob/1072daa0438d4bb787430c9ea980792c6debc44e/scripts/run_systemone.py) sends them to the host you choose; only the `model` field differs between runs, and request bodies are saved alongside answers in [`results/`](https://github.com/huseyinbabal/can-you-fool-jev/tree/1072daa0438d4bb787430c9ea980792c6debc44e/results). [`scripts/summary.py`](https://github.com/huseyinbabal/can-you-fool-jev/blob/1072daa0438d4bb787430c9ea980792c6debc44e/scripts/summary.py) builds the per-type and per-category tables.

## Get started

Run Jev (or any `/v1/systemone` model) and summarize:

```sh
git clone https://github.com/huseyinbabal/can-you-fool-jev.git && cd can-you-fool-jev
SYSTEMONE_HOST=https://api.typesafe.ai SYSTEMONE_KEY=$JEV_API_KEY python3 scripts/run_systemone.py jev-latest
python3 scripts/summary.py
```

A full Jev run is 1,000 requests billed to your TypeSafe key; local models cost nothing beyond your hardware.

## Examples and demos

- README results table (maintainer run on 2026-10-02: Jev 91.4% vs Nimble 9B 81.8% and tev1 4B 76.8%; latency includes Jev's network round trip).
- Video walkthrough linked from the README: *I Tried to Fool 4 AI Decision Models With 1000 Trick Questions*.

## Limits and data handling

Results are the maintainer's single run with default settings; 843 of 1,000 questions are customer messages; labels written by one person. Not re-run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 1072daa0438d](https://github.com/huseyinbabal/can-you-fool-jev/tree/1072daa0438d4bb787430c9ea980792c6debc44e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
