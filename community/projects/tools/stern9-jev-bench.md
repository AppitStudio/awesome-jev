# jev-bench (stern9)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark harness that asks Jev and general LLMs (via system-one-adapter) the same routing, yes/no and rating questions and reports accuracy, p50/p95 latency, calibration and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stern9/jev-bench) |
| Maintainer | [stern9](https://github.com/stern9). Independently curated. |
| Format | Python CLI |
| Requirements | Python; TypeSafe key plus keys for any LLMs you compare. |
| License | [MIT](https://github.com/stern9/jev-bench/blob/87dce85f418f9ba689f6f1193f18d17089f60707/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevbench/runner.py`](https://github.com/stern9/jev-bench/blob/87dce85f418f9ba689f6f1193f18d17089f60707/jevbench/runner.py) at the pinned commit. |

## When to use

- Measure Jev against Claude, GPT or local models on your own labelled decisions.
- Check calibration (ECE, Brier) as well as accuracy.
- Mismatch: the published 72-decision results are small and the author's own.

## How it works

Jev is called via `typesafe-sdk`; every LLM is called through TypeSafe's `system-one-adapter`, so all models receive identical questions and are scored by the same code. Integration evidence: [`jevbench/runner.py`](https://github.com/stern9/jev-bench/blob/87dce85f418f9ba689f6f1193f18d17089f60707/jevbench/runner.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -e '.[dev]'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table (2026-10-14) in the upstream README.

## Limits and data handling

Benchmark items go to TypeSafe and each compared provider, billed to your keys.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 87dce85f418f](https://github.com/stern9/jev-bench/tree/87dce85f418f9ba689f6f1193f18d17089f60707). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
