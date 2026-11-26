# jev drone cam by Todd Dailey (browser demo where a simulated drone sweeps a room photo and Jev finds the object you showed it)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser demo: pick or upload a photo of an object and a simulated top-down drone camera sweeps a room photo frame by frame. Every frame is one Jev call with a Box question (where is it) and a yes/no question (is it in view at all); plain code flies to the box when the yes/no answer passes a threshold you set with a slider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/twidtwid/jev-dronecam) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://jev-dronecam-bq3fs.sprites.app) |
| Pricing and access | Free MIT source. The public demo is free to try and runs on the author's key (calls capped at 90 a minute); self-hosting needs your own TypeSafe key and pays TypeSafe's image-input usage. Checked 2026-11-26. |
| Jev evidence | [`server.py`](https://github.com/twidtwid/jev-dronecam/blob/236227f395bff22bd999475ff7ecde1a512eed5b/server.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/AlexStepherylh/status/2125848761117348038)). |
| Maintainer | [Todd Dailey](https://github.com/twidtwid) (twidtwid). Independently curated. |
| Format | Python server + static web page |
| Platform and availability | Web app: a public demo on sprites.dev run by the author, or a single Python server you run yourself on 127.0.0.1:9470. |
| Jev's role | Each frame goes to Jev with the destination photo and two questions in one request, `where` (Box) and `seen` (noul); the drone moves only when `seen` is above the threshold, because a Box answer always returns a box even when the object is absent. |
| Requirements | Python 3.10+ (no dependencies) and a TypeSafe API key with access to the preview image input. |
| License | [MIT](https://github.com/twidtwid/jev-dronecam/blob/236227f395bff22bd999475ff7ecde1a512eed5b/LICENSE) |

## When to use

- See how a Box question and a yes/no gate work together on images, or demo Jev's image input to an audience.
- Mismatch: real drone or robot control; this is a simulation over still photos and does not fly anything.

## How it works

`server.py` serves the page and handles `POST /api/box`, the only call to Jev: it sends the frame and destination photo as base64 assets to `https://api.typesafe.ai/v1/systemone` with the `TypeSafe-Danger-Zone-Images: true` header (default model `jev-1.14.0`). The key stays on the server. Integration evidence: [`server.py`](https://github.com/twidtwid/jev-dronecam/blob/236227f395bff22bd999475ff7ecde1a512eed5b/server.py).

## Get started

Open the live demo, or run the server locally with your key.

```sh
git clone https://github.com/twidtwid/jev-dronecam
cd jev-dronecam
TYPESAFE_API_KEY=your_key python3 server.py   # http://127.0.0.1:9470
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [jev-dronecam-bq3fs.sprites.app](https://jev-dronecam-bq3fs.sprites.app)

## Limits and data handling

Image input is a TypeSafe preview feature behind a `Danger-Zone` header and may change. The seen/not-seen ranges in the README are the author's own probes on the bundled photos. Uploaded photos go to the server and on to TypeSafe; the public demo is the author's deployment.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 236227f395bf](https://github.com/twidtwid/jev-dronecam/tree/236227f395bff22bd999475ff7ecde1a512eed5b). Inspected the README, LICENSE and `server.py` at the pinned commit; the live demo URL answered HTTP 200 on 2026-11-26 but no Jev call was made from the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
