# JevPokerBench

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Texas Hold'em benchmark and playground for decision models: cash and SNG leaderboards, hand replay/advisor, human rooms against models, and BYOK custom agents. Official TypeSafe Jev is a first-class provider alongside local System One-style routes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Prophetlab/JevPokerBench) |
| Maintainer | [Prophetlab](https://github.com/Prophetlab). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`pokerbench` 0.1.0** (FastAPI backend + Vite/React frontend); optional hosted demo. |
| Requirements | Python ≥ 3.12, Node.js 20.19+ or 22.12+ for the frontend build; provider keys in private `.env` for live play/benchmarks. |
| License | [MIT](https://github.com/Prophetlab/JevPokerBench/blob/9c9816688a3c0853c0fabe15db0af92a8aa23b9c/LICENSE). Provider terms and model weights remain separate. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline backend pytest inspected. Live hosted play and paid inference were not run. Hosted demo URL and invite economics are vendor-operated. |

## When to use

Use it to compare official Jev and other decision agents on poker actions with separate cash/SNG boards, or to play BYOK tables locally. Prefer [playjev](playjev.md) for independent open-weight game research without TypeSafe; prefer [jev-sec-bench](jev-sec-bench.md) for security corpora rather than poker.

## How it works

[`backend/pokerbench/provider.py`](https://github.com/Prophetlab/JevPokerBench/blob/9c9816688a3c0853c0fabe15db0af92a8aa23b9c/backend/pokerbench/provider.py) and [`official_adapter.py`](https://github.com/Prophetlab/JevPokerBench/blob/9c9816688a3c0853c0fabe15db0af92a8aa23b9c/backend/pokerbench/official_adapter.py) call TypeSafe via `typesafe-sdk` / System One (`/v1/systemone`). Example registry entries point at `https://api.typesafe.ai`. Application code owns legality, chip accounting, concurrency pools, SSRF protection for custom agents, and scoring described in `BENCHMARK.md`. Model action probabilities are not calibrated win probabilities.

## Get started

```sh
git clone https://github.com/Prophetlab/JevPokerBench.git
cd JevPokerBench
git checkout 9c9816688a3c0853c0fabe15db0af92a8aa23b9c
python3.12 -m venv .venv
.venv/bin/pip install -e '.[test]'
cp .env.example .env   # private keys; chmod 600
mkdir -p config && cp examples/entries.example.json config/entries.json
cd frontend && npm ci && npm run build && cd ..
.venv/bin/python -m pytest -q
.venv/bin/uvicorn pokerbench.api:app --host localhost --port 8097
# Open http://localhost:8097
```

Optional hosted UI: [JevPokerBench Online](https://123.56.23.73/pokerbench/) (operator-run; registration; BYOK for custom agents). Live inference sends hand/decision state to providers and can incur charges.

## Examples and demos

- Hosted leaderboards/replay/advisor (operator-reported).
- `examples/entries.example.json` Jev direct entry; `scripts/jev_smoke.py`.
- Offline backend tests under `backend/tests/` (executed for this listing).

## Limits and data handling

Hand histories and agent prompts leave the host on live provider calls. Custom-agent keys use browser `sessionStorage` and server memory per upstream docs—verify for your deployment. Concurrency pools and invite DeepSeek allowances are operator policies, not catalog guarantees. Frontend/browser Playwright suites were not re-run here.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 9c98166](https://github.com/Prophetlab/JevPokerBench/tree/9c9816688a3c0853c0fabe15db0af92a8aa23b9c): `pokerbench` **0.1.0**, MIT. AI-assisted source review of README, LICENSE, provider/adapter, examples. Offline `.venv/bin/python -m pytest -q`: **567 passed** (1 Starlette deprecation warning). No live TypeSafe or hosted play.

Related: [Jev Lab](jev-lab.md), [PlayJev](playjev.md), [jev-sec-bench](jev-sec-bench.md).
