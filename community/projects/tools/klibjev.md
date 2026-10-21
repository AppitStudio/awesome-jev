# KLibJev (Kotlin Multiplatform Jev client)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Kotlin Multiplatform client for the Jev API that handles authentication and evaluates text, structured data and images with Noul, Choice, Score and Box questions, returning typed answers with probabilities as a Kotlin `Result`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BoD/KLibJev) |
| Maintainer | [BoD](https://github.com/BoD). Independently curated. |
| Format | Kotlin Multiplatform library (Maven `org.jraf.klibjev:klibjev`) |
| Requirements | Kotlin/Gradle project; a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/BoD/KLibJev/blob/4355d3aa070c125f9999e7a1f0df6adb8148ff3e/LICENSE.txt) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`library/src/commonMain/kotlin/org/jraf/klibjev/client/JevClient.kt`](https://github.com/BoD/KLibJev/blob/4355d3aa070c125f9999e7a1f0df6adb8148ff3e/library/src/commonMain/kotlin/org/jraf/klibjev/client/JevClient.kt) at the pinned commit. |

## When to use

- Call Jev from Kotlin on the JVM or other Kotlin targets without writing HTTP plumbing.
- Ask image and Box questions (since v1.1.0).
- Mismatch: client library only; bring your own app.

## How it works

`JevClient` sends a state and typed questions to the TypeSafe API (model `jev-latest` by default, see `JevClient.kt`) and returns the answers wrapped in a `Result`. Integration evidence: [`library/src/commonMain/kotlin/org/jraf/klibjev/client/JevClient.kt`](https://github.com/BoD/KLibJev/blob/4355d3aa070c125f9999e7a1f0df6adb8148ff3e/library/src/commonMain/kotlin/org/jraf/klibjev/client/JevClient.kt).

## Get started

From the upstream README (not run on the review host):

```sh
dependencies {
  implementation("org.jraf.klibjev:klibjev:$latest_version")
}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- JVM sample: [github.com/BoD/KLibJev/blob/main/samples/sample-jvm/src/main/kotlin/Main.kt](https://github.com/BoD/KLibJev/blob/main/samples/sample-jvm/src/main/kotlin/Main.kt)
- Docs site: [jraf.org/KLibJev/](https://jraf.org/KLibJev/)

## Limits and data handling

Inputs are sent to TypeSafe. Community library, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 4355d3aa070c](https://github.com/BoD/KLibJev/tree/4355d3aa070c125f9999e7a1f0df6adb8148ff3e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
