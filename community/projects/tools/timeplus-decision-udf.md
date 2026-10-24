# Timeplus decision UDF (System One decisions inside streaming SQL)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Proof of concept from Timeplus: a Python UDF inside Timeplus Enterprise calls a System One decision model on streaming windows, with two pipelines for video QoE incident triage and edge DDoS response, and a scorecard against rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timeplus-io/decision-udf-poc) |
| Maintainer | [timeplus-io](https://github.com/timeplus-io). Independently curated. |
| Format | SQL files and Python UDF (Docker) |
| Requirements | Docker; Timeplus Enterprise (amd64); a TypeSafe key for Jev Cloud, or a local model through Ollama. |
| License | [Apache-2.0](https://github.com/timeplus-io/decision-udf-poc/blob/1488b7050051e4e2217b49de8b2ed42a27f4ec4e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sql/01_udf.sql`](https://github.com/timeplus-io/decision-udf-poc/blob/1488b7050051e4e2217b49de8b2ed42a27f4ec4e/sql/01_udf.sql) at the pinned commit. |

## When to use

- Make typed decisions on live event windows without leaving the stream engine.
- Compare model decisions with threshold rules on exact ground truth.
- Mismatch: needs Timeplus Enterprise; Python UDFs are not in Proton OSS.

## How it works

The UDF in `sql/01_udf.sql` posts choice and score questions to `https://api.typesafe.ai/v1/systemone` when `DECISION_BACKEND=jev` (`jev-1.13.0`), or to a local `/v1/systemone` server; results land in a decision log. Integration evidence: [`sql/01_udf.sql`](https://github.com/timeplus-io/decision-udf-poc/blob/1488b7050051e4e2217b49de8b2ed42a27f4ec4e/sql/01_udf.sql).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # DECISION_BACKEND=jev, DECISION_MODEL=jev-1.13.0, TYPESAFE_API_KEY=...
docker compose up -d
./scripts/install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/timeplus-io/decision-udf-poc#readme](https://github.com/timeplus-io/decision-udf-poc#readme)

## Limits and data handling

Synthetic data generated inside the engine. Window summaries are sent to the chosen backend.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 1488b7050051](https://github.com/timeplus-io/decision-udf-poc/tree/1488b7050051e4e2217b49de8b2ed42a27f4ec4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
