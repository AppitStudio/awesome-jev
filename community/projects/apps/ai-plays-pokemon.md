# AI Plays Pokémon (kotlinds)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Kotlin desktop app that puts an AI in front of Pokémon HeartGold on a Nintendo DS emulator: the game RAM is described as JSON, and a Jev backend picks each action from a closed list with per-option probabilities, optionally with an LLM planner in hybrid mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kotlinds/ai-plays-pokemon) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/kotlinds/ai-plays-pokemon#readme); builds on [GitHub Releases](https://github.com/kotlinds/ai-plays-pokemon/releases) (0.1.1 at review). |
| Pricing and access | Public source has **no LICENSE file** — not Open source. No app purchase fee; Jev needs your own TypeSafe key (other backends: OpenRouter/OpenAI/Anthropic keys, Ollama, Claude Code login). You must supply your own ROM. Checked 2026-10-06. |
| Jev evidence | Inspected [`decision/jev/`](https://github.com/kotlinds/ai-plays-pokemon/tree/350405ce338d0e7e3ab12aad1cd09e073c71f31b/src/main/kotlin/me/nathanfallet/aiplayspokemon/decision/jev) (`JevClient.kt`, `JevDecisionModel.kt`); README documents Jev choosing one option with a probability for every option (~150 ms). |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [kotlinds](https://github.com/kotlinds). Independently curated. |
| Format | Kotlin/Compose desktop app (Gradle) with libretro DS core |
| Platform and availability | macOS, Linux, Windows (x86-64 or Apple Silicon) via `./gradlew run` or release builds; experimental hobby project. |
| Jev's role | One of several interchangeable deciders: in pure/assisted modes Jev picks the next button or high-level action from a closed list; in hybrid mode Jev decides and an LLM planner is called when it hesitates or loops. Other modes use LLMs or an MCP-driven agent. |
| Requirements | JDK 21; a Pokémon HeartGold (USA) ROM you dumped yourself; a TypeSafe API key for the Jev backend. |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms; not Open source. Requires a Pokémon HeartGold ROM you dumped yourself. |

## When to use

- Watch and compare how a calibrated decision model and general LLMs play the same game with the same state and controller.
- Study a closed-menu action design where code walks paths and Jev only chooses among legal options.
- Mismatch: needs a legally dumped ROM; no LICENSE, so reuse terms are unspecified.

## How it works

The app reads game RAM (map, position, dialogue, menus, party, battle) and serialises it as JSON state; the chosen mode builds a closed list of actions and the Jev backend returns probabilities for each, which the app executes through the emulator controller. The UI shows exactly what the AI received and Jev's probability per option.

## Get started

Build and run with your ROM (first launch downloads the pinned DeSmuME libretro core):

```sh
git clone https://github.com/kotlinds/ai-plays-pokemon.git
cd ai-plays-pokemon
./gradlew run --args="/path/to/Pokemon - HeartGold Version (USA).nds"
# in the window: choose Jev, paste your TypeSafe key, pick a mode, press ▶
```

Each Jev decision is a TypeSafe request billed to your key; autonomous play makes many calls.

## Examples and demos

- README modes section (pure, assisted, hybrid) and the in-app *What the AI sees* JSON view.
- MCP server mode for driving the game from an external agent.

## Limits and data handling

Hobby project; no published win-rate claims checked. No LICENSE file. Game state is sent to the chosen provider. Not run on the review host (no ROM).

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 350405ce338d](https://github.com/kotlinds/ai-plays-pokemon/tree/350405ce338d0e7e3ab12aad1cd09e073c71f31b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
