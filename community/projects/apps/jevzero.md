# JevZero

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local Gmail inbox helper: TypeSafe Jev classifies messages into categories/priorities and signals, you review exact proposed Gmail labels, then apply with verified receipts and undo. Runs on your computer with encrypted local storage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jayozer/jevzero) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/jayozer/jevzero#readme) — local FastAPI + Next.js app; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Requires your TypeSafe API key and a Google OAuth client (loopback callback). TypeSafe inference and Google API quotas are billed separately. Demo mode works without keys. |
| Jev evidence | Inspected [`jevzero/classifier.py`](https://github.com/jayozer/jevzero/blob/601228d24a8a12eb81a9182c150d3f6e9233cc74/jevzero/classifier.py): one `POST https://api.typesafe.ai/v1/systemone` per message with Choice (category/priority), Score (importance), and Noul signals; labels proposed only after review. Live Gmail/TypeSafe not run. |
| Disclosure | Free source access does not include Google or TypeSafe usage. AI-assisted, independently curated listing; no commercial relationship declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [jayozer](https://github.com/jayozer). |
| Format | Python package **`jevzero` 0.1.0** (`uv run jevzero`) launching local API + Next.js UI. |
| Platform and availability | Source build; default [http://127.0.0.1:3000](http://127.0.0.1:3000). Credentials and mailbox data under `.jevzero-local/` (gitignored). |
| Jev's role | Classifies each message; application code owns review, Gmail label mutations, receipts, and undo. Demo uses authored samples without API calls. |
| Requirements | Python ≥ 3.12, [uv](https://docs.astral.sh/uv/), Node.js 22+ for the frontend build, Google OAuth client with callback `http://127.0.0.1:3000/oauth/callback`, `TYPESAFE_API_KEY` for live classify. |
| License | [MIT](https://github.com/jayozer/jevzero/blob/601228d24a8a12eb81a9182c150d3f6e9233cc74/LICENSE). |

## When to use

Use it when you want localhost Gmail triage with **explicit label preview → apply → undo**, not a read-only tray. Prefer [Jevmail](jevmail.md) for Gateway-hosted read-only trays; prefer [Jev Mail Classifier](jev-mail-classifier.md) for IMAP/TUI automation.

## How it works

[`classifier.py`](https://github.com/jayozer/jevzero/blob/601228d24a8a12eb81a9182c150d3f6e9233cc74/jevzero/classifier.py) builds one bounded System One request per message (category, priority, importance, reply/risk/newsletter/receipt signals, optional custom rules/categories). [`service.py`](https://github.com/jayozer/jevzero/blob/601228d24a8a12eb81a9182c150d3f6e9233cc74/jevzero/service.py) journals apply/undo and verifies label receipts against Gmail. Email body text is treated as untrusted evidence (guard instructions in the request).

## Get started

```sh
git clone https://github.com/jayozer/jevzero.git
cd jevzero
git checkout 601228d24a8a12eb81a9182c150d3f6e9233cc74
uv sync --group dev
uv run pytest -q
uv run jevzero
# Open http://127.0.0.1:3000 — demo without keys, or Connect Gmail + TypeSafe key
```

Live classify sends sender/subject/date and up to ~12k body characters to TypeSafe and can incur charges. Apply mutates Gmail labels only after review.

## Examples and demos

- Upstream demo mode with sample classifications (no API).
- Docs: `docs/local.md`, `docs/capabilities.md`, `docs/verification.md` (author-run launcher checks; not re-run as a full UI smoke here beyond pytest).

## Limits and data handling

Mail-derived text leaves the host on live classify. OAuth tokens and encrypted local store stay on the machine. Treat apply/undo as privileged mailbox mutations. Classification quality is not measured here. This listing did not connect a real Google account or call TypeSafe live.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 601228d](https://github.com/jayozer/jevzero/tree/601228d24a8a12eb81a9182c150d3f6e9233cc74): `jevzero` **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `classifier.py`, `service.py`, credentials/local launcher. Offline `uv run pytest`: **62 passed**. No live Gmail or TypeSafe calls. Frontend domain tests were not executed on this pass (Python suite only).

Related: [Jevmail](jevmail.md), [Jev Mail Classifier](jev-mail-classifier.md).
