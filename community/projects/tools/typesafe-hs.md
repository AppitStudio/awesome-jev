# typesafe-hs (Haskell wire types and servant client for the TypeSafe System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Haskell library on Hackage with typed request and response models, deterministic JSON encoding and lossless decoding for TypeSafe's System One API (OpenAPI 0.2.0, including box questions, inline image assets and the model listing), plus servant routes and authenticated client methods; the author also uses it in the Baikai Haskell AI library.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://hackage.haskell.org/package/typesafe-hs) |
| Maintainer | [shinzui](https://github.com/shinzui). Independently curated. |
| Format | Haskell library (Hackage, GHC 9.12) |
| Requirements | GHC 9.12.4 and Cabal; a TypeSafe API key, which your application looks up and passes in. |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/typesafe-hs-0.1.0.0/src/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Reviewed from the Hackage source package; the GitHub repository linked from Hackage returned 404 at review time. Discovered via X ([post](https://x.com/shinzui/status/2114430600677564801)). |
| Jev evidence | [`src/TypeSafe/V1.hs`](https://hackage.haskell.org/package/typesafe-hs-0.1.0.0/src/src/TypeSafe/V1.hs) at the pinned release. |

## When to use

- Call Jev from a Haskell service with typed requests and responses.
- Check exactly which bytes you send: request encoding is deterministic and golden-tested.
- Mismatch: wire layer only; retries, timeouts, logging and credential handling stay in your application.

## How it works

`TypeSafe/V1.hs` defines the servant route for `POST /v1/systemone` with bearer auth and optional danger-zone headers, and `TypeSafe/Wire/Common.hs` sets the default base URL `https://api.typesafe.ai`; the vendored OpenAPI document is checked for drift by a script. Integration evidence: [`src/TypeSafe/V1.hs`](https://hackage.haskell.org/package/typesafe-hs-0.1.0.0/src/src/TypeSafe/V1.hs).

## Get started

From the Hackage README (not run on the review host): add the package to your Cabal dependencies.

```sh
# my-app.cabal
build-depends: typesafe-hs ^>=0.1
# then import TypeSafe.Wire (wire types) and TypeSafe.V1 (servant client)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hackage package: [hackage.haskell.org/package/typesafe-hs](https://hackage.haskell.org/package/typesafe-hs)
- Author's announcement on X: [x.com/shinzui/status/2114430600677564801](https://x.com/shinzui/status/2114430600677564801)

## Limits and data handling

State, questions and any images you build are sent to TypeSafe when your application calls the client. Unofficial; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [Hackage release 0.1.0.0](https://hackage.haskell.org/package/typesafe-hs-0.1.0.0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
