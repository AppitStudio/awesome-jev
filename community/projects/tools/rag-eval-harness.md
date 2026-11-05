# rag-eval-harness (from-scratch RAG faithfulness evaluation in plain Python with a validated per-sentence Jev judge)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small, complete worked example of evaluating RAG faithfulness without an eval platform: read traces, write one binary judge per failure mode, validate it on a held-out split and correct the raw failure rate with its measured error rates. The judge asks Jev one yes/no question per answer sentence and scores the answer as its weakest sentence; frozen numbers are valid only for `jev-1.14.0`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asharma353/rag-eval-harness) |
| Maintainer | [asharma353](https://github.com/asharma353). Independently curated. |
| Format | Python scripts and datasets |
| Requirements | Python and a Jev key for the live judge; the README says a full 109-answer run cost about $0.03. |
| License | [MIT](https://github.com/asharma353/rag-eval-harness/blob/e75e5a601d04c2f0714f2569c99c3c68d2a88317/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`rag_eval/judge.py`](https://github.com/asharma353/rag-eval-harness/blob/e75e5a601d04c2f0714f2569c99c3c68d2a88317/rag_eval/judge.py) at the pinned commit. |

## When to use

- Learn how to validate a binary LLM-style judge (TPR/TNR) before trusting it.
- Swap the Jev judge for another by replacing `judge_faith`.
- Mismatch: an educational repo, not a framework.

## How it works

`judge_faith` in `rag_eval/judge.py` is the only function that calls Jev; frozen thresholds and balanced-accuracy numbers live in `evalset/faith_judge.json`. Integration evidence: [`rag_eval/judge.py`](https://github.com/asharma353/rag-eval-harness/blob/e75e5a601d04c2f0714f2569c99c3c68d2a88317/rag_eval/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
# from the upstream README (not run): set your Jev key, then run the evaluation scripts described in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with method and measured numbers: [github.com/asharma353/rag-eval-harness/blob/e75e5a601d04c2f0714f2569c99c3c68d2a88317/README.md](https://github.com/asharma353/rag-eval-harness/blob/e75e5a601d04c2f0714f2569c99c3c68d2a88317/README.md)

## Limits and data handling

Reported accuracies are the author's on his own labelled split and say that Jev is not fully deterministic; results should not be generalised.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit e75e5a601d04](https://github.com/asharma353/rag-eval-harness/tree/e75e5a601d04c2f0714f2569c99c3c68d2a88317). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
