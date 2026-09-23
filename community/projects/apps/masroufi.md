# Masroufi

[All projects](../README.md) · [Web apps](README.md#web-apps)

Gaza household expense tracker: import a bank-statement export, let TypeSafe Jev classify notes with confidence, and review low-confidence rows.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wafaa-alhayek/masroufi) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/wafaa-alhayek/masroufi#readme) — local FastAPI app; no separate commercial site. |
| Pricing and access | Public source has no app purchase fee, checked **2026-09-24**. Live Jev path needs `TYPESAFE_API_KEY` (`CLASSIFIER_BACKEND=jev`). Mock backend available. **No LICENSE file** at tip—not open source. |
| Jev evidence | Inspected [`app/classify/jev.py`](https://github.com/wafaa-alhayek/masroufi/blob/00fea30b2463c0f1990132c64f3b5d1dc21245df/app/classify/jev.py): httpx POST `/v1/systemone` with parallel category / merchant / reducibility questions. Live classify **not** run. |
| Disclosure | Source available without a declared open-source license. AI-assisted, independently curated; no commercial relationship declared. Listing is not an endorsement. |
| Maintainer | [wafaa-alhayek](https://github.com/wafaa-alhayek). |
| Format | Python FastAPI app (`masroufi`). |
| Platform and availability | Source build: venv + `pip install -r requirements.txt` + `uvicorn app.main:app --reload`. Phase A: import, categorise, review, repeat patterns. |
| Jev's role | Typed classification of redacted statement notes with confidence; human review for unsure rows. Mock classifier available without keys. |
| Requirements | Python 3.x; optional `TYPESAFE_API_KEY` for live Jev. |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. |

## When to use

Use it when statement-note categorisation needs calibrated confidence and human review, especially where open-banking APIs are unavailable. Prefer generic finance apps when you need hosted multi-bank sync.

## How it works

Imports redact and tidy notes, then `JevClassifier` batches three System One questions per unique note. Low-confidence rows surface for household review; pattern detection builds on accepted categories.

## Get started

```sh
git clone https://github.com/wafaa-alhayek/masroufi.git
cd masroufi
git checkout 00fea30b2463c0f1990132c64f3b5d1dc21245df
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
# mock: CLASSIFIER_BACKEND=mock
# live: CLASSIFIER_BACKEND=jev TYPESAFE_API_KEY=...
uvicorn app.main:app --reload
```

## Examples and demos

- README pipeline examples (redact → translate → tidy → classify).
- Tests under `tests/` (not executed on the review host).

## Limits and data handling

Statement notes and categories go to TypeSafe when `CLASSIFIER_BACKEND=jev`. Designed around Bank of Palestine-style exports; not a general open-banking client. No LICENSE file.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 00fea30](https://github.com/wafaa-alhayek/masroufi/tree/00fea30b2463c0f1990132c64f3b5d1dc21245df). AI-assisted source review of README and `app/classify/jev.py`. No live TypeSafe spend.

Related: [Jev Inbox](jev-inbox.md), [Jev Mail Classifier](jev-mail-classifier.md).
