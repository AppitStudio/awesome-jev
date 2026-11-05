# hydro-jev (Home Assistant lawn-watering advisor that asks Jev whether newly sown grass needs five minutes of water)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Local Python app that pulls Home Assistant weather and pump context and asks Jev whether a newly sown lawn needs a short watering now. The reviewed snapshot can never turn the pump on: there is no code path for `switch.turn_on`, and dry-run is the intended first mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Denbergvanthijs/hydro-jev) |
| Maintainer | [Denbergvanthijs](https://github.com/Denbergvanthijs). Independently curated. |
| Format | Python CLI/service (Apache-2.0) |
| Requirements | Python 3.12, a Home Assistant URL and long-lived token, and a `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/Denbergvanthijs/hydro-jev/blob/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/client.py`](https://github.com/Denbergvanthijs/hydro-jev/blob/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d/jev/client.py) at the pinned commit. |

## When to use

- Decide whether a newly sown lawn needs a short watering from Home Assistant context.
- Keep the pump under human control while you review dry-run advice.
- Mismatch: Dutch/English docs assume a local HA install; live pump control is deliberately absent in this snapshot.

## How it works

`jev/client.py` calls TypeSafe with typed questions built from HA weather, electricity price and lawn metadata; the app prints advice and never issues a pump service call in the reviewed tree. Integration evidence: [`jev/client.py`](https://github.com/Denbergvanthijs/hydro-jev/blob/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d/jev/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
conda create --name hydro-jev python=3.12 && conda activate hydro-jev
pip install -r requirements.txt
cp .env.example .env   # set HA_* and TYPESAFE_API_KEY; keep DRY_RUN=true
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Denbergvanthijs/hydro-jev/blob/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d/README.md](https://github.com/Denbergvanthijs/hydro-jev/blob/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d/README.md)

## Limits and data handling

Home Assistant state and lawn metadata are sent to TypeSafe on your key. Do not disable dry-run until you have reviewed the advice.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0e76a70fa9d2](https://github.com/Denbergvanthijs/hydro-jev/tree/0e76a70fa9d2b103ab537b1e3b22aea88b4e3e6d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
