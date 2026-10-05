# JevBird

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Pygame Flappy Bird where TypeSafe Jev picks one of several simulated flight paths through each pipe gap (roughly one API call per pipe) and the game draws the chosen and rejected paths.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leftspace89/JevBird) |
| Maintainer | [leftspace89](https://github.com/leftspace89). Independently curated. |
| Format | Small game demo / script |
| Requirements | Python 3.10+, `pip install -r requirements.txt` (pygame, typesafe-sdk), and `TYPESAFE_API_KEY` for Jev mode, or `JEV_BASE_URL` for a self-hosted System One-compatible server. |
| License | [MIT](https://github.com/leftspace89/JevBird/blob/e5ace2cd9dbf73ae08d2943475a4c97eb67deb16/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Show a typed-choice control loop where code simulates options and Jev only picks among them.
- Teach how to visualize probability distributions over candidate actions.
- Mismatch: a toy demo, not a benchmark or reusable library.

## How it works

When a new pipe becomes the target, the game simulates a spread of flight paths through the gap and asks Jev which path to fly; the reply's choice and distribution schedule the flaps, and rejected candidates are drawn with opacity by probability ([README](https://github.com/leftspace89/JevBird/blob/e5ace2cd9dbf73ae08d2943475a4c97eb67deb16/README.md)).

## Get started

Install, add your key, run, and press J to hand control to Jev (live Jev calls, about one per pipe):

```sh
git clone https://github.com/leftspace89/JevBird && cd JevBird
pip install -r requirements.txt
echo 'TYPESAFE_API_KEY=...' > .env
python flappy_bird.py   # press J for Jev mode
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Demo GIF and a 2 min 35 s recording in `demo/` (upstream).

## Limits and data handling

Jev mode sends the simulated path descriptions to TypeSafe and is billed per call. No performance claims are made here; the high score file is local.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit e5ace2cd9dbf](https://github.com/leftspace89/JevBird/tree/e5ace2cd9dbf73ae08d2943475a4c97eb67deb16). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
