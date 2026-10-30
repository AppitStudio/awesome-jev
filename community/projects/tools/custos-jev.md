# Custos (Rust behavioral security engine and firewall bouncer that asks Jev to judge suspicious IPs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-binary Rust engine inspired by CrowdSec: it tails web access logs or runs as Axum middleware, drops obvious noise and floods for free, strips prompt-injection text from user agents and URLs, and sends batches of up to 16 suspicious IP windows to Jev in one call for a ban probability and a threat type. Bans go to an HTTP bouncer for Nginx, Caddy or Traefik and to OS firewalls (pf, nftables, ipset, netsh), with an optional gRPC hub for sharing signals between nodes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/george-amir/Custos) |
| Maintainer | [george-amir](https://github.com/george-amir). Independently curated. |
| Format | Rust binary and library |
| Requirements | Rust toolchain; a TypeSafe API key for live mode (a --mock-jev mode runs offline); root to apply firewall rules. |
| License | [MIT](https://github.com/george-amir/Custos/blob/c4faf4b49db1049fc40c49233807b7bb774c256e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/george-amir/Custos/blob/c4faf4b49db1049fc40c49233807b7bb774c256e/src/jev.rs) at the pinned commit. |

## When to use

- Add a judgment step between rate limits and bans for a small self-hosted web server.
- Mismatch: new project; test in preview mode before letting it change firewall rules.

## How it works

`src/jev.rs` builds the `/v1/systemone` request with `noul` (ban) and `choice` (threat type) questions per IP window; the endpoint and `jev-latest` model are set in the config. Integration evidence: [`src/jev.rs`](https://github.com/george-amir/Custos/blob/c4faf4b49db1049fc40c49233807b7bb774c256e/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo run -- replay --log tests/fixtures/sample_access.log --mock-jev
export TYPESAFE_API_KEY=...
cargo run -- replay --log tests/fixtures/sample_access.log
cargo run -- firewall --backend all   # preview only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the tiers and bouncers: [github.com/george-amir/Custos#readme](https://github.com/george-amir/Custos#readme)

## Limits and data handling

IP addresses, paths and user agents from suspicious windows are sent to TypeSafe. `--live` firewall mode changes kernel rules; preview first.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit c4faf4b49db1](https://github.com/george-amir/Custos/tree/c4faf4b49db1049fc40c49233807b7bb774c256e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
