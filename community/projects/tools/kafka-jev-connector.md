# Kafka Jev Connector

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Kafka Connect sink connector that sends each record from your input topics to TypeSafe Jev with a question set you configure and publishes an enriched record (original message, answers, trace and dedupe IDs) to an output topic; at-least-once delivery, dead-letter topic, Confluent Cloud custom-connector or self-managed Connect.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smatiolids/kafka-jev-connector) |
| Maintainer | [smatiolids](https://github.com/smatiolids). Independently curated. |
| Format | Kafka Connect plugin ZIP (GitHub release v0.1) or `mvn package` build |
| Requirements | Kafka Connect 4.2 (Confluent Cloud or self-managed), Java 17 to build, and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/smatiolids/kafka-jev-connector/blob/abc55941aaed59e7bfd60c2ba0f906f723af56dd/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Enrich a stream of tickets or messages with typed Jev answers inside your Kafka pipeline.
- Deduplicate evaluations with deterministic Source and Evaluation IDs.
- Mismatch: early release (v0.1).

## How it works

The connector builds an evaluation state from each record (full value or template), posts it with the configured question set to Jev, and writes an enriched record or a sanitized dead-letter record; contracts are in [`docs/record-contracts.md`](https://github.com/smatiolids/kafka-jev-connector/blob/abc55941aaed59e7bfd60c2ba0f906f723af56dd/docs/record-contracts.md) and options in [`docs/configuration.md`](https://github.com/smatiolids/kafka-jev-connector/blob/abc55941aaed59e7bfd60c2ba0f906f723af56dd/docs/configuration.md). A local stack with a fake Jev lives in [`compose.yaml`](https://github.com/smatiolids/kafka-jev-connector/blob/abc55941aaed59e7bfd60c2ba0f906f723af56dd/compose.yaml).

## Get started

Download the plugin ZIP from the latest release (or build it) and follow `SETUP.md`:

```sh
git clone https://github.com/smatiolids/kafka-jev-connector && cd kafka-jev-connector
mvn package   # plugin ZIP in target/; or download it from Releases
```

Each record is one Jev request billed to your TypeSafe key.

## Examples and demos

- [Setup walkthrough](https://github.com/smatiolids/kafka-jev-connector/blob/abc55941aaed59e7bfd60c2ba0f906f723af56dd/SETUP.md) (Confluent Cloud).
- [Architecture decisions](https://github.com/smatiolids/kafka-jev-connector/tree/abc55941aaed59e7bfd60c2ba0f906f723af56dd/docs/adr).

## Limits and data handling

Record content (or the templated fields) goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit abc55941aaed](https://github.com/smatiolids/kafka-jev-connector/tree/abc55941aaed59e7bfd60c2ba0f906f723af56dd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
