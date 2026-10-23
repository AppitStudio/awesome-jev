# Text-Only YouTube (userscript with Jev genre tags)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Violentmonkey userscript that turns YouTube into a plain list of titles without thumbnails, avatars or Shorts; one click sends the visible titles to Jev to tag each video with a genre icon you can filter by.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JohnVonDrashek/youtube-text-only) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/JohnVonDrashek/youtube-text-only#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free userscript. Genre tagging uses your own TypeSafe key (the README estimates about a twentieth of a cent per 30 videos). Checked 2026-10-24. |
| Jev evidence | [`text-only-youtube.user.js`](https://github.com/JohnVonDrashek/youtube-text-only/blob/59762cfbe6c89f35d993bd2e5b015380469aa7e0/text-only-youtube.user.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JohnVonDrashek](https://github.com/JohnVonDrashek). Independently curated. |
| Format | Userscript (Violentmonkey) |
| Platform and availability | Desktop browsers with Violentmonkey. |
| Jev's role | Optional: one choice question per video assigns a genre from the list in `GENRES`; a ring marks low-confidence answers. |
| Requirements | A browser with Violentmonkey; optional TypeSafe API key for genres. |
| License | [MIT](https://github.com/JohnVonDrashek/youtube-text-only/blob/59762cfbe6c89f35d993bd2e5b015380469aa7e0/LICENSE) |

## When to use

- Browse YouTube by title without thumbnails pulling you in.
- Filter your feed by genre.
- Mismatch: YouTube layout changes can break hiding rules.

## How it works

The script posts titles and channel names to `https://api.typesafe.ai/v1/systemone` with `jev-latest` through `GM_xmlhttpRequest`, only when you click the genre button, and caches answers per video. Integration evidence: [`text-only-youtube.user.js`](https://github.com/JohnVonDrashek/youtube-text-only/blob/59762cfbe6c89f35d993bd2e5b015380469aa7e0/text-only-youtube.user.js).

## Get started

From the upstream README (not run on the review host):

```sh
# Install Violentmonkey, then open:
https://raw.githubusercontent.com/JohnVonDrashek/youtube-text-only/main/text-only-youtube.user.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JohnVonDrashek/youtube-text-only#readme](https://github.com/JohnVonDrashek/youtube-text-only#readme)

## Limits and data handling

Nothing is sent until you click; titles and channel names on screen go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 59762cfbe6c8](https://github.com/JohnVonDrashek/youtube-text-only/tree/59762cfbe6c89f35d993bd2e5b015380469aa7e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
