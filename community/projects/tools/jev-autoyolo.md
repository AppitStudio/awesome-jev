# Jev-AutoYOLO (images/videos in → YOLO model out, with TypeSafe Jev visual grounding)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One-key pipeline that uses TypeSafe Jev (System One) for visual grounding/labeling over images or video frames, then trains a YOLO model—fronted by a web UI with advanced Jev settings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DreamBlooms/Jev-AutoYOLO) |
| Maintainer | [DreamBlooms](https://github.com/DreamBlooms). Independently curated. |
| Format | Python backend + web UI (AGPL-3.0) |
| Requirements | GPU host recommended, Docker/Python per README, and a TypeSafe API key (`TYPESAFE_API_KEY`) with image danger-zone access as required. |
| License | [AGPL-3.0](https://github.com/DreamBlooms/Jev-AutoYOLO/blob/de6b28c1536261404fc7e5de4397a9ac5f8a2899/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`backend/app/services/jev_service.py`](https://github.com/DreamBlooms/Jev-AutoYOLO/blob/de6b28c1536261404fc7e5de4397a9ac5f8a2899/backend/app/services/jev_service.py) at the pinned commit. |

## When to use

- Auto-label images/video for YOLO with Jev grounding.
- Prefer a UI over raw notebook labeling.
- Mismatch: AGPL; training still needs your data and GPU.

## How it works

`backend/app/services/jev_service.py` calls TypeSafe System One with `TypeSafe-Danger-Zone-Images: true` for visual grounding when `TYPESAFE_API_KEY` is configured. Integration evidence: [`backend/app/services/jev_service.py`](https://github.com/DreamBlooms/Jev-AutoYOLO/blob/de6b28c1536261404fc7e5de4397a9ac5f8a2899/backend/app/services/jev_service.py).

## Get started

Follow README Docker/UI quick start and set `TYPESAFE_API_KEY` (enable image danger-zone if required by TypeSafe).

```sh
git clone https://github.com/DreamBlooms/Jev-AutoYOLO.git && cd Jev-AutoYOLO
export TYPESAFE_API_KEY=...
# follow README Docker / UI start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DreamBlooms/Jev-AutoYOLO/blob/de6b28c1536261404fc7e5de4397a9ac5f8a2899/README.md](https://github.com/DreamBlooms/Jev-AutoYOLO/blob/de6b28c1536261404fc7e5de4397a9ac5f8a2899/README.md)

## Limits and data handling

Images/frames under review are sent to TypeSafe on your key (danger-zone header). AGPL obligations apply to derivatives.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit de6b28c15362](https://github.com/DreamBlooms/Jev-AutoYOLO/tree/de6b28c1536261404fc7e5de4397a9ac5f8a2899). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
