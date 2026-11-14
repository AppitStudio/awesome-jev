# AgenticJevNav (robot language-goal navigation where an agent proposes bounded moves and Jev verifies them on events)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code for RGB language-goal object search and navigation: an agent model authorizes bounded actions, Jev runs event-triggered checks (skill routing, success verification, failure detection, recovery routing, task progress), and a shared executor keeps independent local vetoes. Covers the Habitat-Sim simulation snapshot, a physical robot adaptation, controller and SDK bridge source, and offline contract tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZSN2024/AgenticJevNav) |
| Maintainer | [ZSN2024](https://github.com/ZSN2024). Independently curated. |
| Format | Python research package: simulation, physical-robot controller and offline tests (no license file; the README says no project license has been chosen) |
| Requirements | Python 3.10/3.11 for offline tests; for simulation a Linux Habitat-Sim 0.3.3 GPU host and licensed HSSD assets; an OpenAI key for the agent model and a TypeSafe key for Jev. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`controller/jev_decision.py`](https://github.com/ZSN2024/AgenticJevNav/blob/6d99354fe4c1d50bf19ef9505da6365fb5f6b069/controller/jev_decision.py) at the pinned commit. |

## When to use

- Study how a fast verifier changes an agentic navigation loop, in simulation or on a supervised robot.
- Mismatch: unsupervised robot deployment; the authors require a supervised operator and compatible vendor SDK.

## How it works

`controller/jev_decision.py` asks Jev the five decision types over finite JSON state, and `controller/config.yaml` sets provider `jev`, base URL `https://api.typesafe.ai` and `jev-latest`; the README pins the public simulation edition to `jev-1.13.0` with the agent on the official OpenAI Responses API. The packaged controller disables motion by default. Integration evidence: [`controller/jev_decision.py`](https://github.com/ZSN2024/AgenticJevNav/blob/6d99354fe4c1d50bf19ef9505da6365fb5f6b069/controller/jev_decision.py).

## Get started

Run the offline checks first; simulation and robot runs need the documented assets, hardware and keys.

```sh
git clone https://github.com/ZSN2024/AgenticJevNav && cd AgenticJevNav
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_sources.py && python scripts/test_offline.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project page: [zsn2024.github.io/AgenticJevNav/](https://zsn2024.github.io/AgenticJevNav/)
- README: [github.com/ZSN2024/AgenticJevNav/blob/6d99354fe4c1d50bf19ef9505da6365fb5f6b069/README.md](https://github.com/ZSN2024/AgenticJevNav/blob/6d99354fe4c1d50bf19ef9505da6365fb5f6b069/README.md)

## Limits and data handling

Live runs send observations and state to OpenAI and TypeSafe on your keys. Trial recordings, raw results, credentials, proprietary SDK libraries and HSSD meshes are not included. No license is granted for project-authored code.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 6d99354fe4c1](https://github.com/ZSN2024/AgenticJevNav/tree/6d99354fe4c1d50bf19ef9505da6365fb5f6b069). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
