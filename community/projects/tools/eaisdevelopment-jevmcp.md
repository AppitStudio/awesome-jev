# jevmcp (eaisdevelopment)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single Agent Plugins-format install (`jevmcp`) exposing TypeSafe Jev MCP tools and skills for spec-drift checking, CI failure triage, and code-rule audits so the heavy agent only investigates what Jev flags.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eaisdevelopment/jevmcp) |
| Maintainer | [eaisdevelopment](https://github.com/eaisdevelopment). Independently curated. |
| Format | Agent Plugins package with MCP server + skills under `plugins/`. |
| Requirements | Claude Code, Codex, or other Agent Plugins client; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/eaisdevelopment/jevmcp/blob/1c20ed436e3b366ddd0a75bef1448885a240bf8c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live CI/spec runs not executed. Distinct from other jev MCP servers. |

## When to use

Use to **screen** specs, CI logs, and convention rules with Jev before spending frontier tokens. Prefer [askjev](askjev.md) / [jev-mcp (jkudish)](jev-mcp.md) for general judgment MCP tools.

## How it works

Skills call shared MCP tools (`check_spec_drift`, `triage_ci_failure`, `check_code_rules`, plus draft/validate helpers). First-time setup drafts a local `spec_map.json` pairing requirements to code ranges for review.

## Get started

```sh
git clone https://github.com/eaisdevelopment/jevmcp.git
cd jevmcp
git checkout 1c20ed436e3b366ddd0a75bef1448885a240bf8c
# install plugin per claude_how_to_jevmcp.md / codex_how_to_jevmcp.md
```

## Examples and demos

- `spec_map.json` example pairing.
- Skill docs inside the plugin tree.

## Limits and data handling

Code and CI logs reach TypeSafe when tools run. Map drafting is local until you invoke checks.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 1c20ed4](https://github.com/eaisdevelopment/jevmcp/tree/1c20ed436e3b366ddd0a75bef1448885a240bf8c). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [askjev](askjev.md), [jev-mcp (jkudish)](jev-mcp.md), [pymodel-jev-judge-mcp](pymodel-jev-judge-mcp.md).
