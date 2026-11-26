# JEV + EdgeSimPy by Bruno Silva do Canto (research experiment where Jev picks which edge server gets each service in an EdgeSimPy simulation)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experimental Portuguese-language project that plugs Jev into the EdgeSimPy simulator to place services on edge servers. When several servers have enough free CPU and memory, the Jev policy sends their availability and the service's demand to Jev and asks for a choice that balances CPU and memory; the README describes a Least Loaded policy for comparison, and each decision is logged with confidence, probabilities and latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation) |
| Maintainer | [Bruno Silva do Canto](https://github.com/Bscanto). Independently curated. |
| Format | Python research scripts (uv project) |
| Requirements | Python 3.14 via uv, git (EdgeSimPy installs from its repository) and a TypeSafe API key in `.env`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`politica_jev.py`](https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation/blob/baf3bff9923dad6aa9cd6f57d75034eef7e81018/politica_jev.py) at the pinned commit. |

## When to use

- Researchers comparing a decision model with simple heuristics for edge resource allocation in simulation.
- Mismatch: a scheduler for real infrastructure; this is an early experiment on a sample EdgeSimPy scenario.

## How it works

`politica_jev.py` uses `TypeSafeClassifier` and `Choice` from `langchain-typesafe` to ask Jev which viable server to use; with one candidate the choice is direct and no call is made. `simulacao.py` runs up to 100 one-second steps and records results. Integration evidence: [`politica_jev.py`](https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation/blob/baf3bff9923dad6aa9cd6f57d75034eef7e81018/politica_jev.py).

## Get started

Install with uv, add your key to `.env`, then run the simulation.

```sh
git clone https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation
cd Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation
uv sync
echo 'TYPESAFE_API_KEY=...' > .env
uv run preparar_dataset.py
uv run simulacao.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation#readme](https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation#readme)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Early experiment: one sample scenario, no published comparison results, and no model training; only CPU and memory are considered. The README's `politica_least_loaded.py` is not in the reviewed commit, so the comparison policy cannot be run as described. Server and service attributes are sent to TypeSafe for each multi-candidate decision. Documentation is in Portuguese.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit baf3bff9923d](https://github.com/Bscanto/Jev-EdgeSim-System-One-Models-for-Edge-Resource-Allocation/tree/baf3bff9923dad6aa9cd6f57d75034eef7e81018). Inspected the README and `politica_jev.py` at the pinned commit; the simulation was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
