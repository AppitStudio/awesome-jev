# Jev Feedback Triage by Dan Vega (Spring AI 2.1 Decision API sample that triages customer messages with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small Spring Boot app that shows the Decision API new in Spring AI 2.1 with TypeSafe Jev: one call asks a yes/no question (needs a reply today?), a choice (Billing, Technical or Sales) and a score (Unhappy, Neutral, Happy), and the endpoint returns typed results such as `urgent` only when Jev is at least 80% sure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danvega/jev-feedback-triage) |
| Maintainer | [danvega](https://github.com/danvega). Independently curated. |
| Format | Spring Boot sample app (Java 25, Spring AI 2.1.0-RC2; no license file) |
| Requirements | JDK 25+ and a TypeSafe key (`TYPESAFE_API_KEY`). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/dev/danvega/triage/FeedbackTriageApplication.java`](https://github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/src/main/java/dev/danvega/triage/FeedbackTriageApplication.java) at the pinned commit. |

## When to use

- Learn the Spring AI Decision API with a realistic support-triage example.
- Mismatch: a production triage service; it is a teaching sample on release-candidate versions.

## How it works

`FeedbackTriageApplication.java` builds a `SystemOneDecisionModel` from the community `TypeSafeClient` (there is no Spring Boot starter yet), and `TriageController.java` asks the three typed questions in one call. A unit test swaps in a fake decision model. Integration evidence: [`src/main/java/dev/danvega/triage/FeedbackTriageApplication.java`](https://github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/src/main/java/dev/danvega/triage/FeedbackTriageApplication.java).

## Get started

Export your key, start the app and post a message to `/triage`.

```sh
export TYPESAFE_API_KEY=...
./mvnw spring-boot:run
curl -X POST localhost:8080/triage -H 'Content-Type: application/json' -d '{"message":"I was charged twice"}'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/README.md](https://github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/README.md)
- Sample requests: [github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/requests.http](https://github.com/danvega/jev-feedback-triage/blob/755e57532e4e78086ca4f62e9667a20e63a5f549/requests.http)

## Limits and data handling

Each message you post goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 755e57532e4e](https://github.com/danvega/jev-feedback-triage/tree/755e57532e4e78086ca4f62e9667a20e63a5f549). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
