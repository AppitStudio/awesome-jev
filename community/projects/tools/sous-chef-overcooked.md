# Sous Chef (voice-controlled Overcooked! 2 assistant chef where Jev maps your requests to kitchen tasks)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

In-game agent for Overcooked! 2 that plays Player 2 as your assistant chef: you say or type "toss me onions" or "wash the dishes", Jev matches the request to a supported task and target in the live kitchen (asking for clarification when unsure), and a programmed scheduler and pathfinder carry it out.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Henry-The-Yang-101/sous-chef) |
| Maintainer | [Henry-The-Yang-101](https://github.com/Henry-The-Yang-101). Independently curated. |
| Format | BepInEx C# game plugin plus a Python harness with browser controls (no license file) |
| Requirements | macOS, Overcooked! 2 on Steam, Python 3.12+, and a TypeSafe key (`JEV_API_KEY`) for typed or spoken commands; voice needs macOS 27+ with Xcode 27 Swift tools. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/decision/transport.py`](https://github.com/Henry-The-Yang-101/sous-chef/blob/8afd106e3e296ea2420adb34a39694bf33735eb1/harness/decision/transport.py) at the pinned commit. |

## When to use

- Play Overcooked! 2 with a voice-commanded AI teammate.
- Mismatch: Windows/Linux or automatic multi-agent play (assistant mode only so far).

## How it works

`harness/decision/transport.py` calls `api.typesafe.ai` with model `jev-1.14.0` (set in `harness/decision/config.py`). Jev only picks high-level tasks; a Least-Laxity-First scheduler and Dijkstra/A* pathfinding run in code. The author reports most rounds cost under $0.008. Integration evidence: [`harness/decision/transport.py`](https://github.com/Henry-The-Yang-101/sous-chef/blob/8afd106e3e296ea2420adb34a39694bf33735eb1/harness/decision/transport.py).

## Get started

Install the plugin and launch the game, start the harness and open the browser controls; add your key to `.env` for Jev commands.

```sh
python3 scripts/install.py
python3 scripts/launch.py
python3 -m harness.server --local-only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Henry-The-Yang-101/sous-chef/blob/8afd106e3e296ea2420adb34a39694bf33735eb1/README.md](https://github.com/Henry-The-Yang-101/sous-chef/blob/8afd106e3e296ea2420adb34a39694bf33735eb1/README.md)

## Limits and data handling

Your typed or transcribed requests and kitchen state go to TypeSafe on your key. The optional sharing feature can open a temporary Cloudflare tunnel to the local controls.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 8afd106e3e29](https://github.com/Henry-The-Yang-101/sous-chef/tree/8afd106e3e296ea2420adb34a39694bf33735eb1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
