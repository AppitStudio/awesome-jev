# typesafe-agent-gates

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

LangChain / Deep Agents middleware that uses TypeSafe Jev for unattended coding-agent judgments: shell command gates, issue triage, merge-request detection, and weakened-test review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ThiagaoBR/typesafe_agent_gates) |
| Maintainer | [ThiagaoBR](https://github.com/ThiagaoBR). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **typesafe-agent-gates 0.1.0** (`typesafe_agent_gates/`); LangChain middleware + callable judges. |
| Requirements | Python ≥ 3.11; `langchain`, `langgraph`, `langchain-typesafe` (alpha—pin what you test). Live judgment needs `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/ThiagaoBR/typesafe_agent_gates/blob/04a4bc94f3506c12a2acfea5371f0dee5fab3f65/LICENSE). |

## When to use

Use it when a Deep Agents / LangChain coding agent runs unattended and regex blocklists are a poor substitute for reading what a shell command would do. Prefer [toolgate](toolgate.md) for Claude Code PreToolUse / MCP firewalls, or [pi-jev](pi-jev.md) for Pi-native gates.

## How it works

[`typesafe_agent_gates/toolgate.py`](https://github.com/ThiagaoBR/typesafe_agent_gates/blob/04a4bc94f3506c12a2acfea5371f0dee5fab3f65/typesafe_agent_gates/toolgate.py) wraps the `execute` tool with four independent Noul questions in one request (database write, production, destructive, secrets). Only `{role, command}` is sent—not the conversation. Default `fail_closed=True` holds commands when TypeSafe is unreachable. Separate modules cover triage, merge-request gates, note judgments, and spec review. Upstream includes labelled live probes under `tools/`.

## Get started

```sh
git clone https://github.com/ThiagaoBR/typesafe_agent_gates.git
cd typesafe_agent_gates
git checkout 04a4bc94f3506c12a2acfea5371f0dee5fab3f65
uv venv && uv pip install -e ".[dev]"
cp .env.example .env   # TYPESAFE_API_KEY for live probes only
pytest -q
```

`pytest` uses fake classifiers (no network). Live probes (`tools/toolgate_probe.py`, `tools/judgments_probe.py`) call TypeSafe and are billable—not run for this listing.

## Examples and demos

- README middleware wiring for `create_deep_agent` and per-subagent gates.
- [`examples/deep_agent.py`](https://github.com/ThiagaoBR/typesafe_agent_gates/blob/04a4bc94f3506c12a2acfea5371f0dee5fab3f65/examples/deep_agent.py) (needs `deepagents` + a model provider key).
- Probe scripts under [`tools/`](https://github.com/ThiagaoBR/typesafe_agent_gates/tree/04a4bc94f3506c12a2acfea5371f0dee5fab3f65/tools).

## Limits and data handling

Depends on alpha `langchain-typesafe`; pin and re-probe after criterion changes. Gate criteria include a default `CONTEXT` describing legitimate agent work—override with `context=` for your harness. Commands (not full chat history) go to TypeSafe when the gate runs. Hosted eval products elsewhere are unrelated.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 04a4bc9](https://github.com/ThiagaoBR/typesafe_agent_gates/tree/04a4bc94f3506c12a2acfea5371f0dee5fab3f65): **0.1.0**, Apache-2.0. AI-assisted source review of `toolgate.py`, judgments/triage modules, README, and license. **`pytest -q`: 36 passed** with fake classifiers on the review host. No live TypeSafe probes were run.

Related: [toolgate](toolgate.md), [pi-jev](pi-jev.md), [pi-warden](pi-warden.md).
