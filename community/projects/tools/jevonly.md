# JevOnly

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pure-Jev browser agent: application code enumerates options from the page and goal; TypeSafe Jev only picks—no planner or helper LLM—then Chromium acts with verify/undo and an irreversible-action gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/buluoray/JevOnly) |
| Maintainer | [buluoray](https://github.com/buluoray). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package `jevonly` **0.1.0** (Apache-2.0) with CLI (`jevonly`), local viewer, and Playwright Chromium env; Node used for browser JS helpers. |
| Requirements | Python ≥ 3.12, Node.js ≥ 22, `TYPESAFE_API_KEY` (`tsk_…`). `./run.sh` creates a venv, installs Chromium, and opens `http://127.0.0.1:7791`. |
| License | [Apache-2.0](https://github.com/buluoray/JevOnly/blob/96b038d250af09a283319bd719d529ba485d4c47/LICENSE). |

## When to use

Use it to study closed-question browser automation where every action option is code-built and Jev never invents free text. Prefer [Jev Ultrafast](jev-ultrafast.md) or [pi-Jev-browser](pi-jev-browser.md) when you want a helper LLM for typing or a different host agent.

## How it works

Each step observes an accessibility snapshot, asks Jev done/off-path/next-action questions, binds field values only from facts, goal spans, or copied page values, acts in Chromium, and verifies with a before/after Jev comparison. Irreversible actions use a risk gate (`refuse` CLI default, `ask` viewer default, or `allow`). Core client posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` in [`src/jevonly/core/jev.py`](https://github.com/buluoray/JevOnly/blob/96b038d250af09a283319bd719d529ba485d4c47/src/jevonly/core/jev.py).

## Get started

```sh
git clone https://github.com/buluoray/JevOnly.git
cd JevOnly
git checkout 96b038d250af09a283319bd719d529ba485d4c47
./run.sh
# or: export TYPESAFE_API_KEY=tsk_… && jevonly run --start https://en.wikipedia.org --goal "…" --variant noaccept_kb --out events.jsonl
```

Live runs send observations and goals to TypeSafe and drive a real browser. This listing did not execute live browsing goals.

Offline tests:

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q
```

## Examples and demos

- Upstream demo GIFs/videos for Google Flights and Wikipedia goals (maintainer recordings).
- [`tests/`](https://github.com/buluoray/JevOnly/tree/96b038d250af09a283319bd719d529ba485d4c47/tests) and [`docs/`](https://github.com/buluoray/JevOnly/tree/96b038d250af09a283319bd719d529ba485d4c47/docs) architecture/events notes.
- Example CLI goals in the README.

## Limits and data handling

Goals, facts, and page observations go to TypeSafe. Viewer binds to localhost; keys stay in tab `sessionStorage` for the viewer path. English-centric goal splitting; sites that block automation are walls. Step counts and timing in the README are upstream anecdotes, not catalog benchmarks. Default gate refuses irreversible actions in the CLI.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 96b038d](https://github.com/buluoray/JevOnly/tree/96b038d250af09a283319bd719d529ba485d4c47): `jevonly` **0.1.0**, Apache-2.0. AI-assisted source review of core Jev client/loop, browser env, README, and license. On Python 3.12+ with a local venv, **`pytest`: 61 passed, 3 skipped**. No live TypeSafe calls or browser goals were performed.

Related: [pi-Jev-browser](pi-jev-browser.md), [Jev Ultrafast](jev-ultrafast.md), [Jev Browser (tontoko)](jev-browser-tontoko.md).
