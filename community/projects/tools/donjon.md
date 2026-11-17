# Donjon by game-design-projects (hand-drawn dungeon crawler where you can talk to the monsters, and Jev decides how they feel and act)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Godot 4.7 dungeon crawler with Undertale-style fights in a 3D set drawn as glowing line art, for the browser, Windows, macOS and Linux. You can talk to the monsters: each one has a personality, reacts to what you do, and may spare you, join you or turn on you. With Jev the monsters' moods and choices come from typed questions asked through a small proxy; without a key they think with local rules. Tagged releases are published on GitHub.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/game-design-projects/final-project) |
| Maintainer | [game-design-projects](https://github.com/game-design-projects). Independently curated. |
| Format | Godot 4.7 game (GDScript) with a Cloudflare Worker proxy (no license file) |
| Requirements | Godot 4.7.2 to run from source; no key needed (local rules). Jev needs the proxy deployed with a TypeSafe, OpenRouter or gateway key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/mind/jev_mind.gd`](https://github.com/game-design-projects/final-project/blob/459c6c03f7178adf07e00c8efe67c81f3f2993ed/src/mind/jev_mind.gd) at the pinned commit. |

## When to use

- Play a small dungeon crawler where monsters react with Jev-chosen moods and actions.
- Mismatch: a long commercial RPG; it is a course final project.

## How it works

`src/mind/jev_mind.gd` asks the monsters' questions through `proxy/worker.js`, a Cloudflare Worker that holds the key and forwards only System One requests to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), OpenRouter (`~typesafe/jev-latest`) or the author's gateway, with size and host limits. Integration evidence: [`src/mind/jev_mind.gd`](https://github.com/game-design-projects/final-project/blob/459c6c03f7178adf07e00c8efe67c81f3f2993ed/src/mind/jev_mind.gd).

## Get started

Import and play from source with Godot, or download a release build.

```sh
git clone https://github.com/game-design-projects/final-project donjon && cd donjon
godot --headless --path . --import
godot --path .   # plays with local rules unless the Jev proxy is configured
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/game-design-projects/final-project/releases](https://github.com/game-design-projects/final-project/releases)
- Architecture: [github.com/game-design-projects/final-project/blob/459c6c03f7178adf07e00c8efe67c81f3f2993ed/docs/ARCHITECTURE.md](https://github.com/game-design-projects/final-project/blob/459c6c03f7178adf07e00c8efe67c81f3f2993ed/docs/ARCHITECTURE.md)

## Limits and data handling

With Jev on, game state for each monster goes through the proxy to the configured provider on the deployer's key. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 459c6c03f717](https://github.com/game-design-projects/final-project/tree/459c6c03f7178adf07e00c8efe67c81f3f2993ed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
