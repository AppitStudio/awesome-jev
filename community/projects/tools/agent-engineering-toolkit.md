# Agent Engineering Toolkit (skills-first engineering plugin with a TypeSafe Jev reflex adapter for MARGOS)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source skills-first plugin for agent-assisted engineering (repo engineering, Python harness, MARGOS orchestration, instruction audits, plugin authoring); its MARGOS context reflex can call TypeSafe Jev for fast typed routing decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haydarrjr/agent-engineering-toolkit) |
| Maintainer | [haydarrjr](https://github.com/haydarrjr). Independently curated. |
| Format | Agent skills plugin (Python, Apache-2.0) |
| Requirements | Python 3, a supported agent host, and optionally a TypeSafe API key for the Jev reflex. |
| License | [Apache-2.0](https://github.com/haydarrjr/agent-engineering-toolkit/blob/83b52c9256365b2da5fe1164e392efa9e6dae2c0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/margos/scripts/margos_reflex_jev.py`](https://github.com/haydarrjr/agent-engineering-toolkit/blob/83b52c9256365b2da5fe1164e392efa9e6dae2c0/skills/margos/scripts/margos_reflex_jev.py) at the pinned commit. |

## When to use

- Add structured engineering skills to coding agents.
- Use Jev as a cheap reflex for orchestration decisions.
- Mismatch: Jev is one optional adapter in a larger toolkit.

## How it works

`skills/margos/scripts/margos_reflex_jev.py` defaults to `https://api.typesafe.ai` with `jev-latest`; tests cover the adapter and a trace benchmark. Integration evidence: [`skills/margos/scripts/margos_reflex_jev.py`](https://github.com/haydarrjr/agent-engineering-toolkit/blob/83b52c9256365b2da5fe1164e392efa9e6dae2c0/skills/margos/scripts/margos_reflex_jev.py).

## Get started

Install the plugin into your agent host per README and opt into the Jev reflex with a key.

```sh
git clone https://github.com/haydarrjr/agent-engineering-toolkit.git && cd agent-engineering-toolkit
export TYPESAFE_API_KEY=...
python -m pytest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/haydarrjr/agent-engineering-toolkit/blob/83b52c9256365b2da5fe1164e392efa9e6dae2c0/README.md](https://github.com/haydarrjr/agent-engineering-toolkit/blob/83b52c9256365b2da5fe1164e392efa9e6dae2c0/README.md)

## Limits and data handling

Reflex context is sent to TypeSafe on your key when enabled.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 83b52c925636](https://github.com/haydarrjr/agent-engineering-toolkit/tree/83b52c9256365b2da5fe1164e392efa9e6dae2c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
