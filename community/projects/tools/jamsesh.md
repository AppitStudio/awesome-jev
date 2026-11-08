# jamsesh (MIDI robot musician whose choices are made by TypeSafe Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Rust program: you play a MIDI keyboard and a robot musician plays along on a second instrument into Reaper; it analyses chord, key, register and dynamics, builds a small menu of musical moves and asks TypeSafe Jev to choose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kmooney/jamsesh) |
| Maintainer | [kmooney](https://github.com/kmooney). Independently curated. |
| Format | Rust CLI (no SPDX license file on the reviewed commit) |
| Requirements | Rust toolchain, a MIDI keyboard, a DAW such as Reaper, and an OpenRouter key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/kmooney/jamsesh/blob/f59387b4b1ce98233171ad78b7037ba3ea63f7e4/src/jev.rs) at the pinned commit. |

## When to use

- Jam with a bot that picks from sensible musical options.
- See Jev used for real-time choice, not generation.
- Mismatch: experimental; no OSI license on the reviewed commit.

## How it works

`src/jev.rs` posts to `https://openrouter.ai/api/alpha/decisions` with `~typesafe/jev-latest`; `notes/jev.md` records the observed resolved model. Integration evidence: [`src/jev.rs`](https://github.com/kmooney/jamsesh/blob/f59387b4b1ce98233171ad78b7037ba3ea63f7e4/src/jev.rs).

## Get started

Build with cargo, connect MIDI ports and Reaper per README, and set your OpenRouter key.

```sh
git clone https://github.com/kmooney/jamsesh.git && cd jamsesh
export OPENROUTER_API_KEY=...
cargo run --release
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kmooney/jamsesh/blob/f59387b4b1ce98233171ad78b7037ba3ea63f7e4/README.md](https://github.com/kmooney/jamsesh/blob/f59387b4b1ce98233171ad78b7037ba3ea63f7e4/README.md)

## Limits and data handling

Musical state summaries are sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit f59387b4b1ce](https://github.com/kmooney/jamsesh/tree/f59387b4b1ce98233171ad78b7037ba3ea63f7e4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
