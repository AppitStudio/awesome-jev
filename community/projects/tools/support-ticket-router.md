# Support Ticket Router

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

FastAPI service that asks Jev three questions per support ticket in one call (team Choice, urgency Score, churn-risk Noul) and routes by expected cost of a mistake — auto, quick review or human; dashboard, review queue, offline fake backend and a Banking77 calibration benchmark of Jev vs three LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/khaledjamal/support-ticket-router) |
| Maintainer | [khaledjamal](https://github.com/khaledjamal). Independently curated. |
| Format | Python service (uv or Docker) with web dashboard, review queue and API docs |
| Requirements | uv (or Docker); none for the default offline `fake` backend; `TRIAGE_BACKEND=jev` + `TYPESAFE_API_KEY` (TypeSafe or OpenRouter) for Jev, or a laya-serve URL. |
| License | [MIT](https://github.com/khaledjamal/support-ticket-router/blob/e0831fc12abaf918bc7df8fab37165f7098dd3fd/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Assign tickets to team queues while keeping uncertain or expensive-mistake cases for review.
- Replay stored answers under cost vs threshold routing without new Jev calls (`triage-policies`).
- Mismatch: benchmark numbers are the maintainer's (462 Banking77 questions).

## How it works

[`questions.py`](https://github.com/khaledjamal/support-ticket-router/blob/e0831fc12abaf918bc7df8fab37165f7098dd3fd/src/triage/questions.py) defines the three questions; [`decisions/backends.py`](https://github.com/khaledjamal/support-ticket-router/blob/e0831fc12abaf918bc7df8fab37165f7098dd3fd/src/triage/decisions/backends.py) calls Jev, Laya or the fake; [`decisions/policy.py`](https://github.com/khaledjamal/support-ticket-router/blob/e0831fc12abaf918bc7df8fab37165f7098dd3fd/src/triage/decisions/policy.py) multiplies mistake probabilities by configured costs to pick auto / review / human. Benchmark report: [`results/benchmark/report.md`](https://github.com/khaledjamal/support-ticket-router/blob/e0831fc12abaf918bc7df8fab37165f7098dd3fd/results/benchmark/report.md).

## Get started

Run with the offline backend, then switch to Jev (README *Quick start*):

```sh
git clone https://github.com/khaledjamal/support-ticket-router.git && cd support-ticket-router
uv sync
uv run triage-seed
uv run uvicorn triage.main:create_app --factory --reload   # http://localhost:8000
# for Jev: TRIAGE_BACKEND=jev TYPESAFE_API_KEY=...
```

With the Jev backend each ticket is one request billed to your TypeSafe/OpenRouter key; the maintainer's benchmark cost $0.07 for Jev on 462 questions.

## Examples and demos

- README dashboard screenshot (16 sample tickets) and *Benchmark: can the confidence be trusted*.

## Limits and data handling

Ticket text goes to TypeSafe/OpenRouter with the Jev backend. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit e0831fc12aba](https://github.com/khaledjamal/support-ticket-router/tree/e0831fc12abaf918bc7df8fab37165f7098dd3fd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
