# JevDSL (compile-time Jev contracts, caching and runner for Elixir)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Elixir library on Hex that compiles `noul`, `choice`, `score` and multi-question `defjev` contracts into validated SystemOneSDK requests at compile time, caches pre-encoded payloads, and runs them through a content-addressed two-tier cache with confidence-gated TTLs, test stubs and an Igniter installer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/boxxxie/jev_dsl) |
| Maintainer | [boxxxie](https://github.com/boxxxie). Independently curated. |
| Format | Elixir library (Hex `jev_dsl`) |
| Requirements | Elixir with the `system_one_sdk` Hex package; a TypeSafe API key, or an offline cache or mock for tests. |
| License | [MIT](https://github.com/boxxxie/jev_dsl/blob/f54b613b5b8b6914110a72fb77a4afc9be97089e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev_dsl.ex`](https://github.com/boxxxie/jev_dsl/blob/f54b613b5b8b6914110a72fb77a4afc9be97089e/lib/jev_dsl.ex) at the pinned commit. |

## When to use

- Declare the Jev questions an Elixir app asks once and get compile errors for invalid ones.
- Avoid paying twice for identical judgements with the built-in cache.
- Mismatch: version 0.1; the GitHub license field shows NOASSERTION although the LICENSE file is the MIT text.

## How it works

`lib/jev_dsl.ex` validates each contract with `SystemOneSDK.prepare/1` at compile time; the runner checks the ETS and optional second-tier cache before calling Jev through SystemOneSDK, and ambiguous answers (below 0.65) are cached for only five minutes. Integration evidence: [`lib/jev_dsl.ex`](https://github.com/boxxxie/jev_dsl/blob/f54b613b5b8b6914110a72fb77a4afc9be97089e/lib/jev_dsl.ex).

## Get started

From the upstream README (not run on the review host):

```sh
mix igniter.install jev_dsl --module MyApp.TriageContracts --yes
# or add {:jev_dsl, "~> 0.1.0"} to deps in mix.exs
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hex package: [hex.pm/packages/jev_dsl](https://hex.pm/packages/jev_dsl)
- README: [github.com/boxxxie/jev_dsl#readme](https://github.com/boxxxie/jev_dsl#readme)

## Limits and data handling

The state you evaluate goes to TypeSafe through SystemOneSDK on cache misses; cached answers stay in your BEAM node or your second-tier store.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit f54b613b5b8b](https://github.com/boxxxie/jev_dsl/tree/f54b613b5b8b6914110a72fb77a4afc9be97089e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
