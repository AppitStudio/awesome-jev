# Aster (terminal coding agent with experimental Jev loop advice)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-run terminal coding agent for any OpenAI-compatible provider; an experimental `jev` build asks Jev at each tool round whether to continue, retry, ask you or stop, and can let Jev pick the router entry.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Zfinix/aster) |
| Maintainer | [Zfinix](https://github.com/Zfinix). Independently curated. |
| Format | Terminal agent (Rust, Apache-2.0) |
| Requirements | A Rust build with the `jev` cargo feature, `experimental.jev` (or `ASTER_JEV`), and `ASTER_JEV_API_KEY`. |
| License | [Apache-2.0](https://github.com/Zfinix/aster/blob/95772f9c9f791cf004b58ea1202995d50130f8f7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/aster-jev/src/lib.rs`](https://github.com/Zfinix/aster/blob/95772f9c9f791cf004b58ea1202995d50130f8f7/crates/aster-jev/src/lib.rs) at the pinned commit. |

## When to use

- Add an advisory continue/stop check to a coding-agent loop.
- Mismatch: experimental and off by default; the standard install script does not enable it.

## How it works

`crates/aster-jev/src/lib.rs` posts to `{base_url}/v1/systemone` with `jev-latest`; per `docs/CONFIG.md`, advice is ignored below a confidence threshold, the round cap still binds, and each consultation is logged to `~/.aster/logs/mom-router.jsonl`. Integration evidence: [`crates/aster-jev/src/lib.rs`](https://github.com/Zfinix/aster/blob/95772f9c9f791cf004b58ea1202995d50130f8f7/crates/aster-jev/src/lib.rs).

## Get started

Build from source with the `jev` feature, then turn on `experimental.jev` with your key.

```sh
git clone https://github.com/Zfinix/aster.git && cd aster
cargo install --path crates/aster-cli --features jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Config doc: [github.com/Zfinix/aster/blob/95772f9c9f791cf004b58ea1202995d50130f8f7/docs/CONFIG.md](https://github.com/Zfinix/aster/blob/95772f9c9f791cf004b58ea1202995d50130f8f7/docs/CONFIG.md)

## Limits and data handling

Agent-loop state at each tool round goes to TypeSafe on your key when enabled.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 95772f9c9f79](https://github.com/Zfinix/aster/tree/95772f9c9f791cf004b58ea1202995d50130f8f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
