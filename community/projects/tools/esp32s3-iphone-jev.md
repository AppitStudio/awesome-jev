# iPhone Agent with optional Jev navigation (ESP32-S3 HID bridge agent that can let Jev handle bounded navigation steps)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

iPhone app derived from Henry Yuan's ESP32 iPhone Agent that operates an iPhone through an ESP32-S3 USB HID/AirPlay bridge; your own vision model plans, types and verifies, and optional TypeSafe Jev decisions handle bounded navigation steps, falling back to the vision model when unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public) |
| Maintainer | [Running-Snail-GO](https://github.com/Running-Snail-GO). Independently curated. |
| Format | iOS app source + unsigned IPA from GitHub releases (Swift, MIT) |
| Requirements | iOS 18+, an ESP32-S3 USB HID/AirPlay bridge board, personal signing (e.g. AltStore), your own vision-model service and optionally a TypeSafe key. |
| License | [MIT](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`iphone/ios/IPhoneAgent/Services/JevDecision.swift`](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/iphone/ios/IPhoneAgent/Services/JevDecision.swift) at the pinned commit. |

## When to use

- Experiment with phone automation where cheap Jev decisions take routine navigation steps.
- Mismatch: anyone without the ESP32-S3 bridge hardware, or wanting a validated, signed app.

## How it works

`JevDecision.swift` sends a screenshot and the task to TypeSafe (`https://api.typesafe.ai`, default model `jev-latest` from `Settings.swift`) and uses the choice only above a confidence threshold; invalid answers or HTTP errors fall back to the vision model. The author states Jev image support is experimental and no speed or accuracy claim is validated; physical-device operation still needs testing. Integration evidence: [`iphone/ios/IPhoneAgent/Services/JevDecision.swift`](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/iphone/ios/IPhoneAgent/Services/JevDecision.swift).

## Get started

Download the unsigned IPA from Releases, sign it yourself, then enable Settings > Model > Jev execution after adding your own TypeSafe key.

```sh
# Download ESP32Agent-unsigned.ipa from the repository's Releases and sign it (for example with AltStore Classic)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/README.md](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/README.md)
- Provenance: [github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/iphone/SOURCE.md](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/blob/b760806d33738e93a7b48900a525df0e8a2c8fd2/iphone/SOURCE.md)

## Limits and data handling

Screenshots and task text go to TypeSafe (when Jev execution is on) and to your vision-model service; keys are stored in the iOS Keychain.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit b760806d3373](https://github.com/Running-Snail-GO/esp32s3-iphone-jev-public/tree/b760806d33738e93a7b48900a525df0e8a2c8fd2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
