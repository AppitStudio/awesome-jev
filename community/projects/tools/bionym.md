# bionym (resolve gene identifiers into confidence-scored knowledge graphs with Jev only for ambiguity)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Bioinformatics pipeline that gathers evidence from NCBI, UniProt, OMA and related APIs, records asserted facts with provenance at confidence 1.0, and asks TypeSafe Jev only where APIs cannot decide—multi-candidate picks, fuzzy hits, lineage rank—emitting a knowledge graph of scored edges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d-callan/bionym) |
| Maintainer | [d-callan](https://github.com/d-callan). Independently curated. |
| Format | Python package (MIT) |
| Requirements | Python environment, public bio API access, and `TYPESAFE_API_KEY` for ambiguous judgments. |
| License | [MIT](https://github.com/d-callan/bionym/blob/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/bionym/jev.py`](https://github.com/d-callan/bionym/blob/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3/src/bionym/jev.py) at the pinned commit. |

## When to use

- Resolve mixed gene identifiers into a provenance-backed graph.
- Keep model calls off API-assertable facts.
- Mismatch: confidence bands are two-tier (asserted vs Jev-judged), not a calibrated biology score.

## How it works

`src/bionym/jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` for typed ambiguity questions and records `jev_question_id` on sub-1.0 edges. Integration evidence: [`src/bionym/jev.py`](https://github.com/d-callan/bionym/blob/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3/src/bionym/jev.py).

## Get started

Install from the repo and run the pipeline stages documented in the README.

```sh
git clone https://github.com/d-callan/bionym.git && cd bionym
export TYPESAFE_API_KEY=...
# see README for stage commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/d-callan/bionym/blob/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3/README.md](https://github.com/d-callan/bionym/blob/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3/README.md)

## Limits and data handling

Ambiguous identifier context is sent to TypeSafe on your key. Negative claims are never model-guessed.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 9e72e137b30f](https://github.com/d-callan/bionym/tree/9e72e137b30f1fdfa1fb66c966e67ce34b3976d3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
