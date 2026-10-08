# Laser (Omarchy focus mode)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

AI focus mode for Omarchy / Hyprland on Linux: you declare a task, and Laser judges each screen against it with TypeSafe Jev (about half a second per check), escalating from a red dot to a nudge, a red screen edge and a haze over the distracting window; screenshots are OCR'd on device and only text (per privacy level) is sent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iYassr/omarchy-laser) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/iYassr/omarchy-laser#readme) (Omarchy plugin). |
| Pricing and access | Free plugin; bring your own TypeSafe API key (README estimates $0.30–0.50 a month of Jev usage — author-reported). Checked 2026-10-08. |
| Jev evidence | [`laser/jev.py`](https://github.com/iYassr/omarchy-laser/blob/735a6de8952f58b5c63cf995a1f55156e947987f/laser/jev.py) calls `api.typesafe.ai`; [`laser/privacy.py`](https://github.com/iYassr/omarchy-laser/blob/735a6de8952f58b5c63cf995a1f55156e947987f/laser/privacy.py) builds what is sent. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [iYassr](https://github.com/iYassr). Independently curated. |
| Format | Omarchy plugin (Quickshell bar widget + Python daemon) |
| Platform and availability | Linux with Omarchy (Quickshell) on Hyprland; Python 3.11+; optional grim + tesseract for OCR. |
| Jev's role | Answers whether the current screen is on task for the declared goal. |
| Requirements | Omarchy on Hyprland, python3 3.11+, hyprctl; TypeSafe API key. |
| License | [MIT](https://github.com/iYassr/omarchy-laser/blob/735a6de8952f58b5c63cf995a1f55156e947987f/LICENSE). |

## When to use

- Context-aware distraction blocking (Reddit can be on task for some work).
- Privacy-conscious screen classification where images never leave the machine.
- Mismatch: Omarchy/Hyprland only.

## How it works

The daemon samples the active window, builds a text description at the chosen privacy level, asks Jev an on-task question and escalates interventions on drift.

## Get started

Install the plugin (README *Install*):

```sh
omarchy plugin add https://github.com/iYassr/omarchy-laser --enable
```

Each check is a Jev request billed to your key; none outside focus sessions.

## Examples and demos

- README table of declared tasks vs screens with on-task probabilities.

## Limits and data handling

Window titles / OCR text (by privacy level) go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 735a6de8952f](https://github.com/iYassr/omarchy-laser/tree/735a6de8952f58b5c63cf995a1f55156e947987f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
