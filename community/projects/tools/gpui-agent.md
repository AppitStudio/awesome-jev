# gpui-agent

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Experimental macOS-first toolkit: observe a GPUI app’s accessibility tree, ask TypeSafe Jev to choose a typed next action/target (and optional text from a bank), dispatch native input, and return a bounded run report—without sending screenshots to the model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stolinski/gpui-agent) |
| Maintainer | [stolinski](https://github.com/stolinski) / gpui-agent contributors. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust + Python runner + TypeScript/pi integration (experimental; instrumented apps only). |
| Requirements | macOS-oriented; Rust toolchain for native pieces; Python for `python/gpui_agent` (Jev policy posts to `https://api.typesafe.ai/v1/systemone`). Live Jev needs a TypeSafe API key. Requires owning/instrumenting the target GPUI app (gpui-pre + patch/hook per README). |
| License | [MIT](https://github.com/stolinski/gpui-agent/blob/6967b255bde2b117faf397677b7d587550b4e8ef/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Inspected `python/gpui_agent/jev.py` policy wiring. Full native/TypeScript suite not green in this environment (partial TS test failures; no full Rust GUI run). No live TypeSafe. |

## When to use

Use it when you want Jev to drive **your** GPUI fixtures via accessibility refs instead of putting a coding model in the per-click loop. Prefer [agent-desktop](agent-desktop.md) for general macOS a11y CLI, or browser projects ([jevnav](jevnav.md), [Footwork](footwork.md)) for web UIs.

## How it works

[`python/gpui_agent/jev.py`](https://github.com/stolinski/gpui-agent/blob/6967b255bde2b117faf397677b7d587550b4e8ef/python/gpui_agent/jev.py) builds Choice questions over enabled operations/targets (and text-bank values) and POSTs to System One. Application code owns limits, execution, and success checks. No implicit fallback to a larger generative model.

## Get started

```sh
git clone https://github.com/stolinski/gpui-agent.git
cd gpui-agent
git checkout 6967b255bde2b117faf397677b7d587550b4e8ef
# Follow upstream README for gpui-pre patch, native build, and pi `gpui_task` wiring.
python3 -c 'from python.gpui_agent import jev; print(jev.ENDPOINT)'
```

Live runs send UI observations/goal text to TypeSafe and can incur charges. Use disposable fixtures, not personal data.

## Examples and demos

- README `gpui_task({ app, goal, check })` sketch for pi.
- `examples/` and `tests/` in-repo (native/TS coverage environment-dependent).

## Limits and data handling

Experimental; not for arbitrary installed apps. Accessibility labels/values are untrusted observations. This listing did not run a live GPUI+Jev loop.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 6967b25](https://github.com/stolinski/gpui-agent/tree/6967b255bde2b117faf397677b7d587550b4e8ef) (MIT). AI-assisted review of README, LICENSE, and `python/gpui_agent/jev.py`. Import check of Jev endpoint constant succeeded; full native test matrix not claimed green here. No live TypeSafe.

Related: [agent-desktop](agent-desktop.md), [jev-macos-loop](jev-macos-loop.md), [Footwork](footwork.md).
