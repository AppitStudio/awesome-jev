# jev-java

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Java SDK for TypeSafe Jev (and OpenRouter / Vercel AI Gateway adapters): define `Choice`, `Noul`, and `Score` questions in Java, batch them in one `evaluate` call, and receive typed results. Spring Boot starter and WebClient transport are optional. Not affiliated with TypeSafe or Vercel. Distinct from the official JS/Python SDKs and from listed [.NET](typesafe-sdk-csharp.md) / [Swift](typesafe-swift.md) / [Rust](typesafe-api-rs.md) clients.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gudcks0305/jev-java) |
| Maintainer | [gudcks0305](https://github.com/gudcks0305). Independently curated; this entry is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | Maven multi-module **0.1.1** (`jev-typesafe`, `jev-openrouter`, `jev-vercel`, `jev-spring-boot-starter`, `jev-spring-webflux`; groupId `io.github.gudcks0305`). |
| Requirements | Java 17+. Live TypeSafe runs need `TYPESAFE_API_KEY` (or provider-specific keys for OpenRouter / Vercel AI Gateway). |
| License | [MIT](https://github.com/gudcks0305/jev-java/blob/2d2b5c26c803802717b344e5dd5fc4e5524ba4e0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and published Maven POMs inspected. Java unit tests were not executed on the Linux review host (no JDK). Live TypeSafe/OpenRouter/Vercel calls were not made. |

## When to use

Use it when a JVM service should call System One without embedding the JS/Python SDKs. Prefer the [official JavaScript](https://github.com/typesafe-ai/typesafe-sdk-js) or [Python](https://github.com/typesafe-ai/typesafe-sdk-python) SDKs on those stacks. Prefer Spring modules when you want auto-configuration or WebClient.

## How it works

[`TypeSafeJevClient`](https://github.com/gudcks0305/jev-java/blob/2d2b5c26c803802717b344e5dd5fc4e5524ba4e0/jev-typesafe/src/main/java/io/github/gudcks0305/jev/typesafe/TypeSafeJevClient.java) posts to `https://api.typesafe.ai` path `v1/systemone` (default model `jev-latest`) using JDK `HttpClient` and Jackson. Question helpers live in `jev-core`. OpenRouter and Vercel modules adapt the same question types to those providers' evaluation protocols.

## Get started

```xml
<dependency>
  <groupId>io.github.gudcks0305</groupId>
  <artifactId>jev-typesafe</artifactId>
  <version>0.1.1</version>
</dependency>
```

```sh
git clone https://github.com/gudcks0305/jev-java.git
cd jev-java
git checkout 2d2b5c26c803802717b344e5dd5fc4e5524ba4e0
# With JDK 17+: ./mvnw test
# Live (charges): TYPESAFE_API_KEY=... ./mvnw -pl examples exec:java
```

Maven Central artifact `io.github.gudcks0305:jev-typesafe:0.1.1` returned HTTP 200 for its POM on the review host. `./mvnw test` was not run (no Java toolchain).

## Examples and demos

- README quickstart batching Choice/Noul/Score over a sample support ticket.
- `examples/` module and provider-specific README sections.
- Unit tests under each module's `src/test/java` (including `TypeSafeJevClientTest` asserting the System One URI).

## Limits and data handling

Request state and question text leave the host toward TypeSafe, OpenRouter, or Vercel AI Gateway when those clients are used. Do not embed API keys in distributed client apps. Live parity with the official SDKs was not verified here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2d2b5c2](https://github.com/gudcks0305/jev-java/tree/2d2b5c26c803802717b344e5dd5fc4e5524ba4e0): **0.1.1**, MIT. AI-assisted source review of README, `TypeSafeJevClient.java`, root `pom.xml`, and LICENSE. No Maven test run and no live API calls.

Related: [TypeSafe (Swift)](typesafe-swift.md), [typesafe-api (Rust)](typesafe-api-rs.md), [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md), [ruby_decision_model](ruby-decision-model.md).
