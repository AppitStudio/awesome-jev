# Agent Kernel (enterprise agent runtime with a TypeSafe Jev test evaluator)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Yaala Labs' runtime for running, orchestrating and deploying agents; its test framework ships a built-in `jev` evaluator (TypeSafe Noul yes/no probability) alongside DeepEval and Opik.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yaalalabs/agent-kernel) |
| Maintainer | [yaalalabs](https://github.com/yaalalabs). Independently curated. |
| Format | Python runtime + test framework (Apache-2.0) |
| Requirements | Python, `agentkernel[jev]`, and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/yaalalabs/agent-kernel/blob/25cce1e45b17a3c7a247583c30c6d4248290067d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ak-py/src/agentkernel/test/core/evaluator/jev.py`](https://github.com/yaalalabs/agent-kernel/blob/25cce1e45b17a3c7a247583c30c6d4248290067d/ak-py/src/agentkernel/test/core/evaluator/jev.py) at the pinned commit. |

## When to use

- Evaluate agent test cases with calibrated yes/no judgments.
- Swap evaluators without changing tests.
- Mismatch: some metrics are not supported by the Jev evaluator.

## How it works

Set `evaluator: jev` (with `mode: llm`) in test config; `JevAKEvaluator` scores agent responses via TypeSafe. See `examples/cli/jev-evaluator`. Integration evidence: [`ak-py/src/agentkernel/test/core/evaluator/jev.py`](https://github.com/yaalalabs/agent-kernel/blob/25cce1e45b17a3c7a247583c30c6d4248290067d/ak-py/src/agentkernel/test/core/evaluator/jev.py).

## Get started

Install `agentkernel[jev]`, set `TYPESAFE_API_KEY`, and run the `examples/cli/jev-evaluator` tests.

```sh
git clone https://github.com/yaalalabs/agent-kernel.git && cd agent-kernel
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example: [github.com/yaalalabs/agent-kernel/tree/25cce1e45b17a3c7a247583c30c6d4248290067d/examples/cli/jev-evaluator](https://github.com/yaalalabs/agent-kernel/tree/25cce1e45b17a3c7a247583c30c6d4248290067d/examples/cli/jev-evaluator)

## Limits and data handling

Test inputs and agent outputs go to TypeSafe during Jev evaluation.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 25cce1e45b17](https://github.com/yaalalabs/agent-kernel/tree/25cce1e45b17a3c7a247583c30c6d4248290067d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
