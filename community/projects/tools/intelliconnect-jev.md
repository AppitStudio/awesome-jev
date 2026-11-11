# IntelliConnect (xiaozhi-esp32 IoT agent backend with a Jev client)

[All projects](../README.md) · [Home automation](README.md#home-automation)

AI agent IoT platform that serves as a backend for xiaozhi-esp32 devices, with a Java Jev client used by its built-in emotion and youth-protection tools and available to your own code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ruanrongman/IntelliConnect) |
| Maintainer | [ruanrongman](https://github.com/ruanrongman). Independently curated. |
| Format | Java (Spring) backend with web UI (Apache-2.0) |
| Requirements | Java and Maven or Docker, a xiaozhi-esp32 device setup, and a TypeSafe key in the Jev config. |
| License | [Apache-2.0](https://github.com/ruanrongman/IntelliConnect/blob/93b087505fdd9b787caad8c1a5ee25cd64b47a3b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/top/rslly/iot/utility/ai/jev/JevClient.java`](https://github.com/ruanrongman/IntelliConnect/blob/93b087505fdd9b787caad8c1a5ee25cd64b47a3b/src/main/java/top/rslly/iot/utility/ai/jev/JevClient.java) at the pinned commit. |

## When to use

- Add typed moderation or emotion checks to a voice IoT assistant.
- Reuse a Java Jev client.
- Mismatch: docs are in Chinese; Jev is optional.

## How it works

`JevClient.java` calls `POST /v1/systemone` with noul, choice and score questions; `docs/jev-client.md` (Chinese) shows the config and says `EmotionTool` and `YouthProtectionTool` use it, with Jev's `choice` result allowing or blocking in the moderation path. Integration evidence: [`src/main/java/top/rslly/iot/utility/ai/jev/JevClient.java`](https://github.com/ruanrongman/IntelliConnect/blob/93b087505fdd9b787caad8c1a5ee25cd64b47a3b/src/main/java/top/rslly/iot/utility/ai/jev/JevClient.java).

## Get started

Deploy the backend per its docs and add the `base-url` and key from `docs/jev-client.md`.

```sh
git clone https://github.com/ruanrongman/IntelliConnect.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev client doc: [github.com/ruanrongman/IntelliConnect/blob/93b087505fdd9b787caad8c1a5ee25cd64b47a3b/docs/jev-client.md](https://github.com/ruanrongman/IntelliConnect/blob/93b087505fdd9b787caad8c1a5ee25cd64b47a3b/docs/jev-client.md)

## Limits and data handling

Conversation text for the moderation and emotion tools goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 93b087505fdd](https://github.com/ruanrongman/IntelliConnect/tree/93b087505fdd9b787caad8c1a5ee25cd64b47a3b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
