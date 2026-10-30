# systemone-flink (Apache Flink async operator that asks a System One model typed questions about each streamed event)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Java library for Apache Flink: send candidate events, such as log lines a cheap detector flagged, to any `POST /v1/systemone` server and attach the typed answers (choice, score, yes/no with probabilities) to each record. Endpoint, model, questions, retries, cache and timeouts are configuration, and timeouts or HTTP errors come out as failed decisions instead of failing the job.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Karthiktiwari/systemone-flink) |
| Maintainer | [Karthiktiwari](https://github.com/Karthiktiwari). Independently curated. |
| Format | Java library (Flink 1.20) |
| Requirements | Java 17+, Flink 1.20, Maven (not on Maven Central yet; install locally), and a System One server such as TypeSafe Jev via OpenRouter, Ollama or Laya. |
| License | [Apache-2.0](https://github.com/Karthiktiwari/systemone-flink/blob/835a412e452861a9a5a3b961e4107d7fad4f37aa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`java/src/main/java/dev/systemoneflink/systemone/SystemOneClient.java`](https://github.com/Karthiktiwari/systemone-flink/blob/835a412e452861a9a5a3b961e4107d7fad4f37aa/java/src/main/java/dev/systemoneflink/systemone/SystemOneClient.java) at the pinned commit. |

## When to use

- Classify or score high-volume log or event streams inside a Flink job with a fast typed model.
- Mismatch: early release (0.2.0), install from source; you pick the model server.

## How it works

`SystemOneClient.java` encodes the configured questions into a `/v1/systemone` request and decodes probabilities; `DecideAsyncFunction` runs those calls asynchronously with a cache and an in-flight limit. Integration evidence: [`java/src/main/java/dev/systemoneflink/systemone/SystemOneClient.java`](https://github.com/Karthiktiwari/systemone-flink/blob/835a412e452861a9a5a3b961e4107d7fad4f37aa/java/src/main/java/dev/systemoneflink/systemone/SystemOneClient.java).

## Get started

From the upstream README (not run on the review host):

```sh
mvn -f java/pom.xml install
# then add dev.systemoneflink:systemone-flink:0.2.0 to your Flink job
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with a Java example: [github.com/Karthiktiwari/systemone-flink#readme](https://github.com/Karthiktiwari/systemone-flink#readme)

## Limits and data handling

Event text you choose as state is sent to the configured model server. Independent project; not affiliated with TypeSafe or Apache Flink.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 835a412e4528](https://github.com/Karthiktiwari/systemone-flink/tree/835a412e452861a9a5a3b961e4107d7fad4f37aa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
