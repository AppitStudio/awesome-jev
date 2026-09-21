# JevShield

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python runtime security gate for agent tool calls: TypeSafe Jev Choice/Noul/Score dual-factor evaluation with fail-closed parsing, calibrated-confidence routing, and a zero-config local heuristic fallback when no API key is set. Distinct from Node [jev-shield](jev-shield.md) (MCP/Gateway firewall).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lgy1027/jevshield) |
| Maintainer | [lgy1027](https://github.com/lgy1027). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **jevshield** (PyPI; optional `jevshield[langchain]`). |
| Requirements | Python ≥ 3.9; optional `JEV_API_KEY` / `TYPESAFE_API_KEY` (TypeSafe) or OpenRouter System One key. |
| License | [Apache-2.0](https://github.com/lgy1027/jevshield/blob/b669def84f0d7b71a8165ad1888d7fb9daf1a4ac/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest **29 passed / 3 skipped**; live TypeSafe smoke not run. Complements [jev-guard](jev-guard.md) / [toolgate](toolgate.md); not a drop-in for the Node `jev-shield` package. |

## When to use

Use it when Python/LangChain tool functions should be wrapped with a sub-second System One risk gate and a local heuristic path for keyless dry runs. Prefer [jev-shield](jev-shield.md) for MCP wrap via Vercel AI Gateway; prefer [toolgate](toolgate.md) for Claude Code YAML policy + audit log; prefer [jev-guard](jev-guard.md) for multi-agent session risk hooks.

## How it works

[`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/b669def84f0d7b71a8165ad1888d7fb9daf1a4ac/jevshield/client.py) posts typed Choice/Noul/Score questions to TypeSafe or OpenRouter System One. Decorators in [`decorators.py`](https://github.com/lgy1027/jevshield/blob/b669def84f0d7b71a8165ad1888d7fb9daf1a4ac/jevshield/decorators.py) combine severity tier with irreversibility, escalate low confidence, and fail closed on missing fields. Without a key, a local heuristic engine evaluates instead of calling the network.

## Get started

```sh
git clone https://github.com/lgy1027/jevshield.git
cd jevshield
git checkout b669def84f0d7b71a8165ad1888d7fb9daf1a4ac
python3 -m pip install -e ".[dev]"  # or: pip install jevshield
python3 -m pytest tests/ -q
```

```python
from jevshield import guard, SecurityViolationError

@guard(risk_threshold="critical_danger", interactive=True)
def run_terminal(cmd: str):
    ...
```

Set `JEV_API_KEY` / `TYPESAFE_API_KEY` for live Jev (billed); omit for heuristic-only.

## Examples and demos

- Upstream `examples/` and README decorator samples.
- This listing: pytest **29 passed, 3 skipped**. No live TypeSafe call.

## Limits and data handling

Tool docstrings/arguments may reach TypeSafe/OpenRouter when a key is configured (prompt-injection framing applied upstream). Heuristic mode is not a neural judgment. Latency/cost marketing claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b669def](https://github.com/lgy1027/jevshield/tree/b669def84f0d7b71a8165ad1888d7fb9daf1a4ac): Apache-2.0; AI-assisted source review of README, LICENSE, `jevshield/`, and pytest. No live TypeSafe call.

Related: [jev-shield](jev-shield.md), [jev-guard](jev-guard.md), [toolgate](toolgate.md), [typesafe-agent-gates](typesafe-agent-gates.md).
