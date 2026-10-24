# Flink Jev (Jev yes/no decisions in Flink SQL with ML_PREDICT)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community model provider for Apache Flink 2.3 `ML_PREDICT`: asks Jev one yes/no question per row and returns a probability, a route (yes, no, review or failure) and a SHA-256 digest of the text, with uncertain answers kept apart for review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/flink-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Java library (Flink model provider JAR) |
| Requirements | Java 17 and Maven 3.9.6+ to build; an Apache Flink 2.3 cluster; a TypeSafe API key in the TaskManagers' environment. |
| License | [MIT](https://github.com/gbesse/flink-jev/blob/c155770b2b164fd395c60072f3fafd24f04cb8c2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/io/github/gbesse/flink/jev/JevModelProviderFactory.java`](https://github.com/gbesse/flink-jev/blob/c155770b2b164fd395c60072f3fafd24f04cb8c2/src/main/java/io/github/gbesse/flink/jev/JevModelProviderFactory.java) at the pinned commit. |

## When to use

- Classify streaming text such as reviews or tickets inside Flink SQL.
- Keep uncertain rows in a review route instead of forcing a no.
- Mismatch: each row can make a remote call; use a small sample first.

## How it works

`JevModelProviderFactory.java` sets `https://api.typesafe.ai/v1/systemone` and `jev-1.13.0` as defaults; `CREATE MODEL ... WITH ('provider' = 'jev', 'question' = ..., 'threshold' = ...)` configures each model. README in English, French and Spanish. Integration evidence: [`src/main/java/io/github/gbesse/flink/jev/JevModelProviderFactory.java`](https://github.com/gbesse/flink-jev/blob/c155770b2b164fd395c60072f3fafd24f04cb8c2/src/main/java/io/github/gbesse/flink/jev/JevModelProviderFactory.java).

## Get started

From the upstream README (not run on the review host):

```sh
mvn -B verify
# copy target/flink-jev-0.1.2.jar to lib/ on every JobManager and TaskManager
export JEV_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Review inbox example: [github.com/gbesse/flink-jev/blob/main/examples/review-inbox.sql](https://github.com/gbesse/flink-jev/blob/main/examples/review-inbox.sql)
- README: [github.com/gbesse/flink-jev#readme](https://github.com/gbesse/flink-jev#readme)

## Limits and data handling

Row text is sent to TypeSafe. Limits on input size and calls per task are configurable.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit c155770b2b16](https://github.com/gbesse/flink-jev/tree/c155770b2b164fd395c60072f3fafd24f04cb8c2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
