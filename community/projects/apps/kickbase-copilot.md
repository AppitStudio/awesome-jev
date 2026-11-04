# Kickbase KI-Cockpit (self-hosted German fantasy-Bundesliga co-pilot where Jev reads news into lineup odds and code decides)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted web cockpit and optional autopilot for Kickbase (German-language). Jev reads match reports, press conferences and forecasts and returns calibrated start, bench, absent and comeback probabilities that feed a 0-100 player score; code, including a lineup optimizer, makes every purchase and sale. A single guarded executor, dry-run by default, supports three autonomy levels, and it falls back to non-AI sources when no key is set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milopraetzel/kickbase-copilot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/milopraetzel/kickbase-copilot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you host it and supply any TypeSafe key with its charges. No hosted plan was found. Checked 2026-11-05. |
| Jev evidence | [`api/src/kickbase_agent/intel/role_judge.py`](https://github.com/milopraetzel/kickbase-copilot/blob/013db043013073b836b957acca89a0899c128870/api/src/kickbase_agent/intel/role_judge.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [milopraetzel](https://github.com/milopraetzel). Independently curated. |
| Format | Python API and web cockpit run with Docker Compose (German UI and docs) |
| Platform and availability | Self-hosted web app (Docker Compose); no hosted instance. |
| Jev's role | Reads news into calibrated player role and availability probabilities that gate purchases; code does the optimizing and trading. |
| Requirements | Docker and Docker Compose, a Kickbase account; a TypeSafe key is optional. |
| License | [MIT](https://github.com/milopraetzel/kickbase-copilot/blob/013db043013073b836b957acca89a0899c128870/LICENSE) |

## When to use

- Run a transparent co-pilot for a Kickbase league where Jev only judges news and code makes the money decisions.
- Mismatch: it automates actions on a third-party game account (check Kickbase's terms), and Jev acts only at 95% confidence or higher.

## How it works

`role_judge.py` asks Jev (TypeSafe SDK) a Choice question per player and article about the player's role, and the README says a confident absence verdict only blocks a new purchase; Jev tightens rules but never loosens them, and a TypeSafe outage leaves the other signals in charge. Integration evidence: [`api/src/kickbase_agent/intel/role_judge.py`](https://github.com/milopraetzel/kickbase-copilot/blob/013db043013073b836b957acca89a0899c128870/api/src/kickbase_agent/intel/role_judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/milopraetzel/kickbase-copilot.git
cd kickbase-copilot
cp api/.env.example api/.env
docker compose --env-file api/.env up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (German) with the cockpit screenshots, safety rules and quickstart: [github.com/milopraetzel/kickbase-copilot#readme](https://github.com/milopraetzel/kickbase-copilot#readme)

## Limits and data handling

With a key, article snippets and player names go to TypeSafe on your key. The tool connects to your Kickbase account from your own deployment and can place bids when you turn autopilot levels on; start in the default dry-run Co-Pilot mode. No hosted instance is offered. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 013db0430130](https://github.com/milopraetzel/kickbase-copilot/tree/013db043013073b836b957acca89a0899c128870). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
