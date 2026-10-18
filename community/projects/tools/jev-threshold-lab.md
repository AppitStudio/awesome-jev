# jev-threshold-lab

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Fits act/review/escalate thresholds per Jev question on your labeled data, with precision/recall sweeps, expected-cost bands, calibration (ECE), and a debugging ladder.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CapCurious/jev-threshold-lab) |
| Maintainer | [CapCurious](https://github.com/CapCurious). Independently curated. |
| Format | Python CLI (stdlib) with recorded fits and a browser explainer |
| Requirements | Python 3.10+; labeled decisions; JEV_API_KEY or TYPESAFE_API_KEY for live fits. |
| License | [MIT](https://github.com/CapCurious/jev-threshold-lab/blob/8f067576d753e882c353be0810ace3facef89ef6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/CapCurious/jev-threshold-lab/blob/8f067576d753e882c353be0810ace3facef89ef6/jev_client.py) at the pinned commit. |

## When to use

- Choosing act/review/escalate cutoffs from data instead of by eye.
- Need a calibration readout and cost-sensitive band pick.
- Mismatch: lab tool; you bring labels and own the production policy.

## How it works

`jev_client.py` talks to TypeSafe System One. `jev_threshold_lab.py` replays labeled items, sweeps thresholds, picks cost-aware act/review bands, and prints ECE plus a debugging ladder. Integration evidence: [`jev_client.py`](https://github.com/CapCurious/jev-threshold-lab/blob/8f067576d753e882c353be0810ace3facef89ef6/jev_client.py).

## Get started

Clone and run the recorded demo, or fit on your own labeled JSON.

```sh
git clone https://github.com/CapCurious/jev-threshold-lab && cd jev-threshold-lab
python3 jev_threshold_lab.py --demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [capcurious.github.io/jev-threshold-lab/](https://capcurious.github.io/jev-threshold-lab/)
- README sweep table on 120 synthetic commands

## Limits and data handling

Live fits call TypeSafe. Thresholds are only as good as your labels and cost assumptions.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 8f067576d753](https://github.com/CapCurious/jev-threshold-lab/tree/8f067576d753e882c353be0810ace3facef89ef6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
