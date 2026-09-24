# jev-guard (muratcakmak)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin with PreToolUse-style hooks that combine local regex rules and batched TypeSafe Jev `noul` scores to deny rule-breaking edits and unasked-for deploys; every scorer failure path fail-opens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muratcakmak/jev-guard) |
| Maintainer | [muratcakmak](https://github.com/muratcakmak). Independently curated. |
| Format | TypeScript Claude Code plugin (`hooks/`, `scripts/`). |
| Requirements | Claude Code; TypeSafe/Jev endpoint access for JEV_RULES (regex rules need no network). |
| License | [MIT](https://github.com/muratcakmak/jev-guard/blob/304036789298d13f951183abe0fc46d6c6c43bfc/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Claude sessions not run. Distinct from [jev-guard](jev-guard.md) (leepokai) and [jev-guard (CMaintz)](cmaintz-jev-guard.md). |

## When to use

Use to **enforce** CLAUDE.md-class rules as denied tool calls with corrections attached. Prefer [agent-chaperone](agent-chaperone.md) for multi-agent MCP firewalls.

## How it works

`REGEX_RULES` decide locally; `JEV_RULES` batch to Jev per tool call. Deploy gate asks whether a Bash command deploys/publishes and whether the user asked for it. Long-running commands can be rewritten to background.

## Get started

```sh
git clone https://github.com/muratcakmak/jev-guard.git
cd jev-guard
git checkout 304036789298d13f951183abe0fc46d6c6c43bfc
# install Claude Code plugin per .claude-plugin/plugin.json
```

## Examples and demos

- `hooks/guard.test.mjs` and `scripts/__tests__/` (not re-run here).
- README rule tables.

## Limits and data handling

Tool-call snippets reach Jev when JEV_RULES fire. Fail-open means outages do not block—by design.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3040367](https://github.com/muratcakmak/jev-guard/tree/304036789298d13f951183abe0fc46d6c6c43bfc). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [jev-guard](jev-guard.md), [cmaintz-jev-guard](cmaintz-jev-guard.md), [agent-chaperone](agent-chaperone.md).
