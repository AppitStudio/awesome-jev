# CryptoCadence

[All projects](../README.md) · [Web apps](README.md#web-apps)

Paper-trading and backtest platform for crypto that demonstrates a production-shaped stack: features, calibrated TypeSafe Jev decisions, hard risk vetoes, tamper-evident journal, and dashboard—simulation only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KarelTestSpecial/crypto-trading-lab) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/KarelTestSpecial/crypto-trading-lab#readme) |
| Pricing and access | Free MIT source. TypeSafe API key required for live Jev legs (billed). Explicitly simulation/paper trading—not live exchange execution. Checked 2026-10-12. |
| Jev evidence | [`src/judgment/jev.py`](https://github.com/KarelTestSpecial/crypto-trading-lab/blob/088d001c735effcacc9f138fb0e924449e261a09/src/judgment/jev.py); sample journal at `journal/decisions.jsonl`. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Not financial advice; app not run on the review host. |
| Maintainer | [KarelTestSpecial](https://github.com/KarelTestSpecial). Independently curated. |
| Format | Python · paper-trading lab + dashboard |
| Platform and availability | Self-hosted from source. |
| Jev's role | Jev supplies calibrated decisions; code enforces risk vetoes and journaling. |
| Requirements | Python; TypeSafe key for live judgments. |
| License | [MIT](https://github.com/KarelTestSpecial/crypto-trading-lab/blob/088d001c735effcacc9f138fb0e924449e261a09/LICENSE) |

## When to use

- Study a transparent Jev-in-the-loop quant automation shape without live capital.
- Mismatch: Showcase/simulation—not a broker.

## How it works

Feature engine feeds Jev; risk code can veto; journal appends decisions.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/KarelTestSpecial/crypto-trading-lab.git
cd crypto-trading-lab
# setup per README
```

## Limits and data handling

Market/feature text sent to TypeSafe when live; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 088d001c735e](https://github.com/KarelTestSpecial/crypto-trading-lab/tree/088d001c735effcacc9f138fb0e924449e261a09). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
