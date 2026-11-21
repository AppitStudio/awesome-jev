# jevjavauosdk (unofficial Java 21+ SDK for Jev with Micrometer metrics and a test client)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

An independently maintained Java 21+ client for the System One API: synchronous and asynchronous requests, routing helpers in a `patterns` package, a Micrometer metrics module and an in-memory test client, with a compatibility guide comparing it to the official SDKs. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ultonian/jevjavauosdk) |
| Maintainer | [Ultonian](https://github.com/Ultonian). Independently curated. |
| Format | Java library (multi-module) |
| Requirements | Java 21+; build from source (not yet on Maven Central); `TYPESAFE_API_KEY` for live calls. |
| License | [MIT](https://github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-core/src/main/java/net/codefinch/jev/internal/HttpJevClient.java`](https://github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/jev-core/src/main/java/net/codefinch/jev/internal/HttpJevClient.java) at the pinned commit. |

## When to use

- Call Jev from Java services with metrics and a test double.
- Mismatch: you need a published artifact today; it is pre-release and not on Maven Central.

## How it works

`HttpJevClient.java` posts typed questions to `/v1/systemone` (base URL overridable with `TYPESAFE_BASE_URL`) and parses answers into Java types; `jev-micrometer` records latency and usage per response. Integration evidence: [`jev-core/src/main/java/net/codefinch/jev/internal/HttpJevClient.java`](https://github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/jev-core/src/main/java/net/codefinch/jev/internal/HttpJevClient.java).

## Get started

Clone and build locally, then depend on `jev-core` (see the docs index).

```sh
git clone https://github.com/Ultonian/jevjavauosdk && cd jevjavauosdk
# build per docs/README.md, then set TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs index: [github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/docs/README.md](https://github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/docs/README.md)
- Compatibility guide: [github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/docs/PARITY.md](https://github.com/Ultonian/jevjavauosdk/blob/15bafd73d5f72f4230866239a9af0b3468b33c2e/docs/PARITY.md)

## Limits and data handling

Pre-release; API may change. Request content goes to TypeSafe with your key.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 15bafd73d5f7](https://github.com/Ultonian/jevjavauosdk/tree/15bafd73d5f72f4230866239a9af0b3468b33c2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
