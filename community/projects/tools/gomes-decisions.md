# decisions by gomes (Spring Boot playground and REST API that sends one request format to TypeSafe Jev and other decision APIs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Java 21 / Spring Boot app that puts the common decision APIs behind one request format: a playground at `/` that runs the same typed questions on the providers you enable and compares their answers side by side, a REST API at `/api/v1` with RFC 9457 errors, and an Actuator health check. Providers are TypeSafe Jev (`jev-latest` over System One), OpenAI Decisions, Azure OpenAI Decisions, Gemini Decisions, Microsoft-Decision-1, any System One-compatible host and an offline keyword heuristic for trying it without keys. Jev is one of several providers. Docs in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gomes/decisions) |
| Maintainer | [gomes](https://github.com/gomes). Independently curated. |
| Format | Spring Boot web app and REST API (Java, Maven wrapper) |
| Requirements | Java 21+, the bundled Maven wrapper; `TYPESAFE_API_KEY` for Jev (other provider keys optional; without keys only the offline heuristic runs). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/io/github/gomes/decisions/provider/systemone/SystemOneProvider.java`](https://github.com/gomes/decisions/blob/002fb3e47d8960515a9893e5a6ca00195b37fb0b/src/main/java/io/github/gomes/decisions/provider/systemone/SystemOneProvider.java) at the pinned commit. |

## When to use

- Compare Jev's answers with other decision APIs on the same typed questions from one playground.
- Mismatch: a hosted service; it is a local app that uses the keys configured on the server.

## How it works

`provider/systemone/SystemOneProvider.java` and `SystemOneCodec.java` post typed questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default (`TYPESAFE_BASE_URL` and `TYPESAFE_MODEL` override it, set in `application.yml`); the same codec serves Microsoft-Decision-1 and other System One hosts. Integration evidence: [`src/main/java/io/github/gomes/decisions/provider/systemone/SystemOneProvider.java`](https://github.com/gomes/decisions/blob/002fb3e47d8960515a9893e5a6ca00195b37fb0b/src/main/java/io/github/gomes/decisions/provider/systemone/SystemOneProvider.java).

## Get started

Clone, set the keys you have and start the app.

```sh
git clone https://github.com/gomes/decisions && cd decisions
export TYPESAFE_API_KEY=...   # optional; others: OPENAI_API_KEY, GEMINI_API_KEY ...
./mvnw spring-boot:run          # http://localhost:8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gomes/decisions/blob/002fb3e47d8960515a9893e5a6ca00195b37fb0b/README.md](https://github.com/gomes/decisions/blob/002fb3e47d8960515a9893e5a6ca00195b37fb0b/README.md)

## Limits and data handling

Questions and state go to each enabled provider on your keys. The app has no login of its own; put a proxy or SSO in front if you expose it. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 002fb3e47d89](https://github.com/gomes/decisions/tree/002fb3e47d8960515a9893e5a6ca00195b37fb0b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
