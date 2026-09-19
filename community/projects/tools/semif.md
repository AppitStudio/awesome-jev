# SemIf

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

SemIf studies runtime-defined semantic decisions using local open models. It implements a Jev-related interface pattern; it does not run or reproduce official Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheoLeeCJ/SemIf) |
| Maintainer | [TheoLeeCJ](https://github.com/TheoLeeCJ). |
| Format | Python scoring CLI, PyTorch/MLX research code, benchmark bundle, browser lab. |
| Relationship to Jev | Independent project, formerly OpenJev; no TypeSafe affiliation or endorsement. Official Jev appears in published-result comparisons, not local inference. |
| Requirements | Python 3.10+; one CUDA GPU for the PyTorch path, or Apple Silicon/MLX; separate WebGPU-capable browser path. Model downloads and sufficient memory are required. |
| License | [MIT code](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/LICENSE); model weights and external datasets have separate [terms and provenance](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/THIRD_PARTY.md). |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use SemIf to study how a frozen local language model can score a closed set of options without generating a prose answer, or to compare fresh scoring with state-prefix reuse.

It is useful for examining input validation, token boundaries, prompt provenance, and evaluation design. It is not a TypeSafe SDK or a drop-in Jev model.

## How it works

The [direct scorer](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/src/semif_phase1/direct.py) maps option descriptions to single-token letter labels, reads their last-position logits, and normalizes only those selected logits. Output includes option IDs, logits, probabilities, input length, prompt hash, timing, and model metadata.

The [core validation](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/src/semif_phase1/core.py) accepts a state, question, and 2–16 uniquely identified options. It rejects non-finite structured state. Remote PyTorch models require a pinned commit revision, and loading disables remote model code.

Serial and shared modes reuse a state prefix; shared mode requires the exact same state across rows. Reranker mode supplies a separate comparison path. These implementations and the [method notes](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/docs/METHOD.md) establish a concrete relation to typed-decision workflows without claiming access to Jev's model or training.

## Get started

For the Python/CUDA path, follow the [quickstart](https://github.com/TheoLeeCJ/SemIf#quick-start). This installs substantial ML dependencies and downloads model weights on first use; it does not require a TypeSafe account:

```sh
git clone https://github.com/TheoLeeCJ/SemIf.git
cd SemIf
git checkout ca3ba65f142967030ecb453346e94d6f476a69df
python3 -m venv .venv
. .venv/bin/activate
pip install -e '.[test]'
CUDA_VISIBLE_DEVICES=0 semif-score --mode direct \
  --model Qwen/Qwen3.5-4B \
  --revision 851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a \
  --input examples/decisions.jsonl --output results.jsonl
```

Expect one JSON result per example, containing conditional option scores and provenance. The output path must not already exist. Python model loading requires exactly one visible CUDA device for this route.

For Apple Silicon, use the [MLX instructions](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/docs/MLX.md), including the `mlx` installation extra and `--backend mlx`. Model format, precision, and memory settings are backend-specific.

For a separate browser experiment:

```sh
cd webgpu-demo
python3 -m http.server 8080
```

Open `http://localhost:8080` in a compatible browser. The [browser instructions](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/webgpu-demo/README.md) describe multi-gigabyte model choices, caching, and external asset requests. This path compares a constrained one-token readout with generated JSON; it is not the identical Python execution path.

Commands above were inspected, not executed in this catalog review.

## Examples and demos

- [Owned decision examples](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/examples/decisions.jsonl): structured inputs for the scoring CLI.
- [Browser lab](https://github.com/TheoLeeCJ/SemIf/tree/ca3ba65f142967030ecb453346e94d6f476a69df/webgpu-demo): editable evidence, questions, and options; current-session inference after downloads.
- [Replay demo](https://github.com/TheoLeeCJ/SemIf/tree/ca3ba65f142967030ecb453346e94d6f476a69df/demo): previously recorded measurements, distinct from a live run.
- [Reproduction guide](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/docs/REPRODUCE.md) and [test suite](https://github.com/TheoLeeCJ/SemIf/tree/ca3ba65f142967030ecb453346e94d6f476a69df/tests): benchmark provenance and software checks.

## Limits and data handling

- These are probabilities conditional on the displayed label tokens, explicitly uncalibrated as decision confidence. There is no universal correctness guarantee or automatic uncertainty fallback.
- Python direct scoring rejects oversized prompts instead of truncating them, and validates exact label tokenization and boundary consistency. Unsupported model/cache shapes can fail explicitly.
- State-prefix reuse and reduced precision can change results; upstream documents disagreement between execution modes. Browser quantized models and native BF16 benchmark models are distinct artifacts.
- The repository's Jev comparisons reuse selected public records. They are not newly executed official Jev evaluations, and this review did not reproduce those comparisons.
- Local inference avoids a TypeSafe request. Initial dependencies, models, browser assets, and optional external evaluation inputs still use network downloads. The browser uses external model/CDN endpoints and browser-managed caching.
- The CLI writes results to the requested local file. Hardware, storage, download, and optional hosted compute costs remain the operator's responsibility.
- Model and dataset licenses must be assessed separately from the MIT project code; [third-party documentation](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/THIRD_PARTY.md) identifies the sources.

## Review and maintenance

Reviewed **2026-09-19** at [`ca3ba65f142967030ecb453346e94d6f476a69df`](https://github.com/TheoLeeCJ/SemIf/tree/ca3ba65f142967030ecb453346e94d6f476a69df).

Inspected README, license, dependency manifest, third-party notes, input validation, direct logits, shared-state constraints, CLI dispatch, browser instructions, and representative validation/CLI tests. Recorded the revision with `git rev-parse HEAD`.

Source review only: no installation, model download, tests, browser inference, GPU benchmark, or TypeSafe request was performed. Upstream measurements are not catalog-verified results, and no speed or accuracy claim is adopted here.
