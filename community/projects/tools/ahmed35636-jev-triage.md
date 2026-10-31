# JEV SOC alert triage (classifies exported Windows security events with Jev and routes uncertain ones to review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI that classifies exported Windows security events, assigns investigation priority and routes uncertain or high-risk results into a review queue, writing one JSONL decision trail per event (detector hits, backend and model, confidence, severity, routing reasons). Jev is the model backend; a rule baseline runs without credentials and an optional Ollama stage writes investigation notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ahmed35636/jev-triage) |
| Maintainer | [ahmed35636](https://github.com/ahmed35636). Independently curated. |
| Format | Python CLI |
| Requirements | Python; `typesafe-sdk`, `TYPESAFE_API_KEY` and a model id for the Jev backend (rules backend needs nothing). |
| License | [MIT](https://github.com/ahmed35636/jev-triage/blob/7c96f9f36321aec44927fab4242e0a5886001d32/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_triage/classifier.py`](https://github.com/ahmed35636/jev-triage/blob/7c96f9f36321aec44927fab4242e0a5886001d32/src/jev_triage/classifier.py) at the pinned commit. |

## When to use

- Pre-sort Windows event exports for an analyst with an auditable confidence trail.
- Mismatch: offline exports only; not a live SIEM integration.

## How it works

`src/jev_triage/classifier.py` wraps `typesafe_sdk` choice questions in a `JevClassifier` that returns label, confidence and severity; the CLI audits a sample and sends low-confidence or high-risk events to review. Integration evidence: [`src/jev_triage/classifier.py`](https://github.com/ahmed35636/jev-triage/blob/7c96f9f36321aec44927fab4242e0a5886001d32/src/jev_triage/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
jev-triage data/events.jsonl --backend rules --audit-rate 0 --output reports/triage.jsonl
# --backend jev with TYPESAFE_API_KEY and --model for Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ahmed35636/jev-triage#readme](https://github.com/ahmed35636/jev-triage#readme)

## Limits and data handling

Event records are sent to TypeSafe in Jev mode; redact before using real logs. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 7c96f9f36321](https://github.com/ahmed35636/jev-triage/tree/7c96f9f36321aec44927fab4242e0a5886001d32). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
