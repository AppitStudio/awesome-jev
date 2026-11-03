# Drone Commander, Powered by Jev (hex-grid tactics game test build where Jev picks each unit's move from the legal options)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Field test of the Drone Commander MK2 hex-grid tactics game in which Jev, not a chat model, picks each unit's action from a short menu of legal options. The rules engine still resolves movement, fire, damage and objectives, and a deterministic fallback plays the turn when Jev is late, malformed or under the confidence gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev) |
| Maintainer | [Ramolisdenneyous](https://github.com/Ramolisdenneyous). Independently curated. |
| Format | Web game (FastAPI backend, PixiJS frontend, Docker Compose) |
| Requirements | Docker; a TypeSafe API key (`TYPESAFE_API_KEY`) with `TACTICAL_PROVIDER=jev`. |
| License | [MIT](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev/blob/e3a640da3f1d1b7513a949846f0d46d64b2678fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`backend/app/agents/provider.py`](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev/blob/e3a640da3f1d1b7513a949846f0d46d64b2678fb/backend/app/agents/provider.py) at the pinned commit. |

## When to use

- See Jev driving real-time game units as a bounded choice, with a safe fallback behind it.
- Mismatch: an experiment branch of the game, not the live playable build; the README's first results are early playtests, not a benchmark.

## How it works

`backend/app/agents/provider.py` sends each unit's compact battlefield state and the offered option IDs to `<base>/v1/systemone` as a typed `choice` question (`jev-latest` by default), checks the chosen ID against the offered list, and falls back to the deterministic tactic below a 0.60 confidence or 0.10 margin gate; a shadow mode logs Jev's pick without committing it. Integration evidence: [`backend/app/agents/provider.py`](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev/blob/e3a640da3f1d1b7513a949846f0d46d64b2678fb/backend/app/agents/provider.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev.git
cd Drone-Commander-Powered-by-Jev
cp .env.example .env   # set TACTICAL_PROVIDER=jev and TYPESAFE_API_KEY
docker compose up --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the gates, shadow mode and first playtest notes: [github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev#readme](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev#readme)

## Limits and data handling

Compact battlefield state and option IDs go to TypeSafe on your key; the README reports roughly 75 percent lower decision tokens in early local matches, which is the author's own playtest and not independently measured. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit e3a640da3f1d](https://github.com/Ramolisdenneyous/Drone-Commander-Powered-by-Jev/tree/e3a640da3f1d1b7513a949846f0d46d64b2678fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
