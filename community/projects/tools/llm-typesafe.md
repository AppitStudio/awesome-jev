# llm-typesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

[Simon Willison’s LLM](https://llm.datasette.io/) plugin that exposes TypeSafe Jev (`typesafe/jev-latest`, alias `jev`) for noul, choice, and score evaluations from the CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/simonw/llm-typesafe) |
| Maintainer | [simonw](https://github.com/simonw). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | PyPI / `llm` plugin package **`llm-typesafe` 0.1a0** (entry point `typesafe`). |
| Requirements | Python ≥ 3.10; `llm>=0.35`, `httpx2`, `pydantic`. Live calls need an LLM key named `typesafe` (`llm keys set typesafe`) for `https://api.typesafe.ai/v1/systemone`. |
| License | [Apache-2.0](https://github.com/simonw/llm-typesafe/blob/225932cfde461ee6e38ae2b612040c50c086db8c/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest`: **58 passed** at reviewed tip. Upstream GitHub Actions Test + Publish **success** on the same SHA. No live TypeSafe calls here. |

## When to use

Use it when you already use the LLM CLI and want one-shot TypeSafe Jev noul/choice/score answers without writing a custom client. Prefer dedicated SDKs ([typesafe-cli](typesafe-cli.md), [tumf-jev-cli](tumf-jev-cli.md), language clients) when you need library APIs rather than LLM’s model interface.

## How it works

[`llm_typesafe.py`](https://github.com/simonw/llm-typesafe/blob/225932cfde461ee6e38ae2b612040c50c086db8c/llm_typesafe.py) registers a TypeSafe model that POSTs to `/v1/systemone` with options for `answer_type` (noul/choice/score), `criteria`, and text vs JSON `input_format`. Default noul returns a yes-probability; replies that look like free-form generation are rejected.

## Get started

```sh
llm install llm-typesafe
llm keys set typesafe
llm -m jev 'Please refund my last payment.' -s 'Does this message explicitly request a refund?'
# From source at the reviewed commit:
git clone https://github.com/simonw/llm-typesafe.git
cd llm-typesafe
git checkout 225932cfde461ee6e38ae2b612040c50c086db8c
python3 -m pip install -e . 'httpx2-pytest>=2' pytest pytest-asyncio
python3 -m pytest -q
```

Live prompts send state/questions to TypeSafe and can incur charges.

## Examples and demos

- README documents noul, choice, score, and JSON-state examples.
- `tests/` — offline suite with `httpx2_mock` (no API key).

## Limits and data handling

Alpha (`0.1a0`). Prompt/state text leaves the host on live runs. This listing did not execute live `llm -m jev` calls.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 225932c](https://github.com/simonw/llm-typesafe/tree/225932cfde461ee6e38ae2b612040c50c086db8c) (`llm-typesafe` 0.1a0, Apache-2.0). AI-assisted review of README, LICENSE, `llm_typesafe.py`, and offline tests. **`pytest` 58 passed**. Upstream CI Test success on tip. No live TypeSafe.

Related: [typesafe-cli](typesafe-cli.md), [jev-cli (tumf)](tumf-jev-cli.md), [pytest-jev](pytest-jev.md).
