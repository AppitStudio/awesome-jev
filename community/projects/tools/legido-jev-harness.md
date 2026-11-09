# jev-harness by legido-ai (decision harness with confidence-routed cascade and audit ledger for System One models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Open-source harness for System One models: typed questions, per-action thresholds and invariants, a four-layer confidence cascade, an audit ledger and evals; TypeSafe Jev is one of three deciders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/legido-ai/jev-harness) |
| Maintainer | [legido-ai](https://github.com/legido-ai). Independently curated. |
| Format | Python library + CLI + Docker (MIT) |
| Requirements | Python/uv, `uv pip install -e .`, and a `TYPESAFE_API_KEY` for the Jev decider. |
| License | [MIT](https://github.com/legido-ai/jev-harness/blob/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_harness/deciders/typesafe.py`](https://github.com/legido-ai/jev-harness/blob/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69/src/jev_harness/deciders/typesafe.py) at the pinned commit. |

## When to use

- Route cheap Jev answers and escalate uncertain ones.
- Keep an audit ledger of automated decisions.
- Mismatch: you still write the question files and thresholds.

## How it works

`deciders/typesafe.py` calls `https://api.typesafe.ai` over plain HTTP (default `jev-1.13.0`); `cascade.py` routes on confidence and `ledger.py` records every decision. Integration evidence: [`src/jev_harness/deciders/typesafe.py`](https://github.com/legido-ai/jev-harness/blob/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69/src/jev_harness/deciders/typesafe.py).

## Get started

Install, validate a question file (`jev-harness validate --questions examples/email_triage.questions.json`) and run with your key.

```sh
git clone https://github.com/legido-ai/jev-harness.git && cd jev-harness
uv pip install -e ".[dev]"
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/legido-ai/jev-harness/blob/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69/README.md](https://github.com/legido-ai/jev-harness/blob/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69/README.md)

## Limits and data handling

Decision state is sent to TypeSafe or your chosen decider.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 17f2feb6e2ab](https://github.com/legido-ai/jev-harness/tree/17f2feb6e2ab2ab8b3b4e896a2be5a53e8aeeb69). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
