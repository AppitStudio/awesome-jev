# jev4s by Polyvariant (typed, purely functional Scala client for Jev on cats-effect and http4s)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Scala 3 client from Polyvariant for the JVM, Scala.js and Scala Native. Questions are typed values (`Question.noul`, `Question.choice[A]`, `Question.score[A]`) with options derived from enums, and compose as an `Applicative` into one request with a typed answer. A separate project from the listed maxtrezzi/jev4s, despite the shared name.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/polyvariant/jev4s) |
| Maintainer | [polyvariant](https://github.com/polyvariant). Independently curated. |
| Format | Scala 3 library (cats-effect, http4s; snapshot builds on Sonatype Central) |
| Requirements | Scala 3, an http4s client such as Ember, and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/src/main/scala/jev4s/Jev.scala`](https://github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/core/src/main/scala/jev4s/Jev.scala) at the pinned commit. |

## When to use

- Call Jev from a functional Scala codebase with compile-time typed questions and answers.
- Mismatch: if you need a stable release (only snapshots are published) or Spark support; see the listed maxtrezzi jev4s for Spark 4.

## How it works

`core/src/main/scala/jev4s/Jev.scala` and `Provider.scala` build System One requests and post them to `https://api.typesafe.ai/v1/systemone`, decoding the answers into the typed result. Integration evidence: [`core/src/main/scala/jev4s/Jev.scala`](https://github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/core/src/main/scala/jev4s/Jev.scala).

## Get started

Add the Sonatype snapshots resolver and the `org.polyvariant` dependency, then describe your questions and evaluate them.

```sh
// build.sbt
resolvers += "central-snapshots" at "https://central.sonatype.com/repository/maven-snapshots/"
libraryDependencies += "org.polyvariant" %%% "jev4s" % "<version>"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README usage section: [github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/README.md](https://github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/README.md)
- Example triage test: [github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/core/src/test/scala/example/Triage.scala](https://github.com/polyvariant/jev4s/blob/2419f74d2ab1abfd03b1038a0337afdd397e7e26/core/src/test/scala/example/Triage.scala)
- The other Scala client: [jevlist.ai/projects/jev4s](https://jevlist.ai/projects/jev4s)

## Limits and data handling

Early stage: only snapshots are published and the API may change without notice. State and questions are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 2419f74d2ab1](https://github.com/polyvariant/jev4s/tree/2419f74d2ab1abfd03b1038a0337afdd397e7e26). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
