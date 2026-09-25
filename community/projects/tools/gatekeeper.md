# Gatekeeper

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

YAML rulebooks plus TypeSafe Jev Choice route Claude Code prompts/skills to the right handler (allow/route/suggest/confirm/escalate/block) before the model guesses.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AgriciDaniel/gatekeeper) |
| Maintainer | [AgriciDaniel](https://github.com/AgriciDaniel). Independently curated. |
| Format | Python package + Claude Code hooks; tool-neutral engine. |
| Requirements | Python 3.11+; Claude Code for hooks; TypeSafe Jev access for live judgments. |
| License | [MIT](https://github.com/AgriciDaniel/gatekeeper/blob/bcc1c20ce501ca79cc5124ce3ea6f6c0c3bee215/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/Claude Code paths not run on the review host. |

## When to use

Use when **plain-language requests** should be routed to a specific agent/skill under explicit rules and calibrated confidence bands.

## How it works

Deterministic gate rules narrow candidates; Jev answers the remaining typed Choice; confidence bands map to verdicts. Decisions are logged with cost and rulebook version.

## Get started

```sh
git clone https://github.com/AgriciDaniel/gatekeeper.git
cd gatekeeper
git checkout bcc1c20ce501ca79cc5124ce3ea6f6c0c3bee215
pip install -e ".[test]"
python3 -m pytest -q
```

## Examples and demos

- `examples/marketing-team/` and `gatekeeper judge …` CLI samples in the README.

## Limits and data handling

Prompt text and handler names go to TypeSafe for Jev. Hook enforce mode can deny tool calls; advisory modes only annotate.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit bcc1c20](https://github.com/AgriciDaniel/gatekeeper/tree/bcc1c20ce501ca79cc5124ce3ea6f6c0c3bee215). AI-assisted README and LICENSE inspection; live hooks not run.
