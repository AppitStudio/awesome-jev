# Quarkus LangChain4j decision routing (Jev/Kev/Laya)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Proof of concept for Quarkus 4 + Quarkus LangChain4j 2: LangChain4j's `DecisionRouterPlanner` uses a small decision model to route car-rental questions to specialist chat agents and merge their answers, with the same typed decisions runnable against hosted TypeSafe Jev, local Kev, an included Laya sidecar or a deterministic stub — plus Jev-backed reply guardrails.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kdubois/quarkus-langchain4j-jev-laya) |
| Maintainer | [kdubois](https://github.com/kdubois). Independently curated. |
| Format | Quarkus application (`./mvnw quarkus:dev`) with a REST endpoint |
| Requirements | JDK + Maven wrapper; `OPENAI_API_KEY`; `TYPESAFE_API_KEY` for hosted Jev (or run Kev/Laya locally, or the stub). |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Prototype decision-model routing in a Java stack.
- Compare hosted Jev with local Kev/Laya on identical decisions.
- Mismatch: beta Quarkus/LangChain4j versions; a PoC, not a library.

## How it works

The `quarkus-langchain4j-typesafe` extension creates a named `DecisionModel` per backend; [`JevReplyGuardrail.java`](https://github.com/kdubois/quarkus-langchain4j-jev-laya/blob/f312884dbeffeb226a74aab2fe8ee0c9afc076e9/src/main/java/com/tripplanner/poc/guardrails/JevReplyGuardrail.java) checks replies and [`DecisionClient.java`](https://github.com/kdubois/quarkus-langchain4j-jev-laya/blob/f312884dbeffeb226a74aab2fe8ee0c9afc076e9/src/main/java/com/tripplanner/poc/jev/DecisionClient.java) abstracts the backends.

## Get started

Run in dev mode with hosted Jev (README):

```sh
git clone https://github.com/kdubois/quarkus-langchain4j-jev-laya.git && cd quarkus-langchain4j-jev-laya
export OPENAI_API_KEY=sk-...
export TYPESAFE_API_KEY=ts-...
./mvnw quarkus:dev
```

OpenAI chat usage plus Jev decisions (or local Kev/Laya for free).

## Examples and demos

- README sample request: “Book an SUV for Saturday and tell me the price with full insurance.” → routes `reservation`, `cost`.

## Limits and data handling

Requests go to OpenAI and the chosen decision backend. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit f312884dbeff](https://github.com/kdubois/quarkus-langchain4j-jev-laya/tree/f312884dbeffeb226a74aab2fe8ee0c9afc076e9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
