# Falcon by Zheng Li (native macOS Jev HTTP and MCP proxy that records and lets you review every decision for seven days)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native SwiftUI app for developers running local agents against Jev. It serves the System One API (`POST /v1/systemone`, `GET /v1/models`) and an MCP `jev_decide` tool on 127.0.0.1, forwards each call to TypeSafe with a per-source local key, and keeps the state, questions and answers for review, search, flags, notes and CSV/JSON export.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nocoo/falcon) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nocoo/falcon#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT app: signed DMG on [GitHub Releases](https://github.com/nocoo/falcon/releases) (v0.2.0, not notarized) or build from source. Jev calls use your own TypeSafe key and are billed to it; the optional relay runs on your own Cloudflare account. Checked 2026-11-25. |
| Jev evidence | [`Tests/FalconIntegrationTests/TypeSafeIntegrationTests.swift`](https://github.com/nocoo/falcon/blob/eeec00754de11437fee4d622abd3dae423b8d8a6/Tests/FalconIntegrationTests/TypeSafeIntegrationTests.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Zheng Li](https://github.com/nocoo). Independently curated. |
| Format | Native macOS app (Swift) with an optional Cloudflare Worker relay |
| Platform and availability | macOS 15+ on Apple Silicon (arm64). Chinese and English docs. |
| Jev's role | Falcon does not make decisions itself; it proxies your agents' Jev calls to TypeSafe (directly or via your own Cloudflare Worker relay) and records them for review. |
| Requirements | macOS 15+ on Apple Silicon and a TypeSafe API key. |
| License | [MIT](https://github.com/nocoo/falcon/blob/eeec00754de11437fee4d622abd3dae423b8d8a6/LICENSE) |

## When to use

- See exactly what your local agents ask Jev and what it answers, with latency and token charts.
- Give each agent its own local key while sharing one upstream connection.
- Mismatch: if you are not on macOS with Apple Silicon.

## How it works

The app binds to `127.0.0.1:19823` and forwards to `https://api.typesafe.ai`; the optional `services/relay/` Worker forwards to the same fixed host. Integration tests cover the TypeSafe, proxy and relay paths. Integration evidence: [`Tests/FalconIntegrationTests/TypeSafeIntegrationTests.swift`](https://github.com/nocoo/falcon/blob/eeec00754de11437fee4d622abd3dae423b8d8a6/Tests/FalconIntegrationTests/TypeSafeIntegrationTests.swift).

## Get started

Verify and install the release DMG, or build from source.

```sh
shasum -a 256 -c Falcon-0.2.0-arm64.dmg.sha256
# or build from source:
scripts/build-app.sh Release
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/nocoo/falcon/blob/eeec00754de11437fee4d622abd3dae423b8d8a6/docs/README.en.md](https://github.com/nocoo/falcon/blob/eeec00754de11437fee4d622abd3dae423b8d8a6/docs/README.en.md)
- Releases: [github.com/nocoo/falcon/releases](https://github.com/nocoo/falcon/releases)

## Limits and data handling

Upstream keys and relay tokens are stored in plaintext in `~/.config/falcon/credentials.json` (owner-only permissions, no Keychain). Unstarred decision history (including request states) is kept locally for seven days. v0.2.0 is signed with a personal development certificate and not notarized. The project says it is still in development.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit eeec00754de1](https://github.com/nocoo/falcon/tree/eeec00754de11437fee4d622abd3dae423b8d8a6). Inspected the English README, the relay description and the integration tests at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
