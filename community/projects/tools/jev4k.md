# jev4k

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Kotlin DSL and Ktor-based client for TypeSafe Jev: declare Noul/Choice/Score questions in Kotlin (including enum choices), send one System One request, and read typed answers with calibrated probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pambrose/jev4k) · Docs [jev4k.com](https://jev4k.com/) |
| Maintainer | [pambrose](https://github.com/pambrose). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Kotlin library on Maven Central **`com.pambrose:jev4k:0.1.0`** (tip opens **0.1.1**). |
| Requirements | Kotlin / JVM per upstream; live calls need `TYPESAFE_API_KEY` (or explicit config) for `https://api.typesafe.ai/v1/systemone`. |
| License | [Apache-2.0](https://github.com/pambrose/jev4k/blob/e55206acd7894d590a8985dfbdeac04dcf92aaff/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source + unit tests inspected; `./gradlew test` was not run (no JDK in this environment). No live TypeSafe calls. Distinct from [jev-java](jev-java.md) and [jev-android](jev-android.md). |

## When to use

Use it when you want idiomatic Kotlin question DSLs and typed results on the JVM. Prefer [jev-java](jev-java.md) for a Java/Spring-oriented client, or [jev-android](jev-android.md) for accessibility-driven Android UI agents.

## How it works

[`JevClient`](https://github.com/pambrose/jev4k/blob/e55206acd7894d590a8985dfbdeac04dcf92aaff/src/main/kotlin/com/pambrose/jev4k/JevClient.kt) posts to `v1/systemone` (default base `https://api.typesafe.ai`). `JevQuery` property delegates (`noul`, `choice`, `score`) build the wire payload; answers map back to typed values. Offline `ClientTest` asserts the System One URL and error shaping with mocked HTTP—no live key required for those tests.

## Get started

```kotlin
implementation("com.pambrose:jev4k:0.1.0")
```

```sh
git clone https://github.com/pambrose/jev4k.git
cd jev4k
git checkout e55206acd7894d590a8985dfbdeac04dcf92aaff
./gradlew test   # needs a JDK; not run in this listing environment
```

Live `ask` calls send state text to TypeSafe and can incur charges.

## Examples and demos

- README triage DSL sample and [jev4k.com](https://jev4k.com/) docs.
- Mocked client tests under `src/test/kotlin/` (not executed here).

## Limits and data handling

Judged state leaves the host on live calls. Confirm TypeSafe billing separately. Upstream CI badges were not re-run in this environment.

## Review and maintenance

Reviewed on **2026-09-21** at [commit e55206a](https://github.com/pambrose/jev4k/tree/e55206acd7894d590a8985dfbdeac04dcf92aaff): Maven Central **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `JevClient`/`JevConfig`, and test expectations for `/v1/systemone`. No live provider calls; Gradle tests not run here.

Related: [jev-java](jev-java.md), [jev-android](jev-android.md), [Spring AI TypeSafe](spring-ai-typesafe.md).
