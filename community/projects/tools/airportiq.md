# airportiq (airport capacity-pressure agent with a Jev guardrail and Haiku fallback)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One-day take-home: a conversational agent over public FAA and BTS data that shows which US airports are under the most capacity pressure. Numbers come from deterministic code; an LLM calls typed tools, and a guardrail asks Jev first, falling back to Claude Haiku when Jev is unavailable or unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ozeriyarin/airportiq) |
| Maintainer | [ozeriyarin](https://github.com/ozeriyarin). Independently curated. |
| Format | Python (uv) CLI and local web server |
| Requirements | Python 3.12 and uv; optional Anthropic and TypeSafe keys (offline test mode needs none). |
| License | [MIT](https://github.com/ozeriyarin/airportiq/blob/2114a6ccace4524689c4d2c406dac67bf774236e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/app/decide/guard.py`](https://github.com/ozeriyarin/airportiq/blob/2114a6ccace4524689c4d2c406dac67bf774236e/src/app/decide/guard.py) at the pinned commit. |

## When to use

- See a Jev-first guardrail with an LLM fallback in a tool-calling agent.
- Mismatch: a take-home, not a maintained product.

## How it works

`src/app/decide/guard.py` asks `typesafe:jev-latest` typed guard questions and hands the same question to Haiku when Jev errors or its confidence is below `guard_confidence`. Integration evidence: [`src/app/decide/guard.py`](https://github.com/ozeriyarin/airportiq/blob/2114a6ccace4524689c4d2c406dac67bf774236e/src/app/decide/guard.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run agent chat --test "What can you help me with?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: [github.com/ozeriyarin/airportiq/blob/main/docs/DESIGN.md](https://github.com/ozeriyarin/airportiq/blob/main/docs/DESIGN.md)

## Limits and data handling

User questions go to the configured providers. Not investment advice. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 2114a6ccace4](https://github.com/ozeriyarin/airportiq/tree/2114a6ccace4524689c4d2c406dac67bf774236e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
