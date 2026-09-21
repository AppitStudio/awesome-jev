# jev-ra

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Fast browser-use layer for CLI coding agents (Claude Code, Codex, MCP clients): TypeSafe Jev picks each operation and target in one ~300 ms round trip; your agent plans, supplies text values, and takes over on escalation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brnyxx/jev-ra) |
| Maintainer | [brnyxx](https://github.com/brnyxx). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`jev-ra` 0.1.1 on PyPI) with MCP server, CLI, and optional npm launcher; depends on `browser-harness`. |
| Requirements | Python **≥ 3.12**; Chrome/Chromium/Edge; `JEV_RA_API_KEY`, `TYPESAFE_API_KEY`, or `OPENROUTER_API_KEY` (OpenRouter `sk-or-` keys use Decisions `typesafe/jev-1.13`; otherwise TypeSafe `jev-latest`). |
| License | [MIT](https://github.com/brnyxx/jev-ra/blob/04b0d471094bda1ccad39d775178e60591556b6b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline pytest passed; live browser/MCP sessions and live Jev calls were **not** run. Upstream benchmark speedups were not remeasured here. |

## When to use

Use it when a coding agent should drive Chrome through MCP/CLI with Jev choosing click/type targets from a structured observation, without a second LLM inside the loop. Prefer [Jev Ultrafast](jev-ultrafast.md) for the original browser-use research loop; prefer [Jev for Chrome](../apps/jev-for-chrome.md) for an in-tab extension port. Distinct focus: MCP install path for Claude Code/Codex and coding-agent packaging.

## How it works

Code builds a page observation (elements, guards). [`jev_ra/decide/client.py`](https://github.com/brnyxx/jev-ra/blob/04b0d471094bda1ccad39d775178e60591556b6b/jev_ra/decide/client.py) asks Jev for operation, target, value, and goal flags in one request via TypeSafe `/v1/systemone` or OpenRouter Decisions ([`jev_ra/config.py`](https://github.com/brnyxx/jev-ra/blob/04b0d471094bda1ccad39d775178e60591556b6b/jev_ra/config.py)). The agent supplies typed values and handles escalation. Page content and goals leave the host when Jev is called.

## Get started

```sh
export OPENROUTER_API_KEY=sk-or-...   # or TYPESAFE_API_KEY
uvx jev-ra install claude             # or: uvx jev-ra install codex
uvx jev-ra doctor
```

Pinned offline tests:

```sh
git clone https://github.com/brnyxx/jev-ra.git
cd jev-ra
git checkout 04b0d471094bda1ccad39d775178e60591556b6b
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q -o addopts=''
```

Live runs control a real browser and call Jev; they can incur charges.

## Examples and demos

- Upstream [docs/BENCHMARKS.md](https://github.com/brnyxx/jev-ra/blob/04b0d471094bda1ccad39d775178e60591556b6b/docs/BENCHMARKS.md), [docs/AGENT_INSTALL.md](https://github.com/brnyxx/jev-ra/blob/04b0d471094bda1ccad39d775178e60591556b6b/docs/AGENT_INSTALL.md), examples under `examples/`.
- Offline pytest on the review host: **437 passed**, **111 skipped**. No live Chrome MCP session.

## Limits and data handling

DOM observations, goals, and supplied values go to TypeSafe or OpenRouter. Keys are read from the environment and forwarded into MCP config—never print them. Upstream latency/cost/speedup claims are author benchmarks, not revalidated here. Requires a dedicated Chrome profile via the harness.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 04b0d47](https://github.com/brnyxx/jev-ra/tree/04b0d471094bda1ccad39d775178e60591556b6b): **0.1.1**, MIT. AI-assisted source review of README, LICENSE, `jev_ra/config.py`, `jev_ra/decide/client.py`, and tests. **`pytest -o addopts=''`: 437 passed, 111 skipped**. No live TypeSafe/OpenRouter or MCP browser session.

Related: [Jev Ultrafast](jev-ultrafast.md), [Jev Browser Skill](jev-browser-skill.md), [Jev for Chrome](../apps/jev-for-chrome.md).
