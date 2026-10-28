# NotiSift (Android notification organizer where a decision model such as Jev sorts each notification)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Open-source Android app that rebuilds your notification drawer: each notification is decided as Important, Later or Junk and grouped, with important ones on top and the rest in quiet day and group stacks. Decision models (Jev, Perplexity's, or a self-hosted one) or chat models can do the sorting with your own key; codes, chats, calls and alarms never leave the phone, and your own rules always win. Works offline without AI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/procoder-net/notisift) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/procoder-net/notisift#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free. AI sorting is billed to your own provider key. Checked 2026-10-28. |
| Jev evidence | [`app/src/main/java/io/github/notisift/llm/Provider.kt`](https://github.com/procoder-net/notisift/blob/ec1d4a4c1a7562685dbef9a21deb5037991af905/app/src/main/java/io/github/notisift/llm/Provider.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [procoder-net](https://github.com/procoder-net). Independently curated. |
| Format | Android app (Kotlin) |
| Platform and availability | Android; build from source and sideload (no store listing verified). |
| Jev's role | Optional per-notification decision: Important, Later or Junk, plus its group. |
| Requirements | An Android phone and the Android SDK to build; an API key only for AI sorting. |
| License | [MIT](https://github.com/procoder-net/notisift/blob/ec1d4a4c1a7562685dbef9a21deb5037991af905/LICENSE) |

## When to use

- Tame a noisy notification drawer per notification, not per app.
- Mismatch: build from source; Jev is one of several providers.

## How it works

`Provider.kt` registers Jev as a decisions provider (`https://api.typesafe.ai`, path `systemone`, model `jev-latest`) next to Perplexity Decisions, a self-hosted FastJev and chat models. Integration evidence: [`app/src/main/java/io/github/notisift/llm/Provider.kt`](https://github.com/procoder-net/notisift/blob/ec1d4a4c1a7562685dbef9a21deb5037991af905/app/src/main/java/io/github/notisift/llm/Provider.kt).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/procoder-net/notisift.git && cd notisift
./gradlew :app:assembleRelease
adb install -r app/build/outputs/apk/release/app-release.apk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/procoder-net/notisift#readme](https://github.com/procoder-net/notisift#readme)

## Limits and data handling

With AI sorting on, notification text (except codes, chats, calls and alarms) goes to the chosen provider.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit ec1d4a4c1a75](https://github.com/procoder-net/notisift/tree/ec1d4a4c1a7562685dbef9a21deb5037991af905). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
