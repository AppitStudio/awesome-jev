# Spotlight (Buried Signals)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OSINT investigation orchestrator for journalists working with AI agents, with opt-in decision checks via OpenRouter (default `typesafe/jev-1.13`) that flag findings their stored sources do not support, report prose that overstates findings, and knowledge-base drift — flags can only lower confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/buriedsignals/spotlight) |
| Product homepage | [spotlight.buriedsignals.com](https://spotlight.buriedsignals.com/) |
| Maintainer | [buriedsignals](https://github.com/buriedsignals). Independently curated. |
| Format | Agent skill bundle and scripts, installed via Buried Signals Engine (`bsig`) or from source |
| Requirements | A supported agent runtime; your own `OPENROUTER_API_KEY` for the optional decision checks. Sensitive mode never uses them. |
| License | [MIT](https://github.com/buriedsignals/spotlight/blob/3c846ad82545a1481efbae5c0bcfcb4e4b702517/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add a cheap, typed second check that a source excerpt actually supports each claim (partial support, contradictions, allegation stated as fact, amount/date mismatch).
- Catch headlines and summaries that say more than the verified findings allow, before a report goes out.
- Mismatch: the checks never decide a verdict or write text; they only lower confidence, so editorial judgment stays human.

## How it works

At three gates — Gate 1 finding support, the finalizer's `report_fidelity` stage, and knowledge-base ingest — Spotlight sends narrow typed questions with the claim, its quoted evidence and a short source excerpt to a decision model on OpenRouter (default `typesafe/jev-1.13`) using zero-data-retention routing with fallbacks disabled. `advisory` mode shows flags; `enforce` caps displayed confidence. The client, question set and rules live in [`integrations/decisions/`](https://github.com/buriedsignals/spotlight/tree/3c846ad82545a1481efbae5c0bcfcb4e4b702517/integrations/decisions).

## Get started

Install from source for agent use (lighter route), then opt in when preflight asks:

```sh
git clone https://github.com/buriedsignals/spotlight.git
# follow README "Install from source (agents)" to link the skills
python3 integrations/preflight.py --json   # shows decisions opt_in: undecided | enabled | declined
# key: OPENROUTER_API_KEY in a private env file (chmod 600), never in chat
```

Decision checks are billed by OpenRouter (Jev via TypeSafe) only after you opt in; everything else is your agent runtime's cost.

## Examples and demos

- README section *Opt-in decision checks* (gates, data sent, modes).
- `schemas/decision-signals.schema.json` and `scripts/decision-signals.py` for the stored decision signals.

## Limits and data handling

Opt-in; each request sends the claim, quoted evidence and a source excerpt to OpenRouter and TypeSafe (US). The managed `bsig` install route is still finishing its cutover per the README; source install has no updates or credential handling. MIT license includes upstream methodology attributions. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 3c846ad82545](https://github.com/buriedsignals/spotlight/tree/3c846ad82545a1481efbae5c0bcfcb4e4b702517). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
