# DataJev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

System-1 control loop for data analysis agents: an LLM proposes analytical steps, Python executes them, and TypeSafe Jev chooses the next trajectory action (`CONTINUE` / `SWITCH` / `VERIFY` / `STOP`). A heuristic controller supports offline smoke tests without keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zzz1YAO/DataJev) |
| Maintainer | [zzz1YAO](https://github.com/zzz1YAO). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **datajev** 0.1.0 (CLI + controllers; `uv` managed). |
| Requirements | Python 3.12; `uv`; for live control set `TYPESAFE_API_KEY` and an OpenAI-compatible analyst (`DATAJEV_LLM_*`); offline `--controller heuristic` / `examples/quickstart.py --offline` need no keys. |
| License | [MIT](https://github.com/zzz1YAO/DataJev/blob/b42d67c7f2034a802451615c7e60e2c39c174fc3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest **48 passed**; `examples/quickstart.py --offline` OK. Live TypeSafe/LLM smoke not run. |

## When to use

Use it when you want trajectory control separated from generative analysis on tabular data. Prefer plain notebooks when a single scripted path is enough. Heuristic/offline mode does not exercise Jev.

## How it works

[`datajev/controllers/jev.py`](https://github.com/zzz1YAO/DataJev/blob/b42d67c7f2034a802451615c7e60e2c39c174fc3/datajev/controllers/jev.py) posts compressed analytical state (goal, schema, recent results—not the raw CSV by default) to `https://api.typesafe.ai/v1/systemone`. Python applies the chosen verb and continues the loop. Analyst prompts and tool traffic use the configured LLM endpoint separately.

## Get started

```sh
git clone https://github.com/zzz1YAO/DataJev.git
cd DataJev
git checkout b42d67c7f2034a802451615c7e60e2c39c174fc3
uv sync
uv run pytest -q
uv run python examples/quickstart.py --offline
```

For live runs, copy `.env.example`, set TypeSafe and LLM keys, then `uv run datajev analyze …` (billed by both providers).

## Examples and demos

- `examples/quickstart.py --offline` and sample CSVs under `examples/`.
- This listing: pytest **48 passed**; offline quickstart OK. No live TypeSafe call.

## Limits and data handling

Jev sees a structured analytical state derived from the run; the analyst LLM may see richer intermediate artifacts depending on configuration. Heuristic control is not a neural judgment. Quality claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b42d67c](https://github.com/zzz1YAO/DataJev/tree/b42d67c7f2034a802451615c7e60e2c39c174fc3): MIT; AI-assisted source review of README, LICENSE, `datajev/`, pytest, and offline quickstart. No live TypeSafe call.

Related: [daf-jev](daf-jev.md), [decision-first](decision-first.md), [hunch](hunch.md).
