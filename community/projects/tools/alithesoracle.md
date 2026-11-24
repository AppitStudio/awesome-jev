# AlithesOracle by Efstathios Papafotis (self-hosted service that settles yes/no questions about real-world events from independent news coverage, with Jev judging each article)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Spring Boot service that answers discrete yes/no questions about public events (elections, rulings, deals) from multi-source news (GDELT, news RSS fallbacks, Wikipedia citations). Jev assesses each article's stance; deterministic consensus rules, syndication clustering and a `DISPUTED` state decide the outcome, with an evidence trail, REST API, web console and signed webhooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LinearRecession/AlithesOracle) |
| Maintainer | [LinearRecession](https://github.com/LinearRecession). Independently curated. |
| Format | Java / Spring Boot service with PostgreSQL (Docker Compose) |
| Requirements | Docker (or Java and Maven) and a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/io/alithes/oracle/client/JevClient.java`](https://github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/src/main/java/io/alithes/oracle/client/JevClient.java) at the pinned commit. |

## When to use

- Automate checking whether a public event happened, with an auditable evidence trail.
- Mismatch: settling real money without human review; treat outcomes as evidence, not ground truth.

## How it works

`src/main/java/io/alithes/oracle/client/JevClient.java` posts article stance questions to `https://api.typesafe.ai/v1/systemone` and can reject aliased models so a pinned version such as `jev-1.14.0` is used; tests run offline against WireMock stubs. Integration evidence: [`src/main/java/io/alithes/oracle/client/JevClient.java`](https://github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/src/main/java/io/alithes/oracle/client/JevClient.java).

## Get started

Copy the example env file, set `TYPESAFE_API_KEY`, and start the stack with Docker Compose; the console is on port 8080.

```sh
git clone https://github.com/LinearRecession/AlithesOracle.git && cd AlithesOracle
cp .env.example .env   # set TYPESAFE_API_KEY
docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with architecture and REST API: [github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/README.md](https://github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/README.md)
- Build spec: [github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/BUILD_SPEC.md](https://github.com/LinearRecession/AlithesOracle/blob/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75/BUILD_SPEC.md)

## Limits and data handling

News excerpts are sent to TypeSafe and billed to your key. Outcome quality depends on news coverage and the consensus rules; claims about manipulation resistance are the maintainer's. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit fafbf8b3f405](https://github.com/LinearRecession/AlithesOracle/tree/fafbf8b3f4057a7f838d41e3f9ebe8bf4e3d4e75). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
