# jev-foundation-models

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Swift 6 bridge that presents TypeSafe Jev as an Apple Foundation Models `LanguageModel`, so `@Generable` Bool/enum/score fields map to Noul/Choice/Score over `https://api.typesafe.ai/v1/systemone`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peterfriese/jev-foundation-models) |
| Maintainer | [peterfriese](https://github.com/peterfriese). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Swift package **`jev-foundation-models` 0.1.0** (library product `JevFoundationModels`; demo executables). |
| Requirements | Swift 6 tools; platforms per `Package.swift` (very new OS floors in the reviewed manifest). Live calls need a TypeSafe API key passed into configuration—**do not embed keys in shipped iOS/macOS client binaries** (upstream security advisory). |
| License | [Apache-2.0](https://github.com/peterfriese/jev-foundation-models/blob/27963995965d98eb6122e746bbfc6c3c284f75e6/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. No Swift toolchain on the Linux review host—source inspected only; tests not executed. No live TypeSafe calls. Distinct from [TypeSafe (Swift)](typesafe-swift.md) (raw System One client vs Foundation Models `LanguageModel` provider). |

## When to use

Use it when a Swift server, CLI, or gateway already adopts Apple’s Foundation Models `@Generable` API and you want Jev as the decision backend. Prefer [TypeSafe (Swift)](typesafe-swift.md) for a direct Noul/Choice/Score client without the Foundation Models abstraction. For mobile apps, route through your own backend that holds the key.

## How it works

[`JevLanguageModel.swift`](https://github.com/peterfriese/jev-foundation-models/blob/27963995965d98eb6122e746bbfc6c3c284f75e6/Sources/JevFoundationModels/JevLanguageModel.swift) defaults `endpoint` to `https://api.typesafe.ai/v1/systemone`. [`JevExecutor`](https://github.com/peterfriese/jev-foundation-models/blob/27963995965d98eb6122e746bbfc6c3c284f75e6/Sources/JevFoundationModels/JevExecutor.swift) bridges `LanguageModelSession` generation to that API. [`URLSessionTransport` / `MockJevTransport`](https://github.com/peterfriese/jev-foundation-models/blob/27963995965d98eb6122e746bbfc6c3c284f75e6/Sources/JevFoundationModels/Transport/JevTransport.swift) handle HTTP and tests.

## Get started

```swift
// Package.swift
.package(url: "https://github.com/peterfriese/jev-foundation-models.git", from: "0.1.0")
```

```sh
git clone https://github.com/peterfriese/jev-foundation-models.git
cd jev-foundation-models
git checkout 27963995965d98eb6122e746bbfc6c3c284f75e6
# On a Mac with Swift 6:
# swift test
```

This Linux review host did not run `swift test` or live demos. Live calls send application state to TypeSafe and can incur charges.

## Examples and demos

- `Examples/TicketTriageDemo` and `Examples/DuplicateArticleDemo` executables.
- `Tests/JevFoundationModelsTests` (not executed here).

## Limits and data handling

Never ship `TYPESAFE_API_KEY` inside client app binaries. Guided-generation mapping depends on Foundation Models availability on the target OS. Latency/quality claims in the README are upstream-reported and were not re-measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2796399](https://github.com/peterfriese/jev-foundation-models/tree/27963995965d98eb6122e746bbfc6c3c284f75e6) (0.1.0, Apache-2.0). AI-assisted source review of README, LICENSE, `Package.swift`, `JevLanguageModel.swift`, `JevExecutor.swift`, `JevTransport.swift`. No Swift build and no live API call.

Related: [TypeSafe (Swift)](typesafe-swift.md), [jev4k](jev4k.md), [Advocaat](advocaat.md).
