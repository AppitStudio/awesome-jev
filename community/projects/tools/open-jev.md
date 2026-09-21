# open-jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

A TypeScript library for experimenting with typed decisions on-device using independent Kev and DeBERTa models through Transformers.js.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nico-martin/open-jev) |
| Maintainer | [Nico Martin](https://github.com/nico-martin) |
| Format | Browser-focused npm library, with a vanilla TypeScript/Vite demo; reviewed package `open-jev` 0.1.2. |
| Availability | [npm package](https://www.npmjs.com/package/open-jev); WebGPU or WASM in browsers, with a documented Node.js CPU path. Runtime inference was not tested in this review. |
| Jev relationship | Independent implementation of related Choice/Score/Noul patterns. It loads Kev/Qwen3 or DeBERTa ONNX models, not TypeSafe Jev weights, and does not call TypeSafe's API. |
| Requirements | JavaScript/TypeScript application; `@huggingface/transformers` >=4.3.0 as a peer dependency; memory and a supported backend for the selected model. Source development uses pnpm 11.1.1. |
| Access and costs | No TypeSafe account, API key, or hosted inference charge for this local path. Package/model downloads use network bandwidth; inference uses the user's device. |
| License | Library: [MIT](https://github.com/nico-martin/open-jev/blob/52667199e8a55553e1865a41f43fcb7d4dd92779/LICENSE). The linked ONNX model cards declare Apache-2.0; consult their original model and dataset terms separately. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Inclusion does not imply TypeSafe endorsement or equivalent model quality. |

## When to use

Use it to prototype browser-local text classification, ordered ratings, or yes/no judgments with inspectable probabilities. It is useful when you want to explore the typed-decision interface without a hosted inference account, or compare local model behavior in your own application.

Choose the [official JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) when you need TypeSafe Jev itself. This package has its own model behavior and answer contract.

## How it works

The [model adapters](https://github.com/nico-martin/open-jev/blob/52667199e8a55553e1865a41f43fcb7d4dd92779/src/models.ts) resolve three aliases:

| Alias | Model and context |
| --- | --- |
| `kev-0.6b` (default) | [Qwen3-0.6B-based Kev ONNX](https://huggingface.co/onnx-community/kev-0.6b-ONNX); configured limit of 8,192 tokens per state-plus-question branch. |
| `kev-4b` | [Qwen3-4B-based Kev ONNX](https://huggingface.co/onnx-community/kev-4b-ONNX); same branch limit, substantially larger weights and memory needs. |
| `open-jev` | [DeBERTa-v3-large ONNX](https://huggingface.co/onnx-community/open-jev-deberta-v3-large-ONNX); default 512-token total context and 256-token state budget. |

Code tokenizes one text state and each question, builds the model-specific inputs, runs inference, and applies a softmax to each question's option logits. Choice selects the highest-probability option; Score computes an expected level index and a normalized value; Noul returns a yes probability and a boolean thresholded at 0.5. Arrays preserve question order, while object keys name returned answers. Application code owns review thresholds, arithmetic, permissions, and actions.

The [answer decoder](https://github.com/nico-martin/open-jev/blob/52667199e8a55553e1865a41f43fcb7d4dd92779/src/answers.ts) differs from TypeSafe's contract: Choice/Score `confidence` is the largest single-option probability, and Noul includes `answer`, `probability`, and `confidence`. Official TypeSafe Noul uses `noul` without a separate confidence field; its Choice/Score confidence summarizes concentration. Do not reuse thresholds without checking these [confidence semantics](https://docs.typesafe.ai/confidence).

## Get started

In an existing JavaScript/TypeScript application directory, install the reviewed package and its peer dependency. Installation downloads packages, but this step does not load model weights:

```sh
npm install open-jev@0.1.2 @huggingface/transformers@4.3.0
```

Start with this **offline question-construction fragment** after installation. It only builds objects from synthetic input; it makes no inference request and produces no model answers:

```ts
import { choice, noul } from "open-jev";

const state = "Please refund the duplicate charge on my order.";
const questions = {
  team: choice("Which team should handle this message?", [
    "billing", "technical support", "other",
  ]),
  refund: noul("Does the customer request a refund?"),
};

console.log({ state, questions });
```

For optional real local inference, follow the [upstream quick start](https://github.com/nico-martin/open-jev#quick-start): explicitly load a model with `OpenJev.load`, call `decide` with the state and questions, inspect the complete answers, and release the session with `dispose`. Prefer `truncation: "error"` while evaluating so oversized input cannot silently lose its ending. Model loading can download hundreds of megabytes or several gigabytes depending on the model and quantization; it is a separate opt-in step, not part of the offline fragment. No model download or inference was performed for this review.

## Examples and demos

The [included Vite demo](https://github.com/nico-martin/open-jev/tree/52667199e8a55553e1865a41f43fcb7d4dd92779/examples/simple) has model selection, metadata inspection, explicit loading, and decisions for support area, sentiment, and refund intent. To explore it in a separate checkout:

```sh
git clone https://github.com/nico-martin/open-jev.git
cd open-jev
git checkout 52667199e8a55553e1865a41f43fcb7d4dd92779
pnpm install --ignore-scripts
pnpm dev
```

Open Vite's local URL. Metadata inspection may contact Hugging Face even before weights are loaded. The demo fixes `dtype: "q4f16"`, so do not assume it exercises the library's automatic dtype selection on every device. This source-demo launch path was inspected, not executed; no separate hosted demo was verified.

## Limits and data handling

- State and questions are processed by the local ONNX runtime; the inspected library has no hosted inference request. Initial configuration, tokenizer, weight, and runtime downloads contact external hosts, and Transformers.js may cache assets. `OpenJev.info()` is a metadata lookup, not a guaranteed offline operation.
- Default truncation is `"cut"`, which drops trailing state tokens. Questions that exceed the applicable context budget throw. Kev's model cards say longer contexts exceed the lengths used for training; an accepted input length does not establish reliable judgment.
- Inputs require string state/instructions and model-specific option limits. Empty questions, duplicate options, and unsupported model configs are rejected. Concurrent decisions are serialized; runtime errors propagate to the caller. Code must handle failures and uncertain answers explicitly.
- Predictions do not automatically abstain: Choice always selects an option and Noul's boolean uses 0.5. Keep raw probabilities available and define application policy separately. The decoder does not provide a comprehensive guard against malformed/non-finite logits.
- Upstream describes English models trained on a limited collection of domains. Model-card accuracy and calibration results were not independently reproduced; especially do not assume out-of-domain calibration or equivalence to Jev.
- Model aliases resolve remote repositories without a caller-exposed revision pin in this wrapper. Pinning the npm version alone does not freeze model assets. Browser/backend support, memory needs, offline caching behavior, and end-to-end inference remain unverified here.

## Review and maintenance

Reviewed **2026-09-22**, npm **0.1.2** and source commit [`52667199e8a55553e1865a41f43fcb7d4dd92779`](https://github.com/nico-martin/open-jev/tree/52667199e8a55553e1865a41f43fcb7d4dd92779).

Inspected the README, MIT license, manifests, build script, model adapters, encoding, validation, answer decoder, runtime selection, and demo. The npm registry and published archive were accessible; npm's rendered package page returned HTTP 403 to the review tool. All eight implementation sources embedded in the published ESM source map matched the inspected checkout. The three model cards declare Apache-2.0. No matching existing catalog entry or open GitHub issue/PR was found by the project-name search.

Executed in an external temporary checkout with Node.js 22.19.0 and a sanitized environment:

- Dependency installation with lifecycle scripts disabled (`npm install --ignore-scripts --no-audit --no-fund --package-lock=false`) succeeded. This used npm dependency resolution rather than the upstream pnpm lockfile.
- `node node_modules/typescript/bin/tsc --project tsconfig.json --noEmit` passed.
- `node scripts/build.mjs` passed, producing ESM/CommonJS bundles and TypeScript declarations.
- The offline fragment above ran against the built ESM entry with `fetch` replaced by a throwing stub, returning the synthetic state and question objects without loading a model.
- Catalog `npm run check` passed, including Markdown, local-link, directory consistency, and offline test checks.

No upstream automated test suite or test script was found. These checks establish buildability and question construction only. Model weights, browser execution, inference, calibration, and comparative performance were not tested; no TypeSafe/provider calls were made. See the [catalog validation scope](../../../docs/validation.md#community-project-checks).

Related: [Open Alternative to Jev](open-alternative-jev.md) for Python experiments with local decision interfaces, and [NanoJev](nanojev.md) for model research and recorded game controllers.
