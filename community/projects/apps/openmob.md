# OpenMob (self-hosted server and Android companion app that lets AI agents use a phone over REST or MCP, with optional Jev for screen and tap checks)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Self-hosted server with a REST API and an MCP endpoint that lets an AI agent operate a real Android phone, either on its own goal ("open Settings and go to Display") or step by step from your agent. A companion app pairs by QR code, reads the screen through Android Accessibility and checks every action on the phone, refusing banking and password apps. With a TypeSafe key, Jev classifies screen state, rates how risky a tap is and picks the next step; a Faster mode can also send small screenshots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andkhong/openmob) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/andkhong/openmob#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you supply model provider keys, optional TypeSafe key and hosting. Checked 2026-11-04. |
| Jev evidence | [`openmob/jev.py`](https://github.com/andkhong/openmob/blob/03e3cf722a5456fa36b7576bd30943b63f5ac5d4/openmob/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [andkhong](https://github.com/andkhong). Independently curated. |
| Format | Python server (REST and MCP) plus an Android companion app |
| Platform and availability | Self-hosted server with an Android companion app (Android 11+, ARM64, per the README). |
| Jev's role | Optional classifier for screen state, tap risk and next step. |
| Requirements | Python 3.11+, a model provider key, an Android 11+ (ARM64) test phone, and optionally `TYPESAFE_API_KEY` for Jev. |
| License | [MIT](https://github.com/andkhong/openmob/blob/03e3cf722a5456fa36b7576bd30943b63f5ac5d4/LICENSE) |

## When to use

- Let an agent drive a test phone with on-device safety checks and approvals.
- Mismatch: early and self-hosted; use a test phone, and Jev is optional.

## How it works

`openmob/jev.py` posts text descriptions of the foreground app, accessibility elements and OCR words to `https://api.typesafe.ai` System One as typed questions (screen assessment, tap risk and the next operation and target in one request); images are sent only in Faster mode. Integration evidence: [`openmob/jev.py`](https://github.com/andkhong/openmob/blob/03e3cf722a5456fa36b7576bd30943b63f5ac5d4/openmob/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/andkhong/openmob.git && cd openmob
pip install -e .
# set a model provider key and optionally TYPESAFE_API_KEY, then follow the README's pairing steps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the safety model and pairing steps: [github.com/andkhong/openmob#readme](https://github.com/andkhong/openmob#readme)

## Limits and data handling

The README warns that the agent controls a real phone and that screen content goes to the AI providers you configure (and to TypeSafe if Jev is enabled); use a test phone. Task text and step records are kept for 30 days by default with typed text redacted. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 03e3cf722a54](https://github.com/andkhong/openmob/tree/03e3cf722a5456fa36b7576bd30943b63f5ac5d4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
