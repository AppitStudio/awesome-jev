# Jev会計 (jev-kaikei-free)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local Japanese bookkeeping tool (playful "demon ledger" UI) that shows receipts to Jev, which picks the account, consumption-tax class and whether it is a private expense; confident results become journal entries and the rest drop into a human review queue, exportable as CSV.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/USHIKUNDESUYO/jev-kaikei-free) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/USHIKUNDESUYO/jev-kaikei-free#readme) |
| Pricing and access | Free MIT source; Python standard library only. A `--mock` mode needs no key; live mode needs your own TypeSafe key (billed by TypeSafe; on-screen cost is an estimate with no spending cap). Checked 2026-10-12. |
| Jev evidence | [`jev_kaikei/jev_client.py`](https://github.com/USHIKUNDESUYO/jev-kaikei-free/blob/e052dff714b2d60fd4d6262da3c6908917c0c767/jev_kaikei/jev_client.py) minimal client that POSTs receipts and typed questions to `https://api.typesafe.ai/v1/systemone` with your `TYPESAFE_API_KEY`. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Not commercial. Listing is not an endorsement; journal entries are drafts, not accounting or tax advice. App not run on the review host. |
| Maintainer | [Ushio Hoshino (USHIKUNDESUYO)](https://github.com/USHIKUNDESUYO). Independently curated. |
| Format | Local Python web app (browser UI at 127.0.0.1:8765) |
| Platform and availability | Any OS with Python 3.10+; free preview / prototype release (Japanese UI). |
| Jev's role | Core in live mode: Jev chooses account, tax class and private-use flag with confidence; code applies the threshold, routes low-confidence items to review and builds CSV journals. Mock mode uses local keyword rules instead. |
| Requirements | Python 3.10+ (no third-party packages); optional `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/USHIKUNDESUYO/jev-kaikei-free/blob/e052dff714b2d60fd4d6262da3c6908917c0c767/LICENSE). |

## When to use

- Draft journal entries from receipt CSV/JSON with a human-review queue for uncertain items.
- Demo confidence-thresholded routing without a key in mock mode.
- Mismatch: Japanese accounting and UI; outputs are drafts that need professional review.

## How it works

Receipts are loaded from CSV/JSON; each is judged by Jev; items above the confidence threshold are auto-journaled and the rest go to the review screen where you fix debit/credit before export.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/USHIKUNDESUYO/jev-kaikei-free.git
cd jev-kaikei-free
python -m jev_kaikei --mock --no-browser
# open http://127.0.0.1:8765/
```

## Limits and data handling

Live mode sends receipt contents to TypeSafe; check you may share them. Data stays local otherwise. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit e052dff714b2](https://github.com/USHIKUNDESUYO/jev-kaikei-free/tree/e052dff714b2d60fd4d6262da3c6908917c0c767). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
