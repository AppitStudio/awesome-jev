# Klassify

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Kotlin Multiplatform DSL/SDK for TypeSafe System One classification (Noul/Choice/Score), plus a Kotlin/Native CLI and stdio MCP `classify` tool.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fajarnuha/klassify) |
| Maintainer | [fajarnuha](https://github.com/fajarnuha). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Gradle modules **klassify-sdk** (KMP) and **klassify-cli** (Native). JitPack coordinate `com.github.fajarnuha:klassify:v0.1.1`. Optional Homebrew formula `fajarnuha/tools/klassify`. |
| Requirements | JDK/Gradle for SDK consumers; `TYPESAFE_API_KEY` for live evaluate/CLI/MCP. Native CLI targets macOS/Linux/Windows per upstream. |
| License | [Apache-2.0](https://github.com/fajarnuha/klassify/blob/6e8bfcfb4b17d0661eac96a7ee6883070379f93e/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`TypeSafeClient.kt`, README, LICENSE). Gradle build, Homebrew install, and live Jev calls were **not** executed on the review host. Distinct from [jev4k](jev4k.md) (JVM Maven DSL). |

## When to use

Use it when a **Kotlin/KMP** app or Native CLI should ask typed System One questions without free-form generation. Prefer [jev4k](jev4k.md) for a JVM-only Maven Central client, or [jev-android](jev-android.md) for Android UI automation.

## How it works

Delegated properties (`noul` / `choice` / `score`) become question IDs; [`TypeSafeClient.evaluate`](https://github.com/fajarnuha/klassify/blob/6e8bfcfb4b17d0661eac96a7ee6883070379f93e/klassify-sdk/src/commonMain/kotlin/com/fajarnuha/klassify/TypeSafeClient.kt) posts the TypeSafe HTTP System One format and returns typed answers. The CLI runs JSON recipes or stdin state; `klassify mcp` exposes one `classify` tool on stdio.

## Get started

```kotlin
// JitPack JVM/Android sketch — see upstream README for settings.gradle.kts repos
implementation("com.github.fajarnuha:klassify:v0.1.1")
```

```sh
# macOS Homebrew CLI (optional)
brew install fajarnuha/tools/klassify
# or build Native with Gradle per upstream; needs TYPESAFE_API_KEY for live runs
```

Pin for review: [tag v0.1.1 / commit 6e8bfcf](https://github.com/fajarnuha/klassify/tree/6e8bfcfb4b17d0661eac96a7ee6883070379f93e).

## Examples and demos

- README pet classification DSL (`Species` Choice + Noul + Score).
- `examples/pet.json` recipe for the CLI.

## Limits and data handling

Live evaluate/CLI/MCP send state and questions to TypeSafe. This listing did not run Gradle or live calls.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 6e8bfcf](https://github.com/fajarnuha/klassify/tree/6e8bfcfb4b17d0661eac96a7ee6883070379f93e) (Apache-2.0, tag **v0.1.1**). AI-assisted review of README, LICENSE, `TypeSafeClient.kt`. No live TypeSafe spend.

Related: [jev4k](jev4k.md), [jev-java](jev-java.md), [swift-jev](swift-jev.md).
