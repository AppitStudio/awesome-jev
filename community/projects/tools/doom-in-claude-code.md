# Doom in Claude Code (Jev pilots)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Claude Code plugin that runs ViZDoom with Freedoom in a terminal pane: Jev looks at the game screen and picks the strategy about 2.5 times a second, Claude Haiku narrates in Spanish or English, and Python reflexes and an A* navigator handle aiming and the map.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abelardodiaz/doom-in-claude-code) |
| Maintainer | [abelardodiaz](https://github.com/abelardodiaz). Independently curated. |
| Format | Claude Code plugin (Python bridge) |
| Requirements | Claude Code; Python 3.9+; a 24-bit color terminal; optional TypeSafe API key (otherwise Claude pilots). |
| License | [MIT](https://github.com/abelardodiaz/doom-in-claude-code/blob/bd438580678960320b524c73e0cfd40de4afbf30/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bridge/jev_pilot.py`](https://github.com/abelardodiaz/doom-in-claude-code/blob/bd438580678960320b524c73e0cfd40de4afbf30/bridge/jev_pilot.py) at the pinned commit. |

## When to use

- Watch a fast decision model play a real-time game next to an LLM narrator.
- A/B Jev against Claude as the pilot with `/doom claude`.
- Mismatch: finishes MAP01 on its own; later maps are still in progress.

## How it works

`bridge/jev_pilot.py` sends the current frame and state to Jev (`jev-preview`, image input) in a thread and gets back a strategy choice and a danger probability, while `doom_bridge.py` executes reflexes every four tics. Integration evidence: [`bridge/jev_pilot.py`](https://github.com/abelardodiaz/doom-in-claude-code/blob/bd438580678960320b524c73e0cfd40de4afbf30/bridge/jev_pilot.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin install doom-pane --marketplace abelardodiaz/doom-in-claude-code
# then inside Claude Code:
/doom-setup
/doom
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands and architecture in the README: [github.com/abelardodiaz/doom-in-claude-code#readme](https://github.com/abelardodiaz/doom-in-claude-code#readme)
- Changelog: [github.com/abelardodiaz/doom-in-claude-code/blob/main/CHANGELOG.md](https://github.com/abelardodiaz/doom-in-claude-code/blob/main/CHANGELOG.md)

## Limits and data handling

Game frames go to TypeSafe and narration prompts to Anthropic. Uses free Freedoom content; no original Doom files.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit bd4385806789](https://github.com/abelardodiaz/doom-in-claude-code/tree/bd438580678960320b524c73e0cfd40de4afbf30). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
