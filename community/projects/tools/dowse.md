# Dowse (semantic find for Safari)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

macOS app and Safari extension that opens from the MacBook notch: describe a passage you remember, and Jev finds and highlights the matching text on the page so you can step through matches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tinoosan/dowse) |
| Maintainer | [tinoosan](https://github.com/tinoosan). Independently curated. |
| Format | macOS app and Safari extension (Swift, TypeScript); developer build |
| Requirements | Apple Silicon Mac on macOS 14+, full Xcode, Node.js and npm; your own TypeSafe key, stored in Keychain. |
| License | [MIT](https://github.com/tinoosan/dowse/blob/6ce1290b35d5e1e555b451722e88c170e2b1c319/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`App/Jev/JevClient.swift`](https://github.com/tinoosan/dowse/blob/6ce1290b35d5e1e555b451722e88c170e2b1c319/App/Jev/JevClient.swift) at the pinned commit. |

## When to use

- Jump back to a half-remembered passage on a long page.
- Find text by meaning when you don't know the exact words.
- Mismatch: Safari only; not a notarized release, so you build it and allow unsigned extensions.

## How it works

The extension splits the page into passages; `App/Jev/JevClient.swift` sends them with your description to TypeSafe's System One API after you consent, and the best matches are highlighted. Integration evidence: [`App/Jev/JevClient.swift`](https://github.com/tinoosan/dowse/blob/6ce1290b35d5e1e555b451722e88c170e2b1c319/App/Jev/JevClient.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tinoosan/dowse.git && cd dowse
npm ci
scripts/build.sh --install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Build and Safari setup steps in the README: [github.com/tinoosan/dowse#readme](https://github.com/tinoosan/dowse#readme)
- Privacy notes: [github.com/tinoosan/dowse/blob/main/PRIVACY.md](https://github.com/tinoosan/dowse/blob/main/PRIVACY.md)

## Limits and data handling

Page text is sent to TypeSafe only with your consent and key. Demo mode is scripted; there is no offline semantic matching.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 6ce1290b35d5](https://github.com/tinoosan/dowse/tree/6ce1290b35d5e1e555b451722e88c170e2b1c319). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
