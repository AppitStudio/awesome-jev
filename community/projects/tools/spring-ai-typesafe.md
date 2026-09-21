# Spring AI TypeSafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Java client for TypeSafe System One (Jev) on Spring `RestClient` / Jackson, plus Spring AI integrations: `JevJudge`, guardrail/self-refine advisors, RAG post-processor, and tool-search index. Community project under `spring-ai-community`; unofficial relative to TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/spring-ai-community/spring-ai-typesafe) |
| Maintainer | [spring-ai-community](https://github.com/spring-ai-community) / [spring-ai-typesafe](https://github.com/spring-ai-community/spring-ai-typesafe). Independently curated; this page is not an upstream submission or endorsement. Unofficial—not maintained by TypeSafe. |
| Format | Maven multi-module **0.1.0** (`typesafe-java-sdk`, `typesafe-spring-ai`, `spring-ai-starter-typesafe`, BOM); groupId `org.springaicommunity`. Docs site linked from the README. |
| Requirements | Java 17+. Live calls need a TypeSafe API key (`spring.ai.typesafe.*` / client configuration). Spring AI modules need a Spring AI-compatible app. |
| License | [Apache-2.0](https://github.com/spring-ai-community/spring-ai-typesafe/blob/fd8110c0ea8aa3061b8a47db9175e053ba6de523/LICENSE.txt). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source and module layout inspected; unit tests exist under each module but were **not executed** (no JDK on the review host). Live TypeSafe calls were not run. Distinct from [jev-java](jev-java.md) (different groupId/modules; this repo adds Spring AI advisors/RAG/tool-search SPIs). |

## When to use

Use it when a Spring Boot / Spring AI service wants typed Noul/Choice/Score judgments, LLM-as-judge helpers, or RAG/tool filtering driven by Jev probabilities. Prefer [jev-java](jev-java.md) for a smaller unofficial Java client with OpenRouter/Vercel adapters and without Spring AI SPIs. Prefer the official JS/Python SDKs outside the JVM.

## How it works

`TypeSafeClient.systemOne` posts state plus typed questions and returns structured answers (see upstream README examples). `typesafe-spring-ai` wraps the client as `JevJudge` and advisors that act on probabilities in application code. The starter auto-configures a `TypeSafeClient` bean from `spring.ai.typesafe.*` properties.

## Get started

```xml
<dependency>
  <groupId>org.springaicommunity</groupId>
  <artifactId>typesafe-java-sdk</artifactId>
  <version>0.1.0</version>
</dependency>
```

From source:

```sh
git clone https://github.com/spring-ai-community/spring-ai-typesafe.git
cd spring-ai-typesafe
git checkout fd8110c0ea8aa3061b8a47db9175e053ba6de523
# ./mvnw -pl typesafe-java-sdk -am test   # needs JDK 17+; not run here
```

Reference docs: [spring-ai-community.github.io/spring-ai-typesafe](https://spring-ai-community.github.io/spring-ai-typesafe/latest-snapshot/).

## Examples and demos

- Upstream README shows Choice/Noul/Score usage and module table.
- Example/demo tests under `examples/` and advisor tests under `typesafe-spring-ai/src/test` (not executed on this host).

## Limits and data handling

Live `systemOne` calls send state and questions to TypeSafe. Confirm Spring AI and TypeSafe versions/compatibility from the docs site. Snapshot coordinates appear in some README snippets—prefer the **0.1.0** release tag for pinned installs. Unofficial community SDK—not affiliated with TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [tag v0.1.0 / commit fd8110c](https://github.com/spring-ai-community/spring-ai-typesafe/tree/fd8110c0ea8aa3061b8a47db9175e053ba6de523): **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE.txt, module layout, and test file presence. No JDK test run; no live provider call.

Related: [jev-java](jev-java.md), [TypeSafeAI.Net](typesafeai-net.md), [TypeSafe Go](typesafe-go.md).
