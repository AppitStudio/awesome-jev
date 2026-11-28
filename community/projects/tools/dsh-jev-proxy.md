# jev-proxy for dsh by SHTORKA (Rust loopback proxy that adds a Jev judge and safety gates to the dsh coding agent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local loopback proxy between the dsh-tui coding agent and OpenCode Go. A separate Jev judge, called through OpenRouter Decisions, can check turns for drift, loops and premature stops in shadow, advisory or enforce mode, and bridge hooks add deterministic safety denials, staged write locks and verifier-gated completion. Per-turn judging is off by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SSSHHHTTTUUUR/jev-proxy) |
| Maintainer | [{SHTORKA}](https://github.com/SSSHHHTTTUUUR) (SSSHHHTTTUUUR). Independently curated. |
| Format | Rust CLI proxy (Nix flake) |
| Requirements | Rust or Nix, dsh-tui, an OpenRouter key and an upstream HTTP proxy (default 127.0.0.1:1080). |
| License | [MIT](https://github.com/SSSHHHTTTUUUR/jev-proxy/blob/37d7d5f16fbbd04659b2b3883f9f285fa11865e0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/egress.rs`](https://github.com/SSSHHHTTTUUUR/jev-proxy/blob/37d7d5f16fbbd04659b2b3883f9f285fa11865e0/src/egress.rs) at the pinned commit. |

## When to use

- dsh users who want a second-opinion judge and hard safety rules around their coding agent.
- Mismatch: other agents; it is built for dsh and the author's setup.

## How it works

`src/egress.rs` posts judge requests to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.14` (set in `config.example.toml`) using a rolling summary capped at 32 KB, not the raw transcript. Integration evidence: [`src/egress.rs`](https://github.com/SSSHHHTTTUUUR/jev-proxy/blob/37d7d5f16fbbd04659b2b3883f9f285fa11865e0/src/egress.rs).

## Get started

Build with Nix and point dsh at the proxy.

```sh
git clone https://github.com/SSSHHHTTTUUUR/jev-proxy && cd jev-proxy
nix develop --command cargo build --release --locked
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Config example: [github.com/SSSHHHTTTUUUR/jev-proxy/blob/main/config.example.toml](https://github.com/SSSHHHTTTUUUR/jev-proxy/blob/main/config.example.toml)

## Limits and data handling

Personal setup: all egress goes through a mandatory local upstream proxy and the install script targets the author's NixOS host. Summaries of agent turns go to OpenRouter/TypeSafe when the judge is on.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 37d7d5f16fbb](https://github.com/SSSHHHTTTUUUR/jev-proxy/tree/37d7d5f16fbbd04659b2b3883f9f285fa11865e0). Inspected the README, LICENSE, `config.example.toml` and `src/egress.rs` at the pinned commit; nothing was built or run on the review host. Carried over from earlier runs. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
