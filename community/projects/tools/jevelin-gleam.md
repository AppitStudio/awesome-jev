# Jevelin for Gleam by Olaoluwa Osuntokun (sans-I/O library for typed Jev decisions in Gleam, compiling to Erlang and JavaScript)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Gleam library that prepares System One requests and decodes the answers into your own domain types: a Choice returns one of your variants, and independent questions combine into a record or list. It does no I/O itself, so your transport owns credentials, timeouts and retries. Not related to the separately listed Jevelin (henryzhangpku/jevelin).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Roasbeef/jevelin) |
| Maintainer | [Olaoluwa Osuntokun](https://github.com/Roasbeef). Independently curated. |
| Format | Gleam library (Erlang and JavaScript targets) |
| Requirements | Gleam 1.18+ and your own HTTP transport and TypeSafe API key. Not published on Hex; use a path dependency. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevelin.gleam`](https://github.com/Roasbeef/jevelin/blob/493a1b4207d5f935f351f64f258a50a01bd29779/src/jevelin.gleam) at the pinned commit. |

## When to use

- Call Jev from Gleam (BEAM or JavaScript) with typed, exhaustive decoding.
- Mismatch: if you want a ready HTTP client; you supply the transport.

## How it works

`src/jevelin.gleam` builds requests for TypeSafe's System One API (`https://api.typesafe.ai`) and keeps each request's decoder, so a response cannot introduce an unknown Choice label; `test/contract_test.gleam` checks against the bundled OpenAPI document. Integration evidence: [`src/jevelin.gleam`](https://github.com/Roasbeef/jevelin/blob/493a1b4207d5f935f351f64f258a50a01bd29779/src/jevelin.gleam).

## Get started

Clone the repository and run the tests on both targets.

```sh
git clone https://github.com/roasbeef/jevelin
cd jevelin
gleam deps download
gleam test
gleam test --target javascript
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example test: [github.com/Roasbeef/jevelin/blob/493a1b4207d5f935f351f64f258a50a01bd29779/test/example_test.gleam](https://github.com/Roasbeef/jevelin/blob/493a1b4207d5f935f351f64f258a50a01bd29779/test/example_test.gleam)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Early library, not published on Hex.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 493a1b4207d5](https://github.com/Roasbeef/jevelin/tree/493a1b4207d5f935f351f64f258a50a01bd29779). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
