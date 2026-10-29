# N+1 Bench (can Jev spot N+1 queries in Django REST endpoints just by reading the code?)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of 58 small Django REST Framework list endpoints, some with N+1 query problems and some that only look like it, with ground truth measured by serving each one at 5 and 10 rows. Jev and Claude Code (with a bundled audit skill) review the code without running it; the author reports Jev at about 91% accuracy for $0.03 across 174 checks versus Claude at 100% for $7.56–$14.95, and a CI check script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RoRep1ay/django-n-1-jev) |
| Maintainer | [RoRep1ay](https://github.com/RoRep1ay). Independently curated. |
| Format | Python benchmark harness |
| Requirements | Python; a TypeSafe API key for Jev runs; the `claude` CLI for the comparison. |
| License | [MIT](https://github.com/RoRep1ay/django-n-1-jev/blob/1189eeacca0d4607d762efb7d6de838996490b8d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/RoRep1ay/status/2115663369390927934)). |
| Jev evidence | [`harness/jev_check.py`](https://github.com/RoRep1ay/django-n-1-jev/blob/1189eeacca0d4607d762efb7d6de838996490b8d/harness/jev_check.py) at the pinned commit. |

## When to use

- Add a cheap N+1 pre-check to Django code review and know its error rate.
- Mismatch: small synthetic endpoints; results are the author's.

## How it works

`harness/jev_check.py` uses the official `typesafe_sdk` (`TypeSafeClient`, `Choice`) with `jev-latest` to classify each endpoint from its view, serializer and model code. Integration evidence: [`harness/jev_check.py`](https://github.com/RoRep1ay/django-n-1-jev/blob/1189eeacca0d4607d762efb7d6de838996490b8d/harness/jev_check.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/RoRep1ay/django-n-1-jev && cd django-n-1-jev
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
python -m harness.oracle   # measures every case, no key
python -m harness.run_benchmark --skip-skill --repeat 3   # Jev only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/RoRep1ay/django-n-1-jev#readme](https://github.com/RoRep1ay/django-n-1-jev#readme)

## Limits and data handling

Endpoint code goes to TypeSafe (and to Claude for the comparison).

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 1189eeacca0d](https://github.com/RoRep1ay/django-n-1-jev/tree/1189eeacca0d4607d762efb7d6de838996490b8d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
