# TetraJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jev-class decisions on bounded decision problems from two frozen open-weight readers — four readings per item, fit-free fusion, agreement routing, and published coverage–accuracy curves; no fine-tuning and no distillation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FeiLiuEM/tetrajev) |
| Tags | Open source · Free source build |
| Product homepage | [Repository README](https://github.com/FeiLiuEM/tetrajev#readme) — runs locally on one 24 GB GPU; no hosted service. |
| Pricing and access | No accounts and no paid API: everything runs locally. Reader weights come from their official distributions (linked with sha256 in `docs/method.md`); no weights are redistributed. Checked 2026-09-29. |
| Jev evidence | Independent implementation of the decision pattern — it does not call the TypeSafe API. Architecture diagram, method, and per-suite numbers: `docs/method.md`, `docs/results.md`. |
| Disclosure | Author submission (maintainer). Built with extensive AI assistance (LLM coding agents), disclosed in the repository README. Independent research; not TypeSafe's model. Listing is not an endorsement. |
| Maintainer | [FeiLiuEM](https://github.com/FeiLiuEM) (author submission). |
| Format | Decision layer + Python runners (four-reading fusion R4, agreement routing R2) for local inference. |
| Platform and availability | Linux with one 24 GB CUDA GPU for the shipped configuration; Python ≥3.9; runners are standard-library only and speak to a local OpenAI-compatible server exposing logprobs (llama.cpp). |
| Jev's role | Jev-class typed decisions: state + 2–20 options → per-option probability, agreement tier, calibrated release/abstain decision. No TypeSafe API calls; a local alternative for evaluation, not a Jev replacement. |
| Requirements | Python 3.9+; llama.cpp serving GGUF readers (Qwen3.5-27B + Qwen3.5-35B-A3B, run alternately on 24 GB); benchmarks fetched from their original sources. |
| License | [MIT](https://github.com/FeiLiuEM/tetrajev/blob/main/LICENSE). |

## When to use

Use when you want a local, zero-training decision layer with published per-suite numbers: bounded classification-style judgments, entity matching, spam/phishing triage, document reranking, and multiple-choice evaluation. Prefer hosted TypeSafe Jev when you need the official model or hosted scale.

## How it works

Two frozen readers each answer twice per item — a letter readout over the option letters and a per-candidate yes/no readout — giving four per-option distributions that are fused fit-free (equal-weight mean, R4) and routed by reader agreement (strict / unanimous / split, R2) into auto-release or human review. Readings are deterministic: greedy one-token decodes read from token log-probabilities; re-runs are bit-identical. Method and known limits: [`docs/method.md`](https://github.com/FeiLiuEM/tetrajev/blob/main/docs/method.md).

## Get started

```sh
git clone https://github.com/FeiLiuEM/tetrajev.git
cd tetrajev
git checkout 2ee296af7bcf731ecb9a1d3613fad4defaf49a2a
# serve a reader with llama.cpp (`-np 1`), then run a suite, e.g.:
# python scripts/run_dbench_ours.py --server http://127.0.0.1:10361 --tag 27b --out out.jsonl
```

See `scripts/README.md` for the per-suite entry points; benchmarks are fetched from their original sources.

## Examples and demos

- Coverage–accuracy figures for all eight suites and the RAG reranking pass: `assets/coverage_r4_all_suites.png`, `assets/coverage_p3_osbench_spam.png`.
- Per-suite tables and reference values vs published runs (including the DecisionBench official CSV): `docs/results.md`, `docs/decisionbench-bench-v4-reference.csv`.
- No live demo was executed on the review host; every number is reproducible from the shipped scripts and per-suite result files.

## Limits and data handling

- Equal-weight fusion dilutes when one reading is weak (documented in `docs/method.md`; quality-weighted fusion is roadmap).
- Lead candidate: strongest single reading can beat the fused score at high-precision operating points on some suites.
- The RAG reranking pass is pair-structure only; binary items make the two readout structures near-equivalent.
- Reference values for other systems are their published numbers; protocols differ (generated answers with self-reported confidence vs log-probability readouts).
- No data leaves the machine; no accounts, no telemetry, nothing redistributed from benchmark corpora.

## Review and maintenance

Submitted **2026-09-29** by the maintainer (author submission) at [commit 2ee296a](https://github.com/FeiLiuEM/tetrajev/tree/2ee296af7bcf731ecb9a1d3613fad4defaf49a2a). Upstream README, LICENSE, and docs inspected; live inference paths not executed on the review host.
