# llm-openrouter-decisions (LLM CLI plugin for Jev and other models on the OpenRouter Decisions API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Plugin for Simon Willison's `llm` command line that registers every decision model on the OpenRouter Decisions API, Jev included, so you can ask yes/no, category, score, image box and multi-question requests from the shell or Python, classify CSV rows and save reusable templates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aborruso/llm-openrouter-decisions) |
| Maintainer | [aborruso](https://github.com/aborruso). Independently curated. |
| Format | Python package (PyPI) and `llm` plugin |
| Requirements | LLM 0.36+; an OpenRouter API key. |
| License | [Apache-2.0](https://github.com/aborruso/llm-openrouter-decisions/blob/cea2670147d89be0d15aed7509662994d44da2c1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`llm_openrouter_decisions.py`](https://github.com/aborruso/llm-openrouter-decisions/blob/cea2670147d89be0d15aed7509662994d44da2c1/llm_openrouter_decisions.py) at the pinned commit. |

## When to use

- Ask Jev quick typed questions from the terminal or a shell pipeline.
- Classify every row of a CSV file with the same question set.
- Mismatch: goes through OpenRouter's alpha Decisions API, not TypeSafe directly.

## How it works

`llm_openrouter_decisions.py` lists models from OpenRouter's decisions catalog and posts requests to `https://openrouter.ai/api/alpha/decisions`; Jev is reached as `openrouter-decisions/typesafe/jev-1.14` (or another listed version). Integration evidence: [`llm_openrouter_decisions.py`](https://github.com/aborruso/llm-openrouter-decisions/blob/cea2670147d89be0d15aed7509662994d44da2c1/llm_openrouter_decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
llm install llm-openrouter-decisions
llm keys set openrouter
llm aliases set jev14 openrouter-decisions/typesafe/jev-1.14
llm -m jev14 'Please refund my last payment.' -s 'Does this message explicitly request a refund?'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/aborruso/llm-openrouter-decisions#readme](https://github.com/aborruso/llm-openrouter-decisions#readme)
- PyPI: [pypi.org/project/llm-openrouter-decisions/](https://pypi.org/project/llm-openrouter-decisions/)
- Related VisiData plugin: [github.com/ondata/vd-jev](https://github.com/ondata/vd-jev)

## Limits and data handling

Prompts, files and images you pass go to OpenRouter and on to the model provider. Billed to your OpenRouter account.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit cea2670147d8](https://github.com/aborruso/llm-openrouter-decisions/tree/cea2670147d89be0d15aed7509662994d44da2c1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
