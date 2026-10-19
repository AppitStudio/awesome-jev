# Kettei Kart

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Camera-only SuperTuxKart harness for decision models: each frame returns a probability for each of nine controls and the highest wins, with recorded head-to-head results and adapters for Sqwish's Kettei Fat, Liquid D1 Ultra, and TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sqwishai/kettei-kart) |
| Maintainer | [sqwishai](https://github.com/sqwishai). Independently curated. |
| Format | Python harness + recording tools |
| Requirements | Ubuntu 24.04 (or WSL2), Python 3.12, OpenGL/EGL, SuperTuxKart assets; `TYPESAFE_API_KEY` for the Jev adapter. |
| License | [Apache-2.0](https://github.com/sqwishai/kettei-kart/blob/bbf94e0964df645fcf51d551a87f9026cf8a677f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/kettei_kart/client.py`](https://github.com/sqwishai/kettei-kart/blob/bbf94e0964df645fcf51d551a87f9026cf8a677f/src/kettei_kart/client.py) at the pinned commit. |

## When to use

- Compare decision models on a real-time driving task.
- Mismatch: vendor harness led by Sqwish's own model; Jev is one adapter.

## How it works

`src/kettei_kart/client.py` defines provider endpoints, including TypeSafe's `/v1/systemone` with `jev-1.14.0`; the same observation builder and argmax selection drive every model. Integration evidence: [`src/kettei_kart/client.py`](https://github.com/sqwishai/kettei-kart/blob/bbf94e0964df645fcf51d551a87f9026cf8a677f/src/kettei_kart/client.py).

## Get started

From the upstream README: install system packages, clone, set your API key, and run a race.

```sh
git clone https://github.com/sqwishai/kettei-kart && cd kettei-kart
read -rsp 'TypeSafe API key: ' TYPESAFE_API_KEY; export TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- results/README.md

## Limits and data handling

Camera frames go to the chosen provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit bbf94e0964df](https://github.com/sqwishai/kettei-kart/tree/bbf94e0964df645fcf51d551a87f9026cf8a677f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
