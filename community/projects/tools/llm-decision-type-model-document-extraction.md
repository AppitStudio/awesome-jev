# LLM + Decision-Type Model (Russian-language research project on filling bank-document drafts from chat, with Jev as an optional verifier)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research project that tests whether a separate decision-type model improves how a generative LLM fills documents from a conversation. The LLM proposes values, quotes and formulas, Python checks structure and does the arithmetic, and the decision model detects the document type (invoice draft, own-card transfer draft or none) and scores possible semantic errors. The verifier can be Jev, Jeff, CLM, Laya or another compatible service, and the repository has dev and test splits, an experiment protocol and metrics. README and docs are in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexmagikov/jev_agent) |
| Maintainer | [alexmagikov](https://github.com/alexmagikov). Independently curated. |
| Format | Python 3.14 project run with uv (Russian documentation) |
| Requirements | Python 3.14+, uv, an extraction-LLM key, and a `DECISION_API_KEY` for Jev. |
| License | [MIT](https://github.com/alexmagikov/jev_agent/blob/0de089bb88194eb0d06588417f1faf0dd21c631e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.py`](https://github.com/alexmagikov/jev_agent/blob/0de089bb88194eb0d06588417f1faf0dd21c631e/src/client.py) at the pinned commit. |

## When to use

- Reproduce or extend an experiment on checking LLM document extraction with a typed decision model and measured detection metrics.
- Mismatch: research code with Russian documentation, and the verifier is configurable rather than Jev-only; no bank document is issued or payment made.

## How it works

`src/client.py` uses the `typesafe_sdk` async client with `DECISION_BASE_URL` defaulting to `https://api.typesafe.ai` and `DECISION_MODEL=jev-latest`; flagged fields above `DECISION_WRONG_THRESHOLD` (0.8) go to a bounded repair step. Integration evidence: [`src/client.py`](https://github.com/alexmagikov/jev_agent/blob/0de089bb88194eb0d06588417f1faf0dd21c631e/src/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --locked
uv run --locked python -m src.main --mode llm-only --split dev --limit 1 --fail-fast --output outputs/smoke-llm-only.jsonl
uv run --locked python -m src.main --mode full --verifier decision --split dev --limit 1 --fail-fast --output outputs/smoke-full.jsonl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Russian) with modes, verifier choice and data layout: [github.com/alexmagikov/jev_agent#readme](https://github.com/alexmagikov/jev_agent#readme)
- Experiment protocol: [github.com/alexmagikov/jev_agent/blob/0de089bb88194eb0d06588417f1faf0dd21c631e/docs/experiment-protocol.md](https://github.com/alexmagikov/jev_agent/blob/0de089bb88194eb0d06588417f1faf0dd21c631e/docs/experiment-protocol.md)

## Limits and data handling

Dialog text and extracted fields go to your extraction LLM and to TypeSafe on your keys, and runs can consume paid quota. Results in the repository were not reproduced here. Documentation is in Russian. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 0de089bb8819](https://github.com/alexmagikov/jev_agent/tree/0de089bb88194eb0d06588417f1faf0dd21c631e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
