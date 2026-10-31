# sbt-decision-filter (sbt plugin that asks Jev which test classes a change could affect and skips the rest)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

sbt plugin that asks a decision API (TypeSafe Jev or OpenAI Decisions) whether each test class could be affected by the current change and leaves out the ones that cannot via `Tests.Filter`. When in doubt (no key, API error, changed `build.sbt`) every test runs. Scoring questions follow mizchi/jev-test-filter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/krrrr38/sbt-decision-filter) |
| Maintainer | [krrrr38](https://github.com/krrrr38). Independently curated. |
| Format | sbt plugin (Scala) |
| Requirements | sbt; a TypeSafe key (`TYPESAFE_API_KEY`) or an OpenAI key. |
| License | [MIT](https://github.com/krrrr38/sbt-decision-filter/blob/ab18a8dd26c9a159660321b8056257ea822e8f62/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`modules/sbt-plugin-jev/src/main/scala/com/krrrr38/decisionfilter/jev/JevBackend.scala`](https://github.com/krrrr38/sbt-decision-filter/blob/ab18a8dd26c9a159660321b8056257ea822e8f62/modules/sbt-plugin-jev/src/main/scala/com/krrrr38/decisionfilter/jev/JevBackend.scala) at the pinned commit. |

## When to use

- Cut CI time on Scala projects by skipping tests a diff cannot reach.
- Mismatch: probabilistic test selection can miss a test; keep full runs on main.

## How it works

`JevBackend.scala` sends one shared `state` (the diff) with many `score` questions, one per test class, in a single round trip to Jev (`jev-1.13.0` by default); classes under the threshold are filtered out. Integration evidence: [`modules/sbt-plugin-jev/src/main/scala/com/krrrr38/decisionfilter/jev/JevBackend.scala`](https://github.com/krrrr38/sbt-decision-filter/blob/ab18a8dd26c9a159660321b8056257ea822e8f62/modules/sbt-plugin-jev/src/main/scala/com/krrrr38/decisionfilter/jev/JevBackend.scala).

## Get started

From the upstream README (not run on the review host):

```sh
// project/plugins.sbt
addSbtPlugin("com.krrrr38" % "sbt-decision-filter-jev" % "<version>")
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Related: [github.com/mizchi/jev-test-filter](https://github.com/mizchi/jev-test-filter)

## Limits and data handling

The diff and test class names are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit ab18a8dd26c9](https://github.com/krrrr38/sbt-decision-filter/tree/ab18a8dd26c9a159660321b8056257ea822e8f62). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
