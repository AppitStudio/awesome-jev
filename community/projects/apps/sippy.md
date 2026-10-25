# Sippy (macOS water-break companion with optional Jev sip confirmation)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Small native macOS water reminder with a floating droplet buddy and menu-bar progress; Apple Vision face and hand tracking spots a possible sip on device, and with your own TypeSafe key Jev confirms the candidate frame before a drink is logged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milanjain2208/sippy) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/milanjain2208/sippy#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build with no account. The optional Jev check is billed to your own TypeSafe key, at most 3 photos per reminder. Checked 2026-10-26. |
| Jev evidence | [`Sources/SippyCore/JevClient.swift`](https://github.com/milanjain2208/sippy/blob/5cd359cefe761966ae22d89ff907c9ae0844966e/Sources/SippyCore/JevClient.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [milanjain2208](https://github.com/milanjain2208). Independently curated. |
| Format | Native macOS app (Swift) |
| Platform and availability | macOS 13+, built from source (`scripts/build-app.sh`, ad-hoc signed); the README describes DMG/ZIP releases, but none were published at review time. |
| Jev's role | Optional: Jev answers one Noul question about a single candidate JPEG; 0.8 or higher confirms the sip, otherwise the local check decides. |
| Requirements | macOS 13+ with Swift 5.9+ (Xcode or Command Line Tools); an optional TypeSafe API key. |
| License | [MIT](https://github.com/milanjain2208/sippy/blob/5cd359cefe761966ae22d89ff907c9ae0844966e/LICENSE) |

## When to use

- Get reminded to drink water and log sips hands-free.
- Add a cloud double-check on sip detection while keeping video local.
- Mismatch: no published release yet and local builds are ad-hoc signed; Jev image support is experimental.

## How it works

`JevClient.swift` sends one JPEG (280 to 640 px) as a multipart request to `https://api.typesafe.ai/v1/systemone` with pinned `jev-1.14.0` and the image danger-zone header; errors fall back to the local gesture check. Integration evidence: [`Sources/SippyCore/JevClient.swift`](https://github.com/milanjain2208/sippy/blob/5cd359cefe761966ae22d89ff907c9ae0844966e/Sources/SippyCore/JevClient.swift).

## Get started

From the upstream README (not run on the review host):

```sh
bash scripts/build-app.sh
open dist/Sippy.app
# optional: Sippy → Settings → Jev confirmation → paste key → Save key & enable
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/milanjain2208/sippy#readme](https://github.com/milanjain2208/sippy#readme)
- Release notes: [github.com/milanjain2208/sippy/blob/main/RELEASING.md](https://github.com/milanjain2208/sippy/blob/main/RELEASING.md)

## Limits and data handling

Without a key nothing is uploaded. With Jev enabled, only the candidate frame is sent, never a video stream. The key is kept in the macOS Keychain.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 5cd359cefe76](https://github.com/milanjain2208/sippy/tree/5cd359cefe761966ae22d89ff907c9ae0844966e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
