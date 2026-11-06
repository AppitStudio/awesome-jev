# Boyun-core (simulation runtime with a TypeSafe Jev actor-choice adapter)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Python simulation engine, CLI, HTTP APIs and MCP integration where authored worlds settle actor choices; a decision-lab adapter calls TypeSafe System One so Jev selects among structured alternatives without authoring free text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Boyun-Protocol/Boyun-core) |
| Maintainer | [Boyun-Protocol](https://github.com/Boyun-Protocol). Independently curated. |
| Format | Python runtime + CLI/API/MCP (AGPL-3.0) |
| Requirements | Python environment and a TypeSafe key when using the Jev decision-lab adapter. |
| License | [AGPL-3.0](https://github.com/Boyun-Protocol/Boyun-core/blob/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`engine/src/decision_lab/jev.py`](https://github.com/Boyun-Protocol/Boyun-core/blob/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19/engine/src/decision_lab/jev.py) at the pinned commit. |

## When to use

- Run replayable simulations with structured actor menus.
- Let Jev pick among authored alternatives under explicit policy limits.
- Mismatch: AGPL; probabilities are not calibrated market forecasts.

## How it works

`engine/src/decision_lab/jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` with bounded request sizes and returns choice probabilities for actor adapters. Integration evidence: [`engine/src/decision_lab/jev.py`](https://github.com/Boyun-Protocol/Boyun-core/blob/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19/engine/src/decision_lab/jev.py).

## Get started

Clone Boyun-core, follow the README for local CLI/API, and enable the Jev adapter with TYPESAFE_API_KEY when desired.

```sh
git clone https://github.com/Boyun-Protocol/Boyun-core.git && cd Boyun-core
export TYPESAFE_API_KEY=...
# see docs/decision-lab/JEV_INTEGRATION.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev integration docs: [github.com/Boyun-Protocol/Boyun-core/blob/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19/docs/decision-lab/JEV_INTEGRATION.md](https://github.com/Boyun-Protocol/Boyun-core/blob/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19/docs/decision-lab/JEV_INTEGRATION.md)

## Limits and data handling

Actor observations and menus sent through the adapter go to TypeSafe on your key. Outputs are conditional on rules and model behavior, not forecasts.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit fcb5efa8ff4c](https://github.com/Boyun-Protocol/Boyun-core/tree/fcb5efa8ff4c0042b47f1e93981e93fbdb0c1f19). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
