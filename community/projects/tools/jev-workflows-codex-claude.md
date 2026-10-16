# Jev Workflows for Codex and Claude Code

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source Codex and Claude Code plugin that consults Jev about tools, models, tasks, skills, context and custom decisions, diagnoses failed commands and checks completion claims against evidence; eight MCP tools, lifecycle hooks and three standalone skills.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/integrate-your-mind/jev-codex-plugin) |
| Maintainer | [integrate-your-mind](https://github.com/integrate-your-mind). Independently curated. |
| Format | Codex / Claude Code plugin (Git marketplace) with MCP server, hooks and standalone skill ZIPs |
| Requirements | Node.js 22+; Codex or Claude Code; your own `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/integrate-your-mind/jev-codex-plugin/blob/646800ee803c245ad75a95802ec86fcfdb749e0d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/0xBunny/status/2111129958978289708)). |
| Jev evidence | [`plugins/jev-workflows-claude/skills/check-completion/scripts/jev.mjs`](https://github.com/integrate-your-mind/jev-codex-plugin/blob/646800ee803c245ad75a95802ec86fcfdb749e0d/plugins/jev-workflows-claude/skills/check-completion/scripts/jev.mjs) at the pinned commit. |

## When to use

- Ask Jev which of your available tools, models or strategies fits a task before the agent commits to one.
- Have a failed command classified, or a 'done' claim checked against selected evidence, before you trust it.
- Mismatch: community Git marketplace, not an official OpenAI or Anthropic directory listing; automation is off until you enable it.

## How it works

The bundled client posts typed questions to `https://api.typesafe.ai/v1/systemone`, pinned to `jev-1.13.0` by default (Jev 1.14 or `jev-latest` only when you set `JEV_MODEL`). Hooks send text only; experimental image and Box questions need explicit batch opt-in, and receipts keep the model TypeSafe actually returned. Integration evidence: [`plugins/jev-workflows-claude/skills/check-completion/scripts/jev.mjs`](https://github.com/integrate-your-mind/jev-codex-plugin/blob/646800ee803c245ad75a95802ec86fcfdb749e0d/plugins/jev-workflows-claude/skills/check-completion/scripts/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
codex plugin marketplace add integrate-your-mind/jev-codex-plugin
codex plugin add jev-workflows@jev-workflows
# Claude Code:
claude plugin marketplace add integrate-your-mind/jev-codex-plugin
claude plugin install jev-workflows@jev-workflows
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Verification results: `VERIFICATION.md`.
- Cross-host setup: `source/jev-workflows/docs/cross-host.md`.

## Limits and data handling

Selected task context goes to TypeSafe on your key; no plugin quota, but TypeSafe charges and rate limits apply. Review and trust the hooks when your host prompts.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 646800ee803c](https://github.com/integrate-your-mind/jev-codex-plugin/tree/646800ee803c245ad75a95802ec86fcfdb749e0d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
