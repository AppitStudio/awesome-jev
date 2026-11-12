# Jev Agent-First Install Kit (sets up Jev model and effort routing for Codex)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Installer kit a coding agent runs to set up Jev routing for a fresh Codex profile: selecting `jev/auto` lets Jev choose the model and reasoning depth for each task through an embedded router, and checks report what actually worked on your machine.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/teo-nex/jev-codex-harness) |
| Maintainer | [teo-nex](https://github.com/teo-nex). Independently curated. |
| Format | Installer, embedded router and checks (Python and Node.js, MIT); public alpha |
| Requirements | Codex CLI, Python 3.11+, Node.js 22.19+, a per-user service manager, a fresh Codex profile, and a TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/teo-nex/jev-codex-harness/blob/352a8d5e55fde3d42969ec11ed4705bd9014383f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev_server.py`](https://github.com/teo-nex/jev-codex-harness/blob/352a8d5e55fde3d42969ec11ed4705bd9014383f/server/jev_server.py) at the pinned commit. |

## When to use

- Let Jev pick the model and effort for Codex tasks while you can still choose manually.
- Mismatch: public alpha; fresh Codex profiles only, no migration of existing setups.

## How it works

`server/jev_server.py` sends routing decisions to `https://api.typesafe.ai/v1/systemone` or OpenRouter's decisions endpoint, and `server/decision_contract.py` pins the accepted Jev models (`jev-latest` requests, typed v1 responses). Integration evidence: [`server/jev_server.py`](https://github.com/teo-nex/jev-codex-harness/blob/352a8d5e55fde3d42969ec11ed4705bd9014383f/server/jev_server.py).

## Get started

Give a coding agent the repository link and ask it to follow `AGENT_INSTALL.md` for a fresh Codex profile.

```sh
git clone https://github.com/teo-nex/jev-codex-harness && cd jev-codex-harness
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Agent install protocol: [github.com/teo-nex/jev-codex-harness/blob/352a8d5e55fde3d42969ec11ed4705bd9014383f/AGENT_INSTALL.md](https://github.com/teo-nex/jev-codex-harness/blob/352a8d5e55fde3d42969ec11ed4705bd9014383f/AGENT_INSTALL.md)

## Limits and data handling

Task summaries for routing go to TypeSafe or OpenRouter on your key; the key is stored outside the repository.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 352a8d5e55fd](https://github.com/teo-nex/jev-codex-harness/tree/352a8d5e55fde3d42969ec11ed4705bd9014383f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
