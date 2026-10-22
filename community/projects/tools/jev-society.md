# jevSociety (social feed simulation judged by Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Agent-based simulation of 10,000 social-media accounts in which Jev is the only judge of which opinions fit together, asked live for every like and change of mind, to compare a feed ranked by predicted likes against a random feed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/isaacbitran/jev-society) |
| Maintainer | [isaacbitran](https://github.com/isaacbitran). Independently curated. |
| Format | Research simulation with web viewer (Python) |
| Requirements | Python; `TYPESAFE_API_KEY` for live runs. |
| License | [MIT](https://github.com/isaacbitran/jev-society/blob/8084adcc884be8ffa83dbbac62760d391d2701db/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevsociety/jev.py`](https://github.com/isaacbitran/jev-society/blob/8084adcc884be8ffa83dbbac62760d391d2701db/jevsociety/jev.py) at the pinned commit. |

## When to use

- Explore how a ranked feed changes what people see, using a judgment model instead of hand-coded opinion rules.
- Reuse the GSS-matched issue setup for your own experiments.
- Mismatch: findings depend on assumptions; the author notes the polarization result is not robust.

## How it works

`jevsociety/jev.py` asks Jev whether a reader would like a post and whether to change position; the feed ranking is the only difference between the two simulated societies. Integration evidence: [`jevsociety/jev.py`](https://github.com/isaacbitran/jev-society/blob/8084adcc884be8ffa83dbbac62760d391d2701db/jevsociety/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/isaacbitran/jev-society.git
cd jev-society
# see the README for run commands; set TYPESAFE_API_KEY for live Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [jev-society.vercel.app](https://jev-society.vercel.app)
- One-page note (PDF): [github.com/isaacbitran/jev-society/releases/download/v1.0/jev-society-note.pdf](https://github.com/isaacbitran/jev-society/releases/download/v1.0/jev-society-note.pdf)

## Limits and data handling

Simulated opinions only. Live runs make many Jev calls; check costs first. Results are the author's.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 8084adcc884b](https://github.com/isaacbitran/jev-society/tree/8084adcc884be8ffa83dbbac62760d391d2701db). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
