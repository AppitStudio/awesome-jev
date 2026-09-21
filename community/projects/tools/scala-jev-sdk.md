# scala-jev-sdk

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Scala **3.3 LTS** client for TypeSafe System One (Jev): typed `Question` / answer lookup with no bundled effect system—you supply an [sttp](https://sttp.softwaremill.com) 4 backend (`Future`, blocking `Identity`, or cats-effect/ZIO/Monix/Pekko via that backend). Distinct from [jev-sdk-java](jev-sdk-java.md), [jev4k](jev4k.md), and the official JS/Python SDKs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ticofab/scala-jev-sdk) |
| Maintainer | [ticofab](https://github.com/ticofab) / Fabio Tiriticco. Independently curated; this entry is not an upstream submission or endorsement. Unofficial—not affiliated with TypeSafe. |
| Format | Maven Central artifact **`io.github.ticofab:scala-jev-sdk_3:0.1.0`** (Scala 3.3+, JDK 17+). Dependencies: `sttp-client4-core`, `upickle`. |
| Requirements | JDK 17+, Scala 3.3+. Live calls need `TYPESAFE_API_KEY` (optional `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`). |
| License | [Apache-2.0](https://github.com/ticofab/scala-jev-sdk/blob/374c388637510a25a14cdb11c5323de4fa660ea9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and Maven Central POM inspected. Local `sbt test` was not run (no Scala toolchain on the review host). Live TypeSafe calls were not made. |

## When to use

Use it when a Scala 3 service wants compile-time typed Noul/Choice/Score answers looked up by the question value itself, without adopting a particular effect stack. Prefer [jev4k](jev4k.md) for Kotlin DSL; prefer [jev-sdk-java](jev-sdk-java.md) / [jev-java](jev-java.md) for JVM Java.

## How it works

[`JevClient`](https://github.com/ticofab/scala-jev-sdk/blob/374c388637510a25a14cdb11c5323de4fa660ea9/core/src/main/scala/io/github/ticofab/jev/JevClient.scala) posts to `POST /v1/systemone`. [`Question`](https://github.com/ticofab/scala-jev-sdk/blob/374c388637510a25a14cdb11c5323de4fa660ea9/core/src/main/scala/io/github/ticofab/jev/Question.scala) builders cover noul/choice/score; `answers.get(question)` returns a typed `Option`. Application code still owns thresholds and downstream actions. Retry/backoff is configurable; nothing throws into the effect channel for local validation failures.

## Get started

```sh
# libraryDependencies += "io.github.ticofab" %% "scala-jev-sdk" % "0.1.0"
git clone https://github.com/ticofab/scala-jev-sdk.git
cd scala-jev-sdk
git checkout 374c388637510a25a14cdb11c5323de4fa660ea9
# With JDK 17+ and sbt: sbt test
```

Live `JevClient.create(...)` / `ask` sends state and questions to TypeSafe and may incur charges.

## Examples and demos

- README quickstart (`Question.noul` / `choice` / `score`, multi-question `ask`).
- `examples/` in the repo; MUnit suite under `core/src/test`.
- Upstream CI badge and Maven Central badge on the README; Central POM for `0.1.0` returned HTTP 200 on the review host.

## Limits and data handling

Request state and question text leave the host on live calls. Do not embed API keys in distributed clients. Effect interoperability depends on the sttp backend you pass; live API parity beyond source inspection was not re-measured here.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 374c388](https://github.com/ticofab/scala-jev-sdk/tree/374c388637510a25a14cdb11c5323de4fa660ea9): **0.1.0**, Apache-2.0. AI-assisted source review of README, `JevClient` / `Question` / `JevConfig`, LICENSE, CHANGELOG. No local sbt run. Maven Central POM for `io.github.ticofab:scala-jev-sdk_3:0.1.0` returned HTTP 200. No live TypeSafe calls.

Related: [jev-sdk-java](jev-sdk-java.md), [jev4k](jev4k.md), [jev-java](jev-java.md), [typesafe-api (Rust)](typesafe-api-rs.md).
