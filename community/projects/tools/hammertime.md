# Hammertime

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local live Formula 1 strategy desk: a strategy engine owns the numbers (tyre model, pit loss, Monte Carlo), while System One models such as TypeSafe Jev read race-control messages, gauge rain risk, and weigh evidence into box-now or stay-out calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KishoreXO/Hammertime) |
| Maintainer | [KishoreXO](https://github.com/KishoreXO). Independently curated. |
| Format | Python app + local dashboard |
| Requirements | Python; TypeSafe key or another System One-compatible endpoint; optional OpenF1 credentials for live data. |
| License | [MIT](https://github.com/KishoreXO/Hammertime/blob/097fed5771cc823d1a89c8fe09505f7c00e79929/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pitwall/judge/backends.py`](https://github.com/KishoreXO/Hammertime/blob/097fed5771cc823d1a89c8fe09505f7c00e79929/pitwall/judge/backends.py) at the pinned commit. |

## When to use

- Follow a race with lap-by-lap pit calls and visible uncertainty.
- Mismatch: hobby tool; live data needs OpenF1 access.

## How it works

`pitwall/judge/backends.py` targets any endpoint speaking the System One API, including TypeSafe's hosted Jev; the engine passes its evidence to the model for questions code cannot score. Integration evidence: [`pitwall/judge/backends.py`](https://github.com/KishoreXO/Hammertime/blob/097fed5771cc823d1a89c8fe09505f7c00e79929/pitwall/judge/backends.py).

## Get started

From the upstream README: install, start the dashboard, paste a TypeSafe key when asked (or choose another System One model).

```sh
git clone https://github.com/KishoreXO/Hammertime && cd Hammertime
# see README to install and launch the dashboard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo video

## Limits and data handling

Race messages and engine evidence go to the chosen System One endpoint. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 097fed5771cc](https://github.com/KishoreXO/Hammertime/tree/097fed5771cc823d1a89c8fe09505f7c00e79929). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
