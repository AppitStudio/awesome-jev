# jev-claude-code (weiping)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that puts TypeSafe Jev in the agent loop: permission gate, output ladder, and subagent routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/weiping/jev-claude-code) |
| Maintainer | [weiping](https://github.com/weiping). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code marketplace plugin (`jev@jev-engineering`). |
| Requirements | Claude Code ≥2.1.196; Python 3.10+; `TYPESAFE_API_KEY` (jev-1.13.0). |
| License | [MIT](https://github.com/weiping/jev-claude-code/blob/8351fb26fd97f9031932383f820d114a973acb85/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [jev-claude-code (DarioFontanel)](dariofontanel-jev-claude-code.md). |

## When to use

Use when Claude Code should get Jev gates and routing in-loop. Prefer DarioFontanel/jev-claude-code for a paste-in prompt pack without hooks.

## How it works

Hooks call Jev for allow/ask/deny, output truncation, conditional project guidance, and subagent model routing; thresholds stay in code. Shadow mode by default. Distinct from DarioFontanel/jev-claude-code prompt pack. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/weiping/jev-claude-code.git
cd jev-claude-code
git checkout 8351fb26fd97f9031932383f820d114a973acb85
# or: claude plugin marketplace add weiping/jev-claude-code && claude plugin install jev@jev-engineering
export TYPESAFE_API_KEY=ts_...
```

Pin revision `8351fb26fd97f9031932383f820d114a973acb85` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live Claude Code/TypeSafe hooks not run on the review host. Shadow mode default until enforce. Distinct from DarioFontanel/jev-claude-code.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 8351fb2](https://github.com/weiping/jev-claude-code/tree/8351fb26fd97f9031932383f820d114a973acb85). AI-assisted README and LICENSE inspection; install/live paths not executed.
