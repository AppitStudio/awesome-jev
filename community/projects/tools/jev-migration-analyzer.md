# Jev Migration Analyzer by Ram Mehta (Claude Code skill that audits your LLM calls and finds the ones that can move to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Claude Code skill that inventories LLM calls across common SDKs, screens out work Jev should not do (prose, multi-step reasoning, arithmetic, security boundaries), sorts the rest into direct replacement, confidence-gated cascade or keep, estimates monthly cost and latency savings, and drafts before/after diffs plus a shadow-mode wrapper. It never edits code and never calls Jev itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rambmehta/jev-migration-analyzer) |
| Maintainer | [rambmehta](https://github.com/rambmehta). Independently curated. |
| Format | Claude Code skill + Python scripts |
| Requirements | Claude Code and Python 3.10+; web search in Claude Code is optional (live token prices). No TypeSafe key is needed to run the audit. |
| License | [MIT](https://github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`SKILL.md`](https://github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/SKILL.md) at the pinned commit. |

## When to use

- Find which classification, routing or scoring calls in an existing codebase are worth moving to Jev, with a shadow-mode plan before switching.
- Mismatch: proof of accuracy; it estimates and suggests, and every migration still needs validation on your own data.

## How it works

`SKILL.md` drives the six-step audit using `references/jev_primitives_guide.md` and `references/refactoring_patterns.md`; `scripts/scan_llm_calls.py` lists call sites offline and `scripts/roi_calculator.py` compares current cost with Jev's input price for direct or cascade modes. Integration evidence: [`SKILL.md`](https://github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/SKILL.md).

## Get started

Clone the skill into your Claude Code skills folder and ask for an audit, or run the scanner and ROI script directly.

```sh
git clone https://github.com/rambmehta/jev-migration-analyzer ~/.claude/skills/jev-migration-analyzer
# in Claude Code: /jev-migration-analyzer
python3 ~/.claude/skills/jev-migration-analyzer/scripts/scan_llm_calls.py path/to/repo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Shadow-mode wrappers: [github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/references/shadow_mode_wrappers.md](https://github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/references/shadow_mode_wrappers.md)
- Report template: [github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/assets/audit_report_template.md](https://github.com/rambmehta/jev-migration-analyzer/blob/7fab7c9e33a9200e7897a678fe1785afa5cae33c/assets/audit_report_template.md)

## Limits and data handling

The scanner and ROI calculator run locally with no network calls; the built-in price table may be out of date. Not affiliated with TypeSafe (stated in the README).

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 7fab7c9e33a9](https://github.com/rambmehta/jev-migration-analyzer/tree/7fab7c9e33a9200e7897a678fe1785afa5cae33c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
