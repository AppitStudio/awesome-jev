# jev-toolkit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP-first TypeSafe/Jev toolkit: one `jev mcp` stdio server plus CLI triage/audit/label/route commands, a local JSONL event log, and optional Prometheus impact metrics.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jbt95/jev-toolkit) |
| Maintainer | [jbt95](https://github.com/jbt95). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Node.js CLI/MCP (`jev`); Effect-based TypeScript sources; harness plugins under `integrations/`. |
| Requirements | Node ≥ 26, `TYPESAFE_API_KEY`. Optional Grafana scrape of `jev meter`. |
| License | [MIT](https://github.com/jbt95/jev-toolkit/blob/4f042274249c81e6eb64b59a7ec77b6361037aa1/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline vitest run; live billed Jev not separately exercised beyond whatever the suite mocks. |

## When to use

Use it when you want a single MCP + CLI surface for typed Jev asks, failure triage, claim audit, and local impact metrics across MCP-capable harnesses. Prefer lighter [askjev](askjev.md) or [jev-mcp](jev-mcp.md) when you only need judgment tools without the audit/meter stack.

## How it works

`typesafe_ask` / `typesafe_verify` / `typesafe_review` MCP tools and `jev ask` CLI wrap TypeSafe System One question packs. Local regex hooks trigger directives; model-first audits detect claims. Events append to a local JSONL log; `jev meter serve` exposes Prometheus series. Code owns thresholds, redaction, and harness wiring.

## Get started

```sh
git clone https://github.com/jbt95/jev-toolkit.git
cd jev-toolkit
git checkout 4f042274249c81e6eb64b59a7ec77b6361037aa1
npm ci
# export TYPESAFE_API_KEY=...
# scripts/install.sh   # optional: link ~/.local/bin/jev
npx vitest run
```

Wire MCP clients with `command: jev`, `args: ["mcp"]` per upstream `docs/mcp.md`.

## Examples and demos

- Upstream CLI table (`jev triage`, `jev audit`, `jev route skills`, `jev meter`).
- This listing ran `npx vitest run`: **559 passed** across 57 files. No separate live TypeSafe spend beyond suite behavior.

## Limits and data handling

Prompts, transcripts, and review payloads can reach TypeSafe. Event logs stay local by default; treat them as sensitive. Node ≥ 26 is a hard requirement.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4f04227](https://github.com/jbt95/jev-toolkit/tree/4f042274249c81e6eb64b59a7ec77b6361037aa1): MIT; AI-assisted source review of README, LICENSE, MCP server, tests; vitest **559 pass**. Live production harness not run.

Related: [askjev](askjev.md), [jev-mcp](jev-mcp.md), [jev-harness](jev-harness.md).
