# jev-sdk (dev.isira, Java 25)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small unofficial Java client for `https://api.typesafe.ai/v1/systemone`, published on Maven Central as `dev.isira:jev-sdk`: send a state with Choice, Score or Noul questions and get typed answers with probabilities and token usage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SL-Pirate/jev-sdk-java) |
| Maintainer | [SL-Pirate](https://github.com/SL-Pirate). Independently curated. |
| Format | Java library (Maven Central) |
| Requirements | Java 25+; a Jev API key. |
| License | [MIT](https://github.com/SL-Pirate/jev-sdk-java/blob/8ba83d4160b503b3b694058366b6092ae7569da7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/dev/isira/jev/JevClient.java`](https://github.com/SL-Pirate/jev-sdk-java/blob/8ba83d4160b503b3b694058366b6092ae7569da7/src/main/java/dev/isira/jev/JevClient.java) at the pinned commit. |

## When to use

- Call Jev from a modern Java service without hand-writing HTTP.
- Want a published Maven artifact rather than a source build.
- Mismatch: requires Java 25; for Java 17 or 21 see the other Java clients in this catalog.

## How it works

`JevClient` builds a JSON request for the System One endpoint with JDK `HttpClient` and maps responses into typed answers: the chosen option and per-option probabilities for Choice, a score and legend for Score, and a value from 0 to 1 for Noul. Integration evidence: [`src/main/java/dev/isira/jev/JevClient.java`](https://github.com/SL-Pirate/jev-sdk-java/blob/8ba83d4160b503b3b694058366b6092ae7569da7/src/main/java/dev/isira/jev/JevClient.java).

## Get started

From the upstream README: add `dev.isira:jev-sdk` from Maven Central and create a client with your key.

```sh
dependencies {
    implementation("dev.isira:jev-sdk:1.0.2")
}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README question-type table and usage examples

## Limits and data handling

State text goes to TypeSafe. Unofficial; not affiliated with TypeSafe. Distinct from [jev-sdk-java](jev-sdk-java.md) (Java 21).

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 8ba83d4160b5](https://github.com/SL-Pirate/jev-sdk-java/tree/8ba83d4160b503b3b694058366b6092ae7569da7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
