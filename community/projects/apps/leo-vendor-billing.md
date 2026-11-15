# LEO (hackathon app that reads vendor contracts, emails and invoices, uses Jev to filter and validate, and flags billing leaks against card charges)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Berkeley Business Society x Ramp hackathon project for small businesses: LEO reads vendor contracts, emails (read-only Gmail sync) and invoices, records each agreed term with its source quote, and checks card charges against them to flag renewals, price increases, cap breaches and seat overages with the dollars at stake. Jev labels each document first so noise never reaches the LLM, and later checks the extracted terms; Claude Haiku extracts and drafts cancellation or negotiation emails, which are never sent without approval. Ships with a fictional coffee-shop demo dataset.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lewisyang3/LEO) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/lewisyang3/LEO#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; no hosted version. You pay TypeSafe and Anthropic for your own calls. No license file. Checked 2026-11-15. |
| Jev evidence | [`leo/pipeline/classify.py`](https://github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/leo/pipeline/classify.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [lewisyang3](https://github.com/lewisyang3). Independently curated. |
| Format | Python (FastAPI) backend and React dashboard with Docker Compose Postgres |
| Platform and availability | Web (self-hosted FastAPI + React dashboard on localhost) |
| Jev's role | Jev classifies every incoming document and checks extracted terms, so only relevant documents reach Claude. |
| Requirements | Python 3.13 with uv, Docker Compose, Node 22+; `ANTHROPIC_API_KEY` and `JEV_API_KEY` to run the pipeline (the seeded demo needs no keys). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Prototype contract-versus-charge reconciliation where Jev keeps noise away from the LLM.
- Mismatch: a production finance tool; this is a hackathon build with synthetic data.

## How it works

`leo/pipeline/classify.py` asks Jev a Choice question through the TypeSafe Python SDK (contract, order form, price notice, invoice, noise); `leo/pipeline/validate.py` uses Jev again to check extracted terms before they are kept. Integration evidence: [`leo/pipeline/classify.py`](https://github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/leo/pipeline/classify.py).

## Get started

Set up, start Postgres, seed the demo, then run the API and dashboard; add keys to run the live pipeline.

```sh
git clone https://github.com/lewisyang3/LEO && cd LEO
make setup && make up && make migrate && make seed
make api    # terminal 1
make web    # terminal 2 -> http://localhost:5173
# live pipeline: add ANTHROPIC_API_KEY and JEV_API_KEY to .env, then make ingest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/README.md](https://github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/README.md)
- Stack and LLM policy: [github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/docs/STACK.md](https://github.com/lewisyang3/LEO/blob/0283d61a436f31e571e6da4d5614440f3162f591/docs/STACK.md)

## Limits and data handling

Documents go to TypeSafe and Anthropic on your keys; Gmail tokens are encrypted at rest. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 0283d61a436f](https://github.com/lewisyang3/LEO/tree/0283d61a436f31e571e6da4d5614440f3162f591). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
