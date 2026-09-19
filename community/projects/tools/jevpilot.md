# JevPilot

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Inspect Jev choosing sampled driving maneuvers in a browser simulation, alongside deterministic geometry, collision checks and braking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/standardagents/jevpilot) |
| Maintainer | [Standard Agents](https://github.com/standardagents). |
| Format | Experimental JavaScript/Three.js driving simulator with Vite and a server-side Jev adapter. |
| Jev's role | Selects eligible simulated motion/path candidates and, when needed, an alternate route. |
| Requirements | A modern WebGL browser, Node.js 20.19+ within 20.x or 22.12+ (the locked Vite 8 requirement), npm; `TYPESAFE_API_KEY` for local Jev mode. |
| Access and costs | Local manual free play requires no provider key. Jev mode uses the operator's TypeSafe account and can incur charges. Hosted Jev mode requires Standard Agents sign-in; credit/access terms were not independently verified. |
| License | No project-level code license or package license declaration was found. Third-party models and textures have separate notices under `public/`; those do not license the application. |

## When to use

Use this developer demo to inspect candidate generation, compact structured state,
stale-result rejection and local controls around model choices. Its JSON inspector
makes the decision boundary visible while a simulated car follows a route.
The driving scenario is a visualization and experiment; it provides no evidence
of suitability for controlling a real vehicle.

## How it works

The [request builder](https://github.com/standardagents/jevpilot/blob/e1beeb13b9a928fb76f167f86af584f4ce9cf180/src/jev-request.js)
compresses candidate paths, boundaries, nearby traffic, stop memory and destination
guidance into tables. Local code samples steering/speed combinations and filters
eligible choices; questions with only one eligible answer resolve locally.

The [server adapter](https://github.com/standardagents/jevpilot/blob/e1beeb13b9a928fb76f167f86af584f4ce9cf180/server/jev.js)
uses `POST https://api.typesafe.ai/v1/systemone` with `jev-latest`. It validates
candidate state, maps short model IDs back to local candidates, checks returned
selection/usage, and rejects moving paths marked as imminent collisions.
The browser checks batch identity, route version and decision age before applying
steering and target speed. Local simulation code also supplies a collision brake.

The supplied driving instructions favor aggressive progress. This is a specific
simulation policy rather than neutral driving advice; candidate coverage and
local brake behavior materially influence observed outcomes.

## Get started

This source-build path was inspected, not executed. Package installation uses the
network. Local development bypasses hosted login and demo-credit restrictions.

```sh
git clone https://github.com/standardagents/jevpilot.git
cd jevpilot
npm ci --ignore-scripts
npm run dev
```

Open `http://localhost:5173`. Manual mode starts with autopilot disabled: use WASD
to drive and Space to brake. No TypeSafe key is needed for this initial mode.
The [README](https://github.com/standardagents/jevpilot#run-locally) explains controls.

For live model control, create the private `.env` from `.env.example`, set
`TYPESAFE_API_KEY` there and restart the server. Keep the key server-side; do not
use a `VITE_` variable. Press **J** or **Engage Jev** to begin recurring billable
requests, and toggle it off to stop. There is no local demo-credit spending cap.

Use **Candidates** to see the generated alternatives and **JSON** to inspect the
provider payload, probabilities and chosen maneuver. The displayed cost is an
estimate based on configured token prices, not an independently verified invoice.

## Examples and demos

- The [upstream README](https://github.com/standardagents/jevpilot) links a hosted demo and recording; this review did not sign in or exercise either.
- [Jev adapter tests](https://github.com/standardagents/jevpilot/blob/e1beeb13b9a928fb76f167f86af584f4ce9cf180/tests/jev.test.js) contain mocked decisions, invalid distributions, mismatched candidates and HTTP-failure cases.
- [Simulation tests](https://github.com/standardagents/jevpilot/blob/e1beeb13b9a928fb76f167f86af584f4ce9cf180/tests/simulation.test.js) and related collision/traffic tests document deterministic control behavior. They were inspected only in scope described below, not run.

## Limits and data handling

TypeSafe receives compact simulated scene state through the app server. The key
stays on that server. Hosted mode adds Standard Agents authentication and usage
accounting; local dev/preview deliberately omit that access control. Do not treat
a local dev server as a ready-made public deployment.

Requests can recur several times per second. Errors set target speed to zero,
back off and disable autopilot after three failures. Responses older than 1.8
seconds are rejected, and changed scene context triggers replanning. These are
implementation safeguards, not a demonstrated safety guarantee. Choice scores
are not a validated measure of driving reliability; there is no general
confidence-based abstention threshold.

The repository includes third-party assets with attribution requirements,
including the depicted car model. Inspect their individual notices before reuse.
App-code licensing remains unspecified. Live routing quality, hosted credits,
provider compatibility and browser rendering were not tested.

## Review and maintenance

Source-reviewed **2026-09-19** at
[`e1beeb13b9a928fb76f167f86af584f4ce9cf180`](https://github.com/standardagents/jevpilot/commit/e1beeb13b9a928fb76f167f86af584f4ce9cf180).
Inspected README/setup, package metadata, license inventory and asset attribution,
request builder, server adapter, candidate validation, browser result/error
handling and representative mocked Jev tests. No dependency installation, test
execution, browser run, sign-in or live requests were performed. See [validation scope](../../../docs/validation.md#community-project-checks).

AI-assisted catalog review; contributor affiliation/commercial relationships
were not supplied. Listing is not an endorsement.
