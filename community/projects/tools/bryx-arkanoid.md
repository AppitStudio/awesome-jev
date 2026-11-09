# BRYX (Rust brick-breaker whose autopilot asks a TypeSafe System One model where to aim)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Single-player wgpu brick-breaking game in Rust; with the `typesafe` feature, a System One model picks which part of the wall to attack at each serve and paddle hit while code flies the paddle.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chussenot/arkanoid) |
| Maintainer | [chussenot](https://github.com/chussenot). Independently curated. |
| Format | Rust game (MIT) |
| Requirements | Rust toolchain; `TYPESAFE_API_KEY` and `--features typesafe` for the Jev autopilot (heuristic autopilot needs no network). |
| License | [MIT](https://github.com/chussenot/arkanoid/blob/8db5745ae6119bde2d12b65e38861b1b16a9f11c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/autopilot/advisor.rs`](https://github.com/chussenot/arkanoid/blob/8db5745ae6119bde2d12b65e38861b1b16a9f11c/src/autopilot/advisor.rs) at the pinned commit. |

## When to use

- Watch a decision model play a game in real time.
- Study an async, latency-budgeted model call in a game loop.
- Mismatch: Jev only drives the optional autopilot.

## How it works

`autopilot/advisor.rs` builds the hosted client from `TYPESAFE_API_KEY` via the `judgment` crate (model `TYPESAFE_MODEL` or `jev-latest`); the game never waits and falls back to a heuristic on late or unconfident answers. Integration evidence: [`src/autopilot/advisor.rs`](https://github.com/chussenot/arkanoid/blob/8db5745ae6119bde2d12b65e38861b1b16a9f11c/src/autopilot/advisor.rs).

## Get started

Clone and run `TYPESAFE_API_KEY=... cargo run --release --features typesafe -- --autopilot`.

```sh
git clone https://github.com/chussenot/arkanoid.git && cd arkanoid
TYPESAFE_API_KEY=... cargo run --release --features typesafe -- --autopilot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Autopilot design: [github.com/chussenot/arkanoid/blob/8db5745ae6119bde2d12b65e38861b1b16a9f11c/docs/autopilot.md](https://github.com/chussenot/arkanoid/blob/8db5745ae6119bde2d12b65e38861b1b16a9f11c/docs/autopilot.md)

## Limits and data handling

Board state is sent to TypeSafe on each consulted shot.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 8db5745ae611](https://github.com/chussenot/arkanoid/tree/8db5745ae6119bde2d12b65e38861b1b16a9f11c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
