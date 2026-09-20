# ExcelPilot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Live cross-platform Excel agent: Office.js task pane or headless openpyxl/DuckDB workflows, with Qwen for planning and TypeSafe Jev for intent routing, tool gating, and claim checks (cascade to OpenRouter / offline policy).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vikramlingam/excelpilot) |
| Maintainer | [vikramlingam](https://github.com/vikramlingam). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **excelpilot 1.0.0** + React Office.js add-in (uv / FastMCP tools). |
| Requirements | Python ≥ 3.12; Excel on macOS/Windows for the add-in; `TYPESAFE_API_KEY` and/or `OPENROUTER_API_KEY` per cascade. |
| License | [MIT](https://github.com/vikramlingam/excelpilot/blob/701e24c7122844c2a326ed5d8c9a04a808d296ee/LICENSE). |

## When to use

Use it to drive an open workbook with approval cards, snapshots, and undo while Jev gates intents and tools. Prefer lighter CLIs when you only need a one-shot spreadsheet judgment. Workbook contents can leave the host for providers when live.

## How it works

[`server/excelpilot/agent/jev/client.py`](https://github.com/vikramlingam/excelpilot/blob/701e24c7122844c2a326ed5d8c9a04a808d296ee/server/excelpilot/agent/jev/client.py) tries TypeSafe System One, then OpenRouter System One, then a local deterministic policy. Gates in `agent/jev/gates.py` judge intent/tier; Qwen (OpenRouter) plans and calls FastMCP Excel tools. Pre-write snapshots support rollback.

## Get started

```sh
git clone https://github.com/vikramlingam/excelpilot.git
cd excelpilot
git checkout 701e24c7122844c2a326ed5d8c9a04a808d296ee
uv sync
cp .env.example .env   # TYPESAFE_API_KEY / OPENROUTER_API_KEY
uv run python -m excelpilot doctor
./start.sh             # sideload add-in + local servers
```

Live agent turns send workbook context and prompts to providers and can incur charges. This listing did not launch Excel or run live inference.

## Examples and demos

- README one-command launch and Office.js sideload notes.
- Offline tests under `tests/` (store, gates, Jev cascade probes).

## Limits and data handling

Sheet data and user prompts may leave the machine for TypeSafe/OpenRouter. Destructive tools can change workbooks—use approval/undo. Upstream cascade probe results were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 701e24c7](https://github.com/vikramlingam/excelpilot/tree/701e24c7122844c2a326ed5d8c9a04a808d296ee): **1.0.0**, MIT. AI-assisted source review of README, `jev/client.py`, gates, `pyproject.toml`, and license. `uv` install, Excel sideload, and live provider calls were not executed on the review host.

Related: [SlidePilot](slidepilot.md), [SemDecide](semdecide.md), [toolgate](toolgate.md).
