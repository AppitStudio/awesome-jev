# Jev Game Engine

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Early Rust desktop prototype for controlling games through bounded goals: TypeSafe Jev selects a goal, a local executor handles movement, validation and stopping, and every decision is traced, timed and replayable; Minecraft Java 26.2 is the first integration, with an offline fixture preview.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/King4s/jev-game-engine) |
| Maintainer | [King4s](https://github.com/King4s). Independently curated. |
| Format | Rust desktop binary (`cargo run`) with fixture and live Minecraft modes |
| Requirements | Rust toolchain; Minecraft Java 26.2 server for live mode; `TYPESAFE_API_KEY` or `TYPESAFE_API_KEY_FILE`. |
| License | [MIT](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Study how a System One model can pick bounded goals while deterministic code executes.
- Inspect recorded decisions and latency per goal.
- Mismatch: early prototype; the README screenshot uses synthetic offline data.

## How it works

[`src/provider.rs`](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/src/provider.rs) calls the TypeSafe HTTP API; [`src/engine.rs`](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/src/engine.rs) and [`src/minecraft.rs`](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/src/minecraft.rs) execute goals; [`src/recording.rs`](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/src/recording.rs) traces every decision. Missing keys or rejected responses surface as visible errors, with no hidden fixture fallback.

## Get started

Try the offline preview, then live Minecraft (README *Quick start*):

```sh
git clone https://github.com/King4s/jev-game-engine.git && cd jev-game-engine
cargo run -- --fixture-preview
TYPESAFE_API_KEY=... cargo run -- --live-preview --port 25565 --bot JevBot
```

Live goals are Jev requests billed to your key and bounded by configured budgets.

## Examples and demos

- Architecture: [`docs/architecture.md`](https://github.com/King4s/jev-game-engine/blob/c9c409ba5efddd3e82b420eec85da4d13014cd6b/docs/architecture.md).

## Limits and data handling

Game observations go to TypeSafe in live mode. Prototype quality. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c9c409ba5efd](https://github.com/King4s/jev-game-engine/tree/c9c409ba5efddd3e82b420eec85da4d13014cd6b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
