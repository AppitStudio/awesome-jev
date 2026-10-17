# JEVDrive

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Highway driving simulation where Jev picks one of five manoeuvres (change left, keep course, change right, speed up, slow down) from a computed time-to-collision and headway assessment, with a Pygame cockpit HUD showing the action probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hasim2006/JEVDrive) |
| Maintainer | [hasim2006](https://github.com/hasim2006). Independently curated. |
| Format | Python simulation (HighwayEnv, Pygame CE, `typesafe-sdk`) |
| Requirements | Python 3.13+, uv or pip; a TypeSafe API key for the Jev policy (a rule-based offline policy runs without one). |
| License | [MIT](https://github.com/hasim2006/JEVDrive/blob/414a843f31ad5bd96b0361c3359fe247d0c94540/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/driving_jev/policy.py`](https://github.com/hasim2006/JEVDrive/blob/414a843f31ad5bd96b0361c3359fe247d0c94540/src/driving_jev/policy.py) at the pinned commit. |

## When to use

- Watch a decision model make discrete driving choices in dense simulated traffic and compare it with a heuristic policy.
- Collect telemetry from headless benchmark runs.
- Mismatch: a simulation demo, not a driving system.

## How it works

Before each step the app computes time-to-collision for four lanes, a three-second headway and speed differences, and `policy.py` sends that assessment to Jev as a Choice through `TypeSafeClient`; the chosen manoeuvre drives the HighwayEnv car and the probabilities render on the HUD. Integration evidence: [`src/driving_jev/policy.py`](https://github.com/hasim2006/JEVDrive/blob/414a843f31ad5bd96b0361c3359fe247d0c94540/src/driving_jev/policy.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hasim2006/JEVDrive.git
cd JEVDrive
uv venv --python 3.13 .venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots and HUD explanation in the README.

## Limits and data handling

Simulated traffic state goes to TypeSafe on your key in Jev mode; each step is a paid call.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 414a843f31ad](https://github.com/hasim2006/JEVDrive/tree/414a843f31ad5bd96b0361c3359fe247d0c94540). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
