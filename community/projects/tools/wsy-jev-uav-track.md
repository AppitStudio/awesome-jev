# wsy-jev-uav-track (Jev for UAV target tracking)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research prototype where Jev picks the next high-level drone tracking behavior from safety-filtered candidates with predicted outcomes, while a flight controller or NMPC keeps the fast inner loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lian-wsy/wsy-jev-uav-track) |
| Maintainer | [lian-wsy](https://github.com/lian-wsy). Independently curated. |
| Format | Python package (prototype); README in Chinese |
| Requirements | Python with pip; optional TypeSafe API key (the demo uses an offline mock). |
| License | [MIT](https://github.com/lian-wsy/wsy-jev-uav-track/blob/3e3e4ead8a70316cb960306eee017407bc0accf0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_uav_track/jev_client.py`](https://github.com/lian-wsy/wsy-jev-uav-track/blob/3e3e4ead8a70316cb960306eee017407bc0accf0/src/jev_uav_track/jev_client.py) at the pinned commit. |

## When to use

- Explore Jev as a discrete decision layer over rollouts and hard safety filters.
- Prototype confidence and hysteresis gating with a fallback action.
- Mismatch: the rollout model is a constant-velocity approximation; not for real flight per the README.

## How it works

Candidate behaviors are rolled out, filtered by collision, margin, speed and battery checks, then sent to Jev as one Choice question (`jev_client.py`, `https://api.typesafe.ai/v1/systemone`); low-confidence answers fall back. Integration evidence: [`src/jev_uav_track/jev_client.py`](https://github.com/lian-wsy/wsy-jev-uav-track/blob/3e3e4ead8a70316cb960306eee017407bc0accf0/src/jev_uav_track/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/lian-wsy/wsy-jev-uav-track.git && cd wsy-jev-uav-track
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m jev_uav_track.demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture and module list in the README: [github.com/lian-wsy/wsy-jev-uav-track#readme](https://github.com/lian-wsy/wsy-jev-uav-track#readme)

## Limits and data handling

Algorithm and interface prototype only; not validated flight dynamics. State summaries are sent to TypeSafe when the real client is used.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 3e3e4ead8a70](https://github.com/lian-wsy/wsy-jev-uav-track/tree/3e3e4ead8a70316cb960306eee017407bc0accf0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
