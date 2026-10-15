# libtypesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial C++17 client for the TypeSafe API with compile-time-checked answer types, non-blocking `Pending<T>` calls pumped from your loop, and pluggable HTTP transport.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jasonduncan/libtypesafe) |
| Maintainer | [jasonduncan](https://github.com/jasonduncan). Independently curated. |
| Format | C++17 static library (CMake) |
| Requirements | CMake 3.24+, C++17 compiler, nlohmann_json, libcurl (default transport); TypeSafe API key. |
| License | [MIT](https://github.com/jasonduncan/libtypesafe/blob/34c4e880d9dfcb08ed69519c8599cb934ecc26e0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/wire.hpp`](https://github.com/jasonduncan/libtypesafe/blob/34c4e880d9dfcb08ed69519c8599cb934ecc26e0/src/wire.hpp) at the pinned commit. |

## When to use

- Call Jev from game loops, embedded or native C++ apps without blocking.
- Use Jev with exceptions and RTTI disabled (`Result<T>` errors).
- Mismatch: unofficial; same maintainer as the listed libsemop but a separate client.

## How it works

Questions are declared with typed handles; `system_one_async` returns a `Pending<T>` that resolves when `client.pump()` runs, and the wire format is built to match the official Python SDK's requests byte for byte. Integration evidence: [`src/wire.hpp`](https://github.com/jasonduncan/libtypesafe/blob/34c4e880d9dfcb08ed69519c8599cb934ecc26e0/src/wire.hpp).

## Get started

From the upstream README (not run on the review host):

```sh
add_subdirectory(third_party/libtypesafe)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples: `examples/` (e.g. `examples/triage.cpp`) and `docs/DESIGN.md`.

## Limits and data handling

Requests go to TypeSafe and are billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 34c4e880d9df](https://github.com/jasonduncan/libtypesafe/tree/34c4e880d9dfcb08ed69519c8599cb934ecc26e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
