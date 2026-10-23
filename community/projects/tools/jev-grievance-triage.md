# jev-grievance-triage (auditable grievance triage for development finance)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Reads one grievance about a development project and returns a structured, auditable triage decision: Jev answers 23 narrow questions as calibrated probabilities in one request, versioned thresholds turn them into flags, and plain Python policy rules decide routing, urgency and human review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aen07/jev-grievance-triage) |
| Maintainer | [aen07](https://github.com/aen07). Independently curated. |
| Format | Python CLI, HTTP API and Streamlit UI |
| Requirements | Python 3.11+; a TypeSafe API key (offline replay of recorded answers needs none); optional Anthropic key for a drafted letter. |
| License | [Apache-2.0](https://github.com/aen07/jev-grievance-triage/blob/80a5672ac18e77d5cec784202d13abcc60df61cf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`triage/jev_client.py`](https://github.com/aen07/jev-grievance-triage/blob/80a5672ac18e77d5cec784202d13abcc60df61cf/triage/jev_client.py) at the pinned commit. |

## When to use

- Route complaints so dangerous cases reach the right people within hours.
- Keep every decision traceable to probabilities, thresholds and rules.
- Mismatch: built around one development-finance brief; adapt questions and policy to your own process.

## How it works

`triage/jev_client.py` calls Jev through the official `typesafe-sdk` with all 23 questions in one request; `config/thresholds.yaml` sets the cutoffs and the P1–P8 rules make the final decision, so no LLM output can change it. Integration evidence: [`triage/jev_client.py`](https://github.com/aen07/jev-grievance-triage/blob/80a5672ac18e77d5cec784202d13abcc60df61cf/triage/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv
.venv/bin/pip install -e ".[dev]"
triage --cache replay one samples/test1.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture, question design and results in the README: [github.com/aen07/jev-grievance-triage#readme](https://github.com/aen07/jev-grievance-triage#readme)

## Limits and data handling

Grievance text is sent to TypeSafe in live mode; the README describes identity redaction for routed cases. Evaluation numbers are on the author's test set.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 80a5672ac18e](https://github.com/aen07/jev-grievance-triage/tree/80a5672ac18e77d5cec784202d13abcc60df61cf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
