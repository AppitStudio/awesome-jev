# FlowMesh

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows voice-workflow app built for the Wispr No Hands challenge: dictate into the command box, review an exact plan, then approve; Jev picks which registered routine (focus, meeting, research or none) fits, and a local runtime runs only allowlisted actions with receipts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HamzaShaikh-source/flowmesh) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://github.com/HamzaShaikh-source/flowmesh/releases/latest) |
| Pricing and access | Free download from GitHub Releases (v1.0.0, checked 2026-10-20); you pay for your own Jev calls. |
| Jev evidence | [`bridge.py`](https://github.com/HamzaShaikh-source/flowmesh/blob/39b610b13b295dbf4daeba5bbaaacef77032f4cc/bridge.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [HamzaShaikh-source](https://github.com/HamzaShaikh-source). Independently curated. |
| Format | Windows desktop app (Python, WebView2; release zip) |
| Platform and availability | Windows (unsigned release zip; Windows may show a publisher warning). |
| Jev's role | Jev answers one Choice question to route a spoken request among three registered routines or none; it never generates shell commands or unregistered device actions. |
| Requirements | Windows with WebView2 Runtime; Wispr Flow for dictation (optional, you can type); a TypeSafe key for Jev routing; optional Home Assistant. |
| License | [MIT](https://github.com/HamzaShaikh-source/flowmesh/blob/39b610b13b295dbf4daeba5bbaaacef77032f4cc/LICENSE) |

## When to use

- Trigger desk routines (focus, meeting, research) by voice with an approval step.
- Combine Wispr Flow dictation with Home Assistant lights or phone notifications.
- Mismatch: Windows only; hackathon project; live integrations need your own Wispr, Jev and Home Assistant setup.

## How it works

The desktop app sends your dictated request to a local runtime bound to `127.0.0.1`. `bridge.py` calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` to pick a routine; without a key, labeled local rules route instead. Plans expire after five minutes and run once after approval. Integration evidence: [`bridge.py`](https://github.com/HamzaShaikh-source/flowmesh/blob/39b610b13b295dbf4daeba5bbaaacef77032f4cc/bridge.py).

## Get started

From the upstream README: download the release zip, extract it and run `FlowMesh.exe`, then add keys under Connect devices.

```sh
# Download FlowMesh-Windows.zip from
# https://github.com/HamzaShaikh-source/flowmesh/releases/latest
# Extract the FlowMesh folder and run FlowMesh.exe
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [github.com/HamzaShaikh-source/flowmesh/releases/latest](https://github.com/HamzaShaikh-source/flowmesh/releases/latest)
- SUBMISSION.md

## Limits and data handling

Request text goes to TypeSafe when keyed. The release is unsigned. Automated tests use controlled responses, not live-device proof.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 39b610b13b29](https://github.com/HamzaShaikh-source/flowmesh/tree/39b610b13b295dbf4daeba5bbaaacef77032f4cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
