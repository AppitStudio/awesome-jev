# jev-computer-use-skill (Mrchen116)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Codex/agent skill that delegates repetitive computer-use judgments to TypeSafe Jev to save LLM calls

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mrchen116/jev-computer-use-skill) |
| Maintainer | [Mrchen116](https://github.com/Mrchen116). Independently curated. Distinct from framework-scale computer-use stacks (CUA-JEV, Flick, typesafe-computer-use). |
| Format | Python · agent skill for Codex and similar agents (MIT). |
| Requirements | Python; TypeSafe API key; host agent that can load the skill per upstream README. |
| License | [MIT](https://github.com/Mrchen116/jev-computer-use-skill/blob/3ca557454b5c17fc1be2f2ba3e10af28654dc9cc/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live computer-use/Jev not run on the review host. |

## When to use

Use when an agent should offload repeated UI/action judgments to Jev while keeping planning in the main model.

## How it works

Skill describes when Codex (or peers) should ask Jev for narrow computer-use decisions instead of spending a full LLM turn.

## Get started

```sh
git clone https://github.com/Mrchen116/jev-computer-use-skill.git
cd jev-computer-use-skill
git checkout 3ca557454b5c17fc1be2f2ba3e10af28654dc9cc
# follow upstream README for skill install into Codex/agents
```

## Examples and demos

Upstream README usage notes. No live agent session on the review host.

## Limits and data handling

UI/state text may be sent to TypeSafe when live. Does not replace sandboxing.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 3ca5574](https://github.com/Mrchen116/jev-computer-use-skill/tree/3ca557454b5c17fc1be2f2ba3e10af28654dc9cc). AI-assisted README + LICENSE inspection; live paths not executed.
