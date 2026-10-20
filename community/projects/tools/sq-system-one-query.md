# sq (System One Query)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust CLI and local relay that runs Choice, Score and Noul decisions over shell pipelines with bounded concurrency and ordered JSON-line output, for Jev, Drex or a local Laya server, plus a typed Python SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LIghtJUNction/sq) |
| Maintainer | [LIghtJUNction](https://github.com/LIghtJUNction). Independently curated. |
| Format | CLI (Rust; release binaries and AUR package) and Python SDK |
| Requirements | `TYPESAFE_API_KEY` for Jev (or a Drex key or a running Laya server); Rust 1.85+ to build from source. |
| License | [MIT](https://github.com/LIghtJUNction/sq/blob/f75a509f3a994af36d1d2a056ab5ca2a102c9800/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.rs`](https://github.com/LIghtJUNction/sq/blob/f75a509f3a994af36d1d2a056ab5ca2a102c9800/src/config.rs) at the pinned commit. |

## When to use

- Label log lines or records in a shell pipeline and filter the JSON output with jq.
- Switch the same pipeline between hosted Jev and a local System One server.
- Mismatch: the binary name `sq` clashes with other tools; check `sq --version`.

## How it works

sq reads records from stdin (text or JSON lines), sends each as a System One request to the chosen provider (Jev at `https://api.typesafe.ai` by default, see `src/config.rs`) with bounded concurrency, and prints one result per input in order. Integration evidence: [`src/config.rs`](https://github.com/LIghtJUNction/sq/blob/f75a509f3a994af36d1d2a056ab5ca2a102c9800/src/config.rs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY='your-key'
printf '%s\n' 'disk is full' 'service recovered' | sq --choice 'normal,warning,critical' | jq '.choice'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Protocol notes: [github.com/LIghtJUNction/sq/blob/main/docs/protocol.md](https://github.com/LIghtJUNction/sq/blob/main/docs/protocol.md)
- AUR package: [aur.archlinux.org/packages/sq-system-one-bin](https://aur.archlinux.org/packages/sq-system-one-bin)

## Limits and data handling

Records are sent to the provider you choose. sq bundles no model weights and runs no inference itself.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit f75a509f3a99](https://github.com/LIghtJUNction/sq/tree/f75a509f3a994af36d1d2a056ab5ca2a102c9800). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
