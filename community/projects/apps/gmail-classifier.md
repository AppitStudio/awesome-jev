# Gmail Classifier

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Local Gmail triage workbench: fetch headers/summaries, ask TypeSafe Jev for category and priority, preview a report, then apply reversible labels—plus phishing checks, unsubscribe analysis, filter generation, and an optional Chrome sidebar.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leomfu/gmail-classifier) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/leomfu/gmail-classifier#readme) — CLI + optional Chrome panel. |
| Pricing and access | MIT source; Google OAuth desktop client + `TYPESAFE_API_KEY`. No app purchase fee, checked **2026-09-24**. Google/TypeSafe billed separately (~$0.06/900 msgs per README). |
| Jev evidence | Inspected [`src/classify.py`](https://github.com/leomfu/gmail-classifier/blob/223856ff7680fd9e4a9659ca51f9cba189bb286f/src/classify.py): `AsyncTypeSafeClient` with Choice/Noul/Score batches. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Gmail/Jev not run. |
| Maintainer | [leomfu](https://github.com/leomfu). Independently curated. |
| Format | Python CLI (`uv`) + Chrome sidebar talking to local `server.py`. |
| Platform and availability | macOS/Linux/Windows for core scripts; launchd/notifications helpers are macOS-oriented. |
| Jev's role | Classifies each thread with parallel typed questions; code owns apply/undo and Gmail writes. |
| Requirements | Python via uv; `credentials.json` Gmail OAuth; TypeSafe key in `.env`. |
| License | [MIT](https://github.com/leomfu/gmail-classifier/blob/223856ff7680fd9e4a9659ca51f9cba189bb286f/LICENSE). |

## When to use

Use it for **batch Gmail labeling with preview/undo** and optional phishing/unsubscribe reports. Prefer [Inbox Triage](inbox-triage.md) for narrower label-only policy or [JevZero](jevzero.md) for interactive apply receipts.

## How it works

`fetch.py` pulls headers/summaries; `classify.py` redacts then batches Jev questions; `report.py` shows results; `apply.py` writes labels with `undo.py`. The Chrome panel calls local `server.py` for the same actions.

## Get started

```sh
git clone https://github.com/leomfu/gmail-classifier.git
cd gmail-classifier
git checkout 223856ff7680fd9e4a9659ca51f9cba189bb286f
uv sync
# place Google OAuth desktop JSON as credentials.json; set TYPESAFE_API_KEY in .env
uv run src/fetch.py --limit 20
uv run src/classify.py --limit 20
uv run src/report.py
# apply only after review: uv run src/apply.py
```

## Examples and demos

- README pipeline table and taxonomy (`taxonomy.yaml`).
- Chrome `extension/` folder for the sidebar.

## Limits and data handling

Subject/summary excerpts go to TypeSafe; tokens stay local. `gmail.modify` can add labels but README states no delete calls. Google Testing OAuth refresh may expire after seven days.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 223856f](https://github.com/leomfu/gmail-classifier/tree/223856ff7680fd9e4a9659ca51f9cba189bb286f). AI-assisted README + `src/classify.py` inspection. No live Gmail or TypeSafe spend.

Related: [Inbox Triage](inbox-triage.md), [JevZero](jevzero.md), [Jevmail](jevmail.md).
