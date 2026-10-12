# Laya × Jev ticket classification

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Structured SaaS support-ticket classification you can drop into a helpdesk: a Python SDK with a `JevEngine` (TypeSafe API) and a local fine-tuned `LayaEngine`, plus a REST service, an optional shared inbox and Zendesk sync.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mike-Animal-Counseling/laya-jev-lab) |
| Maintainer | [Mike-Animal-Counseling](https://github.com/Mike-Animal-Counseling). Independently curated. |
| Format | Python SDK + REST service + optional Docker inbox |
| Requirements | Python 3.12; your TypeSafe key for `JevEngine` (no Torch needed); Node.js 22.13+ for the local demo UI; Laya weights for the local engine. |
| License | [Apache-2.0](https://github.com/Mike-Animal-Counseling/laya-jev-lab/blob/6554a6e95e28add587b7111b444e8462808516df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Classify tickets into a shared rubric from an existing helpdesk via REST.
- Compare hosted Jev with a local Laya model on the same tickets.
- Mismatch: SDK is not on PyPI; install from a checkout. The helpdesk keeps conversations and actions.

## How it works

`JevEngine.classify` sends the ticket to `https://api.typesafe.ai/v1/systemone` through a transport that keeps credentials out of the local backend; `LayaEngine` runs the reviewed V5 weights locally. Jev integration: [`ticket_engine/jev.py`](https://github.com/Mike-Animal-Counseling/laya-jev-lab/blob/6554a6e95e28add587b7111b444e8462808516df/ticket_engine/jev.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Mike-Animal-Counseling/laya-jev-lab.git
cd laya-jev-lab
python -m pip install .
# then: from ticket_engine import JevEngine
```

## Limits and data handling

Ticket text goes to TypeSafe with JevEngine; Laya runs locally. Optional Kaggle training uses your own account. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 6554a6e95e28](https://github.com/Mike-Animal-Counseling/laya-jev-lab/tree/6554a6e95e28add587b7111b444e8462808516df). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
