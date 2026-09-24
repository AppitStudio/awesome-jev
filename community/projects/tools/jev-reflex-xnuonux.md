# jev-reflex (xnuonux)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable TypeSafe Jev decision sidecar for coding agents: stdio MCP, JSON CLI, Python API, and a Pi extension—versioned recipes for context planning, model/tool advice, failure triage, and risk flags with durable SQLite budgets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xnuonux/jev-reflex) |
| Maintainer | [xnuonux](https://github.com/xnuonux) / Eternities. Independently curated. |
| Format | Python package (`src/jev_reflex`) + MCP server + Pi adapter. |
| Requirements | Python 3; TypeSafe (or configured) provider credentials per docs. |
| License | [MIT](https://github.com/xnuonux/jev-reflex/blob/3c49e2834e47c007415dd666608a0ad2f8745c63/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live MCP/Jev not run. Distinct from other “jev-reflex” name collisions. |

## When to use

Use it when agents need **bounded Jev judgments with accounting** (budgets, dedupe, evidence hashes) rather than a thin HTTP wrapper. Prefer [pi-jev-sentinel](pi-jev-sentinel.md) for Pi-only tool gates.

## How it works

Recipes in [`src/jev_reflex`](https://github.com/xnuonux/jev-reflex/tree/3c49e2834e47c007415dd666608a0ad2f8745c63/src/jev_reflex) batch up to eight questions, reserve cost in SQLite before dispatch, and return distributions plus receipts. Uncertainty is first-class; Score is intentionally omitted in this release.

## Get started

```sh
git clone https://github.com/xnuonux/jev-reflex.git
cd jev-reflex
git checkout 3c49e2834e47c007415dd666608a0ad2f8745c63
# follow README for pip/MCP/pi install; set provider credentials
```

## Examples and demos

- `examples/` and `docs/RECIPES.md`.
- `tests/test_mcp.py` (not executed here).

## Limits and data handling

Caller-supplied excerpts leave the host for Jev. No silent provider fallback—failed attempts stay visible in accounting. Not an official TypeSafe product.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3c49e28](https://github.com/xnuonux/jev-reflex/tree/3c49e2834e47c007415dd666608a0ad2f8745c63). AI-assisted README + package layout inspection. No live TypeSafe spend.

Related: [pi-jev-sentinel](pi-jev-sentinel.md), [askjev](askjev.md), [agent-chaperone](agent-chaperone.md).
