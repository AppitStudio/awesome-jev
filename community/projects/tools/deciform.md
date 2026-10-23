# DeciForm (structured objects from System One decision models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library that fills Pydantic schemas with System One decision models instead of generated text: enum, bool, bounded-int and optional fields become typed questions with calibrated per-field confidence, with escalation to an LLM only for free text or low confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taneemishere/deciform) |
| Maintainer | [taneemishere](https://github.com/taneemishere). Independently curated. |
| Format | Python library |
| Requirements | Python; pydantic and httpx; a `/v1/systemone` endpoint such as TypeSafe Jev (API key) or Baseten; optional OpenAI-compatible LLM for fallback. |
| License | [MIT](https://github.com/taneemishere/deciform/blob/8647564bf3aec920fe20567225161f5a0fc13c5b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`deciform/backends/systemone.py`](https://github.com/taneemishere/deciform/blob/8647564bf3aec920fe20567225161f5a0fc13c5b/deciform/backends/systemone.py) at the pinned commit. |

## When to use

- Extract typed fields like category, urgency and priority with confidence per field.
- Spend LLM calls only on free-text fields or uncertain answers.
- Mismatch: v0.x and not on PyPI yet; install from source.

## How it works

`deciform/backends/systemone.py` talks to any `/v1/systemone` provider; the docstring shows TypeSafe Jev with `https://api.typesafe.ai`, `jev-latest` and `TYPESAFE_API_KEY` (the default preset is Baseten's elephant model). Integration evidence: [`deciform/backends/systemone.py`](https://github.com/taneemishere/deciform/blob/8647564bf3aec920fe20567225161f5a0fc13c5b/deciform/backends/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/taneemishere/deciform
cd deciform && pip install -e .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Ticket triage example: [github.com/taneemishere/deciform/blob/main/examples/ticket_triage.py](https://github.com/taneemishere/deciform/blob/main/examples/ticket_triage.py)
- Benchmark write-up: [github.com/taneemishere/deciform/blob/main/REPORT.md](https://github.com/taneemishere/deciform/blob/main/REPORT.md)

## Limits and data handling

Input text goes to the configured decision and fallback providers. Jev is one supported backend, not the default.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 8647564bf3ae](https://github.com/taneemishere/deciform/tree/8647564bf3aec920fe20567225161f5a0fc13c5b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
