# EHDS Health Data Access Body prototype (rules decide health-data requests, Jev can reject or flag but never approve)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hackathon prototype (AIM Healthcare Hackathon Vienna 2026, European Health Data Space track) for deciding health-data access requests: fixed rules run the decision order and an Article 54 lexicon, a decision model reads only the request text and can reject a prohibited purpose or flag for review but never approve, and an officer signs off every case. Hosted Jev or a local Kev-4B model can fill the model role. Synthetic data only; the README reports 10/10 correct decisions in the demo set and documents holdout failures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/noah-stockinger/ehds-access-body) |
| Maintainer | [noah-stockinger](https://github.com/noah-stockinger). Independently curated. |
| Format | Python service + React UI (uv, Make) |
| Requirements | Python via uv; `TYPESAFE_API_KEY` for the Jev-led mode (and `ANTHROPIC_API_KEY` for writing help). |
| License | [MIT](https://github.com/noah-stockinger/ehds-access-body/blob/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/hdab/kev.py`](https://github.com/noah-stockinger/ehds-access-body/blob/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8/src/hdab/kev.py) at the pinned commit. |

## When to use

- Prototype a regulated approval workflow where a model can only tighten, never loosen, rule-based decisions.
- Mismatch: demo with synthetic patients; not legal advice or a certified EHDS system.

## How it works

`kev.py` asks fixed typed questions about the request purpose of local Kev or hosted Jev (`KEV_PROVIDER=jev`); in `assisted` mode disagreement or confidence under 0.80 sets `needs_review`, in `led` mode the model may reject but not approve. Only request text is sent, never data rows. Integration evidence: [`src/hdab/kev.py`](https://github.com/noah-stockinger/ehds-access-body/blob/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8/src/hdab/kev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone --recursive https://github.com/noah-stockinger/ehds-access-body.git && cd ehds-access-body
uv sync
cp .env.example .env   # add TYPESAFE_API_KEY
make seed && make dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Metric results and holdouts: [github.com/noah-stockinger/ehds-access-body/blob/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8/README.md#metric-results](https://github.com/noah-stockinger/ehds-access-body/blob/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8/README.md#metric-results)

## Limits and data handling

Request text is sent to TypeSafe in Jev mode. All patient data is synthetic. Hackathon prototype. Not affiliated with TypeSafe or the EU.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 9632c92eb921](https://github.com/noah-stockinger/ehds-access-body/tree/9632c92eb9210addfc0be5370c5a1da5a3d3fbb8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
