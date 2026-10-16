# Gmail notifications with Jev (Safari)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Free, open-source Safari extension for Gmail on Mac: write in plain language which emails deserve your attention, and Jev decides which new messages trigger a floating alert. Interface and docs are in Spanish.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jaumesaa/gmail-jev-notifications) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jaumesaa/gmail-jev-notifications#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`native/SafariWebExtensionHandler.swift`](https://github.com/jaumesaa/gmail-jev-notifications/blob/b8b3dbc3a1dcbcb43409c066e0269bcfc3a7bffe/native/SafariWebExtensionHandler.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jaumesaa](https://github.com/jaumesaa). Independently curated. |
| Format | Safari Web Extension for macOS (source build, preliminary 0.1.0) |
| Platform and availability | macOS Safari (source build) |
| Jev's role | Jev judges each new email against your plain-language alert criterion. |
| Requirements | Mac (Apple Silicon or Intel) with Safari and Gmail open, Node.js to build, a TypeSafe API key stored in the macOS keychain. |
| License | [MIT](https://github.com/jaumesaa/gmail-jev-notifications/blob/b8b3dbc3a1dcbcb43409c066e0269bcfc3a7bffe/LICENSE) |

## When to use

- Get alerted only for the mail you describe (a stream starting, a teacher changing a deadline) and ignore promotions.
- Mismatch: Gmail and Safari must stay open; it watches the visible Inbox list and may briefly mark mail as read while reading it.

## How it works

Each new Inbox message is read in a temporary background tab (up to 12,000 characters), restored to unread when it was unread, and sent with your criterion to Jev (`jev-1.13.0` or `jev-1.14.0`) through the native handler, which never follows redirects so the key only reaches `api.typesafe.ai`. A minimum probability and daily query cap are configurable. Integration evidence: [`native/SafariWebExtensionHandler.swift`](https://github.com/jaumesaa/gmail-jev-notifications/blob/b8b3dbc3a1dcbcb43409c066e0269bcfc3a7bffe/native/SafariWebExtensionHandler.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jaumesaa/gmail-jev-notifications.git && cd gmail-jev-notifications
npm ci && npm test && npm run build:mac
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup steps and known limits in the README (Spanish).

## Limits and data handling

Email content goes to TypeSafe on your key; the key stays in the macOS keychain. No server, Google Cloud project or OAuth setup.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit b8b3dbc3a1dc](https://github.com/jaumesaa/gmail-jev-notifications/tree/b8b3dbc3a1dcbcb43409c066e0269bcfc3a7bffe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
