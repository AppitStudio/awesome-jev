# jev-mcp (legostin)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server that lets Claude Code, Codex, and other MCP agents drive a real Chrome browser while TypeSafe Jev answers typed element/action questions with calibrated confidence—the agent plans; Jev executes small browser decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/legostin/jev-mcp) |
| Maintainer | [legostin](https://github.com/legostin). Independently curated. |
| Format | TypeScript MCP server + Chrome extension helper. |
| Requirements | Node.js ≥ 22.18; Chrome; TypeSafe (or configured) Jev provider key. |
| License | [MIT](https://github.com/legostin/jev-mcp/blob/392a4f2d872d2f60fd90f5750ca14aef81f4bf31/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live browser/MCP sessions not run. Distinct from [jev-mcp (jkudish)](jev-mcp.md). |

## When to use

Use when an agent should **plan** while Jev executes fast typed browser decisions with confidence gates. Prefer [jev-chrome-mcp](jev-chrome-mcp.md) / [jev-ra](jev-ra.md) for other MCP browser stacks, or [jev-mcp (jkudish)](jev-mcp.md) for judgment tools without Chrome driving.

## How it works

MCP tools snapshot a filtered page model; Jev answers Choice/Score/Noul questions (which element, did the click work). Low-confidence paths ask the agent. Decisions are traced for replay. Upstream latency/cost figures were not re-measured here.

## Get started

```sh
git clone https://github.com/legostin/jev-mcp.git
cd jev-mcp
git checkout 392a4f2d872d2f60fd90f5750ca14aef81f4bf31
# follow README Quick start: install, configure provider key, register MCP, load Chrome helper
```

Live Chrome automation sends page content to the Jev provider and can incur charges.

## Examples and demos

- Upstream website/docs and `evals/` materials (not re-run here).
- MCP tool list and confidence/HITL notes in the README.

## Limits and data handling

Browser content and goals reach the Jev provider. Review upstream safety gates before irreversible actions. Performance claims are upstream-reported.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 392a4f2](https://github.com/legostin/jev-mcp/tree/392a4f2d872d2f60fd90f5750ca14aef81f4bf31). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [jev-mcp (jkudish)](jev-mcp.md), [jev-chrome-mcp](jev-chrome-mcp.md), [jev-ra](jev-ra.md).
