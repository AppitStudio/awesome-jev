# PitCrowd by Paul Leppard (3D open-outcry trading floor in Rust where paper traders can consult Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

A 3D trading floor in Rust and Bevy (native and in the browser): simulated pit crowds trade around a market price, paper traders (hand-written, evolved genomes and classifier-assisted ones) walk to the pits they trade, and a level-2 feed draws Bitcoin's order book as a heatmap. It runs offline on a synthetic market with no key, and real prices can be plugged in. The author built it to learn Rust and Jev and includes a Rust-plus-Jev course.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bwizrd/PitCrowd) |
| Maintainer | [Bwizrd](https://github.com/Bwizrd). Independently curated. |
| Format | Rust/Bevy app (native + wasm) with local services |
| Requirements | Rust via rustup with the wasm target and trunk for the browser floor; optional `JEV_KEY` (TypeSafe) for Jev; optional InfluxDB for the research tools. |
| License | [MIT or Apache-2.0 (dual)](https://github.com/Bwizrd/PitCrowd/blob/22bc881afeaf25901215134594707a4f4c9ccd8f/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_relay/src/main.rs`](https://github.com/Bwizrd/PitCrowd/blob/22bc881afeaf25901215134594707a4f4c9ccd8f/jev_relay/src/main.rs) at the pinned commit. |

## When to use

- Learn Rust and Jev on a visual, offline-first market simulation, or experiment with Jev-assisted paper traders.
- Mismatch: a trading strategy; the author reports nothing tried so far has shown Jev adding an edge over a simpler rule, and the synthetic market has no edge by construction.

## How it works

`jev_relay/src/main.rs` is a small local HTTP relay that holds the TypeSafe key, forwards `POST /jev` to `https://api.typesafe.ai/v1/systemone` one call at a time with a minimum gap (so a buggy client cannot burn the budget) and logs each call for replay; `opencry-visual/src/jev.rs` is the floor's client. Without a key a free rule of thumb stands in. Integration evidence: [`jev_relay/src/main.rs`](https://github.com/Bwizrd/PitCrowd/blob/22bc881afeaf25901215134594707a4f4c9ccd8f/jev_relay/src/main.rs).

## Get started

Try the browser demo with no install, or build and start the local floor services.

```sh
git clone https://github.com/Bwizrd/PitCrowd && cd PitCrowd
(cd opencry-visual && cargo build --release --bin paper_desk --bin genome_backtest) && ./start-floor.sh
# open http://localhost:8180
cp jevfloor_learning_day/.env.example jevfloor_learning_day/.env   # optional: add JEV_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Browser demo (synthetic market, no Jev): [bwizrd.github.io/PitCrowd/](https://bwizrd.github.io/PitCrowd/)
- Rust + Jev course: [github.com/Bwizrd/PitCrowd/tree/22bc881afeaf25901215134594707a4f4c9ccd8f/jevfloor_learning_day](https://github.com/Bwizrd/PitCrowd/tree/22bc881afeaf25901215134594707a4f4c9ccd8f/jevfloor_learning_day)
- Web research notes: [github.com/Bwizrd/PitCrowd/blob/22bc881afeaf25901215134594707a4f4c9ccd8f/research/web-search-2026-10-25.md](https://github.com/Bwizrd/PitCrowd/blob/22bc881afeaf25901215134594707a4f4c9ccd8f/research/web-search-2026-10-25.md)

## Limits and data handling

Paper trading only, no real orders. Work in progress, published for collaboration. Market state sent to Jev goes to TypeSafe when a key is set.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 22bc881afeaf](https://github.com/Bwizrd/PitCrowd/tree/22bc881afeaf25901215134594707a4f4c9ccd8f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
