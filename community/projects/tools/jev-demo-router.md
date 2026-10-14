# Jev Support Ticket Router

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Support-ticket routing demo (English/Chinese) that asks Jev department, urgency and tone in one call and sends low-confidence tickets to a human queue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Zafer-Liu/jev-demo-router) |
| Maintainer | [Zafer-Liu](https://github.com/Zafer-Liu). Independently curated. |
| Format | Flask demo (Python) |
| Requirements | Python 3.10+, flask, typesafe-sdk, TypeSafe API key. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/0xkurt/status/2109991254700224661)). |
| Jev evidence | [`router.py`](https://github.com/Zafer-Liu/jev-demo-router/blob/52515898362e7ce2c06d0561855c4d6f460bee47/router.py) at the pinned commit. |

## When to use

- Try the decide-vs-write split on support tickets with synthetic data.
- Mismatch: no LICENSE file; sample tickets are synthetic and the 0.75 cutoff is a starting point.

## How it works

One Jev call answers department (Choice), urgent (Noul) and tone (Score); code dispatches when confidence ≥ 0.75 and otherwise escalates to a human queue. Integration evidence: [`router.py`](https://github.com/Zafer-Liu/jev-demo-router/blob/52515898362e7ce2c06d0561855c4d6f460bee47/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Zafer-Liu/jev-demo-router.git
cd jev-demo-router
pip install flask typesafe-sdk requests
cp .env.example .env   # set TYPESAFE_API_KEY
python app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Recorded run summary: `results/run.json` (upstream; not reproduced).
- Highlighted in an X post (linked in Disclosure).

## Limits and data handling

Ticket text goes to TypeSafe; API calls are billed.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 52515898362e](https://github.com/Zafer-Liu/jev-demo-router/tree/52515898362e7ce2c06d0561855c4d6f460bee47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
