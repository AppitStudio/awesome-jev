# Jev Comment Moderation by Dan Vega (Spring AI 2.1 Decision API sample that publishes, holds or rejects blog comments with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

A small Spring Boot app: post a comment and Jev, through the Spring AI 2.1 `DecisionModel`, picks publish, hold or reject; plain Java acts on the typed answer, and when Jev declines to answer a person decides.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danvega/jev-comment-moderation) |
| Maintainer | [danvega](https://github.com/danvega). Independently curated. |
| Format | Java 25 / Spring Boot 4.2 sample app |
| Requirements | JDK 25+; a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/dev/danvega/moderation/ModerationController.java`](https://github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/src/main/java/dev/danvega/moderation/ModerationController.java) at the pinned commit. |

## When to use

- See a minimal Spring AI Decision API moderation flow with a human fallback.
- Mismatch: a production moderation system.

## How it works

`ModerationController.java` calls the auto-configured `DecisionModel` from `spring-ai-starter-model-systemone`; the key is set as `spring.ai.systemone.api-key` in `application.yaml`. Integration evidence: [`src/main/java/dev/danvega/moderation/ModerationController.java`](https://github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/src/main/java/dev/danvega/moderation/ModerationController.java).

## Get started

Export your key and run.

```sh
git clone https://github.com/danvega/jev-comment-moderation.git && cd jev-comment-moderation
export TYPESAFE_API_KEY=...
./mvnw spring-boot:run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/README.md](https://github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/README.md)
- Requests: [github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/requests.http](https://github.com/danvega/jev-comment-moderation/blob/6b93d0c7c75092273d54587eca75c0f12eb85492/requests.http)

## Limits and data handling

Comment text is sent to TypeSafe. No license file. A sibling of the listed Jev Feedback Triage sample by the same author.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 6b93d0c7c750](https://github.com/danvega/jev-comment-moderation/tree/6b93d0c7c75092273d54587eca75c0f12eb85492). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
