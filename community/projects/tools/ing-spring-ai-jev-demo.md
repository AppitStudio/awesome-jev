# ING AI Guild Spring AI demos (compliance RAG where Jev screens and reranks passages)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Two Spring AI demos shown at the ING AI Guild meetup on 27 October 2026, built on use cases ING runs on its GenAI platform: a compliance assistant for new products in a naive RAG and a modular RAG version, and a customer-support agent. In the modular version Jev screens the retrieved passages for injection, contradiction and relevance and reranks them before Gemini answers. Slides included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tzolov/ing-guild-meetup-demo) |
| Maintainer | [tzolov](https://github.com/tzolov). Independently curated. |
| Format | Java 17 Spring Boot CLI apps (Maven) |
| Requirements | Java 17+, Maven, Gemini on Vertex AI and a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ing-compliance-assistant-3/src/main/java/com/example/demo/ComplianceAssistantApplication.java`](https://github.com/tzolov/ing-guild-meetup-demo/blob/7f28411eca3977f2f4a12fa7d7403904c221a3be/ing-compliance-assistant-3/src/main/java/com/example/demo/ComplianceAssistantApplication.java) at the pinned commit. |

## When to use

- See Jev as a post-retrieval filter in a Spring AI RAG pipeline.
- Mismatch: demo code with synthetic passages.

## How it works

The module uses the community `spring-ai-starter-typesafe` (`TypeSafeClient`, `JevDocumentFilter`, `JevDocumentReranker`) to screen and reorder passages before the model call. Integration evidence: [`ing-compliance-assistant-3/src/main/java/com/example/demo/ComplianceAssistantApplication.java`](https://github.com/tzolov/ing-guild-meetup-demo/blob/7f28411eca3977f2f4a12fa7d7403904c221a3be/ing-compliance-assistant-3/src/main/java/com/example/demo/ComplianceAssistantApplication.java).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tzolov/ing-guild-meetup-demo && cd ing-guild-meetup-demo
cp .env.example .env   # Vertex AI project and TYPESAFE_API_KEY
mvn install -DskipTests
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Slides: [github.com/tzolov/ing-guild-meetup-demo/blob/main/slides/ING-2026-Oct-Final.pdf](https://github.com/tzolov/ing-guild-meetup-demo/blob/main/slides/ING-2026-Oct-Final.pdf)
- README: [github.com/tzolov/ing-guild-meetup-demo#readme](https://github.com/tzolov/ing-guild-meetup-demo#readme)

## Limits and data handling

Retrieved passages go to TypeSafe for screening and to Gemini for answers.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7f28411eca39](https://github.com/tzolov/ing-guild-meetup-demo/tree/7f28411eca3977f2f4a12fa7d7403904c221a3be). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
