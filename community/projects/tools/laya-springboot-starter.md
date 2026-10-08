# Laya Spring Boot Starter

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community Spring Boot 4 starter that auto-configures a `LayaClient` (Spring MVC + RestClient + Jackson 3) for self-hosted Laya's Jev-compatible `POST /v1/systemone`, with typed `choice`, `score` and `noul` questions and several decisions in one request; inspired by the Jev Spring Boot Starter but an original implementation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kelsonthony/laya-springboot-starter) |
| Maintainer | [kelsonthony](https://github.com/kelsonthony). Independently curated. |
| Format | Maven Spring Boot starter (`io.github.kelsonthony:laya-springboot-starter`, 0.1.0-SNAPSHOT; install locally) |
| Requirements | Java 17+, Spring Boot 4 (Spring MVC), a running Laya server (`pip install "laya[serve]"`, `laya-serve`); optional `LAYA_API_KEY`. Not a hosted Jev client. |
| License | [Apache-2.0](https://github.com/kelsonthony/laya-springboot-starter/blob/b37cf09dab1177299c5a34e29c8a095581eb773c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep typed decisions on your own infrastructure in a Spring MVC service.
- Prototype with Laya and keep the same question shapes as Jev.
- Mismatch: not on Maven Central yet; for hosted Jev use the Jev Spring Boot Starter instead.

## How it works

[`LayaClient.java`](https://github.com/kelsonthony/laya-springboot-starter/blob/b37cf09dab1177299c5a34e29c8a095581eb773c/src/main/java/io/github/kelsonthony/laya/LayaClient.java) builds requests from [`Question.java`](https://github.com/kelsonthony/laya-springboot-starter/blob/b37cf09dab1177299c5a34e29c8a095581eb773c/src/main/java/io/github/kelsonthony/laya/Question.java) factories and parses labels, probabilities and confidence; `laya.base-url` / `laya.api-key` properties configure it. A support-triage example lives in [`examples/support-triage`](https://github.com/kelsonthony/laya-springboot-starter/tree/b37cf09dab1177299c5a34e29c8a095581eb773c/examples/support-triage).

## Get started

Install the starter locally, run Laya, then add the dependency (README *Getting started*):

```sh
git clone https://github.com/kelsonthony/laya-springboot-starter.git && cd laya-springboot-starter
./mvnw clean install
python -m pip install "laya[serve]" && LAYA_HOST=127.0.0.1 laya-serve
```

No hosted inference charges when you self-host Laya.

## Examples and demos

- [Support triage example](https://github.com/kelsonthony/laya-springboot-starter/tree/b37cf09dab1177299c5a34e29c8a095581eb773c/examples/support-triage).
- Portuguese README: [`README.pt-BR.md`](https://github.com/kelsonthony/laya-springboot-starter/blob/b37cf09dab1177299c5a34e29c8a095581eb773c/README.pt-BR.md).

## Limits and data handling

Requests go to your own Laya server. Not an official SDK; not affiliated with TypeSafe or the Laya authors. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b37cf09dab11](https://github.com/kelsonthony/laya-springboot-starter/tree/b37cf09dab1177299c5a34e29c8a095581eb773c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
