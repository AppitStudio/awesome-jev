# jev-judge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pytest/Vitest-style CI evaluations of LLM and RAG outputs: declarative YAML tests (faithfulness, relevance, hallucination, guardrails) answered by TypeSafe Jev noul/score questions instead of an LLM-as-a-judge, with JSON/Markdown reports and an MCP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/00200200/jev-judge) |
| Maintainer | [00200200](https://github.com/00200200). Independently curated. |
| Format | Python CLI + library + MCP server |
| Requirements | Python 3.10+; `TYPESAFE_API_KEY`. The README's `pip install jev-judge` was **not** found on PyPI at review — install from the repository. |
| License | [MIT](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Gate RAG/support-bot changes in CI with faithfulness and hallucination checks on fixed cases.
- Export JSON or Markdown reports to CI summaries or observability tools.
- Mismatch: judgments are calibrated probabilities, not explanations.

## How it works

Each YAML test lists context/input/output and assertions; [`jev_judge/evaluators.py`](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/jev_judge/evaluators.py) maps them to Jev noul (pass/fail) and score (1–5) questions via [`jev_judge/client.py`](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/jev_judge/client.py), and the runner compares results to thresholds.

## Get started

Install from source and run the bundled evals (live TypeSafe calls):

```sh
pip install git+https://github.com/00200200/jev-judge.git@5d4ac63cad80a87b4c7930aeb49fd607372fb671
export TYPESAFE_API_KEY=...
jev-judge test evals/ --threshold 0.85 --markdown > report.md
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README YAML example `evals/customer_support.yaml`.
- README benchmark table (upstream-reported timings and costs).

## Limits and data handling

Latency/cost figures in the README are upstream; the PyPI package named in the README was not published at review. Test inputs/outputs are sent to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 5d4ac63cad80](https://github.com/00200200/jev-judge/tree/5d4ac63cad80a87b4c7930aeb49fd607372fb671). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
