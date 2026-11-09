# Production-Grade Document RAG (Docling RAG engine with a TypeSafe Jev entailment guardrail)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Document RAG engine (Docling parsing, VLM table repair, hybrid RRF retrieval) whose tier-2 hallucination guardrail checks claim entailment with TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Souheil007/Rag_Full_Version) |
| Maintainer | [Souheil007](https://github.com/Souheil007). Independently curated. |
| Format | Python service (MIT) |
| Requirements | Python, the README's model keys, and a TypeSafe key for the Jev entailment engine. |
| License | [MIT](https://github.com/Souheil007/Rag_Full_Version/blob/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/guardrails/jev_client.py`](https://github.com/Souheil007/Rag_Full_Version/blob/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee/src/guardrails/jev_client.py) at the pinned commit. |

## When to use

- Verify RAG answers claim by claim.
- Swap a heuristic guardrail for typed entailment.
- Mismatch: needs several external model keys.

## How it works

`jev_client.py` calls `https://api.typesafe.ai/v1` with `jev-1.13.0`; `config.yaml` sets `entailment_engine: jev` (alternatives: heuristic, mock) for the hallucination detector. Integration evidence: [`src/guardrails/jev_client.py`](https://github.com/Souheil007/Rag_Full_Version/blob/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee/src/guardrails/jev_client.py).

## Get started

Install with `pip install -r requirements.txt`, set keys in `.env`, and keep `entailment_engine: jev` in `config.yaml`.

```sh
git clone https://github.com/Souheil007/Rag_Full_Version.git && cd Rag_Full_Version
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Souheil007/Rag_Full_Version/blob/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee/README.md](https://github.com/Souheil007/Rag_Full_Version/blob/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee/README.md)

## Limits and data handling

Retrieved passages and generated claims are sent to TypeSafe for entailment.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit a9aeab5d35cc](https://github.com/Souheil007/Rag_Full_Version/tree/a9aeab5d35cc0efbf0908c6fa88ed15a6877daee). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
