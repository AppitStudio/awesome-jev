# AgentScope Java Jev extension (typed Jev decisions for Java agent harnesses: tool selection, response review, routing, context and task supervision)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

`agentscope-extensions-jev` for Alibaba's AgentScope Java adds a reactive `JevClient` and a set of opt-in components that bring typed Jev decisions into an agent harness: tool selection and pre-execution checks, conditional response review and draft revision, retrieval evidence checks, model and stage routing, context compaction and memory admission, long-task supervision, and trace evaluation. Middleware defaults to OFF, a SHADOW mode records recommendations without acting, and the docs state that a semantic approval never replaces authorization or proves an action happened.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agentscope-ai/agentscope-java) |
| Maintainer | [agentscope-ai](https://github.com/agentscope-ai). Independently curated. |
| Format | Java library (Maven artifact `agentscope-extensions-jev`) inside the AgentScope Java framework |
| Requirements | Java and Maven; a `TYPESAFE_API_KEY` (or `JEV_API_KEY`) for live calls; the offline example needs no key. |
| License | [Apache-2.0](https://github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/awais_khawar/status/2118059454394667009)). |
| Jev evidence | [`agentscope-extensions/agentscope-extensions-judge/agentscope-extensions-jev/src/main/java/io/agentscope/extensions/judge/jev/JevClient.java`](https://github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/agentscope-extensions/agentscope-extensions-judge/agentscope-extensions-jev/src/main/java/io/agentscope/extensions/judge/jev/JevClient.java) at the pinned commit. |

## When to use

- Add typed, auditable semantic checks (tool choice, answer review, routing, supervision) to a Java agent while keeping authorization and completion checks in deterministic code.
- Mismatch: Jev is an optional extension of a large framework, and the detailed guides are currently Chinese-only.

## How it works

`JevClient.java` builds typed System One requests (state plus noul, choice and score questions) and posts them to `https://api.typesafe.ai` with model `jev-latest`, a 5-second timeout and a retry policy; harness middleware, defaulting to OFF, maps the answers to the component-specific policies. Integration evidence: [`agentscope-extensions/agentscope-extensions-judge/agentscope-extensions-jev/src/main/java/io/agentscope/extensions/judge/jev/JevClient.java`](https://github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/agentscope-extensions/agentscope-extensions-judge/agentscope-extensions-jev/src/main/java/io/agentscope/extensions/judge/jev/JevClient.java).

## Get started

From the upstream docs (not run on the review host):

```sh
<dependency>
  <groupId>io.agentscope</groupId>
  <artifactId>agentscope-extensions-jev</artifactId>
  <version>${agentscope.version}</version>
</dependency>
# offline scripted example, no key: see the Jev page in the docs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs overview (English): [github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/docs/v2/en/jev/index.md](https://github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/docs/v2/en/jev/index.md)
- Client guide (Chinese): [github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/docs/v2/zh/jev/guides/client.md](https://github.com/agentscope-ai/agentscope-java/blob/f9d717ec56201404067d26b55f4308c3ef69ef16/docs/v2/zh/jev/guides/client.md)
- Announcement post on X: [x.com/awais_khawar/status/2118059454394667009](https://x.com/awais_khawar/status/2118059454394667009)

## Limits and data handling

Live decisions send the state you pass (answers, records, messages) to TypeSafe on your key; ENFORCE mode applies component policies, so start in SHADOW. The extension is separate from the already-listed Python AgentScope entry. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit f9d717ec5620](https://github.com/agentscope-ai/agentscope-java/tree/f9d717ec56201404067d26b55f4308c3ef69ef16). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
