# ContextOS (desktop workbench for coding-agent sessions, with Jev-assisted compression of long chats)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Desktop workbench built on Wake that gathers sessions from the coding agents on your machine: browse and full-text search conversations and tool calls, resume or export sessions, track project file changes, manage memories and skills, see token stats, and compress long sessions with rules, Jev judgments and a configurable LLM. Exposes MCP and a CLI. Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KeLe3377/ContextOS) |
| Maintainer | [KeLe3377](https://github.com/KeLe3377). Independently curated. |
| Format | Desktop app (Rust, GPUI) |
| Requirements | Rust toolchain to build; optionally a TypeSafe key for Jev compression. |
| License | [MIT](https://github.com/KeLe3377/ContextOS/blob/b48ce600e48cf8bf0ac2066ccb7dfa66999e50e5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/wake-core/src/services/compression_settings.rs`](https://github.com/KeLe3377/ContextOS/blob/b48ce600e48cf8bf0ac2066ccb7dfa66999e50e5/crates/wake-core/src/services/compression_settings.rs) at the pinned commit. |

## When to use

- Search and tidy coding-agent history across tools in one place.
- Mismatch: development builds only; Chinese UI.

## How it works

`crates/wake-core/src/services/compression_settings.rs` sets Jev (`jev-latest`) as a compression decision model, and `laya_runtime.rs` handles local `/v1/systemone` runtimes. Integration evidence: [`crates/wake-core/src/services/compression_settings.rs`](https://github.com/KeLe3377/ContextOS/blob/b48ce600e48cf8bf0ac2066ccb7dfa66999e50e5/crates/wake-core/src/services/compression_settings.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/KeLe3377/ContextOS && cd ContextOS
cargo run -p wake
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/KeLe3377/ContextOS#readme](https://github.com/KeLe3377/ContextOS#readme)
- Upstream Wake: [github.com/iAmCorey/Wake](https://github.com/iAmCorey/Wake)

## Limits and data handling

Session index stays local; text sent for compression goes to the services you configure.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit b48ce600e48c](https://github.com/KeLe3377/ContextOS/tree/b48ce600e48cf8bf0ac2066ccb7dfa66999e50e5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
