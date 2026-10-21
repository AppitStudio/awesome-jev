# fmev (System One API on Apple Foundation Models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Local server that implements TypeSafe's System One API (`POST /v1/systemone`, `GET /v1/models`) on the Apple Foundation Models model built into macOS, so existing Jev clients and SDKs work offline once you change the base URL.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrubens/fmev) |
| Maintainer | [mrubens](https://github.com/mrubens). Independently curated. |
| Format | Local server (Swift; Homebrew and notarized binary) |
| Requirements | Apple Silicon Mac on macOS 27+ with Apple Intelligence on. |
| License | [MIT](https://github.com/mrubens/fmev/blob/4f9c2d140878b2f859364feda229b22d7cc05fb7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Sources/fmev/main.swift`](https://github.com/mrubens/fmev/blob/4f9c2d140878b2f859364feda229b22d7cc05fb7/Sources/fmev/main.swift) at the pinned commit. |

## When to use

- Develop and test Jev clients locally at no cost.
- Run noul, choice and score questions on-device.
- Mismatch: this is a Jev-compatible runtime with Apple's model, not TypeSafe's Jev, so quality differs.

## How it works

`Sources/fmev/main.swift` serves the System One routes on `localhost:8787` and answers each question with Apple's on-device model, returning Jev-shaped probabilities, legends and confidence. Integration evidence: [`Sources/fmev/main.swift`](https://github.com/mrubens/fmev/blob/4f9c2d140878b2f859364feda229b22d7cc05fb7/Sources/fmev/main.swift).

## Get started

From the upstream README (not run on the review host):

```sh
brew install mrubens/tap/fmev
fmev
curl -s localhost:8787/v1/models
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Request and response example in the README: [github.com/mrubens/fmev#readme](https://github.com/mrubens/fmev#readme)
- Releases: [github.com/mrubens/fmev/releases](https://github.com/mrubens/fmev/releases)

## Limits and data handling

Runs on-device; nothing is sent to TypeSafe. Independent project, not affiliated with TypeSafe AI or Apple.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 4f9c2d140878](https://github.com/mrubens/fmev/tree/4f9c2d140878b2f859364feda229b22d7cc05fb7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
