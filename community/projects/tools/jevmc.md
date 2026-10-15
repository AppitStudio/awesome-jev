# JevMC

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial dependency-free Java SDK for the TypeSafe Jev API aimed at PaperMC Minecraft plugins, with typed Noul/Choice/Score answers, async calls and a chat-moderation example.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PabloB07/JevMC) |
| Maintainer | [PabloB07](https://github.com/PabloB07). Independently curated. |
| Format | Java library (Java 17+, Maven/JitPack) + example Paper plugin |
| Requirements | Java 17+, Paper server for the plugin; TypeSafe API key. |
| License | [MIT](https://github.com/PabloB07/JevMC/blob/b86fd3c6fe6835ef14fc5851c1698eec90672229/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/dev/blancocl/jevmc/JevClient.java`](https://github.com/PabloB07/JevMC/blob/b86fd3c6fe6835ef14fc5851c1698eec90672229/src/main/java/dev/blancocl/jevmc/JevClient.java) at the pinned commit. |

## When to use

- Moderate Minecraft chat with typed toxicity checks from a Paper plugin.
- Call Jev from any Java 17+ app without extra HTTP dependencies.
- Mismatch: thin wrapper; it contains no moderation policy of its own beyond the example.

## How it works

`JevClient` wraps `POST /v1/systemone` with `java.net.http`, maps the three primitives to immutable records and retries 429/529 and network errors with exponential backoff, returning `CompletableFuture` results. Integration evidence: [`src/main/java/dev/blancocl/jevmc/JevClient.java`](https://github.com/PabloB07/JevMC/blob/b86fd3c6fe6835ef14fc5851c1698eec90672229/src/main/java/dev/blancocl/jevmc/JevClient.java).

## Get started

From the upstream README (not run on the review host):

```sh
<dependency>
  <groupId>com.github.PabloB07</groupId>
  <artifactId>JevMC</artifactId>
  <version>1.0.0</version>
</dependency>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Moderation plugin example: `src/main/java/dev/blancocl/jevmc/paper/ModerationPlugin.java`.

## Limits and data handling

Chat messages you check are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b86fd3c6fe68](https://github.com/PabloB07/JevMC/tree/b86fd3c6fe6835ef14fc5851c1698eec90672229). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
