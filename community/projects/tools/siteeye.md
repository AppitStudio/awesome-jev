# SiteEye

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Construction-site near-miss prediction prototype: YOLO vision plus TypeSafe Jev 1.14 noul questions over detected statements, served as a local web app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seominpapa/siteeye) |
| Maintainer | [seominpapa](https://github.com/seominpapa). Independently curated. |
| Format | Local Python web app + legacy Jev client |
| Requirements | Python; YOLO weights; TYPESAFE_API_KEY; local GPU/CPU as documented. |
| License | [AGPL-3.0](https://github.com/seominpapa/siteeye/blob/d7fb822d43df72b809b81d0d648123d29a6adbcb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`legacy/jev.py`](https://github.com/seominpapa/siteeye/blob/d7fb822d43df72b809b81d0d648123d29a6adbcb/legacy/jev.py) at the pinned commit. |

## When to use

- Prototype vision + Jev noul judgments for site safety statements.
- Want calibrated yes/no thresholds on detector outputs.
- Mismatch: AGPL-3.0 research prototype; not a certified safety system.

## How it works

`legacy/jev.py` documents the TypeSafe System One noul endpoint and thresholds. The app pairs YOLO detections with Jev questions for near-miss style flags. Integration evidence: [`legacy/jev.py`](https://github.com/seominpapa/siteeye/blob/d7fb822d43df72b809b81d0d648123d29a6adbcb/legacy/jev.py).

## Get started

Clone, install deps, configure TypeSafe credentials, run the local web app per README.

```sh
git clone https://github.com/seominpapa/siteeye && cd siteeye
# AGPL-3.0; see README for YOLO + TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README near-miss pipeline
- legacy/jev.py

## Limits and data handling

AGPL-3.0. Not validated as a safety product. Images/text may leave the host when calling TypeSafe.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit d7fb822d43df](https://github.com/seominpapa/siteeye/tree/d7fb822d43df72b809b81d0d648123d29a6adbcb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
