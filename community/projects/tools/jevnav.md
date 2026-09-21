# jevnav

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser automation where TypeSafe Jev picks page elements (and, in loop mode, action/goal/context), every decision is traced to JSONL, risky steps are gated, and `replay` re-resolves traces offline in CI without another model call. Distinct from [Jev Ultrafast](jev-ultrafast.md) (operation+target agent with a separate text model) by emphasizing audit traces and deterministic replay.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dtduc-git/jevnav) |
| Maintainer | [dtduc-git](https://github.com/dtduc-git). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jevnav 0.1.0** (PyPI; CLI `jevnav`; optional MCP extra). |
| Requirements | Python ≥ 3.10; Playwright Chromium; live `run`/`go` need `TYPESAFE_API_KEY` or `~/.config/typesafe/apikey.txt`. `replay` needs no key. |
| License | [Apache-2.0](https://github.com/dtduc-git/jevnav/blob/96f5438bea96dc07e5af0efef2d7ff71c3f541f4/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest (Playwright) inspected. Live TypeSafe `go`/`run` loops were not executed. |

## When to use

Use it when you want Jev-chosen clicks/fills with a portable trace you can re-check in CI after the page changes. Prefer [Jev Ultrafast](jev-ultrafast.md) or [Jev for Chrome](../apps/jev-for-chrome.md) for fuller computer-use agent loops; prefer [Jevaluate](jevaluate.md) for confidence-gated walkthrough scripts.

## How it works

[`decide.py`](https://github.com/dtduc-git/jevnav/blob/96f5438bea96dc07e5af0efef2d7ff71c3f541f4/src/jevnav/decide.py) and [`agent.py`](https://github.com/dtduc-git/jevnav/blob/96f5438bea96dc07e5af0efef2d7ff71c3f541f4/src/jevnav/agent.py) call `client.system_one` (via `jevassert`) so Jev chooses among extracted page candidates. Code applies probability/intent gates, records candidates/choice/cost in JSONL, and `replay` re-resolves fingerprints against the live DOM without calling the model. Optional `--success` selectors verify `done` claims against the page.

## Get started

```sh
git clone https://github.com/dtduc-git/jevnav.git
cd jevnav
git checkout 96f5438bea96dc07e5af0efef2d7ff71c3f541f4
uv sync
uv run playwright install chromium
uv run pytest -q --ignore=tests/test_mcp.py
# Live: uv tool install jevnav && playwright install chromium
# TYPESAFE_API_KEY=... jevnav go --goal "..." --start https://...
# Live loops send page text/candidates to TypeSafe and incur charges.
```

## Examples and demos

- Upstream README quickstarts for `go`, YAML `run` flows, and offline `replay`.
- Review host: **`uv run pytest -q --ignore=tests/test_mcp.py`**: **90 passed** (after Playwright Chromium install). MCP extra tests not run.

## Limits and data handling

Page candidates, intents, and context values used in questions leave the host toward TypeSafe on live runs. Secrets in fill values should stay in env refs (not written into traces). Replay quality depends on stable accessible names/fingerprints. Accuracy and cost of live goals were not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 96f5438](https://github.com/dtduc-git/jevnav/tree/96f5438bea96dc07e5af0efef2d7ff71c3f541f4): **0.1.0**, Apache-2.0. AI-assisted source review of README, `decide.py`, `agent.py`, LICENSE, and tests. Offline pytest: **90 passed**. No live TypeSafe calls.

Related: [Jev Ultrafast](jev-ultrafast.md), [JevOnly](jevonly.md), [Jevaluate](jevaluate.md).
