# xks-folder by Lasimeri (Claude Code hook that asks Jev or a local model where each new file belongs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A fixed standard (xks-folder/1), Rust library, `xtf` CLI and Claude Code plugin: a project describes its layout once in `xks-project.json`, and every new file or folder an agent creates becomes the same typed question about role and naming, answered by TypeSafe's Jev or a local Jev-like server, acted on only when confident and logged. Rules handle the obvious cases first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt) |
| Maintainer | [Lasimeri](https://github.com/Lasimeri). Independently curated. |
| Format | Rust CLI + MCP server + Claude Code hook |
| Requirements | Rust to build; a TypeSafe key (`TYPESAFE_API_KEY`) or a local System One server such as jevbase; Claude Code for the plugin. |
| License | [MIT OR Apache-2.0](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/xtf-standard/src/lib.rs`](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/crates/xtf-standard/src/lib.rs) at the pinned commit. |

## When to use

- Keep coding agents from scattering files by asking the same typed layout question for every new path.
- Mismatch: projects without a stable layout to describe in a manifest.

## How it works

`crates/xtf-standard/src/lib.rs` reads `TYPESAFE_BASE_URL`, `TYPESAFE_API_KEY` and `TYPESAFE_DEFAULT_MODEL` and sends the manifest plus the projected operation as one System One request; the hook in `crates/xtf-hook` and the MCP server in `crates/xtf-mcp` call it for every create, move or rename. Integration evidence: [`crates/xtf-standard/src/lib.rs`](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/crates/xtf-standard/src/lib.rs).

## Get started

Build the workspace, add an `xks-project.json` manifest, then install the Claude Code plugin (see the README).

```sh
git clone https://github.com/Lasimeri/xks-toolintercept-folder_mngmt && cd xks-toolintercept-folder_mngmt
cargo build --release
export TYPESAFE_API_KEY=...   # or point TYPESAFE_BASE_URL at a local jevbase
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Standard: [github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/SPEC.md](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/SPEC.md)
- README: [github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/README.md](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/blob/a4df8d442989fef5e242282d0f5c00bb9a24c9a9/README.md)

## Limits and data handling

File paths, short summaries and the manifest are sent to the configured model. Version 0.3.0; calibration covers six repositories.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit a4df8d442989](https://github.com/Lasimeri/xks-toolintercept-folder_mngmt/tree/a4df8d442989fef5e242282d0f5c00bb9a24c9a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
