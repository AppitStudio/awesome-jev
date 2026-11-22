# Antispam for Apple Mail by pravbeseda (Mail extension that sorts every new message into spam, phishing, promo or legit with Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

An Apple Mail extension for macOS that classifies every newly received message in every Mail account. Spam and phishing above the confidence threshold (0.9 by default) move to Junk, below it they get a yellow background and gray flag; promotions get a purple flag. On any error the message is left untouched, and a watchdog checks every 30 minutes that filtering still works.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pravbeseda/antispam) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/pravbeseda/antispam#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build that you compile and install yourself with Xcode and your own TypeSafe key. No signed release and no license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`Packages/AntispamCore/Sources/AntispamCore/Jev/JevClient.swift`](https://github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/Packages/AntispamCore/Sources/AntispamCore/Jev/JevClient.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [pravbeseda](https://github.com/pravbeseda). Independently curated. |
| Format | macOS Mail extension (Swift) |
| Platform and availability | macOS 14+ Apple Mail (MailKit extension + SwiftUI host app). |
| Jev's role | One `choice` per new message among spam, phishing, promo and legit, with the confidence compared against your threshold. |
| Requirements | macOS 14 or later, Xcode with an Apple Development certificate (a free Personal Team works), XcodeGen, and a TypeSafe Jev API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Add a second spam and phishing filter across all your Mail accounts, with a threshold you control.
- Mismatch: existing mail (only newly received messages are checked) or anyone who cannot build with Xcode.

## How it works

`JevClient.swift` sends key headers, up to 8,000 characters of plain-text body and the link domains to `https://api.typesafe.ai/v1/systemone`; `MailExtension/` turns the answer into a Mail action and the host app keeps a decisions table. Integration evidence: [`Packages/AntispamCore/Sources/AntispamCore/Jev/JevClient.swift`](https://github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/Packages/AntispamCore/Sources/AntispamCore/Jev/JevClient.swift).

## Get started

Put your Apple team ID in `Config/Local.xcconfig`, run the install script, then enable Antispam in Mail's Extensions settings and paste your key in the app.

```sh
git clone https://github.com/pravbeseda/antispam && cd antispam
brew install xcodegen
echo 'DEVELOPMENT_TEAM = <your team id>' > Config/Local.xcconfig
scripts/install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README limitations section: [github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/README.md](https://github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/README.md)
- Watchdog script: [github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/scripts/doctor.sh](https://github.com/pravbeseda/antispam/blob/1d61b7ab341fbb5d061b855557946d0bca605d3c/scripts/doctor.sh)

## Limits and data handling

Key headers, up to 8,000 characters of each message's plain-text body and its link domains are sent to TypeSafe. The API key is stored in plain text in the App Group container. The author notes Jev is less accurate on Russian than English. Personal Team builds stop working when the certificate expires. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 1d61b7ab341f](https://github.com/pravbeseda/antispam/tree/1d61b7ab341fbb5d061b855557946d0bca605d3c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
