# AgentCompass (sub-agent router across coding subscriptions with a TypeSafe Jev scorer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Deterministic task router and quota scheduler for Claude Code, Codex, Gemini CLI, Grok and others, with an optional TypeSafe Jev scorer for task reasoning depth and a Windows tray app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akiiwa-games/AgentCompass) |
| Maintainer | [akiiwa-games](https://github.com/akiiwa-games). Independently curated. |
| Format | Python router + agent skill + Windows tray (MIT) |
| Requirements | Python 3.11+, the coding CLIs you route to, and optionally a TypeSafe API key for the Jev scorer. |
| License | [MIT](https://github.com/akiiwa-games/AgentCompass/blob/967855202181be6bb795ad812a19cc042c8732b5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/agent-compass/scripts/route_judge.py`](https://github.com/akiiwa-games/AgentCompass/blob/967855202181be6bb795ad812a19cc042c8732b5/skills/agent-compass/scripts/route_judge.py) at the pinned commit. |

## When to use

- Spread sub-agent work across subscriptions by strength and live quota.
- Use Jev to score task depth before choosing a model.
- Mismatch: Jev is optional; heuristics-only mode exists.

## How it works

`skills/agent-compass/scripts/route_judge.py` defines a `jev` scorer (provider typesafe, base `https://api.typesafe.ai`, `jev-latest`) that scores task reasoning depth before routing. Integration evidence: [`skills/agent-compass/scripts/route_judge.py`](https://github.com/akiiwa-games/AgentCompass/blob/967855202181be6bb795ad812a19cc042c8732b5/skills/agent-compass/scripts/route_judge.py).

## Get started

Clone, install the skill per README, and configure the Jev scorer key in the tray or env.

```sh
git clone https://github.com/akiiwa-games/AgentCompass.git && cd AgentCompass
export TYPESAFE_API_KEY=...
python skills/agent-compass/scripts/route_judge.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/akiiwa-games/AgentCompass/blob/967855202181be6bb795ad812a19cc042c8732b5/README.md](https://github.com/akiiwa-games/AgentCompass/blob/967855202181be6bb795ad812a19cc042c8732b5/README.md)

## Limits and data handling

Task summaries are sent to TypeSafe when the Jev scorer is enabled.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 967855202181](https://github.com/akiiwa-games/AgentCompass/tree/967855202181be6bb795ad812a19cc042c8732b5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
