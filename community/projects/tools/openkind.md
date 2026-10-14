# OpenKind

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust decision engine with CLI and server implementing the TypeSafe Jev protocol for locally hosted models, plus research into custom Qwen 3.5 decision models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/whit3rabbit/openkind) |
| Maintainer | [whit3rabbit](https://github.com/whit3rabbit). Independently curated. |
| Format | Rust CLI, HTTP/gRPC server and library |
| Requirements | Rust toolchain or Homebrew; local GPU/Apple silicon for local models; TypeSafe key only for hosted Jev. |
| License | [MIT](https://github.com/whit3rabbit/openkind/blob/b9061ee352fe9d15de2ea4683fb9c093e0fc785e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/openkind-api/src/lib.rs`](https://github.com/whit3rabbit/openkind/blob/b9061ee352fe9d15de2ea4683fb9c093e0fc785e/crates/openkind-api/src/lib.rs) at the pinned commit. |

## When to use

- Run Jev-shaped decision requests against local models with the same request format.
- Study the documented research on custom decision models.
- Mismatch: local models are not Jev; quality differs and is the author's claim.

## How it works

OpenKind exposes the Jev System One request/response shape over HTTP and gRPC and serves it from local models; the Rust client can also talk to hosted Jev. Integration evidence: [`crates/openkind-api/src/lib.rs`](https://github.com/whit3rabbit/openkind/blob/b9061ee352fe9d15de2ea4683fb9c093e0fc785e/crates/openkind-api/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
brew install whit3rabbit/tap/openkind
openkind version
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Research notes and notebooks: `research/`.

## Limits and data handling

Local mode keeps data on your machine; pointing the client at hosted Jev sends state to TypeSafe and bills your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b9061ee352fe](https://github.com/whit3rabbit/openkind/tree/b9061ee352fe9d15de2ea4683fb9c093e0fc785e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
