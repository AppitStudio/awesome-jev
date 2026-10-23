# jev-judge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prototype CLI, library and MCP server for declarative LLM/RAG evaluations and reports. The pinned provider adapter needs compatibility and fallback repairs before it can be trusted as a CI gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/00200200/jev-judge) |
| Maintainer | [00200200](https://github.com/00200200). Independently curated. |
| Format | Python **0.1.0** CLI + library + MCP server |
| Requirements | Python 3.10+; source installation. `TYPESAFE_API_KEY` is needed for intended live calls, which may incur charges; explicit mock mode needs no key. PyPI returned 404 for `jev-judge` on 23 October 2026. |
| License | [MIT](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

Study declarative assertions and reports, or try the explicit mock demonstration. Do not use the pinned adapter as a live CI gate without repairing the behavior below.

## How it works

Tests supply context, input, output and assertions. [`evaluators.py`](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/jev_judge/evaluators.py) builds question definitions; [`client.py`](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/jev_judge/client.py) sends them and converts responses to verdicts.

The adapter reads top-level `choices` and `choice`/`probability`, whereas the current [API](https://docs.typesafe.ai/primitives/choice) returns `answers` with typed fields. Missing records default to `True` and `0.95`, potentially passing expected-true assertions without a judgment. Choice requests use `options` instead of `criteria`; Score requests omit ordered criteria. Strict mode does not repair these defects.

## Get started

For a disposable, offline inspection checkout (commands inspected, not executed in this audit):

```sh
git clone https://github.com/00200200/jev-judge.git
cd jev-judge
git checkout 5d4ac63cad80a87b4c7930aeb49fd607372fb671
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/jev-judge init
.venv/bin/jev-judge test evals/ --mock --markdown > report.md
```

`init` writes example suites and `.github/workflows/evals.yml`, overwriting those named files if present. Examples include intentional failures. `--mock` uses local heuristics, simulated latency and fixed cost fields; this checks report behavior, not Jev quality or billing. Live use needs corrected typed parsing, rejection of missing answers and response/failure tests.

## Examples and demos

- [`cli.py` initializer](https://github.com/00200200/jev-judge/blob/5d4ac63cad80a87b4c7930aeb49fd607372fb671/jev_judge/cli.py) generates `evals/rag_evals.yaml` and `evals/agent_evals.yaml`; there is no bundled `evals/` directory at the pinned revision.
- README YAML examples and benchmark table. Timing, determinism and cost claims were not independently reproduced.

## Limits and data handling

Without strict mode, a missing key selects mocks; exhausted network/parsing exceptions can also fall back to mocks without marking result records. HTTP error responses instead produce failures. Nonempty `GITHUB_ACTIONS`, or library option `strict_api=True`, disables implicit mock fallback; explicit `--mock` still works. Successful-response defaults remain unsafe in strict mode.

Cost fields are fixed per-assertion constants, including intended live results. The runner can report success with no discovered suites; require a nonempty expected case count independently.

Live calls transmit input, context and output and may incur charges. `TYPESAFE_API_URL` changes the destination receiving both state and bearer key; verify it and keep credentials out of fixtures and reports.

## Review and maintenance

Refreshed **2026-10-23** at [commit 5d4ac63cad80](https://github.com/00200200/jev-judge/tree/5d4ac63cad80a87b4c7930aeb49fd607372fb671). AI-assisted inspection of README, MIT license, metadata, client, evaluators, runner and CLI, compared with current official API docs. PyPI and pinned `evals/` returned 404. No installation, package tests, MCP session, live inference or quality/cost measurement.
