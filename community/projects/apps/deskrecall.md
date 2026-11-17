# DeskRecall by sreenivasanac (macOS menu bar app that restores window layouts per display setup, with Jev deciding the fuzzy matches)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS menu bar app that puts every window back on the right display, Mission Control desktop (Space), size and minimized state for whichever monitors are plugged in. You save one profile per display setup and click Arrange. Exact cases are settled locally; the judgement calls go to Jev: which profile fits a new set of monitors, which display stands in for which, and which window is which when titles have changed. Low-confidence answers become one dialog with the best guess preselected. A Profiles window draws each saved layout to scale.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sreenivasanac/deskrecall) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/sreenivasanac/deskrecall#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build with no license file (reuse terms not granted); you pay for your own TypeSafe calls. Checked 2026-11-17. |
| Jev evidence | [`Sources/DeskRecall/Jev.swift`](https://github.com/sreenivasanac/deskrecall/blob/5ec4abb873de3ce1052503f5900ad531cd588781/Sources/DeskRecall/Jev.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [sreenivasanac](https://github.com/sreenivasanac). Independently curated. |
| Format | macOS menu bar app (Swift, source build; no license file) |
| Platform and availability | macOS (menu bar app, source build) |
| Jev's role | Jev decides the fuzzy matches: which profile, which display stands in for which, and which window goes in which saved slot. |
| Requirements | macOS 26.4+ to move windows between desktops (frames work on macOS 14+), Xcode command line tools, Accessibility permission and a TypeSafe key stored in the login keychain. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Restore window layouts across laptop, home and office monitor setups, including Spaces and minimized windows.
- Mismatch: window snapping and keyboard tiling; the README points to Rectangle for that.

## How it works

`Sources/DeskRecall/Jev.swift` sends the profile, display and window matching questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (set in `Sources/DeskRecall/Config.swift`); the key is read from the keychain or `TYPESAFE_API_KEY`. Integration evidence: [`Sources/DeskRecall/Jev.swift`](https://github.com/sreenivasanac/deskrecall/blob/5ec4abb873de3ce1052503f5900ad531cd588781/Sources/DeskRecall/Jev.swift).

## Get started

Build and install the app, grant Accessibility, then add your key from the menu bar icon.

```sh
git clone https://github.com/sreenivasanac/deskrecall && cd deskrecall
scripts/build-app.sh   # builds, signs, installs to /Applications and launches
# menu bar icon -> Add TypeSafe Jev Key...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sreenivasanac/deskrecall/blob/5ec4abb873de3ce1052503f5900ad531cd588781/README.md](https://github.com/sreenivasanac/deskrecall/blob/5ec4abb873de3ce1052503f5900ad531cd588781/README.md)

## Limits and data handling

Window titles, app names and display details are sent to TypeSafe on your key when a match is not exact. Needs Accessibility permission to read and move windows. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 5ec4abb873de](https://github.com/sreenivasanac/deskrecall/tree/5ec4abb873de3ce1052503f5900ad531cd588781). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
