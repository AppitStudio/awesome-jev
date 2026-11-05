# bevy-jev (Bevy ECS plugin for async, provenance-checked Jev decisions via a gateway)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Bevy plugin for asynchronous Jev decisions that keeps network work off the main schedule and accepts only responses that match the captured request, world revision, pack, model and finite outcome allowlist. Expects a short-lived gateway token — never a TypeSafe key in the game binary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/bevy-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Rust crate for Bevy 0.19 (MIT) |
| Requirements | Rust 1.95+, Bevy 0.19.1, and an HTTPS gateway that holds the TypeSafe credentials. |
| License | [MIT](https://github.com/gbesse/bevy-jev/blob/17e18c29e23b42e2f2338effbfa14d82fb18d52a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib.rs`](https://github.com/gbesse/bevy-jev/blob/17e18c29e23b42e2f2338effbfa14d82fb18d52a/src/lib.rs) at the pinned commit. |

## When to use

- Drive NPC or gameplay choices with typed Jev outcomes inside Bevy.
- Fail closed when a late or forged outcome arrives.
- Mismatch: you must run a gateway; the plugin does not embed TypeSafe keys.

## How it works

The plugin queues `JevRequest`s through a `GatewayProvider`; late replies that miss revision/pack/model/outcome checks are ignored. Examples use synthetic providers without live keys. Integration evidence: [`src/lib.rs`](https://github.com/gbesse/bevy-jev/blob/17e18c29e23b42e2f2338effbfa14d82fb18d52a/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo test --all-features
cargo run --example minimal
cargo run --example rejected_outcome
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/bevy-jev/blob/17e18c29e23b42e2f2338effbfa14d82fb18d52a/README.md](https://github.com/gbesse/bevy-jev/blob/17e18c29e23b42e2f2338effbfa14d82fb18d52a/README.md)

## Limits and data handling

Decision payloads go to your gateway (and then TypeSafe). Tests do not call the live Jev API.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 17e18c29e23b](https://github.com/gbesse/bevy-jev/tree/17e18c29e23b42e2f2338effbfa14d82fb18d52a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
