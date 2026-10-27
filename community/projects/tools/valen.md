# Valen

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open multimodal System One–style decision models: text, images, and video in; probabilities over supplied candidates out—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Valen-Team/Valen) |
| Maintainer | [Liuziyu77](https://github.com/Liuziyu77) / Valen-Team. |
| Format | Model weights, training and evaluation code, local runtimes, SDKs, and a hosted demo/API. |
| Requirements | The hosted demo and free API do not require a model download or API key; local requirements vary by runtime. See the [deployment guide](https://valen-team.github.io/docs/valen/onnx/). |
| License | [Apache-2.0](https://github.com/Valen-Team/Valen/blob/5b5945386619c32fe257a994dc46639a7d2647d9/LICENSE); base models and datasets retain their own terms. |
| Disclosure | Independent open model research—not TypeSafe-hosted Jev. This update was proposed by the project team with AI assistance. Listing is not an endorsement. |

## When to use

Try typed decisions over text, images, or video, run a model locally, or train on your own data. Valen returns candidate probabilities; application code decides how to act on them.

## How it works

The model uses a shared decision head to score supplied candidates without generating answer tokens. Its interfaces support choice, score, and boolean questions. The repository includes data processing, SFT, experimental RLCD, inference, and evaluation.

## Get started

Try the [web demo](https://valen-team.github.io/) or the [free decision API](https://valen-team.github.io/docs/valen/api/); the hosted service has usage limits. For local deployment, consult the [ONNX and SDK guide](https://valen-team.github.io/docs/valen/onnx/) and the [GGUF guide](https://valen-team.github.io/docs/valen/gguf/). GGUF uses Valen's custom runtime; unmodified llama.cpp/Ollama support is not claimed.

Current weights are published in [0.8B](https://huggingface.co/Valen-Team/Valen-0.8B), [2B](https://huggingface.co/Valen-Team/Valen-2B), and [4B](https://huggingface.co/Valen-Team/Valen-4B) sizes. Local inference requires downloading weights and meeting the selected runtime's hardware requirements.

## Examples and demos

- [Web demo](https://valen-team.github.io/) and [API quickstart](https://valen-team.github.io/cookbook/api-quickstart/).
- [Cookbook](https://valen-team.github.io/cookbook/) with local inference, ticket routing, product-image screening and video tagging examples.
- [VisualDecisionBench](https://huggingface.co/datasets/Valen-Team/VisualDecisionBench) and [JevalKit](https://github.com/Valen-Team/JevalKit) for evaluation; results and comparisons require attention to dataset and evaluation conditions.

## Limits and data handling

Valen is not official Jev. Hosted inputs are sent to the service; consult its [data handling and retention policy](https://valen-team.github.io/docs/valen/api/data-handling/). Free API access has quotas, while higher-volume access requires contacting the team. Probabilities and routing thresholds should be evaluated on the intended data; benchmark results are upstream-reported.

## Review and maintenance

Originally reviewed **2026-09-26** at [commit 06251f9](https://github.com/Valen-Team/Valen/tree/06251f9d9d3c06ea690be93b8696ccc66471f8c9); install/train/inference were not executed. This update reflects AI-assisted inspection of the upstream README and license at [commit 5b59453](https://github.com/Valen-Team/Valen/tree/5b5945386619c32fe257a994dc46639a7d2647d9) on 2026-10-27. No new installation, training, live API or model-quality evaluation was run for this update.
