# jev-claude-code (DarioFontanel)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Three paste-in Claude Code prompts that wire TypeSafe Jev into model/effort routing, context compaction (keep/truncate tool calls), and a 14-question diff review—distinct from packaged `claude-code-jev` hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DarioFontanel/jev-claude-code) |
| Maintainer | [DarioFontanel](https://github.com/DarioFontanel). Independently curated. |
| Format | Markdown prompt pack (`prompts/01-model-router.md`, `02-context-compaction.md`, `03-code-review.md`) plus generated project files. |
| Requirements | Claude Code; TypeSafe Jev API access for live decisions. |
| License | [MIT](https://github.com/DarioFontanel/jev-claude-code/blob/a9bf51aadbc30b93d80e80c88bf3a1446da6c8de/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Claude Code/Jev sessions not run on the review host. Distinct from RahulBalakavi/claude-code-jev. |

## When to use

Use when you want **prompt-driven Claude Code setups** for Jev routing, compaction, or review without installing a separate npm/Python package.

## How it works

Each prompt builds hooks/scripts in-repo: Jev answers typed questions; code applies thresholds (model choice, tool-call retention, BLOCK/MERGE verdicts).

## Get started

```sh
git clone https://github.com/DarioFontanel/jev-claude-code.git
cd jev-claude-code
git checkout a9bf51aadbc30b93d80e80c88bf3a1446da6c8de
# Paste prompts/01-model-router.md (or 02/03) into a Claude Code session per README
```

## Examples and demos

- Three prompt files and Italian/English README sections describing the systems.

## Limits and data handling

Prompts, diffs, and tool metadata go to TypeSafe when Jev runs. Compaction keeps user/Claude text verbatim while truncating tool payloads per policy.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit a9bf51a](https://github.com/DarioFontanel/jev-claude-code/tree/a9bf51aadbc30b93d80e80c88bf3a1446da6c8de). AI-assisted README and LICENSE inspection; live sessions not run.

Related: [claude-code-jev](claude-code-jev.md).
