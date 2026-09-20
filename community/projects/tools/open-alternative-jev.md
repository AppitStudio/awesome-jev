# Open Alternative to Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

A Python research library that extracts typed choices and probability distributions from open-weight language models, comparing packed questions with separate inference and optional calibration.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ikermoel/open-alternative-jev) |
| Maintainer | [ikermoel](https://github.com/ikermoel). Independent community project. |
| Format | Python package `open-alternative-jev`, imported as `so1`; version 0.1.0, alpha status at review. |
| Relationship to Jev | Explores a related typed-decision interface using other models. It does not call TypeSafe, provide Jev weights, or reproduce Jev's architecture. |
| Requirements | Python 3.10+; model inference uses PyTorch, Transformers, and Accelerate, with optional vLLM or bitsandbytes. Model downloads, memory, and hardware needs depend on the chosen checkpoint/backend. |
| Access | Library source is freely available; model licenses and any hosted GPU or inference charges are separate. No TypeSafe key is needed for the local library. |
| License | [Apache-2.0 library code](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/LICENSE); external model and dataset terms require separate review. |
| Disclosure | AI-assisted independent catalog review; contributor affiliation/commercial relationships were not supplied. No TypeSafe endorsement or performance equivalence is implied. |

## When to use

Use this to study typed decisions over a shared context with local models, compare inference layouts, or fit probability calibration on labeled examples. It offers a concrete implementation and scripts for investigating how backend, model size, and question grouping affect results.

This belongs in independent model research rather than the Jev integration directory. Its benchmarks compare the library's own modes and baselines on the same open models; they do not measure performance against TypeSafe Jev.

## How it works

The [prompt builder](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/so1/prompting.py) renders a state and multiple-choice questions with option letters. The default `packed` mode writes the state once, adds question turns with fixed placeholder answers, and reads a distribution at each answer position. Later questions can attend to earlier questions and placeholders, so their decisions are not isolated.

The [Decider](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/so1/decider.py) restricts scores to each question's option labels and applies softmax. `Choice`, `yes_no`, and `scale` provide related typed interfaces; this is not the TypeSafe SDK contract. Raw label scores and probabilities are available in decision objects. `confidence` is the selected option's probability, not independently verified correctness.

In `separate` mode, each question has its own sequence. The [Transformers backend](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/so1/backends/hf.py) reads model logits. The [vLLM backend](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/so1/backends/vllm.py) uses prompt log-probabilities for packed mode and constrained one-token generation for separate mode. Packed vLLM scoring approximates labels missing from its top-k output and tracks those omissions in `missing_labels`.

## Get started

Start with the model-free schema/calibration tests. The following installs only pytest and runs the selected tests from the checkout; it does not install the full inference stack or download model weights:

```sh
git clone https://github.com/ikermoel/open-alternative-jev.git
cd open-alternative-jev
git checkout 6ad87d7ce2f4ef472acb9253419134a2643a57d2
python3 -m venv .venv
.venv/bin/python -m pip install pytest
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
  .venv/bin/python -m pytest tests/test_schema_and_calibration.py -q
```

Expected result at this revision: **5 passed**. These synthetic tests exercise option validation, decision properties, temperature scaling, cross-fold calibration, and application of a fitted temperature. They establish code behavior, not model calibration on your workload.

For real inference, follow the [upstream installation and quickstart](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/README.md#quickstart). Install the library with its inference dependencies, select a licensed checkpoint compatible with your hardware, and create a `Decider` using the `hf` or `vllm` backend. Model loading can download substantial files. The README's large quantized-model example requires much more hardware than the model-free tests above.

## Examples and demos

- [Schema and calibration tests](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/tests/test_schema_and_calibration.py): the verified offline starting path.
- [Benchmark write-up](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/benchmarks/docs/RESULTS.md) and [scripts](https://github.com/ikermoel/open-alternative-jev/tree/6ad87d7ce2f4ef472acb9253419134a2643a57d2/benchmarks/scripts): upstream experiments on shared-state throughput, question interference, calibration, and backend differences. These results were not reproduced in this review.
- [Demo link in the README](https://github.com/ikermoel/open-alternative-jev/blob/6ad87d7ce2f4ef472acb9253419134a2643a57d2/README.md): points to a Hugging Face Space. Hosted inference availability, data handling, and access limits were not validated here.

## Limits and data handling

- Raw probabilities are not calibrated out of the box. Temperature fitting needs representative labeled data and evaluation on held-out examples; the included synthetic check cannot establish real-world calibration.
- Packed questions share context and can change one another's answers. The upstream experiments describe model- and backend-dependent tradeoffs, including cases where separate inference is faster or more accurate. They do not establish a universal packing advantage.
- vLLM packed mode uses approximate top-k readout. The default prompt format targets ChatML-style models; other templates need adaptation. Review the external checkpoint's license and compatibility separately.
- The local library passes your state to the selected local model backend, not the TypeSafe API. Downloads contact model hosts; hosted demos or remote compute have their own data recipients and costs.
- The full pytest suite includes tokenizer/model loading and GPU-dependent tests. Do not describe a full test run as offline unless models are already available and network access is explicitly disabled.
- Typed output does not establish factual correctness, action authorization, or suitability for a consequential decision. Application code must handle uncertainty and downstream effects.

## Review and maintenance

Reviewed on **2026-09-20** at commit [`6ad87d7ce2f4ef472acb9253419134a2643a57d2`](https://github.com/ikermoel/open-alternative-jev/commit/6ad87d7ce2f4ef472acb9253419134a2643a57d2), package **0.1.0**. Inspected the README, Apache license, package metadata, decision/schema/calibration code, prompt construction, Transformers/vLLM backends, benchmark descriptions, and test fixtures.

Ran `python -m pytest tests/test_schema_and_calibration.py -q` with Python 3.12.14, pytest in a separate virtual environment, a credential-free environment, and Hugging Face/Transformers offline flags: **5 passed**. No checkpoint, dataset, GPU backend, hosted demo, or benchmark was executed. Catalog checks are recorded in the publication pull request.

Related: [NanoJev](nanojev.md) studies trained decision heads; [SemIf](semif.md) explores another independent typed-decision implementation.
