# kotlin-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Kotlin/JVM SDK and CLI for TypeSafe Jev System One—typed questions and answers inspired by mattn/go-jev patterns.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/satoshihiraishi/kotlin-jev) |
| Maintainer | [satoshihiraishi](https://github.com/satoshihiraishi). Independently curated. |
| Format | Gradle multi-module (`jev-cli` + library modules). |
| Requirements | JDK/Gradle; `TYPESAFE_API_KEY` for live calls. |
| License | [MIT](https://github.com/satoshihiraishi/kotlin-jev/blob/b0ee7ff7df0067517eb9fe4d292915f263ae3a7e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live CLI/Jev not run. |

## When to use

Use it to call **System One from Kotlin** or a JVM CLI. Prefer [jev4j](jev4j.md) / [spring-ai-typesafe](spring-ai-typesafe.md) for other JVM stacks; [jevgo](jevgo.md) for Go.

## How it works

Gradle modules expose client helpers and a `jev-cli` front-end that posts typed questions to TypeSafe and prints structured answers (see README).

## Get started

```sh
git clone https://github.com/satoshihiraishi/kotlin-jev.git
cd kotlin-jev
git checkout b0ee7ff7df0067517eb9fe4d292915f263ae3a7e
./gradlew build
# TYPESAFE_API_KEY=... ./gradlew :jev-cli:run --args='...'
```

## Examples and demos

- README Japanese/English overview.
- GitHub Actions build/release workflows.

## Limits and data handling

Request payloads leave your process for TypeSafe. Unofficial community port—track upstream API changes.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit b0ee7ff](https://github.com/satoshihiraishi/kotlin-jev/tree/b0ee7ff7df0067517eb9fe4d292915f263ae3a7e). AI-assisted README + tree inspection. No live TypeSafe spend.

Related: [jevgo](jevgo.md), [jev4j](jev4j.md), [TypeSafe Go](typesafe-go.md).
