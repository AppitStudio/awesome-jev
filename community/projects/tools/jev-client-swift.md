# JevClient (Swift)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Swift package for the TypeSafe System One API: send a state and named Choice, Score or Noul questions, get typed answers with probabilities and confidence, plus experimental images, Box answers and model listing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enapiuz/jev-client-swift) |
| Maintainer | [enapiuz](https://github.com/enapiuz). Independently curated. |
| Format | Swift package (SwiftPM, from `0.1.0`) |
| Requirements | Swift 6.4; macOS 12+ / iOS 15+ (Linux via FoundationNetworking); a TypeSafe API key supplied by your app. |
| License | [MIT](https://github.com/enapiuz/jev-client-swift/blob/5bacace1e79a56dbb9249af01143a51c0e13c675/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Sources/JevClient/Transport/JevConfiguration.swift`](https://github.com/enapiuz/jev-client-swift/blob/5bacace1e79a56dbb9249af01143a51c0e13c675/Sources/JevClient/Transport/JevConfiguration.swift) at the pinned commit. |

## When to use

- Add Jev decisions (refund request? which team?) to an iOS or macOS app.
- Batch several questions over one state in a single call from Swift.
- Mismatch: unofficial; no streaming or chat; the client never reads environment variables, so key storage is up to your app.

## How it works

`JevConfiguration` defaults to `https://api.typesafe.ai`; `JevClient(apiKey:)` exposes helpers such as `noul(state:instructions:)` and `evaluate(state:questions:)`, decodes typed values and request metadata, and keeps Noul as a probability rather than a Boolean. Integration evidence: [`Sources/JevClient/Transport/JevConfiguration.swift`](https://github.com/enapiuz/jev-client-swift/blob/5bacace1e79a56dbb9249af01143a51c0e13c675/Sources/JevClient/Transport/JevConfiguration.swift).

## Get started

From the upstream README (not run on the review host):

```sh
# Xcode: File > Add Package Dependencies > https://github.com/Enapiuz/jev-client-swift (from 0.1.0)
# or Package.swift:
# .package(url: "https://github.com/Enapiuz/jev-client-swift.git", from: "0.1.0")
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- First-request and batch examples in the README.
- Release notes: [github.com/Enapiuz/jev-client-swift/releases/tag/0.1.0](https://github.com/Enapiuz/jev-client-swift/releases/tag/0.1.0)

## Limits and data handling

State and images go to TypeSafe on the key your app passes in; the package stores no credentials.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 5bacace1e79a](https://github.com/enapiuz/jev-client-swift/tree/5bacace1e79a56dbb9249af01143a51c0e13c675). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
