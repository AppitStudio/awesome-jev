# Jev LLM router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python project that asks TypeSafe Jev which OpenAI model should handle a text query, then has an independent local Ollama model review that routing decision—without calling the selected OpenAI model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dbokatov/jev-llm-router) |
| Maintainer | [dbokatov](https://github.com/dbokatov). Independently curated. |
| Format | Python · CLI |
| Requirements | Python 3.10+; TypeSafe API key; Ollama locally. |
| License | [MIT](https://github.com/dbokatov/jev-llm-router/blob/e89e1c8a7f0f1858ff5c72e59302bb16eb44c363/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Inspect and critique Jev routing behavior offline with a second opinion.
- Mismatch: Does not execute the chosen OpenAI model.

## How it works

CLI sends the query to Jev for a route, then to Ollama for an independent review, printing probabilities. Evidence: [`jev_router/decision.py`](https://github.com/dbokatov/jev-llm-router/blob/e89e1c8a7f0f1858ff5c72e59302bb16eb44c363/jev_router/decision.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/dbokatov/jev-llm-router.git
cd jev-llm-router
pip install -e .
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit e89e1c8a7f0f](https://github.com/dbokatov/jev-llm-router/tree/e89e1c8a7f0f1858ff5c72e59302bb16eb44c363). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
