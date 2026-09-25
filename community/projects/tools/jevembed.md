# JevEmbed

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent Python framework that turns embedding models into Choice, Score, and Noul decisions with Jev-style request/response schemas (API, CLI, optional HTTP server).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HITsz-TMG/JevEmbed) |
| Maintainer | [HITsz-TMG](https://github.com/HITsz-TMG) / HIT-TMG. Independently curated. |
| Format | Python package (`jevembed`) with YAML model configs, CLI, and FastAPI server option. |
| Requirements | Python 3.10–3.12 recommended; PyTorch/transformers stack per `requirements.txt`; embedding weights downloaded on first use. |
| License | [Apache-2.0](https://github.com/HITsz-TMG/JevEmbed/blob/45b7055800ea49786510f48b0751e86c6a09f6eb/LICENSE). |
| Disclosure | Independent implementation—not TypeSafe-hosted Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Local inference not run on the review host. |

## When to use

Use when you want **local embedding-backed typed decisions** with a familiar System One-shaped interface. Prefer hosted TypeSafe Jev for the official cloud model.

## How it works

Configured embedding models encode state/options; the framework maps similarities into Choice/Score/Noul-shaped answers. Optional HTTP server exposes a Jev-shaped API.

## Get started

```sh
git clone https://github.com/HITsz-TMG/JevEmbed.git
cd JevEmbed
git checkout 45b7055800ea49786510f48b0751e86c6a09f6eb
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
# Example: python -m jevembed --config configs/kalm-embedding-v2.5.yaml --input examples/official_choice_exchange.json
```

## Examples and demos

- `examples/` exchange JSON files; HF merged weights `HIT-TMG/JevEmbed-KaLM-Embedding-V2.5`.
- CLM guide under `docs/clm.md`.

## Limits and data handling

Weights and `trust_remote_code` behavior follow each model config. Not a drop-in replacement for hosted `jev-latest`. Quality depends on the embedding backbone and task.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 45b7055](https://github.com/HITsz-TMG/JevEmbed/tree/45b7055800ea49786510f48b0751e86c6a09f6eb). AI-assisted README and LICENSE inspection; install/inference not executed.
