# Jev Inspector (native desktop inspector that shows every TypeSafe request, response and Jev answer through a local relay)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust desktop app plus a loopback relay: point your backend's `TYPESAFE_BASE_URL` at `jev-bridge`, which forwards requests to the TypeSafe API unchanged and keeps a bounded history, and the inspector shows live traffic, answer probabilities and confidence, timing, token use, a diagram of each Jev question, diffs against a baseline exchange and estimated cost per model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/diegoag64/jev-inspector) |
| Maintainer | [diegoag64](https://github.com/diegoag64). Independently curated. |
| Format | Rust desktop app and local relay built with Rune (macOS and Windows, MIT; experimental) |
| Requirements | Git, Python 3.11.4+, Rust via rustup, and platform build tools (Xcode CLT or Visual Studio Build Tools). The demo needs no key; your own backend keeps its TypeSafe key. |
| License | [MIT](https://github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/diegoarias941/status/2121475312160477279)). |
| Jev evidence | [`crates/jev-bridge/src/main.rs`](https://github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/crates/jev-bridge/src/main.rs) at the pinned commit. |

## When to use

- Debug the questions, answers and confidence your app sends to and gets back from Jev during development.
- Mismatch: production traffic you are not allowed to record; captured bodies can contain application data.

## How it works

`crates/jev-bridge/src/main.rs` defaults the upstream to `https://api.typesafe.ai`, and `lib.rs` refuses to start unless both the relay and the inspector API listen on loopback. Bodies are only recorded with `--capture-bodies`; otherwise metadata only. A macOS app bundle can run the relay itself. Integration evidence: [`crates/jev-bridge/src/main.rs`](https://github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/crates/jev-bridge/src/main.rs).

## Get started

Run the demo (mock API, no key, never contacts TypeSafe), or put the relay in front of your own backend.

```sh
git clone https://github.com/diegoag64/jev-inspector.git && cd jev-inspector
python3 dev.py demo
# your own backend:
cargo run -p jev-bridge -- --capture-bodies
cargo run -p jev-inspector
export TYPESAFE_BASE_URL=http://127.0.0.1:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/README.md](https://github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/README.md)
- Bridge quickstart: [github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/docs/bridge-quickstart.md](https://github.com/diegoag64/jev-inspector/blob/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2/docs/bridge-quickstart.md)
- Related in-app drawer by the same maintainer: [github.com/diegoag64/jev-devtools](https://github.com/diegoag64/jev-devtools)

## Limits and data handling

Requests still go to TypeSafe on your own key; the relay keeps a bounded local history (bodies only with `--capture-bodies`). Review exports before sharing. Linux is untested and there is no hosted CI.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 27a3de3c13f7](https://github.com/diegoag64/jev-inspector/tree/27a3de3c13f74f28834d8b67bac9ea01e9f86ad2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
