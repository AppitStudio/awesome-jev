# Jev examples

Four small, original recipes illustrate how to turn Jev's typed answers into application behavior. They use Python 3.10+ and its standard library. These are teaching examples, not a production SDK or measured demonstrations of model quality.

## Run offline

From the repository root:

```sh
python3 examples/run.py support-routing
python3 examples/run.py quality-rubric
python3 examples/run.py span-selection
python3 examples/run.py rag-triage
```

The default mode loads hand-authored synthetic responses. `--mock` makes that choice explicit. No account, key, package installation, or network access is needed, even if a key is present in your environment. Output identifies the mode; zero token counts in mock fixtures are placeholders, not measured usage.

| Recipe | What to adapt | Primitives |
| --- | --- | --- |
| [Support routing](support-routing/README.md) | Route a request and abstain when the department is unclear. | Choice, Noul |
| [Quality rubric](quality-rubric/README.md) | Normalize different rubric lengths and combine scores in code. | Score |
| [Span selection](span-selection/README.md) | Select an exact candidate span extracted by deterministic code. | Choice |
| [RAG passage triage](rag-triage/README.md) | Evaluate query/passage relevance, evidence, and contradictions independently. | Noul |

Each directory contains an `input.json` and `mock-response.json`. The shared [recipe functions](jev_examples/recipes.py) build requests and apply application policy. The [small HTTP client](jev_examples/client.py) implements just the contract needed here.

## Inspect or call the API

Inspect the actual generated request without making a call:

```sh
python3 examples/run.py support-routing --show-request
```

For live mode, obtain a TypeSafe API key and set `TYPESAFE_API_KEY` in your shell using your preferred secret-management method. Never put the key in these files. Live requests send the selected fixture input to TypeSafe and may incur provider charges.

```sh
python3 examples/run.py support-routing --live
```

Live mode pins `jev-1.13.0`. Set `JEV_MODEL` explicitly if evaluating a different supported version. Output reports the model returned by the API; an alias can change over time. `--show-request` always exits before a network call, including when combined with `--live`.

The client uses a 30-second per-attempt timeout and at most three attempts. It retries only HTTP 429 and 529 with backoff; `Retry-After` is honored up to a 30-second wait, after which it stops. Invalid credentials, malformed requests, other HTTP failures, and ambiguous network failures stop with an error. Server response bodies and keys are not echoed. Invalid answer IDs, types, choices, probability distributions, and scores stop processing rather than making a decision from malformed data.

## What these examples establish

- Questions in the same request are independent and evaluate the same state. One question does not consume another answer.
- Results are accessed by their question IDs. IDs themselves are not part of the model's instructions.
- Noul returns a value from 0 to 1; it does not return the `confidence` field that Choice and Score return.
- Score levels are zero-indexed and ordered. A three-level rubric returns a weighted score between 0 and 2.
- Choice selects one of the supplied options. Add an explicit `none` or `other` option where needed.
- Thresholds and weights are illustrative application policy. Confidence is not a guarantee of correctness, and high confidence does not establish factual truth or authorization.
- Retrieved or user-supplied text can steer the model. The examples do not provide a security boundary against malicious content.

The input and response fixtures are original synthetic material. They are not captured Jev output, and the confidence values are illustrative. Offline tests verify request construction, response validation, and application branches; they do not establish live API compatibility, model accuracy, reliability, or latency. Before using real data, evaluate representative cases, check current provider requirements, and define your own fallback policy.

## Computer-use decision cycle

The standalone [computer-use example](computer-use/README.md) adds a synthetic UI executor and independent assertions around form-field selection and exact source extraction. It prints raw answers, rejects stale observations, and catches incorrect completion. It does not launch or drive a browser or device.

```sh
python3 examples/computer-use/run.py
```

Its optional `--live` mode makes at most one HTTP attempt while keeping UI execution simulated. The shared runner above still supports the original four recipes. See the [computer-use guide](../docs/computer-use.md) for actual browser and native implementations.

## Check changes

```sh
python3 -m unittest discover -s examples/tests -v
```

No tests call the real provider. For all repository checks, see [Contributing](../CONTRIBUTING.md#run-checks).

Contract references: [API](https://docs.typesafe.ai/api), [models](https://docs.typesafe.ai/models), [confidence](https://docs.typesafe.ai/confidence), and [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13). These examples follow the documentation reviewed on 2026-09-18.
