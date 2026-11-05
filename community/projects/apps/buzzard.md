# Buzzard (AUR helper that reviews every package with rules, Jev and a sandbox before install)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Arch Linux AUR helper written in Rust that reads each PKGBUILD, runs local rules, asks Jev about credential exfiltration and download-and-run risks, optionally asks a local LLM for an advisory review, and only then builds in a sandbox after you confirm.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kanyefue/buzzard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/kanyefue/buzzard#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply TypeSafe (and optional local LLM) keys. Checked 2026-11-06. |
| Jev evidence | [`src/jev.rs`](https://github.com/kanyefue/buzzard/blob/7237d491a000263c0fa7cf08f724f16ab7d5ee58/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [kanyefue](https://github.com/kanyefue). Independently curated. |
| Format | Rust CLI for Arch Linux (MIT) |
| Platform and availability | Arch Linux CLI; install from source or releases. |
| Jev's role | Optional but primary risk scorer: Jev estimates maliciousness and specific risk flags on each PKGBUILD before install. |
| Requirements | Arch Linux, Rust toolchain to build from source, and a `TYPESAFE_API_KEY` for Jev scoring (optional local LLM for advisory review). |
| License | [MIT](https://github.com/kanyefue/buzzard/blob/7237d491a000263c0fa7cf08f724f16ab7d5ee58/LICENSE) |

## When to use

- Review AUR packages before `yay`-style installs.
- Keep a typed audit trail of Jev risk scores next to sandbox builds.
- Mismatch: Arch-only; without a TypeSafe key the Jev stage is unavailable.

## How it works

`src/jev.rs` posts typed risk questions about the PKGBUILD to TypeSafe Jev and surfaces probabilities such as credential_or_exfil and downloads_and_runs before the confirm prompt. Integration evidence: [`src/jev.rs`](https://github.com/kanyefue/buzzard/blob/7237d491a000263c0fa7cf08f724f16ab7d5ee58/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
cargo install --path .   # or use a release binary from upstream
buzzard install <query>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kanyefue/buzzard/blob/7237d491a000263c0fa7cf08f724f16ab7d5ee58/README.md](https://github.com/kanyefue/buzzard/blob/7237d491a000263c0fa7cf08f724f16ab7d5ee58/README.md)

## Limits and data handling

PKGBUILD text is sent to TypeSafe on your key. Jev scores are advisory; you still type the package name to continue.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 7237d491a000](https://github.com/kanyefue/buzzard/tree/7237d491a000263c0fa7cf08f724f16ab7d5ee58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
