# vigilant-heron (reverse-proxy attack screen that scores unclear requests with Jev or Clef)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust reverse-proxy router between your edge and site: fixed rules block obvious attacks and less obvious requests go to a decision model (Jev by default, or Clef/Strands/your own) to block, redirect or forward.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coo-quack/vigilant-heron) |
| Maintainer | [coo-quack](https://github.com/coo-quack). Independently curated. |
| Format | Rust binary + Docker image (MIT; early development) |
| Requirements | Linux binary or Docker (or Rust toolchain), and `TYPESAFE_API_KEY` for `backend jev`. |
| License | [MIT](https://github.com/coo-quack/vigilant-heron/blob/185922d4cfce637760e8b502257c642b94b837ba/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/system_one.rs`](https://github.com/coo-quack/vigilant-heron/blob/185922d4cfce637760e8b502257c642b94b837ba/src/system_one.rs) at the pinned commit. |

## When to use

- Add a model-scored second screen in front of a web app.
- Compare Jev and Clef on your own traffic in shadow mode.
- Mismatch: not validated on real traffic yet.

## How it works

`system_one.rs` implements the System One backends (TypeSafe Jev, Cloudflare Clef); `backend jev;` in the config reads `TYPESAFE_API_KEY`, and the changelog records a 25.7-hour run with p50 133 ms. Integration evidence: [`src/system_one.rs`](https://github.com/coo-quack/vigilant-heron/blob/185922d4cfce637760e8b502257c642b94b837ba/src/system_one.rs).

## Get started

Download a release binary or run `ghcr.io/coo-quack/vigilant-heron`, write a config with `backend jev;`, and start in shadow mode.

```sh
docker run --rm ghcr.io/coo-quack/vigilant-heron:latest --version
TYPESAFE_API_KEY=... vigilant-heron -t -c vigilant-heron.conf
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/coo-quack/vigilant-heron/blob/185922d4cfce637760e8b502257c642b94b837ba/README.md](https://github.com/coo-quack/vigilant-heron/blob/185922d4cfce637760e8b502257c642b94b837ba/README.md)

## Limits and data handling

Request details for unclear requests are sent to the chosen decision model.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 185922d4cfce](https://github.com/coo-quack/vigilant-heron/tree/185922d4cfce637760e8b502257c642b94b837ba). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
