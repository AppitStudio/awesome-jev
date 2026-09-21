# Jev Second Brain

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local-first Markdown/Obsidian vault CLI: indexes notes, suggests related pairs with source paths, and optionally asks TypeSafe Jev (via Vercel AI Gateway) to classify relationships—never auto-edits your vault.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fellowship-dev/jev-second-brain) |
| Maintainer | [fellowship-dev](https://github.com/fellowship-dev) / Max F. Findel. Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`jev-second-brain` 0.1.0); console script `secondbrain`. Install from GitHub (not on PyPI yet). |
| Requirements | Python **≥ 3.11**. Indexing/search need no key. Optional judgments need `AI_GATEWAY_API_KEY` (Vercel AI Gateway → `typesafe-ai/jev`). |
| License | [MIT](https://github.com/fellowship-dev/jev-second-brain/blob/0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline pytest passed; live Gateway/Jev judgments were **not** run. Distinct from [PerfectRecall](perfectrecall.md) (Hermes memory) and [Jev-Mem](jev-mem.md) (agentic graph memory). |

## When to use

Use it when you want local FTS search and human-reviewed link suggestions over a Markdown vault, with optional Jev pair judgments and ZDR-oriented private-mode gates. Prefer [PerfectRecall](perfectrecall.md) for agent session memory; prefer [jlink](jlink.md) for generic record linking.

## How it works

`secondbrain init/index/search/suggest` keep SQLite state outside the vault. Without `--evaluate`, suggest only shows candidates. With `--evaluate`, [`provider.py`](https://github.com/fellowship-dev/jev-second-brain/blob/0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae/src/jev_second_brain/provider.py) calls Vercel AI Gateway `typesafe-ai/jev` with optional zero-data-retention evidence checks before private runs. Proposals stay pending until you record a decision by ID—source notes are never rewritten by the CLI.

## Get started

```sh
pipx install "git+https://github.com/fellowship-dev/jev-second-brain.git@0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae"
git clone https://github.com/fellowship-dev/jev-second-brain.git
cd jev-second-brain && git checkout 0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae
state_dir="$(mktemp -d)"
secondbrain init examples/synthetic-vault --state "$state_dir" --json
secondbrain index --state "$state_dir" --json
secondbrain search "Aurora onboarding" --state "$state_dir" --json
```

Pinned offline tests:

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -e . pytest
pytest -q tests/ --ignore=tests/test_benchmark.py --ignore=tests/test_live_alignment_benchmark.py --ignore=tests/test_rerank_benchmark.py
```

Optional `--evaluate` / `--rerank` sends note excerpts to the Gateway/Jev and can incur charges; use `--public` only for non-private material.

## Examples and demos

- Fictional vault under `examples/synthetic-vault`.
- Privacy/canary docs: [docs/PRIVACY.md](https://github.com/fellowship-dev/jev-second-brain/blob/0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae/docs/PRIVACY.md), [docs/LIVE-CANARY.md](https://github.com/fellowship-dev/jev-second-brain/blob/0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae/docs/LIVE-CANARY.md).
- Offline pytest on the review host: **55 passed** (benchmark modules ignored—collection needs extra deps).

## Limits and data handling

Vault stays authoritative; derived SQLite is separate. Evaluations may send pair excerpts through Vercel to TypeSafe; private mode requires ZDR evidence per upstream policy. MVP / pre-release install from GitHub only.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 0fd1bba](https://github.com/fellowship-dev/jev-second-brain/tree/0fd1bba7b733efb38e586cf47fbccaa2d3c2b3ae): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev_second_brain/provider.py`, and tests. **55 passed** offline. No live Gateway/Jev.

Related: [PerfectRecall](perfectrecall.md), [Jev-Mem](jev-mem.md), [jlink](jlink.md).
