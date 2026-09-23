# Jevcast

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS launcher and window manager (Option–Space): open apps, find files, calculate, move windows, and reuse clipboard text. Optional TypeSafe Jev matching for loose natural-language requests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RyanErkal/jevcast) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [jevcast.vercel.app](https://jevcast.vercel.app) |
| Pricing and access | MIT source; no app purchase fee, checked **2026-09-23**. Core launcher works without Jev. Optional Jev mode needs your TypeSafe or OpenRouter (`sk-or-`) key in Settings › Input (Keychain). Provider usage billed separately. |
| Jev evidence | Inspected [`JevService.swift`](https://github.com/RyanErkal/jevcast/blob/b477acd1e5480b31ed601d6b0000198bb260fcf1/Sources/JevLauncher/JevService.swift) and README Jev section: Jev chooses among candidate action/app names or returns no match; it never writes commands. Live macOS build not run on the Linux review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; Xcode build, Gatekeeper install, and live Jev matching were **not** executed here. |
| Maintainer | [RyanErkal](https://github.com/RyanErkal). |
| Format | Native SwiftUI/AppKit macOS application (SwiftPM `JevLauncher`). |
| Platform and availability | macOS **14+**, Apple silicon and Intel. Source-build with Xcode **26+** per upstream agent install prompt; website documents the product. |
| Jev's role | Optional natural-language matching over a closed candidate list (apps, settings panes, window actions, commands, …). Local search never waits on Jev. Jev use is optional. |
| Requirements | macOS 14+, Xcode 26+ to build; Accessibility/related permissions as prompted. Optional `TYPESAFE`/OpenRouter key for NL matching. |
| License | [MIT](https://github.com/RyanErkal/jevcast/blob/b477acd1e5480b31ed601d6b0000198bb260fcf1/LICENSE). |

## When to use

Use it as a **local-first launcher/window manager** that can optionally map fuzzy phrases onto known actions with Jev. Prefer [Jaste](jaste.md) / [JevPaste](jevpaste.md) for clipboard-field paste workflows, or [Jev Voice](jev-voice.md) for spoken command routing.

## How it works

Core search, clipboard history, and window layouts run on-device. With Jev enabled, [`JevService`](https://github.com/RyanErkal/jevcast/blob/b477acd1e5480b31ed601d6b0000198bb260fcf1/Sources/JevLauncher/JevService.swift) sends the request text plus candidate names to TypeSafe or OpenRouter Jev; code executes only a selected known action. Paths, clipboard bodies, and audio are not added beyond what you type.

## Get started

```sh
git clone https://github.com/RyanErkal/jevcast.git
cd jevcast
git checkout b477acd1e5480b31ed601d6b0000198bb260fcf1
# On macOS with Xcode 26+: swift test && scripts/build.sh
# Install path and codesign steps: see upstream README agent install prompt
```

Website: [jevcast.vercel.app](https://jevcast.vercel.app).

## Examples and demos

- README tables for launcher queries (layouts, convert, ports, timers, …).
- Site screenshots under `site/images/`.

## Limits and data handling

With Jev on, request text and candidate names leave the Mac for TypeSafe or OpenRouter. Key stays in Keychain. Build/install not verified on this Linux host.

## Review and maintenance

Reviewed on **2026-09-23** at [commit b477acd](https://github.com/RyanErkal/jevcast/tree/b477acd1e5480b31ed601d6b0000198bb260fcf1) (MIT). AI-assisted review of README, LICENSE, `JevService.swift`, `Package.swift`. No macOS build/live run.

Related: [Jaste](jaste.md), [JevPaste](jevpaste.md), [Jev Voice](jev-voice.md).
