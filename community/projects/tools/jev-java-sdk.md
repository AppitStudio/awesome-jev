# Jev Java SDK (dmishra2022)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community Java 26 client for the System One API with typed noul, choice and score questions, retries, timeouts and virtual threads, plus an optional structured-concurrency module and Spring Boot 4 sample.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dmishra2022/jev-java-sdk) |
| Maintainer | [dmishra2022](https://github.com/dmishra2022). Independently curated. |
| Format | Java library (Maven/Gradle, Jackson 3) |
| Requirements | JDK 26 (`--enable-preview` only for `jev-sdk-structured` and the triage sample); `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/dmishra2022/jev-java-sdk/blob/770a411026f891ed63c8edaee64eca339587d864/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-sdk/src/main/java/io/github/dmishra2022/jev/JevClient.java`](https://github.com/dmishra2022/jev-java-sdk/blob/770a411026f891ed63c8edaee64eca339587d864/jev-sdk/src/main/java/io/github/dmishra2022/jev/JevClient.java) at the pinned commit. |

## When to use

- Call Jev from a JVM service with typed answers and confidence checks.
- Fan out many questions with hedging and chunking on virtual threads.
- Mismatch: targets JDK 26; older Java versions are not supported.

## How it works

`JevClient.create()` reads `TYPESAFE_API_KEY` and posts state plus typed questions to TypeSafe (`JevClient.java`); results expose helpers like `isTrue()`, `choice()` and `isConfident(0.8)`. Integration evidence: [`jev-sdk/src/main/java/io/github/dmishra2022/jev/JevClient.java`](https://github.com/dmishra2022/jev-java-sdk/blob/770a411026f891ed63c8edaee64eca339587d864/jev-sdk/src/main/java/io/github/dmishra2022/jev/JevClient.java).

## Get started

From the upstream README (not run on the review host):

```sh
<dependency>
  <groupId>io.github.dmishra2022</groupId>
  <artifactId>jev-sdk</artifactId>
  <version>0.1.0</version>
</dependency>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Spring Boot sample: [github.com/dmishra2022/jev-java-sdk/tree/main/jev-spring-boot-sample](https://github.com/dmishra2022/jev-java-sdk/tree/main/jev-spring-boot-sample)
- Offline triage sample: [github.com/dmishra2022/jev-java-sdk/tree/main/jev-sample](https://github.com/dmishra2022/jev-java-sdk/tree/main/jev-sample)

## Limits and data handling

State text is sent to TypeSafe. Community SDK, not affiliated with TypeSafe; wire format follows the public API reference.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 770a411026f8](https://github.com/dmishra2022/jev-java-sdk/tree/770a411026f891ed63c8edaee64eca339587d864). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
