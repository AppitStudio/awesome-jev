# jevbrief

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Playwright briefing layer for TypeSafe Jev: filters page elements with drop reasons, asks one Choice for the next click, and writes a local trace viewer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Parthkomalwad/jevbrief) |
| Maintainer | [Parthkomalwad](https://github.com/Parthkomalwad). Independently curated. Not an endorsement. |
| Format | Python package **jevbrief** (PyPI) + CLI. |
| Requirements | Python; Playwright Chromium; `TYPESAFE_API_KEY` for live asks (`inspect` needs no key). |
| License | [MIT](https://github.com/Parthkomalwad/jevbrief/blob/2819d621945f665e045942128f1db8530062f389/LICENSE). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live Jev **not** run. Token-savings claim is upstream benchmark, not re-measured. |

## When to use

Use it when a browser agent should send a smaller, explained element set to Jev for next-click choice with auditable drops. Prefer full CUA frameworks when you need multi-channel computer use.

## How it works

`Brief` extracts elements, drops hidden/disabled/duplicates/off-goal with reason codes, budgets state, then `next_click()` asks Jev one Choice. JSONL traces open in a local viewer showing kept vs dropped elements.

## Get started

```sh
pip install jevbrief && playwright install chromium
jevbrief inspect https://news.ycombinator.com --goal "log in"   # no key
# TYPESAFE_API_KEY=... jevbrief ask URL --goal "..." --view
```

Pin: [commit 2819d62](https://github.com/Parthkomalwad/jevbrief/tree/2819d621945f665e045942128f1db8530062f389).

## Examples and demos

- Upstream demo.gif and Async/Sync Playwright snippets.

## Limits and data handling

Page URLs/element labels go to TypeSafe on ask. Filter-only mode can omit the API. Accuracy/token figures are author-reported.

## Review and maintenance

Reviewed **2026-09-23** at [commit 2819d62](https://github.com/Parthkomalwad/jevbrief/tree/2819d621945f665e045942128f1db8530062f389) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [cua-jev-use](cua-jev-use.md), [Footwork](footwork.md).
