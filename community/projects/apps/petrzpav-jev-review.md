# Jev Review (Gmail)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that grades Gmail compose/reply text with TypeSafe Jev on configurable criteria and tracks which questions from the other person's email remain unanswered.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/petrzpav/jev-review) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/petrzpav/jev-review#readme) |
| Pricing and access | Free source build (load unpacked); BYOK TypeSafe. Checked 2026-10-03. |
| Jev evidence | [Upstream README](https://github.com/petrzpav/jev-review/blob/dc1518816c37a060b03389e9d2a84551ce1b221a/README.md) documents live Gmail grading via TypeSafe Jev (spun out of omarchy-mail). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from NiazMorshed2007/jev-review (MCP rubric), devagrawal09/jev-review (JS/TS dashboard), fatwang2/jev-review-action, and RomanXSad/jev-review-gate. Live install/UI paths not run on the Linux review host. |
| Maintainer | [petrzpav](https://github.com/petrzpav). Independently curated. |
| Format | Chrome extension for Gmail compose grading (MIT) |
| Platform and availability | Chrome extension (Gmail web) |
| Jev's role | Jev grades draft text on criteria and estimates unanswered questions; the extension owns UI badges/cards and debounce. |
| Requirements | Chrome; TypeSafe API key; Gmail in browser |
| License | [MIT](https://github.com/petrzpav/jev-review/blob/dc1518816c37a060b03389e9d2a84551ce1b221a/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Chrome extension that grades Gmail compose/reply text with TypeSafe Jev on configurable criteria and tracks which questions from the other person's email remain unanswered. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/petrzpav/jev-review.git
cd jev-review
git checkout dc1518816c37a060b03389e9d2a84551ce1b221a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit dc1518816c37](https://github.com/petrzpav/jev-review/tree/dc1518816c37a060b03389e9d2a84551ce1b221a). AI-assisted README and license inspection; live paths not executed.
