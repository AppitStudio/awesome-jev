# TypeSafe (Swift)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

SwiftPM client for the TypeSafe System One API: typed `Noul`, `Choice`, and `Score` questions with answer decoding aligned to the official JavaScript SDK shape.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/krzyzanowskim/TypeSafe) |
| Maintainer | [krzyzanowskim](https://github.com/krzyzanowskim) (Marcin Krzyżanowski). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Swift package **TypeSafe 0.1.0** (library product `TypeSafe`; demo executable `TypeSafeDemo`). |
| Requirements | Swift 6 tools; platforms per `Package.swift` (macOS 13+, iOS 16+, and related). Live calls need `TYPESAFE_API_KEY` (or `Configuration.apiKey`). |
| License | [MIT](https://github.com/krzyzanowskim/TypeSafe/blob/419521307c944f32ca3b0d830b8f8b5b6ccbf273/LICENSE). |

## When to use

Use it when a Swift or SwiftUI app or server should call System One without embedding the JS/Python SDKs. Prefer the [official JavaScript](https://github.com/typesafe-ai/typesafe-sdk-js) or [Python](https://github.com/typesafe-ai/typesafe-sdk-python) SDKs on those stacks. Do not ship a TypeSafe API key inside a distributed iOS/macOS client binary—call from a server you control, or treat any in-app key as public (upstream warns about this).

## How it works

[`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/krzyzanowskim/TypeSafe/blob/419521307c944f32ca3b0d830b8f8b5b6ccbf273/Sources/TypeSafe/TypeSafeClient.swift) posts to `https://api.typesafe.ai` path `/v1/systemone` (default model `jev-latest`). Question types live in [`Questions.swift`](https://github.com/krzyzanowskim/TypeSafe/blob/419521307c944f32ca3b0d830b8f8b5b6ccbf273/Sources/TypeSafe/Questions.swift); configuration and retries are in `Configuration.swift` / `Retry.swift`.

## Get started

```swift
// Package.swift
.package(url: "https://github.com/krzyzanowskim/TypeSafe", .upToNextMinor(from: "0.1.0")),
// … .product(name: "TypeSafe", package: "TypeSafe")
```

```sh
git clone https://github.com/krzyzanowskim/TypeSafe.git
cd TypeSafe
git checkout 419521307c944f32ca3b0d830b8f8b5b6ccbf273
swift test
# Live demo (billable): TYPESAFE_API_KEY=… swift run TypeSafeDemo
```

This listing did not run `swift test` (no Swift toolchain on the Linux review host) and did not call TypeSafe.

## Examples and demos

- README quickstart with `Choice` / `Noul` / `Score` over a sample ticket.
- [`Examples/Demo`](https://github.com/krzyzanowskim/TypeSafe/tree/419521307c944f32ca3b0d830b8f8b5b6ccbf273/Examples/Demo) (`TypeSafeDemo`).
- Unit tests under `Tests/TypeSafeTests`; integration tests under `Tests/TypeSafeIntegrationTests`.

## Limits and data handling

Request state and question text go to TypeSafe. Client apps must not embed secrets. Behavior is intended to follow the official JS SDK; live parity was not verified here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 4195213](https://github.com/krzyzanowskim/TypeSafe/tree/419521307c944f32ca3b0d830b8f8b5b6ccbf273): **0.1.0**, MIT. AI-assisted source review of README, `Package.swift`, `TypeSafeClient.swift`, and `Version.swift`. No Swift build and no live API call.

Related: [Advocaat](advocaat.md), [ruby_decision_model](ruby-decision-model.md), [typesafe-cli](typesafe-cli.md).
