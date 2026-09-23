# jevgate (craxrev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: before Bash/Write, TypeSafe Jev reports risk facts; fixed rules allow, ask, or deny—aimed at `bypassPermissions` mode. Distinct from [agy-jevgate](agy-jevgate.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/craxrev/jevgate) |
| Maintainer | [craxrev](https://github.com/craxrev). Independently curated. Not an endorsement. |
| Format | Claude Code plugin (no runtime deps). |
| Requirements | Claude Code 2.1.274+; Node 22.18+; `TYPESAFE_API_KEY`; function hooks enabled. |
| License | [MIT](https://github.com/craxrev/jevgate/blob/e361fca87ada0951399c3daa2839443b7fa826d5/LICENSE). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live Claude Code/Jev **not** run. |

## When to use

Use it when Claude Code should skip the slow built-in classifier for read-only commands and gate risky shell/file ops with typed Jev facts. Prefer [agy-jevgate](agy-jevgate.md) for Antigravity, [hookgate](hookgate.md) for audit/fail-open harness hooks.

## How it works

Read-only Bash runs immediately. Other Bash/Write-outside-repo calls get one Jev fact bundle (delete/ship/sudo/secret/upload/…); a fixed table maps facts × “asked for?” into allow/ask/deny. `/jevgate` panel shows tallies. Credential-path reads are refused.

## Get started

```sh
git clone https://github.com/craxrev/jevgate ~/jevgate
cd ~/jevgate && git checkout e361fca87ada0951399c3daa2839443b7fa826d5
claude plugin marketplace add ~/jevgate && claude plugin install jevgate
# TYPESAFE_API_KEY + CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 in ~/.claude/settings.json
```

## Examples and demos

- README sample allow/ask/deny lines and panel screenshot.

## Limits and data handling

Command text and paths go to TypeSafe when judged. Not a full sandbox. Policy thresholds are author-chosen.

## Review and maintenance

Reviewed **2026-09-23** at [commit e361fca](https://github.com/craxrev/jevgate/tree/e361fca87ada0951399c3daa2839443b7fa826d5) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [agy-jevgate](agy-jevgate.md), [hookgate](hookgate.md), [claude-code-jev](claude-code-jev.md).
