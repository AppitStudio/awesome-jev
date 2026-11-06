# Spring AI hybrid search + System One Jev (Java demo that reranks and filters RAG hits with TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Spring AI demo that combines hybrid search with TypeSafe System One Jev for filtering and reranking: `SystemOneFilter` / `SystemOneReranker` wrap a recording TypeSafe client so RAG hits get typed decisions before they reach the user.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev) |
| Maintainer | [letrthang](https://github.com/letrthang). Independently curated. |
| Format | Java / Spring Boot demo (Apache-2.0) |
| Requirements | Java and Maven as in the POM, plus TypeSafe credentials for live System One calls. |
| License | [Apache-2.0](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/blob/58c45e409b63d1f7e28c76df49585a69df843bed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/com/example/ragdemo/system1/SystemOneReranker.java`](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/blob/58c45e409b63d1f7e28c76df49585a69df843bed/src/main/java/com/example/ragdemo/system1/SystemOneReranker.java) at the pinned commit. |

## When to use

- Prototype Jev-gated RAG in Spring AI.
- Record System One calls while developing filters/rerankers.
- Mismatch: demo quality; not a production starter kit.

## How it works

`SystemOneReranker` and `SystemOneFilter` call through `RecordingTypeSafeClient` to TypeSafe System One; tests cover the system1 package. Integration evidence: [`src/main/java/com/example/ragdemo/system1/SystemOneReranker.java`](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/blob/58c45e409b63d1f7e28c76df49585a69df843bed/src/main/java/com/example/ragdemo/system1/SystemOneReranker.java).

## Get started

From the upstream README (not run on the review host):

```sh
mvn test
# configure TypeSafe credentials per README before a live run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/blob/58c45e409b63d1f7e28c76df49585a69df843bed/README.md](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/blob/58c45e409b63d1f7e28c76df49585a69df843bed/README.md)

## Limits and data handling

Retrieved passages sent for filtering/reranking go to TypeSafe on live runs.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 58c45e409b63](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev/tree/58c45e409b63d1f7e28c76df49585a69df843bed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
