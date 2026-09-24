# orca-jev-advisor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Orca Lab plugin that judges agent shell/tool commands with TypeSafe Jev before they run—silent on routine work, asks on force-push/merge/apply-class actions—with a local-rule fallback when no API key is set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ab2webco/orca-jev-advisor) |
| Maintainer | [ab2webco](https://github.com/ab2webco). Independently curated. |
| Format | Orca Lab / Electron plugin (Claude Code `PreToolUse` hooks). |
| Requirements | Orca Lab; optional TypeSafe API key in plugin settings (`safeStorage`). |
| License | **Unspecified** at tip (no LICENSE file). Do not assume OSI terms. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Orca/Jev not run. |

## When to use

Use it when Orca agents should get a **cheap command gate** before consequential shell actions. Prefer host-agnostic gates ([agent-chaperone](agent-chaperone.md), [toolgate](toolgate.md)) outside Orca.

## How it works

Local millisecond rules cover obvious danger; grey-area commands POST to `api.typesafe.ai` via [`src/core/jev.ts`](https://github.com/ab2webco/orca-jev-advisor/blob/04ec39f65446ca28526346913cb3ecc325912315/src/core/jev.ts). The Advisor panel counts pass/ask latency; command text is not stored—only coarse families.

## Get started

```sh
git clone https://github.com/ab2webco/orca-jev-advisor.git
cd orca-jev-advisor
git checkout 04ec39f65446ca28526346913cb3ecc325912315
# Load as an Orca development plugin or install from Ab2Web marketplace
# Settings → Jev Advisor → paste TypeSafe key → Set up Claude Code integration
```

## Examples and demos

- README command examples (silent vs ask).
- Measured latency notes in README (local vs Jev vs cache).

## Limits and data handling

Judged command context leaves the host for TypeSafe when the key is set. Hooks write into Claude Code config roots (Revert in settings). Calibration is corpus-based—treat thresholds as defaults.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 04ec39f](https://github.com/ab2webco/orca-jev-advisor/tree/04ec39f65446ca28526346913cb3ecc325912315). AI-assisted README + `src/core/jev.ts` inspection. No live Orca/TypeSafe run.

Related: [agent-chaperone](agent-chaperone.md), [claude-code-jev](claude-code-jev.md), [toolgate](toolgate.md).
