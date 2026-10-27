# Audience Moderator (Android counter for people and raised hands, with an optional Jev round insight)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Android helper for event moderators: counts people and raised hands on-device (MediaPipe or YOLOv8n-pose), runs timed question rounds, picks a random audience member, and can optionally send round results, or one photo you confirm, to Jev for a short insight and a second count; camera pictures are never saved and there is no face recognition.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/irvan-putra/jev-moderator) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/irvan-putra/jev-moderator#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (AGPL-3.0); free source build. Optional Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. |
| Jev evidence | [`app/src/main/java/com/irvanputra/jevmoderator/JevClient.java`](https://github.com/irvan-putra/jev-moderator/blob/62aebf35c4f484ab1d31c7ae594d518bce3a5d67/app/src/main/java/com/irvanputra/jevmoderator/JevClient.java) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [irvan-putra](https://github.com/irvan-putra). Independently curated. |
| Format | Android app (Java) |
| Platform and availability | Android arm64; debug APK built from source. The author notes the APK had not been run on a device at the time of writing. |
| Jev's role | Optional insight: one Choice and one Noul question about a round, plus an experimental photo check. |
| Requirements | JDK 17 and Android SDK 34 to build; a TypeSafe API key only for the optional Jev features. |
| License | [AGPL-3.0](https://github.com/irvan-putra/jev-moderator/blob/62aebf35c4f484ab1d31c7ae594d518bce3a5d67/LICENSE) |

## When to use

- Run hands-up polls at events without a voting app.
- Mismatch: early build, Jev calls tested only against a mock server; packed rooms undercount.

## How it works

`JevClient.java` posts to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with one Choice and one Noul question; the experimental photo question uses TypeSafe's image header. Integration evidence: [`app/src/main/java/com/irvanputra/jevmoderator/JevClient.java`](https://github.com/irvan-putra/jev-moderator/blob/62aebf35c4f484ab1d31c7ae594d518bce3a5d67/app/src/main/java/com/irvanputra/jevmoderator/JevClient.java).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/irvan-putra/jev-moderator && cd jev-moderator
gradle assembleDebug
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/irvan-putra/jev-moderator#readme](https://github.com/irvan-putra/jev-moderator#readme)

## Limits and data handling

Counting runs on the phone. Round numbers, and a photo only after you confirm it, go to TypeSafe when the optional features are on.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 62aebf35c4f4](https://github.com/irvan-putra/jev-moderator/tree/62aebf35c4f484ab1d31c7ae594d518bce3a5d67). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
