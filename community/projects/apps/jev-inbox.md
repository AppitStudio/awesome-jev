# Jev Inbox

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that reorders the Gmail message list: unread first, critical on top (TypeSafe Jev critical/urgency + your label chips), without reading bodies. Distinct from [Jev Inbox Queue](jev-inbox-queue.md) (local IMAP/CLI queue app).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iamomiid/jev-inbox) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/iamomiid/jev-inbox#readme) |
| Pricing and access | [Build and load unpacked](https://github.com/iamomiid/jev-inbox#install-from-source) (`npm run build` → `dist/`). No app purchase fee. Bring a TypeSafe or Vercel AI Gateway key. Inference can incur charges. Reviewed 2026-09-23. |
| Jev evidence | [`src/jev.ts`](https://github.com/iamomiid/jev-inbox/blob/2ad5aaa745c2f85b2c0725590c0e9fdfbe5dd3b7/src/jev.ts) uses Vercel AI SDK `experimental_evaluate` with `createTypeSafeAi().evaluationModel('jev-latest')` or Gateway `typesafe-ai/jev`: boolean `critical`, score `urgency`, plus one boolean per user label. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, PRIVACY, `src/jev.ts`, `src/content.ts`). Chrome install and live Gmail/Jev were **not** tested on the review host. Unofficial; not affiliated with Google, TypeSafe, or Vercel. |
| Maintainer | [iamomiid](https://github.com/iamomiid). |
| Format | Manifest V3 Chromium extension **jev-inbox 0.1.0** (TypeScript build to `dist/`). |
| Platform and availability | Chrome Developer mode → Load unpacked on `dist/`. Source-build only (no store listing verified here). |
| Jev's role | Classifies unread list-row metadata into criticality, urgency, and label chips; extension code reorders the DOM list and caches results. Never marks, archives, deletes, or opens mail. |
| Requirements | Chromium; TypeSafe or Vercel AI Gateway API key in the popup (`chrome.storage.local`). |
| License | [MIT](https://github.com/iamomiid/jev-inbox/blob/2ad5aaa745c2f85b2c0725590c0e9fdfbe5dd3b7/LICENSE). |

## When to use

Use it when you want Gmail’s existing list reordered by Jev judgments over **visible row metadata**, with your own label descriptions as criteria. Prefer [Jev Inbox Queue](jev-inbox-queue.md) for a local queue/CLI over IMAP demos.

## How it works

The content script reads sender, subject, snippet, and date for unread rows (no bodies/attachments). Batches of 20 go to the service worker, which asks Jev critical/urgency/label questions. Critical rows (above your sensitivity) sort first by urgency, then remaining unread, then read. Cache in `chrome.storage.local` (bounded). Gmail markup changes can break selectors (`docs/gmail-dom.md`).

## Get started

```sh
git clone https://github.com/iamomiid/jev-inbox.git
cd jev-inbox
git checkout 2ad5aaa745c2f85b2c0725590c0e9fdfbe5dd3b7
npm install
npm run build
# chrome://extensions → Load unpacked → dist/
```

Live classification sends row metadata + label names/descriptions to the provider you pick and can incur charges.

## Examples and demos

- Screenshots under `docs/images/`.
- `dev/demo.html` after build: Gmail-like list with stubbed `chrome` and canned classifications (no network).

## Limits and data handling

Only list metadata and label criteria leave the browser. Keys stay in extension storage. One tab does the work; keyboard `j`/`k` follow Gmail’s native order after reorder. This listing did not load Chrome or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 2ad5aaa](https://github.com/iamomiid/jev-inbox/tree/2ad5aaa745c2f85b2c0725590c0e9fdfbe5dd3b7) (**0.1.0**, MIT). AI-assisted source review of README, PRIVACY, LICENSE, `src/jev.ts`. No live TypeSafe/Vercel spend.

Related: [Jev Inbox Queue](jev-inbox-queue.md), [Tab Bouncer](tab-bouncer.md).
