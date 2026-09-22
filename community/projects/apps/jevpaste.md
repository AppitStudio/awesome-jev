# JevPaste

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

macOS menu bar Smart Paste: TypeSafe Jev selects which exact value from a copied multi-field block (or a Keychain profile) best fits the focused input, then inserts it—without inventing new text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taiki510/JevPaste) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [JevPaste project homepage](https://github.com/taiki510/JevPaste) — source-build entry; no separate commercial site reviewed. |
| Pricing and access | No app purchase fee for the MIT source build reviewed **2026-09-22**. Bring a TypeSafe API key (Keychain); provider usage can incur charges. Packaged distribution beyond `Scripts/package-app.sh` was not verified. |
| Jev evidence | [`JevClient.swift`](https://github.com/taiki510/JevPaste/blob/c4a39f301e0b23f73601bdc5b475371ac99a67ac/Sources/JevPaste/JevClient.swift) posts to `https://api.typesafe.ai/v1/systemone`; Keychain account `typesafe-api-key`; redirects other than that host are rejected. |
| Disclosure | Independently curated; no affiliation. Listing is not endorsement. Linux review host could not run `swift test`; upstream GitHub Actions **CI** (`swift test` on macos-15) succeeded on a recent main tip. Live Accessibility/paste and live TypeSafe matching were not executed here. Distinct from closed-source [Jaste](jaste.md). |
| Maintainer | [taiki510](https://github.com/taiki510). Independently curated; not an upstream submission. |
| Format | Native SwiftPM macOS menu bar application. |
| Platform and availability | macOS **14+**; Xcode 16 / compatible CLT; Accessibility permission. Early source distribution. |
| Jev's role | Chooses among exact candidate substrings from the clipboard/profile given focused-field labels; code inserts the selected value. No generative rewrite of values. |
| Requirements and costs | TypeSafe key in Keychain; Accessibility. Source MIT; inference charges possible. |
| License | [MIT](https://github.com/taiki510/JevPaste/blob/c4a39f301e0b23f73601bdc5b475371ac99a67ac/LICENSE). |

## When to use

Use it when you copy a block of contact or form fields and want **Command-J** (or Command-Shift-J from a saved profile) to paste only the value that fits the focused field. Prefer [Jaste](jaste.md) if you want the commercial Mac beta with Direct Jev mode and no public source. Do not use it as a password manager or for sensitive secure fields—the app refuses password/OTP-like fields and secret-shaped clipboard text.

## How it works

Local code extracts bounded candidates from the clipboard, builds field context from Accessibility, and asks Jev which candidate fits. [`JevClient`](https://github.com/taiki510/JevPaste/blob/c4a39f301e0b23f73601bdc5b475371ac99a67ac/Sources/JevPaste/JevClient.swift) talks only to TypeSafe System One over HTTPS. Sensitive-field and secret filters run locally before any network call. Encrypted local clipboard history is optional storage on device.

## Get started

```sh
git clone https://github.com/taiki510/JevPaste.git
cd JevPaste
git checkout c4a39f301e0b23f73601bdc5b475371ac99a67ac
# On macOS 14+ with Swift toolchain:
swift test
./Scripts/package-app.sh
open dist/JevPaste.app
```

Live Smart Paste sends field context and candidate text to TypeSafe and may incur charges. The Linux review host did not run `swift test` or the packaged app.

## Examples and demos

- Source-reviewed: `SensitiveDataFilterTests` and related Swift Testing cases under `Tests/JevPasteTests/`.
- Upstream CI: [Actions run](https://github.com/taiki510/JevPaste/actions/runs/35693137766) reported **success** for `swift test` on macos-15 (recent main). Not re-run on this host.
- Usage notes: [docs/USAGE.md](https://github.com/taiki510/JevPaste/blob/c4a39f301e0b23f73601bdc5b475371ac99a67ac/docs/USAGE.md).

## Limits and data handling

Requires Accessibility. Refuses sensitive fields and secret-shaped text. External I/O is limited to TypeSafe’s System One endpoint. Independent of Jaste; not an official TypeSafe or Jaste product.

## Review and maintenance

Reviewed on **2026-09-22** at [commit c4a39f3](https://github.com/taiki510/JevPaste/tree/c4a39f301e0b23f73601bdc5b475371ac99a67ac): MIT. AI-assisted source review of README, LICENSE, `JevClient.swift`, Keychain/sensitive-data paths, and tests. Offline Swift execution unavailable on the Linux review host; upstream CI success cited. No live TypeSafe paste session.

Related: [Jaste](jaste.md), [TipTour](tiptour.md), [TypeSafe (Swift)](../tools/typesafe-swift.md).
