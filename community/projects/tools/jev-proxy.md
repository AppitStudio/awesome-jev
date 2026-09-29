# jev-proxy

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local TypeSafe System One proxy that records, caches, and replays calls with a web inspector.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/baptiste-mnh/jev-proxy) |
| Maintainer | [baptiste-mnh](https://github.com/baptiste-mnh). Independently curated. |
| Format | Rust local proxy for TypeSafe /v1/systemone with record/cache/replay and HTMX UI. |
| Requirements | Rust toolchain; TYPESAFE_API_KEY; local port 8420 default. |
| License | [MIT](https://github.com/baptiste-mnh/jev-proxy/blob/fdc649767ec47d054a77ed4f31f941f5874a0b28/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when developing against Jev and you want deterministic replay or an audit UI. Prefer direct API calls in production without caching needs.

## How it works

Unofficial proxy forwards System One requests, stores them in SQLite, and serves an HTMX inspector.

## Get started

```sh
git clone https://github.com/baptiste-mnh/jev-proxy.git
cd jev-proxy
git checkout fdc649767ec47d054a77ed4f31f941f5874a0b28
# cargo run --release --manifest-path rust/Cargo.toml
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit fdc6497](https://github.com/baptiste-mnh/jev-proxy/tree/fdc649767ec47d054a77ed4f31f941f5874a0b28). AI-assisted README and license inspection; install/live paths not executed.
