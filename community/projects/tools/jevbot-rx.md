# JevBOT Rx by Mahesh K (simulated hospital delivery robot where Jev picks the path several times a second, raced against LLMs)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

JEVATHON SF 2026 demo of a hospital delivery robot that has to choose paths around people and carts a few times a second. A nurse texts a request, and Jev and an LLM race the same STAT delivery; the README reports 143 ms p50 per Jev decision against 2.3 s or more for the LLMs tested. Extends Standard Agents' JevPilot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bouncypitch/hospital-delivery-robot) |
| Maintainer | [bouncypitch](https://github.com/bouncypitch). Independently curated. |
| Format | Node.js / Vite web simulation (Cloudflare Worker backend) |
| Requirements | Node.js and a TypeSafe API key; optional LLM keys for the comparison. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.js`](https://github.com/bouncypitch/hospital-delivery-robot/blob/247bc7956fa46eb031f75adacab9a32e099ff8bf/server/jev.js) at the pinned commit. |

## When to use

- See Jev used as a fast, cheap per-tick decision maker in a simulation.
- Mismatch: real robot control; this is a hackathon simulation.

## How it works

`server/jev.js` posts the robot's surroundings with a route Choice to `https://api.typesafe.ai/v1/systemone` and validates the returned choice; `server/nurse-text.js` uses Jev to parse the nurse's text request. Integration evidence: [`server/jev.js`](https://github.com/bouncypitch/hospital-delivery-robot/blob/247bc7956fa46eb031f75adacab9a32e099ff8bf/server/jev.js).

## Get started

Watch the demo page, or run it locally with your key in `.env`.

```sh
git clone https://github.com/bouncypitch/hospital-delivery-robot.git && cd hospital-delivery-robot
cp .env.example .env   # add TYPESAFE_API_KEY
npm ci && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo page: [bouncypitch.github.io/hospital-delivery-robot/](https://bouncypitch.github.io/hospital-delivery-robot/)
- Builds on JevPilot: [github.com/standardagents/jevpilot](https://github.com/standardagents/jevpilot)

## Limits and data handling

Benchmark numbers are the authors' own 20-decision test. Simulation state is sent to TypeSafe. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 247bc7956fa4](https://github.com/bouncypitch/hospital-delivery-robot/tree/247bc7956fa46eb031f75adacab9a32e099ff8bf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
