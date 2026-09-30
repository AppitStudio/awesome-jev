# WorkflowEvals

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Official TypeSafe reproducibility harness for [evals.typesafe.ai](https://evals.typesafe.ai) workflow benchmarks (invoice, customer service, agent traces, security incidents).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/typesafe-ai/WorkflowEvals) |
| Maintainer | [typesafe-ai](https://github.com/typesafe-ai). Independently curated. |
| Format | Python (uv) workflow eval runners with HF datasets and multi-provider model clients. |
| Requirements | Python 3.13+; uv; provider API keys (`TYPESAFE_API_KEY` and/or OpenAI/Anthropic/…). |
| License | [Apache-2.0](https://github.com/typesafe-ai/WorkflowEvals/blob/0ac3b8ad845429f0d8e064ecfb2430a47c5a25cb/LICENSE). Live evals incur provider charges. |
| Disclosure | Official TypeSafe org repo. AI-assisted catalog review; AppitStudio has no paid placement relationship via this listing. Live evals not run on the review host. |

## When to use

Use to reproduce published TypeSafe workflow eval results or compare models on the same workflows. Prefer smaller offline fixtures when you only need a smoke check.

## How it works

Workflows under `evals/` load cases from the Hugging Face WorkflowEvals collection; `run.py` executes a chosen `provider:model` (default `typesafe:jev-1.13.0`) with dry-run, resume, and reference comparison options.

## Get started

```sh
git clone https://github.com/typesafe-ai/WorkflowEvals.git
cd WorkflowEvals
git checkout 0ac3b8ad845429f0d8e064ecfb2430a47c5a25cb
uv sync --locked
# export TYPESAFE_API_KEY=…
# uv run python run.py invoice_processing --limit 5
# uv run python run.py invoice_processing --dry-run
```

## Examples and demos

- Site: [evals.typesafe.ai](https://evals.typesafe.ai).
- Workflows: invoice_processing, customer_service, agent_trace_observability, security_incidents.

## Limits and data handling

Live runs send cases to chosen providers and may incur charges; datasets download from Hugging Face. Catalog checks used README/license inspection only (`--dry-run` not executed here).

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 0ac3b8a](https://github.com/typesafe-ai/WorkflowEvals/tree/0ac3b8ad845429f0d8e064ecfb2430a47c5a25cb). AI-assisted README and license inspection; live evals not executed.
