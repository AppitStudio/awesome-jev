# jev-gen-detect (AI-generated image detector)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust web UI and CLI that asks Jev Image whether a picture is generated or authentic, or which generator made it, and asks Jev Box for the most telling artifact region, showing probabilities, latency and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eforus-overseer/jev-gen-detect) |
| Maintainer | [eforus-overseer](https://github.com/eforus-overseer). Independently curated. |
| Format | Rust CLI and local web UI |
| Requirements | Rust toolchain; `OPENROUTER_API_KEY` (Jev is reached through OpenRouter's Decisions API); Box needs Jev 1.14+. |
| License | [MIT](https://github.com/eforus-overseer/jev-gen-detect/blob/bc172c85b927e9f30c342c14d0f13a96a6a1a124/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/eforus-overseer/jev-gen-detect/blob/bc172c85b927e9f30c342c14d0f13a96a6a1a124/src/jev.rs) at the pinned commit. |

## When to use

- Triage suspicious images quickly with a probability per option.
- Point to the region behind a generated verdict.
- Mismatch: classification quality is Jev's; treat results as a signal, not proof.

## How it works

`src/jev.rs` sends the image with a multiple-choice question to Jev through OpenRouter (default `~typesafe/jev-latest`) plus a Box request for the artifact region; results are cached per mode. Integration evidence: [`src/jev.rs`](https://github.com/eforus-overseer/jev-gen-detect/blob/bc172c85b927e9f30c342c14d0f13a96a6a1a124/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # add OPENROUTER_API_KEY
cargo build --release
cargo run --release -- serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Web UI and CLI usage in the README: [github.com/eforus-overseer/jev-gen-detect#readme](https://github.com/eforus-overseer/jev-gen-detect#readme)

## Limits and data handling

Images are sent to OpenRouter and TypeSafe. The local server binds to 127.0.0.1 only.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit bc172c85b927](https://github.com/eforus-overseer/jev-gen-detect/tree/bc172c85b927e9f30c342c14d0f13a96a6a1a124). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
