# AGORA by Sammi De Blas (local typed-decision console with general and SOC/SIEM packs, using local backends or Jev in the cloud)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Spanish-language console for typed choice, score and noul decisions: pick a pack, paste a case and get calibrated probabilities and a confidence card, compare the same question across backends, and keep a searchable history. Backends include a deterministic mock, local LAYA and local chat servers, and optional JEV / TypeSafe cloud; cloud hosts must be authorised explicitly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PoisonXploIT/agora-decision-console) |
| Maintainer | [PoisonXploIT](https://github.com/PoisonXploIT). Independently curated. |
| Format | Python (FastAPI) service with a no-build web UI and MCP server |
| Requirements | Python with pip; a `JEV_API_KEY` only for the optional cloud backend. |
| License | [Apache-2.0](https://github.com/PoisonXploIT/agora-decision-console/blob/b68f029b170b7c0694622ff03b9588f35e7f88cc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agora_serve/providers.py`](https://github.com/PoisonXploIT/agora-decision-console/blob/b68f029b170b7c0694622ff03b9588f35e7f88cc/agora_serve/providers.py) at the pinned commit. |

## When to use

- Compare Jev with local decision backends on the same typed questions, including SOC triage packs.
- Mismatch: English-only teams; the UI and docs are Spanish.

## How it works

`agora_serve/providers.py` defines a `JEV / TypeSafe (nube)` preset on the native `/v1/systemone` API at `https://api.typesafe.ai` with the key read from `JEV_API_KEY`; `agora_serve/security.py` enforces the host allow-list. Integration evidence: [`agora_serve/providers.py`](https://github.com/PoisonXploIT/agora-decision-console/blob/b68f029b170b7c0694622ff03b9588f35e7f88cc/agora_serve/providers.py).

## Get started

Install in a virtual environment and start the local console.

```sh
git clone https://github.com/PoisonXploIT/agora-decision-console.git && cd agora-decision-console
python -m venv .venv && .venv/bin/python -m pip install -e ".[test]"
agora serve   # http://127.0.0.1:8800/ui
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Spanish): [github.com/PoisonXploIT/agora-decision-console/blob/b68f029b170b7c0694622ff03b9588f35e7f88cc/README.md](https://github.com/PoisonXploIT/agora-decision-console/blob/b68f029b170b7c0694622ff03b9588f35e7f88cc/README.md)

## Limits and data handling

Case text leaves the machine only when a cloud backend such as Jev is chosen and authorised; that is logged in `audit.log`.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit b68f029b170b](https://github.com/PoisonXploIT/agora-decision-console/tree/b68f029b170b7c0694622ff03b9588f35e7f88cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
