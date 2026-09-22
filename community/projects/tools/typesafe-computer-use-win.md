# typesafe-computer-use-win

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Windows port of [typesafe-computer-use](typesafe-computer-use.md): deterministic UI Automation + OCR observations, TypeSafe Jev multi-Choice decisions per step, and an optional writer model only for free text (`winclicker`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vatsa10/typesafe-computer-use-win) |
| Maintainer | [Vatsa10](https://github.com/Vatsa10) (port); macOS original by [awlevin](https://github.com/awlevin/typesafe-computer-use). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`typesafe-computer-use-win` 0.1.0** (CLI `winclicker` / inspect / daemon / UI). |
| Requirements | Windows 10/11; Python ≥ 3.12; `TYPESAFE_API_KEY`; optional Anthropic (or configured writer) for free-text fields. WinRT/UIAutomation wheels are Windows-native. |
| License | [MIT](https://github.com/Vatsa10/typesafe-computer-use-win/blob/5c00b0398b48e3270382f757ff14e4a9fe1fd7eb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source inspected on a Linux review host where WinRT wheels cannot build; desktop control and live TypeSafe not run here. Upstream CI on tip was **failure** at review time—re-check before trusting release health. |

## When to use

Use it when you want the **macOS typesafe-computer-use loop on Windows** (UIA + built-in OCR, Jev for action choice). Prefer [typesafe-computer-use](typesafe-computer-use.md) on Mac, or browser agents when the target is the DOM. Do not treat it as a permission boundary for arbitrary desktop tasks.

## How it works

Perception builds a structured screen state. [`decide.py`](https://github.com/Vatsa10/typesafe-computer-use-win/blob/5c00b0398b48e3270382f757ff14e4a9fe1fd7eb/typesafe_computer_use_win/decide.py) posts multi-Choice (and verify Noul) questions via `typesafe_sdk.TypeSafeClient.system_one`. Code executes only the selected branch; a writer model is used when typing free text is required.

## Get started

```sh
# On Windows 10/11:
git clone https://github.com/Vatsa10/typesafe-computer-use-win.git
cd typesafe-computer-use-win
git checkout 5c00b0398b48e3270382f757ff14e4a9fe1fd7eb
uv sync
# Export TYPESAFE_API_KEY; then: uv run winclicker "your goal" --act
```

Live steps send screen-derived text/context to TypeSafe (and screenshots/context to the writer when used) and may incur charges. This Linux review host could not `uv sync` (WinRT extension build unsupported) and did not drive a desktop.

## Examples and demos

- Source review of `decide.py`, `runner.py`, and Windows OCR/UIA modules; pure modules `decide`/`dates`/`models`/`dotenv_io`/`config` compile under CPython 3 on Linux.
- Upstream README comparison table and `winclicker` examples; optional RapidOCR/voice extras.

## Limits and data handling

Screen text and goals leave the host on live decisions; writer paths may include screenshots. Abort-corner and policy limits are code-owned—inspect upstream. Windows-only dependencies; not runnable as a full stack on Linux/macOS.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 5c00b03](https://github.com/Vatsa10/typesafe-computer-use-win/tree/5c00b0398b48e3270382f757ff14e4a9fe1fd7eb): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `typesafe_computer_use_win/decide.py`. Full install/pytest blocked by WinRT on the Linux review host; upstream Actions run on this tip concluded **failure**. No live TypeSafe or Windows UI automation here.

Related: [typesafe-computer-use](typesafe-computer-use.md), [jev-macos-loop](jev-macos-loop.md), [computer-use guide](../../../docs/computer-use.md).
