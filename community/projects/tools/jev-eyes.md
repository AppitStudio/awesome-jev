# jev-eyes

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local OCR + spatial layout package that turns an image into the text `state` TypeSafe Jev can decide over—CLI, Python API, optional MCP—without sending pixels to Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LeddoEngano/jev-eyes) |
| Maintainer | [LeddoEngano](https://github.com/LeddoEngano). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`jev-eyes` 0.1.0): `see()` / `ask()`, CLI, optional MCP extras. |
| Requirements | Python ≥ 3.10; Pillow/numpy/RapidOCR; `TYPESAFE_API_KEY` only for `ask()` / live System One (`see()` needs no key). |
| License | [MIT](https://github.com/LeddoEngano/jev-eyes/blob/9ae9a6dc2088359a52d7092891bbf7c8f2030936/LICENSE). TypeSafe inference billed separately when used. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest -m 'not slow'` → **22 passed**, 1 skipped. Slow RapidOCR image test not required for listing. Live TypeSafe `ask()` not run. |

## When to use

Use it when you need honest, inspectable perception for a text-only Jev decision (screenshots, documents, UI) and want the OCR/layout state as the return value. Prefer full browser agents ([Jev Ultrafast](jev-ultrafast.md), [jevnav](jevnav.md)) when the loop needs click/type actions rather than a single image→state handoff.

## How it works

[`see.py`](https://github.com/LeddoEngano/jev-eyes/blob/9ae9a6dc2088359a52d7092891bbf7c8f2030936/src/jev_eyes/see.py) runs local OCR backends and builds a plain dict (`text`, `layout`, …). [`ask.py`](https://github.com/LeddoEngano/jev-eyes/blob/9ae9a6dc2088359a52d7092891bbf7c8f2030936/src/jev_eyes/ask.py) calls `TypeSafeClient().system_one(state=..., questions=...)`. [`mcp_server.py`](https://github.com/LeddoEngano/jev-eyes/blob/9ae9a6dc2088359a52d7092891bbf7c8f2030936/src/jev_eyes/mcp_server.py) exposes `see` over MCP. Pixels stay local for `see()`; the derived text state (and questions) leave the host only when `ask()` runs with a key.

## Get started

```sh
git clone https://github.com/LeddoEngano/jev-eyes.git
cd jev-eyes
git checkout 9ae9a6dc2088359a52d7092891bbf7c8f2030936
pip install -e '.[dev]'
pytest -m 'not slow'
jev-eyes see examples/sample_screen.png --show   # no API key
```

Live `ask()` / System One needs `TYPESAFE_API_KEY` and bills TypeSafe.

## Examples and demos

- Upstream `examples/sample_screen.png`, `docs/demo.gif`, agent skill under `skills/`.
- This listing: `pytest -m 'not slow'` → **22 passed**, 1 skipped. No live TypeSafe call.

## Limits and data handling

OCR quality depends on installed backends (RapidOCR/Tesseract/optional label models). `see()` never needs a key; `ask()` sends state+questions to TypeSafe. Not a VLM substitute—escalate when `needs_vision`-style gates are high. Benchmarks/cost claims were not re-measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9ae9a6d](https://github.com/LeddoEngano/jev-eyes/tree/9ae9a6dc2088359a52d7092891bbf7c8f2030936): MIT; AI-assisted source review of README, LICENSE, `src/jev_eyes/`, and offline unit tests. No live TypeSafe call.

Related: [doc-router](doc-router.md), [Jev Ultrafast](jev-ultrafast.md), [jevnav](jevnav.md).
