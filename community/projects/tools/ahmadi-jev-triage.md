# jev-triage (warehouse remarks benchmark)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Spring Boot benchmark comparing Java keyword rules, Jev and Claude Haiku 5.5 on triaging warehouse goods-receipt remarks (category, block from putaway, severity), with accuracy, latency and cost per 100k decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mohammedahmadi1990/jev-triage) |
| Maintainer | [mohammedahmadi1990](https://github.com/mohammedahmadi1990). Independently curated. |
| Format | Java Spring Boot project (Gradle) with datasets and analysis output |
| Requirements | Java and Gradle; a TypeSafe API key and an Anthropic key to re-run the model strategies. |
| License | [MIT](https://github.com/mohammedahmadi1990/jev-triage/blob/9f90e768f619cebd19d1e0f9b96961579911c508/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/org/ahmadi/jevtriage/jev/JevClient.java`](https://github.com/mohammedahmadi1990/jev-triage/blob/9f90e768f619cebd19d1e0f9b96961579911c508/src/main/java/org/ahmadi/jevtriage/jev/JevClient.java) at the pinned commit. |

## When to use

- See where a decision model beats rules and where an LLM still wins on a concrete logistics task.
- Reuse the Spring Boot client and benchmark profiles for your own data.
- Mismatch: 100 synthetic test remarks; some criteria and labels changed after the first run, as the author discloses.

## How it works

`JevClient.java` posts each remark with typed questions to `/v1/systemone`; the benchmark profile runs rules, Jev (two criteria versions) and Haiku over the same split. The README reports 100% category accuracy for both models, block accuracy of 72% to 85% for Jev against 98% for Haiku, and Jev about 6 to 8 times faster and 9 times cheaper. Integration evidence: [`src/main/java/org/ahmadi/jevtriage/jev/JevClient.java`](https://github.com/mohammedahmadi1990/jev-triage/blob/9f90e768f619cebd19d1e0f9b96961579911c508/src/main/java/org/ahmadi/jevtriage/jev/JevClient.java).

## Get started

From the upstream README (not run on the review host):

```sh
./gradlew bootRun --args='--spring.profiles.active=smoke'
./gradlew bootRun --args='--spring.profiles.active=benchmark --benchmark.limit=5 --benchmark.repeats=1'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full analysis output in `analysis/final/analysis-output.txt`.
- Companion to the author's article on testing Jev with Spring Boot.

## Limits and data handling

Synthetic remarks go to TypeSafe and Anthropic on your keys when you re-run.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 9f90e768f619](https://github.com/mohammedahmadi1990/jev-triage/tree/9f90e768f619cebd19d1e0f9b96961579911c508). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
