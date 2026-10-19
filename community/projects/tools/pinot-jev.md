# Pinot Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Apache Pinot scalar-function plugin for semantic predicates backed by TypeSafe Jev (`jevAll`, `jevAny`, `jevProbability`), fusing up to eight conditions per row into one request with per-server caching.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/pinot-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Java plugin JAR for Apache Pinot |
| Requirements | Java 17, Maven, Pinot servers with `JEV_API_KEY` set. |
| License | [MIT](https://github.com/gbesse/pinot-jev/blob/a0cd0fbf87c9287fdf5651b3916c9a121350fea8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/org/apache/pinot/function/jev/JevClient.java`](https://github.com/gbesse/pinot-jev/blob/a0cd0fbf87c9287fdf5651b3916c9a121350fea8/src/main/java/org/apache/pinot/function/jev/JevClient.java) at the pinned commit. |

## When to use

- Filter Pinot rows by meaning, such as reviews that recommend a film.
- Mismatch: initial release; every uncached row is a paid call at query time.

## How it works

`JevClient.java` sends fused conditions for a row to Jev and returns probabilities; boolean functions use a 0.5 threshold and NULL text skips the call. Integration evidence: [`src/main/java/org/apache/pinot/function/jev/JevClient.java`](https://github.com/gbesse/pinot-jev/blob/a0cd0fbf87c9287fdf5651b3916c9a121350fea8/src/main/java/org/apache/pinot/function/jev/JevClient.java).

## Get started

From the upstream README: build with Maven, copy the JAR to Pinot's plugins directory, set `JEV_API_KEY`, and restart.

```sh
mvn --batch-mode verify
# copy target/pinot-jev-0.1.1.jar to Pinot /plugins, set JEV_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README query examples (English and French)

## Limits and data handling

Row text goes to TypeSafe from Pinot servers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit a0cd0fbf87c9](https://github.com/gbesse/pinot-jev/tree/a0cd0fbf87c9287fdf5651b3916c9a121350fea8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
