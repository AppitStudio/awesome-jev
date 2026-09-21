# jev-sdk-java

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Java **21** client for TypeSafe System One: sealed `Question` / `Answer` types (records, no request maps) over JDK `HttpClient` and Jackson. Distinct from [jev-java](jev-java.md) (Java 17+, multi-module OpenRouter/Vercel/Spring) and from [jev4k](jev4k.md) (Kotlin DSL).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luigivis/jev-sdk-java) |
| Maintainer | [luigivis](https://github.com/luigivis) / Luigi Vismara. Independently curated; this entry is not an upstream submission or endorsement. Unofficial—not affiliated with TypeSafe. |
| Format | Maven artifact coordinates **`com.luigivismara:jev-sdk-java:0.1.0`** in the POM (Java 21). At review time Maven Central returned **404** for that POM; treat install as **source build** until Central publish succeeds. |
| Requirements | JDK 21+. Live calls need `TYPESAFE_API_KEY` (or `JevClient.fromEnv()` as documented). |
| License | [MIT](https://github.com/luigivis/jev-sdk-java/blob/fead1cc314a5e91e6a1d0502880d554020e255d4/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and upstream CI inspected. Local `mvn test` was not run (no JDK on the review host). Live TypeSafe calls were not made. Maven Central publish had not succeeded for 0.1.0 at review time. |

## When to use

Use it when a Java 21 service wants compile-time exhaustiveness for Noul/Choice/Score (sealed answers, named option records) without Spring AI SPIs. Prefer [jev-java](jev-java.md) for Java 17, OpenRouter/Vercel adapters, or Spring Boot starters; prefer [Spring AI TypeSafe](spring-ai-typesafe.md) for Spring AI advisors.

## How it works

[`JevClient`](https://github.com/luigivis/jev-sdk-java/blob/fead1cc314a5e91e6a1d0502880d554020e255d4/src/main/java/com/luigivismara/jev/JevClient.java) posts typed questions to System One. `Question.noul` / `choice` / `score` builders and sealed `Answer` variants keep wire-shape mistakes in the compiler. Application code still owns thresholds and downstream actions. Unit tests cover serialization; `JevLiveApiTest` is for optional live runs.

## Get started

```sh
git clone https://github.com/luigivis/jev-sdk-java.git
cd jev-sdk-java
git checkout fead1cc314a5e91e6a1d0502880d554020e255d4
# With JDK 21+: mvn test
```

Until Maven Central lists the artifact, depend on the GitHub source or a local `mvn install`. Live `JevClient.fromEnv()` sends state/questions to TypeSafe and may incur charges.

## Examples and demos

- README quickstart (`Question.noul` / `choice` / `score`, reading named answers).
- JUnit tests under `src/test/java` (serialization and client unit coverage).
- Upstream GitHub Actions **CI** succeeded on the reviewed tip; **Release to Maven Central** had failed earlier the same day.

## Limits and data handling

Request state and question text leave the host on live calls. Do not embed API keys in distributed clients. Central availability and live API parity were not verified beyond the HTTP 404 on the published POM URL and green upstream CI.

## Review and maintenance

Reviewed on **2026-09-22** at [commit fead1cc](https://github.com/luigivis/jev-sdk-java/tree/fead1cc314a5e91e6a1d0502880d554020e255d4): POM **0.1.0**, MIT. AI-assisted source review of README, `JevClient` / `Question` / `Answer`, `pom.xml`, and LICENSE. No local Maven run (no Java toolchain). Upstream Actions run for this SHA concluded **success**. No live TypeSafe calls. Maven Central POM for `com.luigivismara:jev-sdk-java:0.1.0` returned HTTP 404 on the review host.

Related: [jev-java](jev-java.md), [jev4k](jev4k.md), [Spring AI TypeSafe](spring-ai-typesafe.md), [typesafe-api (Rust)](typesafe-api-rs.md).
