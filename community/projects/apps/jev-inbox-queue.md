# Jev Inbox Queue

[All projects](../README.md) · [Web apps](README.md#web-apps)

Turn an email inbox into a short action queue: TypeSafe Jev answers seven typed questions per thread; plain Python policy decides To do / Check / Filtered out.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tusharck/jev-inbox-queue) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/tusharck/jev-inbox-queue#readme) — local CLI/UI over a demo or IMAP inbox; no separate hosted product. |
| Pricing and access | MIT source; no app purchase fee, checked **2026-09-23**. Needs `TYPESAFE_API_KEY`. Optional Gmail IMAP app password for a real inbox. TypeSafe usage billed separately. |
| Jev evidence | Inspected [`inbox_queue/classify.py`](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/classify.py) (`AsyncTypeSafeClient.system_one`) and [`inbox_queue/questions.py`](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/questions.py); policy in [`inbox_queue/policy.py`](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/policy.py). Live IMAP/Jev not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; `uv sync`, demo UI, and live TypeSafe/IMAP were **not** executed here. Distinct from [Jevmail](jevmail.md) (Gmail Gateway triage product). |
| Maintainer | [tusharck](https://github.com/tusharck). |
| Format | Python package (`inbox_queue`) with demo data, evaluate CLI, and local queue UI. |
| Platform and availability | Python **3.10+**, [uv](https://docs.astral.sh/uv/). Source-build only. |
| Jev's role | Seven parallel typed questions per thread (three Noul, three Choice, one Score); application code owns queue thresholds and filters. Answers are cached on disk. |
| Requirements | `TYPESAFE_API_KEY`; optional `IMAP_USER` / app password and `MY_NAME` for Gmail. |
| License | [MIT](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/LICENSE). |

## When to use

Use it to **prototype inbox triage** where Jev only judges and code owns the queue rules. Prefer [Jevmail](jevmail.md) for a Gmail OAuth + Vercel AI Gateway productized triage UI.

## How it works

Each thread becomes System One state; Jev returns needs-action / waiting / promotional / kind / workflow / next-step / urgency in one request. [`policy.py`](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/policy.py) maps probabilities into queue buckets without new API calls when thresholds change.

## Get started

```sh
git clone https://github.com/tusharck/jev-inbox-queue.git
cd jev-inbox-queue
git checkout c5203bb06ae3446e757c312bb02a4cfea9d39fe0
uv sync
cp .env.example .env   # add TYPESAFE_API_KEY
# uv run python -m inbox_queue demo
# uv run python -m inbox_queue evaluate
```

Demo inbox is synthetic (`data/demo_inbox.json`). Live demo/evaluate not run here.

## Examples and demos

- Screenshots in upstream `docs/` (demo queue, real-inbox stats).
- Upstream reports labeled demo metrics; treat them as author-reported, not independently verified here.

## Limits and data handling

Thread text leaves the host on live Jev calls; IMAP credentials stay in `.env`. Cached answers live under `.cache/jev/`. This listing did not run the demo or call TypeSafe.

## Review and maintenance

Reviewed on **2026-09-23** at [commit c5203bb](https://github.com/tusharck/jev-inbox-queue/tree/c5203bb06ae3446e757c312bb02a4cfea9d39fe0) (MIT). AI-assisted review of README, LICENSE, classify/questions/policy. No live TypeSafe/IMAP.

Related: [Jevmail](jevmail.md), [Crush Monitor](crush-monitor.md).

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev use cases: nine patterns developers are building](../../knowledge-base/articles/jev-use-cases.md) — Independently suggested by JevList; not an endorsement by Matt Van Horn. Pattern 7: triage email by asking several typed questions per thread.
- [10 Jev project ideas with practical starting points](../../knowledge-base/articles/jev-project-ideas.md) — Independently suggested by JevList; not an endorsement by rody. Build 1: route email into a reviewable action queue.
<!-- knowledge:backlinks:end -->
