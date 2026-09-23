# jev-judge-mcp (PyModel)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed judgment MCP tools (verify/screen/find/classify/rerank/decide/…) over TypeSafe Jev — model judges, policy decides auto/review/escalate (distinct from gecm0/jev-judge-mcp).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PyModel/jev-judge-mcp) |
| Maintainer | [PyModel](https://github.com/PyModel). Independently curated. Not an endorsement. |
| Format | Python MCP server (`jev-mcp-python` / uv). |
| Requirements | Python 3.12+; `uv`; `TYPESAFE_API_KEY` (or documented provider) for live tools. |
| License | [MIT](https://github.com/PyModel/jev-judge-mcp/blob/81aedb658d04a113aac8f28a101f577c5b634ae9/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, ADR docs). Live MCP/Jev **not** run. Distinct from other `jev-judge-mcp` owners. |

## When to use

Use it when an MCP agent should call narrow typed judgment tools and leave auto/review/escalate to local policy. Prefer thinner askjev-style servers when you only need raw Noul/Choice/Score.

## How it works

MCP tools wrap TypeSafe Jev judgments; policy code maps envelopes to auto/review/escalate. Setup/install CLIs configure keys and client registrations.

## Get started

```sh
git clone https://github.com/PyModel/jev-judge-mcp.git
cd jev-judge-mcp
git checkout 81aedb658d04a113aac8f28a101f577c5b634ae9
uv sync --extra typesafe
uv run jev-mcp-python setup
uv run jev-mcp-python install
```

## Examples and demos

- README banner/CI badges and tool list.
- ADRs under `docs/adr/` (model-judges-policy-decides, etc.).

## Limits and data handling

Agent-supplied evidence goes to TypeSafe when tools run live. Paid-path contract tests exist upstream; not executed here. Policy must still own consequential actions.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 81aedb6](https://github.com/PyModel/jev-judge-mcp/tree/81aedb658d04a113aac8f28a101f577c5b634ae9) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [askjev](askjev.md), [typesafe-as-a-judge](typesafe-as-a-judge.md), [agent-chaperone](agent-chaperone.md).
