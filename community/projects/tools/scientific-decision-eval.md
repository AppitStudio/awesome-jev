# Scientific Decision Evaluation

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and data for evaluating Jev and other models on scientific Choice decisions where deterministic code computes downstream counts, relations and claim labels, reporting semantic, downstream and final-label correctness separately.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bydeng01/scientific-decision-eval) |
| Maintainer | [bydeng01](https://github.com/bydeng01). Independently curated. |
| Format | Python research code + data (arXiv paper) |
| Requirements | Python 3.12; provider keys (TypeSafe Jev via OpenRouter and others) only for new model runs. |
| License | [Apache-2.0](https://github.com/bydeng01/scientific-decision-eval/blob/c24ff2e74007d0bfee2380a3f13564626358d5ae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`development/s2-execution-v1/run.py`](https://github.com/bydeng01/scientific-decision-eval/blob/c24ff2e74007d0bfee2380a3f13564626358d5ae/development/s2-execution-v1/run.py) at the pinned commit. |

## When to use

- See how a decision model's discrete choices propagate into downstream scientific results.
- Reuse the decision-program pattern: model answers narrow Choices, code does the rest.
- Mismatch: development results on prepared inputs; the authors note it does not establish generalization or calibration.

## How it works

Case records define scientific Choices; `run.py` dispatches them to configured providers (Jev as `typesafe/jev-1.13` through OpenRouter, per `config.json`) and deterministic code computes downstream outcomes for scoring. Integration evidence: [`development/s2-execution-v1/run.py`](https://github.com/bydeng01/scientific-decision-eval/blob/c24ff2e74007d0bfee2380a3f13564626358d5ae/development/s2-execution-v1/run.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bydeng01/scientific-decision-eval.git && cd scientific-decision-eval
python3 -m pip install -r requirements.txt
python3 -B scripts/verify_release.py
python3 -B development/s2-execution-v1/run.py check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2609.24965](https://arxiv.org/abs/2609.24965)
- Thirteen-model report: `results/s2-thirteen-model-analysis-v1/REPORT.md`.

## Limits and data handling

New runs send prepared scientific inputs to the configured providers on your keys.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit c24ff2e74007](https://github.com/bydeng01/scientific-decision-eval/tree/c24ff2e74007d0bfee2380a3f13564626358d5ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
