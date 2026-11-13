# gray-hands (gray agent plugin that drives an Android phone, with an autonomous Jev task loop)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Plugin for the gray agent harness with tools to read the UI tree, tap, type, swipe, launch apps and take screenshots on a connected Android device, plus `device_run`, which asks Jev to pick each next action from the live UI state until a natural-language task is done (default 15 steps, capped at 30).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vstaln/gray-hands) |
| Maintainer | [vstaln](https://github.com/vstaln). Independently curated. |
| Format | gray plugin (Rust with a Python motor sidecar, MIT; releases on GitHub) |
| Requirements | The gray harness, `mobilerun` on PATH with a device reachable over adb, and a TypeSafe key for `device_run` only. |
| License | [MIT](https://github.com/vstaln/gray-hands/blob/3212caef068d2ff924adbc0ddec4e8a8260f8feb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`motor/typesafe_sdk.py`](https://github.com/vstaln/gray-hands/blob/3212caef068d2ff924adbc0ddec4e8a8260f8feb/motor/typesafe_sdk.py) at the pinned commit. |

## When to use

- Let an agent operate a test phone through natural-language tasks.
- Mismatch: phones with sensitive apps; the UI tree of the current screen goes to TypeSafe.

## How it works

`motor/typesafe_sdk.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default; `motor/hands_sidecar.py` builds the step loop over a vendored TypeSafe computer-use motor. The tool description estimates about $0.0002 per step and 2–3 s per step. Integration evidence: [`motor/typesafe_sdk.py`](https://github.com/vstaln/gray-hands/blob/3212caef068d2ff924adbc0ddec4e8a8260f8feb/motor/typesafe_sdk.py).

## Get started

Install from the gray plugin hub (or build from source), connect a device and set your key.

```sh
gray plugin install hands
export TYPESAFE_API_KEY=...
# in a gray session: /hands run "open settings and search for 'wifi'"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vstaln/gray-hands/blob/3212caef068d2ff924adbc0ddec4e8a8260f8feb/README.md](https://github.com/vstaln/gray-hands/blob/3212caef068d2ff924adbc0ddec4e8a8260f8feb/README.md)
- Releases: [github.com/vstaln/gray-hands/releases](https://github.com/vstaln/gray-hands/releases)

## Limits and data handling

UI tree and OCR text of the current screen go to TypeSafe on your key at each `device_run` step.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 3212caef068d](https://github.com/vstaln/gray-hands/tree/3212caef068d2ff924adbc0ddec4e8a8260f8feb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
