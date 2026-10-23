# Jev Claude Code Starter Kit (Jev setup, tests and templates for sales systems)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Starter kit for adding Jev to an AI sales or support system with Claude Code or Codex: setup guide and prompts, a tested Python client, a 300-reply test set with scoreboard and cost calculator, ten decision templates, a Claude Code skill and five worked examples, all runnable offline against a fake Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/onittindwani-ai/jev-claude-code-starter-kit) |
| Maintainer | [onittindwani-ai](https://github.com/onittindwani-ai). Independently curated. |
| Format | Python scripts, prompts and Claude Code skill |
| Requirements | Python 3; Claude Code or Codex (optional); a TypeSafe API key for live calls. |
| License | [MIT](https://github.com/onittindwani-ai/jev-claude-code-starter-kit/blob/145e1dcda3937e88e773c7f4fd9c0b6f293fbc6e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tools/jev.py`](https://github.com/onittindwani-ai/jev-claude-code-starter-kit/blob/145e1dcda3937e88e773c7f4fd9c0b6f293fbc6e/tools/jev.py) at the pinned commit. |

## When to use

- Get a first Jev decision running and measured in a sales or support workflow.
- Reuse ready decision sets for reply triage, lead fit and guardrails.
- Mismatch: sales-focused; results on the bundled test set may not match your inbox.

## How it works

`tools/jev.py` is the kit's client for TypeSafe's Jev API; the examples (reply router, lead scoring, call outcome router, guardrail before send) import it, and a mock server stands in when no key is set. Integration evidence: [`tools/jev.py`](https://github.com/onittindwani-ai/jev-claude-code-starter-kit/blob/145e1dcda3937e88e773c7f4fd9c0b6f293fbc6e/tools/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/onittindwani-ai/jev-claude-code-starter-kit
cd jev-claude-code-starter-kit
export TYPESAFE_API_KEY="your-key"
python3 tools/jev_check.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide: [github.com/onittindwani-ai/jev-claude-code-starter-kit/blob/main/00-SETUP-JEV.md](https://github.com/onittindwani-ai/jev-claude-code-starter-kit/blob/main/00-SETUP-JEV.md)

## Limits and data handling

Live tests send message text to TypeSafe. Scores in `results/` are the author's own runs.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 145e1dcda393](https://github.com/onittindwani-ai/jev-claude-code-starter-kit/tree/145e1dcda3937e88e773c7f4fd9c0b6f293fbc6e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
