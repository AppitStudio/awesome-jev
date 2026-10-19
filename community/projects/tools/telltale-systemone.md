# telltale-systemone

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reference analyzer extension for the Telltale agent-monitoring tool that asks Jev narrow typed questions about agent actions from configurable guard packs, beside Telltale's deterministic rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/christian-taillon/telltale-systemone) |
| Maintainer | [christian-taillon](https://github.com/christian-taillon). Independently curated. |
| Format | Rust CLI / JSONL extension |
| Requirements | Rust toolchain; Telltale; a TypeSafe key for live System One calls (offline fixtures need none). |
| License | [Apache-2.0](https://github.com/christian-taillon/telltale-systemone/blob/7f716e24424a7f8609f6f858354bbeb4b6aa5100/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone.rs`](https://github.com/christian-taillon/telltale-systemone/blob/7f716e24424a7f8609f6f858354bbeb4b6aa5100/src/systemone.rs) at the pinned commit. |

## When to use

- Add model-based guard checks on agent actions without replacing rules.
- Inspect exactly what would be sent before sending it.
- Mismatch: extension for Telltale; packs need tuning for your agents.

## How it works

Telltale observations become analysis inputs; guard packs define the questions and map answers to Telltale categories. `src/systemone.rs` calls the System One API (`jev-1.13.0` in the example config), the model supplies only probabilities, and the host validates results before they become findings. Integration evidence: [`src/systemone.rs`](https://github.com/christian-taillon/telltale-systemone/blob/7f716e24424a7f8609f6f858354bbeb4b6aa5100/src/systemone.rs).

## Get started

From the upstream README: build with Cargo, lint a pack, and evaluate example inputs offline.

```sh
cargo build
./target/debug/telltale-systemone evaluate --config examples/config.fixture.yaml --input examples/mode-b-inputs.jsonl --print-requests
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- packs/core.yaml
- examples/config.typesafe.yaml

## Limits and data handling

Agent action text goes to TypeSafe in live mode. Guard results are probabilities, not enforcement on their own.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7f716e24424a](https://github.com/christian-taillon/telltale-systemone/tree/7f716e24424a7f8609f6f858354bbeb4b6aa5100). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
