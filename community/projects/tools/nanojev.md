# NanoJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

NanoJev studies a Qwen3-0.6B backbone with typed decision heads and code-composed game controllers. It is an independent model project, not official Jev or TypeSafe's implementation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TianyuCodings/NanoJev) |
| Maintainer | [TianyuCodings](https://github.com/TianyuCodings). |
| Format | Python training/inference scripts, local HTTP service, checkpoint/data releases, and recorded browser replay. |
| Relationship to Jev | Related typed-question design; separate scripts call a Jev provider for teaching/comparison. Local NanoJev inference does not call Jev. |
| Requirements | Python for replay; CUDA/PyTorch and downloaded checkpoint for inference. Provider-backed JavaScript experiments require Node 22+ and separate credentials. |
| License | [MIT repository code](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/LICENSE); external backbone, checkpoint, and dataset terms require separate review. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use NanoJev to inspect how an independent decision head produces complete distributions over dynamic choices, Boolean propositions, or ordered levels, and how a controller combines those judgments with deterministic planning.

The maze and Snake experiments are useful for studying model-versus-controller responsibilities. Their selected recorded outcomes do not establish general reasoning or official Jev equivalence.

## How it works

The [`DecisionModel`](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/scripts/train_toy_decisions.py) builds candidate paths from state, instructions, and descriptions, passes them through the backbone, and scores final hidden states. Optional set attention combines candidates within Choice questions. Boolean uses one semantic path; ordered Score values are computed from the level distribution in code.

The [predictor](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/scripts/predict_toy_decisions.py) validates requests and probabilities, loads local safetensors and tokenizer/config files, and retains full distributions and execution metadata. Question IDs stay out of model input. Batched candidate paths repeat the state; this is not shared-prefix caching.

The [contract audit](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/docs/TYPESAFE_CONTRACT.md) explicitly documents incompatibilities with the [TypeSafe interface](https://docs.typesafe.ai/api): local `boolean` rather than `noul`, string-only instructions/descriptions, and missing provider response fields. Do not treat it as a drop-in API replacement.

## Get started

The shortest path is recorded playback, without ML dependencies, a model download, or a provider key:

```sh
git clone https://github.com/TianyuCodings/NanoJev.git
cd NanoJev
git checkout 71a513bb0163b5634467842b523ee0c0ed6fb1c7
python3 -m http.server 8080 --bind 127.0.0.1 --directory web
```

Open `http://127.0.0.1:8080/side-by-side.html`. The inspected viewer fetches `side_by_side_results.json` and replays stored trajectories. Its panels labeled Jev, NanoJev, and Qwen display recorded runs, not new inference.

For actual local inference:

1. Prepare the CUDA environment described in [requirements-toy.txt](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/requirements-toy.txt).
2. Follow [model download instructions](https://github.com/TianyuCodings/NanoJev#download-and-run-the-model) to obtain checkpoint, tokenizer, and backbone configuration files.
3. Start the persistent service from the repository root:

```sh
python scripts/serve_decisions.py \
  --checkpoint-dir checkpoints/NanoJev --web-root web --port 8765
```

Open `http://127.0.0.1:8765`; inference uses `POST /api/evaluate`. This entry point requires a CUDA device and supports no CPU/remote fallback. The default BF16 mode additionally requires device support.

The [game-release guide](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/docs/GAME_RELEASE.md) distinguishes task-specific variants. The root checkpoint is an initialization/earlier-navigation artifact, not the checkpoint used for every showcase.

Commands above were inspected, not run during this review. Downloads can be large and local GPU compute has its own costs.

## Examples and demos

- [Side-by-side viewer](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/web/side-by-side.html): recorded Snake and maze trajectories with probability bars.
- [Atomic-planning notes](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/docs/ATOMIC_PLANNING.md): local judgments composed with memory, exploration, and path planning.
- [Question-contract tests](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/scripts/test_question_contract.py): synthetic character-tokenizer tests for transport IDs, question isolation, and output arithmetic; they do not load the model.
- [Pipeline runbook](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/research/pipeline_runbook.md): training and evaluation workflow; some routes use external provider labels.

## Limits and data handling

- Independent research checkpoints have task-specific training. Selected game results combine model predictions with substantial shared controller logic.
- Local inference rejects unsupported question shapes, oversized candidate paths, and invalid probability distributions. It does not automatically abstain on uncertainty; calibration must be established separately.
- Structured state currently becomes Python string formatting rather than canonical JSON. Structured instructions and criteria are not fully supported, and local `noul` requests fail validation.
- The service binds to localhost by default, checks origin on POST, and limits request bytes, states, questions, and candidate paths. Inference errors return an error rather than silently switching to a teacher model.
- Checkpoint inference forces offline Hugging Face loading and disables remote model code. Initial package/checkpoint/data downloads contact external hosts; provider comparison/labeling scripts are a separate outbound, potentially billed path.
- Local results retain distributions and metadata; browser replay reads committed data. Provider comparison records are upstream evidence, not calls made by this review.
- Repository code licensing does not establish the terms of every external backbone, checkpoint, or dataset. Those releases were not downloaded or independently licensed in this review.

## Review and maintenance

Reviewed **2026-09-19**, commit [`71a513bb0163b5634467842b523ee0c0ed6fb1c7`](https://github.com/TianyuCodings/NanoJev/tree/71a513bb0163b5634467842b523ee0c0ed6fb1c7).

Inspected README, MIT license, dependency manifests, contract audit, decision head, predictor validation/loading/readout, HTTP handler, replay data loading, and representative contract tests. Recorded the revision with `git rev-parse HEAD`.

Source review only: no installs, tests, checkpoint downloads, GPU inference, training, provider requests, or browser replay were executed. Upstream accuracy, calibration, throughput, and comparative gameplay claims were not independently verified.
