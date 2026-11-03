# Aura Autopilot (open-source game tester for Unreal, Unity and Godot that plays in real time with Jev making the moves)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Open-source playtesting agent from the team behind Aura: describe what to explore, test, verify or achieve, and it plays your game in the editor, finds broken mechanics and gets better run after run. A coding agent writes harnesses for the game, and Jev makes the real-time play decisions inside them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ramenvr/autopilot) |
| Maintainer | [ramenvr](https://github.com/ramenvr). Independently curated. |
| Format | Unreal, Unity and Godot editor plugin (Python agent service) |
| Requirements | Unreal Engine 5.4+, Unity 6 or Godot 4.7+ on Windows or macOS; an Aura account, or your own Anthropic and `TYPESAFE_API_KEY` keys (or a Claude Code / Codex subscription plus a TypeSafe key). |
| License | [Apache-2.0](https://github.com/ramenvr/autopilot/blob/31cb1e5cc02abcce1a91367abb87718803ab983a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/xyntechx/status/2117292394769256824)). |
| Jev evidence | [`autopilot/runtime.py`](https://github.com/ramenvr/autopilot/blob/31cb1e5cc02abcce1a91367abb87718803ab983a/autopilot/runtime.py) at the pinned commit. |

## When to use

- Let an agent playtest a level, check a feature or chase a goal after each code change.
- Mismatch: the first runs are rough while it builds project memory; the recommended path uses an Aura account.

## How it works

`autopilot/runtime.py` runs the harness tick loop on the live game and asks Jev, through `typesafe_sdk`'s `TypeSafeClient` pinned to `jev-1.13.0`, the choice and score questions that pick each action, with a 1.5 s timeout and a kept-warm connection; executors carry the moves out and every step is traced. Integration evidence: [`autopilot/runtime.py`](https://github.com/ramenvr/autopilot/blob/31cb1e5cc02abcce1a91367abb87718803ab983a/autopilot/runtime.py).

## Get started

Prebuilt packages for each engine are on [tryaura.dev/autopilot](https://www.tryaura.dev/autopilot). Building from source (Unreal only), from the upstream README (not run on the review host):

```sh
git clone https://github.com/ramenvr/autopilot.git
cd autopilot
powershell -ExecutionPolicy Bypass -File tools\build_unreal.ps1 -EngineDir "C:\path\to\UnrealEngine" -PluginsDir "C:\path\to\YourProject\Plugins"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product page and whitepaper results: [www.tryaura.dev/autopilot](https://www.tryaura.dev/autopilot)
- Creator's post on BYOK use with a TypeSafe key: [x.com/xyntechx/status/2117292394769256824](https://x.com/xyntechx/status/2117292394769256824)

## Limits and data handling

Game state and harness questions go to TypeSafe (and code context to the coding agent you choose) on your keys or through your Aura account. Run sharing is optional. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 31cb1e5cc02a](https://github.com/ramenvr/autopilot/tree/31cb1e5cc02abcce1a91367abb87718803ab983a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
