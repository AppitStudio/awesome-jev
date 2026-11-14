# JAF: Jev Agent Firewall (three-hop guard against jailbreaks, indirect prompt injection and Base64 exfiltration, with Jev answering typed attack questions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jevathon project that wraps an agent with checks on what comes in, what it reads from the web and tools, and what it sends out: Jev answers `is_attack` and related typed questions in one request per check, and egress rules plus a canary catch encoded exfiltration. Ships a scripted demo with a local dummy attacker, a poisoned local wiki and a Streamlit dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yazeedallabadi24/JAF) |
| Maintainer | [yazeedallabadi24](https://github.com/yazeedallabadi24). Independently curated. |
| Format | Python library, agent runner and Streamlit dashboard |
| Requirements | Python 3.11+; an OpenRouter key for Jev via the Decisions API (or a TypeSafe key for the direct provider). 41 offline tests need no key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/jev_client.py`](https://github.com/yazeedallabadi24/JAF/blob/fd72b3e4d48bdd67e753f8d82dd45b2350145f6a/core/jev_client.py) at the pinned commit. |

## When to use

- Study a layered prompt-injection and exfiltration guard for tool-using agents.
- Mismatch: production security without your own evaluation; when no key works the direct provider falls back to simulated scores.

## How it works

`core/jev_client.py` calls the OpenRouter Decisions endpoint with `typesafe/jev-1.13`; `core/decision_engine.py` also has a direct TypeSafe provider (`https://api.typesafe.ai/v1/systemone`) that only sends the key to a `typesafe.ai` URL. Without a working key that provider silently returns a simulated answer, so check the reported backend. Integration evidence: [`core/jev_client.py`](https://github.com/yazeedallabadi24/JAF/blob/fd72b3e4d48bdd67e753f8d82dd45b2350145f6a/core/jev_client.py).

## Get started

Run the offline tests and the scripted unprotected/protected demo.

```sh
git clone https://github.com/yazeedallabadi24/JAF && cd JAF
pip install -r requirements.txt
python -m pytest -q
python -m c2_server.c2_listener      # terminal 1: local dummy attacker
python -m agent.agent_runner --scripted --mode protected
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/yazeedallabadi24/JAF/blob/fd72b3e4d48bdd67e753f8d82dd45b2350145f6a/README.md](https://github.com/yazeedallabadi24/JAF/blob/fd72b3e4d48bdd67e753f8d82dd45b2350145f6a/README.md)

## Limits and data handling

Checked text goes to OpenRouter or TypeSafe on your key. The demo attacker and wiki bind to localhost. README shows an MIT badge, but the repository has no LICENSE file, so no license is actually granted.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit fd72b3e4d48b](https://github.com/yazeedallabadi24/JAF/tree/fd72b3e4d48bdd67e753f8d82dd45b2350145f6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
