# DocJev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Classify or split PDF/DOCX/PPTX packets with local LiteParse OCR text and TypeSafe Jev category/boundary judgments; optional LlamaParse for hard scans.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jerryjliu/docjev) |
| Maintainer | [jerryjliu](https://github.com/jerryjliu). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package/CLI **docjev** (alias `jev-docs`); local visual demo optional. |
| Requirements | Python ≥ 3.11, `TYPESAFE_API_KEY`. Optional `LLAMA_CLOUD_API_KEY` / `OPENAI_API_KEY`. DOCX/PPTX need LibreOffice. |
| License | [Apache-2.0](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/LICENSE). TypeSafe and optional cloud OCR have separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest run; live Jev classify/split and billed OCR not run. |

## When to use

Use it for inbox-style document classification and multi-document PDF splitting with typed Jev answers over extracted page text. Prefer [doc-router](doc-router.md) when you only need page-level OCR routing rather than category/boundary judgments. Distinct from LlamaIndex hosted Classify/Split APIs (explicitly not used).

## How it works

LiteParse (or optional LlamaParse) extracts page text; [`engines/jev.py`](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/src/jev_docs/engines/jev.py) calls TypeSafe via `typesafe-sdk` with `Choice`/`Noul` questions for category or split boundaries. Application code owns rules YAML, PDF export, and metrics. Jev inference is hosted even when OCR is local.

## Get started

```sh
git clone https://github.com/jerryjliu/docjev.git
cd docjev
git checkout 9ed0fe05984ce1906af9272b8b400c8d46520f98
uv sync
# export TYPESAFE_API_KEY=...
uv run docjev doctor --smoke
```

Live classify/split examples are in the upstream README (incurs TypeSafe charges).

## Examples and demos

- Upstream README Quick start, rules YAML, and visual report under `docs/report/`.
- Local demo: `uv sync --extra demo` then `uv run docjev demo` (needs keys for live runs).
- This listing ran `uv run pytest -q -m 'not live'`: **174 passed**, **3 failed** (`tests/test_ocr_contract.py` cloud-contract cases), **3 deselected**. No live TypeSafe call.

## Limits and data handling

Document text and rules reach TypeSafe for judgments. Optional LlamaParse/OpenAI paths send content to those providers. Treat upstream accuracy/timing tables as reported, not re-measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9ed0fe0](https://github.com/jerryjliu/docjev/tree/9ed0fe05984ce1906af9272b8b400c8d46520f98): Apache-2.0; AI-assisted source review of README, LICENSE, `engines/jev.py`, CLI; offline pytest as above. No live TypeSafe call.

Related: [doc-router](doc-router.md), [jev-table](jev-table.md), [llama-index-jev](llama-index-jev.md).
