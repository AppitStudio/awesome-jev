# swift-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Swift library and CLI for TypeSafe Jev: typed Choice/Noul/Score questions with calibrated probabilities—no free-form text generation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d-date/swift-jev) |
| Maintainer | [d-date](https://github.com/d-date). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | SwiftPM library product **Jev** plus executable **jev** (CLI/agent skill). |
| Requirements | Swift **6.2**; macOS 13+, iOS 16+, tvOS 16+, watchOS 9+, visionOS 1+ (Linux declared, not CI-covered). Live calls need `TYPESAFE_API_KEY` or `--api-key-file`. No third-party package dependencies. |
| License | [MIT](https://github.com/d-date/swift-jev/blob/d5d2280c01a33b08888958bbeb866ae7ca50f883/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected. Swift toolchain tests and live TypeSafe calls were **not** run on the Linux review host. Distinct from [TypeSafe (Swift)](typesafe-swift.md) (`krzyzanowskim/TypeSafe`). |

## When to use

Use it when a Swift/SwiftUI app or agent skill should call System One with typed question builders and `require`/`confidence` helpers, or when a `swift run jev` JSON CLI is enough. Prefer the [official JS/Python SDKs](https://docs.typesafe.ai) on those stacks. Prefer [TypeSafe (Swift)](typesafe-swift.md) if you already standardize on that package.

## How it works

[`Sources/Jev/JevClient.swift`](https://github.com/d-date/swift-jev/blob/d5d2280c01a33b08888958bbeb866ae7ca50f883/Sources/Jev/JevClient.swift) posts to the System One endpoint (default `jev-latest`). Question types and answer helpers live beside the client; the CLI reads JSON on stdin/`--input` and writes only the response JSON to stdout.

## Get started

```swift
.package(url: "https://github.com/d-date/swift-jev", from: "1.0.0"),
// .product(name: "Jev", package: "swift-jev")
```

```sh
git clone https://github.com/d-date/swift-jev.git
cd swift-jev
git checkout d5d2280c01a33b08888958bbeb866ae7ca50f883
# Needs Swift 6.2 — not run on this Linux review host
# swift test
# TYPESAFE_API_KEY=… swift run jev --input request.json
```

## Examples and demos

- README triage sample (department Choice, urgency Noul, frustration Score in one request).
- Bundled agent skill under `skills/jev/`.

## Limits and data handling

State/question payloads leave the host on live calls. Do not embed a TypeSafe key in a distributed client binary. Linux is untested upstream.

## Review and maintenance

Reviewed on **2026-09-23** at [commit d5d2280](https://github.com/d-date/swift-jev/tree/d5d2280c01a33b08888958bbeb866ae7ca50f883) (MIT). AI-assisted review of README, LICENSE, `JevClient.swift`, `Package.swift`. No Swift/live run.

Related: [TypeSafe (Swift)](typesafe-swift.md), [jev-foundation-models](jev-foundation-models.md).
