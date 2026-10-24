# Pointsman by RomainJeff (macOS link router that picks the right browser with Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS menu bar app you set as the default browser: describe once how you use each real browser, and each clicked link goes to the right one, chosen by Jev from your descriptions, the app the link came from and the URL without its query string.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RomainJeff/pointsman) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/RomainJeff/pointsman#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls go through your own OpenRouter key (the README estimates about $0.00002 per link). Checked 2026-10-25. |
| Jev evidence | [`Sources/Router.swift`](https://github.com/RomainJeff/pointsman/blob/7b6f03aa341b719d1f04082fd5c00dc14f542107/Sources/Router.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [RomainJeff](https://github.com/RomainJeff). Independently curated. |
| Format | macOS menu bar app (Swift) |
| Platform and availability | macOS on Apple silicon; build from source (no signed release yet). |
| Jev's role | Core: Jev returns a probability for each browser plus none; below a 60% threshold, on error or after 1.5 s the link goes to your fallback browser. |
| Requirements | macOS 15+ on Apple silicon, Xcode Command Line Tools, an OpenRouter API key. |
| License | [MIT](https://github.com/RomainJeff/pointsman/blob/7b6f03aa341b719d1f04082fd5c00dc14f542107/LICENSE) |

## When to use

- Send work links to your work browser and personal links to another without domain lists.
- Use where the link came from (Slack, Mail, a terminal) as a signal.
- Mismatch: distinct from the listed Kai-Leee Pointsman task router.

## How it works

`Sources/Router.swift` sends your context, the browser descriptions, the source app and the redacted URL to Jev (`typesafe/jev-1.13`) through OpenRouter; localhost links always go to the fallback browser. Integration evidence: [`Sources/Router.swift`](https://github.com/RomainJeff/pointsman/blob/7b6f03aa341b719d1f04082fd5c00dc14f542107/Sources/Router.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/romainjeff/pointsman.git
cd pointsman
./build.sh --install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/RomainJeff/pointsman#readme](https://github.com/RomainJeff/pointsman#readme)

## Limits and data handling

Redacted URLs, the source app name and your descriptions go to OpenRouter and TypeSafe. A wrong guess opens one link in the wrong browser.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 7b6f03aa341b](https://github.com/RomainJeff/pointsman/tree/7b6f03aa341b719d1f04082fd5c00dc14f542107). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
