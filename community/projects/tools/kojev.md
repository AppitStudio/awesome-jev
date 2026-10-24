# kojev (Kotlin Multiplatform client that returns your own enums)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Kotlin Multiplatform client for Jev: you describe choices as your own enums or sealed types and get typed answers and probabilities back, with no string keys or casts. Targets JVM, Android and iOS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ItisNoMatter/kojev) |
| Maintainer | [ItisNoMatter](https://github.com/ItisNoMatter). Independently curated. |
| Format | Kotlin Multiplatform library (Ktor) |
| Requirements | Kotlin with any Ktor client engine; a TypeSafe API key. |
| License | [MIT](https://github.com/ItisNoMatter/kojev/blob/3782d10273769c07f6fe61e5deac93c7451b8062/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/commonMain/kotlin/io/github/itisnomatter/kojev/JevClient.kt`](https://github.com/ItisNoMatter/kojev/blob/3782d10273769c07f6fe61e5deac93c7451b8062/src/commonMain/kotlin/io/github/itisnomatter/kojev/JevClient.kt) at the pinned commit. |

## When to use

- Call Jev from Android, iOS (KMP) or JVM backends with compile-time-checked answers.
- Keep decision options in enums shared with the rest of your code.
- Mismatch: 0.x API; breaking changes are expected between releases.

## How it works

`JevClient.kt` posts to `https://api.typesafe.ai` with `jev-latest` by default (pin `jev-1.13.0` once thresholds are tuned); answers are decoded into your enum types. Live tests run only when `TYPESAFE_API_KEY` is set. Integration evidence: [`src/commonMain/kotlin/io/github/itisnomatter/kojev/JevClient.kt`](https://github.com/ItisNoMatter/kojev/blob/3782d10273769c07f6fe61e5deac93c7451b8062/src/commonMain/kotlin/io/github/itisnomatter/kojev/JevClient.kt).

## Get started

From the upstream README (not run on the review host). The README gives these coordinates; Maven Central publication was not confirmed at review time, so building from source may be needed:

```sh
// build.gradle.kts
implementation("io.github.itisnomatter:kojev:0.1.0")
implementation("io.ktor:ktor-client-cio:3.6.0")
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with compiled snippet: [github.com/ItisNoMatter/kojev#readme](https://github.com/ItisNoMatter/kojev#readme)

## Limits and data handling

Not affiliated with TypeSafe. The README advises keeping the API key on a server, not in shipped mobile apps.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 3782d1027376](https://github.com/ItisNoMatter/kojev/tree/3782d10273769c07f6fe61e5deac93c7451b8062). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
