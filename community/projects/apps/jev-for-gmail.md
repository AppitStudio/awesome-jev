# Jev for Gmail

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension that paints TypeSafe Jev priority-score badges on Gmail’s Primary inbox (last seven days)—with local redaction and a hard lock for patient-related mail—without changing labels or read state.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JeonKH81/jev-for-gmail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/JeonKH81/jev-for-gmail#readme) — unpacked extension; no separate commercial site. |
| Pricing and access | MIT source; load unpacked with your TypeSafe key in options (`chrome.storage.local`). No app purchase fee, checked **2026-09-24**. TypeSafe billed separately (~$0.0001/email per README). |
| Jev evidence | Inspected [`background.js`](https://github.com/JeonKH81/jev-for-gmail/blob/e62ea0102681ee46e231add73c7b0f9f4c27a4b9/background.js): Noul/Score/Choice questions and `callJev` to TypeSafe. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Chrome install and live Gmail/Jev not run. Not a medical device. |
| Maintainer | [JeonKH81](https://github.com/JeonKH81). Independently curated. |
| Format | Chrome MV3 extension (`content.js` + service worker). |
| Platform and availability | Chromium via Developer mode unpacked load. |
| Jev's role | Scores needs-action, urgency, importance, already-handled, and category; code computes the badge. Without a key badges do not score. |
| Requirements | Chromium; TypeSafe API key; Gmail Primary tab. |
| License | [MIT](https://github.com/JeonKH81/jev-for-gmail/blob/e62ea0102681ee46e231add73c7b0f9f4c27a4b9/LICENSE). |

## When to use

Use it to **triage Primary Gmail by calibrated priority** with patient-mail locking. Prefer [Jev Inbox](jev-inbox.md) for list reordering or [Inbox Triage](inbox-triage.md) for label writes.

## How it works

The content script reads list rows; the worker redacts PII, skips locked patient patterns, calls Jev with fixed questions, caches scores locally, and draws color badges. Gmail data is never modified.

## Get started

```sh
git clone https://github.com/JeonKH81/jev-for-gmail.git
cd jev-for-gmail
git checkout e62ea0102681ee46e231add73c7b0f9f4c27a4b9
# chrome://extensions → Developer mode → Load unpacked → this folder
# Options: paste TypeSafe key, role, self email; Test connection; refresh Gmail
```

## Examples and demos

- README demo screenshot (`docs/demo.png`).
- File map: `manifest.json`, `content.js`, `background.js`, `options.html`.

## Limits and data handling

Redacted subject/body excerpts (≤2500 chars) go to TypeSafe (US). Filters are imperfect—residual PII is possible. Primary tab + 7-day window only. Institutional privacy policy still applies.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit e62ea01](https://github.com/JeonKH81/jev-for-gmail/tree/e62ea0102681ee46e231add73c7b0f9f4c27a4b9). AI-assisted README + `background.js` inspection. No Chrome/Gmail/TypeSafe live run.

Related: [Jev Inbox](jev-inbox.md), [Inbox Triage](inbox-triage.md), [Jevmail](jevmail.md).
