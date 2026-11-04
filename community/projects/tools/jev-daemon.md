# jev-daemon (per-user Rust daemon and CLI that hold your TypeSafe keys and let paired local programs ask Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust `jevd` daemon and `jev` CLI that keep TypeSafe API keys in the OS keyring and send requests to Jev on behalf of local programs. A program pairs once and you approve it in a terminal with `jev allow`; `jevd` then checks each request for shape, rate limit (120 per 60 seconds by default) and secrets before sending, and exits after two idle hours. A Claude Code plugin lets other plugins call Jev without holding a key. The README marks it as pre-release with no release archive yet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mattbran87/jev-daemon) |
| Maintainer | [mattbran87](https://github.com/mattbran87). Independently curated. |
| Format | Rust workspace (`jev` CLI, `jevd` daemon, Claude Code plugin); build from source with cargo |
| Requirements | Rust 1.85+ to build; a TypeSafe API key stored with `jev key add`. |
| License | [Apache-2.0](https://github.com/mattbran87/jev-daemon/blob/c5412088349b6a21a97c98009032f435c17bca2a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/jevd/src/jev.rs`](https://github.com/mattbran87/jev-daemon/blob/c5412088349b6a21a97c98009032f435c17bca2a/crates/jevd/src/jev.rs) at the pinned commit. |

## When to use

- Give several local scripts, editor extensions or Claude Code plugins controlled access to Jev without scattering API keys.
- Mismatch: it is before its first release, so there are no prebuilt binaries and the interface may change.

## How it works

`crates/jevd/src/jev.rs` sends the validated, rate-limited request to `https://api.typesafe.ai/v1/systemone` with the key held in the daemon; clients get a revocable pairing token and never see the key. Integration evidence: [`crates/jevd/src/jev.rs`](https://github.com/mattbran87/jev-daemon/blob/c5412088349b6a21a97c98009032f435c17bca2a/crates/jevd/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install --locked --git https://github.com/mattbran87/jev-daemon jev
jev key add
jev ask   # JSON on stdin; approve a pairing with `jev allow`
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the build, daemon and plugin steps: [github.com/mattbran87/jev-daemon#readme](https://github.com/mattbran87/jev-daemon#readme)
- Design document: [github.com/mattbran87/jev-daemon/blob/c5412088349b6a21a97c98009032f435c17bca2a/docs/superpowers/specs/2026-11-02-jev-daemon-design.md](https://github.com/mattbran87/jev-daemon/blob/c5412088349b6a21a97c98009032f435c17bca2a/docs/superpowers/specs/2026-11-02-jev-daemon-design.md)

## Limits and data handling

Requests that pass the daemon's checks go to TypeSafe on your key and are billed there. The README says no release exists yet, so install is a source build, and the secret checks and rate limits were not independently tested. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit c5412088349b](https://github.com/mattbran87/jev-daemon/tree/c5412088349b6a21a97c98009032f435c17bca2a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
