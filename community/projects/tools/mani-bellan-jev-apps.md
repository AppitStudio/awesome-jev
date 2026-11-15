# Jev apps by mani-bellan (five small Python apps on Jev: pipeline-failure triage, support routing, agent-run EKG, Scam Shield and complaint autolabeling)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Five small Python apps with write-ups: pipeline failure triage decides what to do about a failed data task in about 100 ms; a customer support router sends messages to specialist agents; Agent EKG scores every step of agent runs to find where they derail and how early failing runs can be stopped; Scam Shield rates a suspicious text (with 89 real messages received in India and an evaluation harness); and Autolabel labels consumer complaints with Jev or the open Strands Decider and compares both on 770 held-out complaints for accuracy and calibration.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mani-bellan/jev-apps) |
| Maintainer | [mani-bellan](https://github.com/mani-bellan). Independently curated. |
| Format | Python apps (uv) with blog write-ups and evaluation data |
| Requirements | Python with uv and `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scam-shield/shield/jev.py`](https://github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/scam-shield/shield/jev.py) at the pinned commit. |

## When to use

- Copy working patterns for triage, routing, agent evaluation and labeling with Jev.
- Mismatch: production services; these are compact demos with their own evaluations.

## How it works

`scam-shield/shield/jev.py` posts to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` (thresholds are tuned to that version); `triage.py` and the router use the TypeSafe Python SDK client. Integration evidence: [`scam-shield/shield/jev.py`](https://github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/scam-shield/shield/jev.py).

## Get started

Install with uv, set your key and run one of the apps.

```sh
git clone https://github.com/mani-bellan/jev-apps && cd jev-apps
export TYPESAFE_API_KEY=...
uv run triage.py samples/*.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/README.md](https://github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/README.md)
- Write-up (Jev vs Strands Decider): [github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/blog/autolabel.md](https://github.com/mani-bellan/jev-apps/blob/c3932b01e566e575d2dfe6f21b564d592ccbaa78/blog/autolabel.md)

## Limits and data handling

Messages, logs and complaints go to TypeSafe on your key. Evaluation results are the maker's own on the included data. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit c3932b01e566](https://github.com/mani-bellan/jev-apps/tree/c3932b01e566e575d2dfe6f21b564d592ccbaa78). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
