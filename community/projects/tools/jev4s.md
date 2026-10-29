# jev4s (typed Scala 3 and 2.13 client for Jev, with Spark 4 support)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Scala client: in Scala 3 the compiler checks your questions and answers (asking for an answer you did not request, or reading it as the wrong type, fails to compile); in Scala 2.13 it targets Spark 4 so you can ask Jev about each row of a Dataset. Plain direct-style calls returning `Either[JevError, A]`, virtual threads on JDK 21.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maxtrezzi/jev4s) |
| Maintainer | [maxtrezzi](https://github.com/maxtrezzi). Independently curated. |
| Format | Scala library (Maven Central `io.github.maxtrezzi::jev4s`) |
| Requirements | Scala 3.9 or 2.13, a JDK and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/maxtrezzi/jev4s/blob/226b216e162b7641e29054eda9f9ab4e2e681d5b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scala213/src/main/scala/io/github/maxtrezzi/jev4s/JevConfig.scala`](https://github.com/maxtrezzi/jev4s/blob/226b216e162b7641e29054eda9f9ab4e2e681d5b/scala213/src/main/scala/io/github/maxtrezzi/jev4s/JevConfig.scala) at the pinned commit. |

## When to use

- Use Jev from Scala or Spark jobs with type safety.
- Mismatch: unofficial; version 0.1.0.

## How it works

`JevConfig.scala` and `JdkTransport.scala` build requests to TypeSafe's `/v1/systemone` endpoint and decode typed answers. Integration evidence: [`scala213/src/main/scala/io/github/maxtrezzi/jev4s/JevConfig.scala`](https://github.com/maxtrezzi/jev4s/blob/226b216e162b7641e29054eda9f9ab4e2e681d5b/scala213/src/main/scala/io/github/maxtrezzi/jev4s/JevConfig.scala).

## Get started

From the upstream README (not run on the review host):

```sh
// build.sbt
libraryDependencies += "io.github.maxtrezzi" %% "jev4s" % "0.1.0"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Scala 3 guide: [github.com/maxtrezzi/jev4s/blob/main/docs/guide/scala3.md](https://github.com/maxtrezzi/jev4s/blob/main/docs/guide/scala3.md)
- README: [github.com/maxtrezzi/jev4s#readme](https://github.com/maxtrezzi/jev4s#readme)

## Limits and data handling

Each request goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 226b216e162b](https://github.com/maxtrezzi/jev4s/tree/226b216e162b7641e29054eda9f9ab4e2e681d5b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
