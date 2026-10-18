# SWAT

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI that finds domains impersonating a brand: an LLM proposes lookalike and typosquat candidates, live ones are checked via certificate logs and DNS/HTTP, then TypeSafe Jev answers yes/no on domain and homepage impersonation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/r0075h3ll/SWAT) |
| Maintainer | [r0075h3ll](https://github.com/r0075h3ll). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python 3.12+, uv, an OpenRouter key for candidate generation and a Jev (TypeSafe) API key. |
| License | [MIT](https://github.com/r0075h3ll/SWAT/blob/aad301b8c2b7421d0bd907d12c53cfe9913cdaef/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/r0075h3ll/status/2111873027311043026)). |
| Jev evidence | [`swat/classifier.py`](https://github.com/r0075h3ll/SWAT/blob/aad301b8c2b7421d0bd907d12c53cfe9913cdaef/swat/classifier.py) at the pinned commit. |

## When to use

- Brand-protection sweeps for typosquat and lookalike domains with a typed Jev verdict per gate.
- Want cheap pre-filters (edit distance, liveness) before any Jev call.
- Mismatch: research-grade CLI; verdicts need human review before takedown requests.

## How it works

The pipeline is generate, pre-filter, liveness check, Jev judgment. `swat/classifier.py` uses the TypeSafe SDK `Choice` to ask two yes/no questions per live domain (does the domain impersonate the brand, does the homepage clone the reference site) and writes per-gate decisions to JSON. Integration evidence: [`swat/classifier.py`](https://github.com/r0075h3ll/SWAT/blob/aad301b8c2b7421d0bd907d12c53cfe9913cdaef/swat/classifier.py).

## Get started

From the upstream README: clone, `uv sync`, set `OPENROUTER_API_KEY` and `JEV_API_KEY`, then run against a target domain.

```sh
git clone https://github.com/r0075h3ll/SWAT.git && cd SWAT
uv sync
export OPENROUTER_API_KEY=... JEV_API_KEY=...
uv run python3 -m swat -d example.com -o output.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README pipeline and output schema (`decisions`, `results`)
- tests/test_classifier.py

## Limits and data handling

Candidate domains and fetched homepage content go to OpenRouter and TypeSafe. Live checks contact third-party domains. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit aad301b8c2b7](https://github.com/r0075h3ll/SWAT/tree/aad301b8c2b7421d0bd907d12c53cfe9913cdaef). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
