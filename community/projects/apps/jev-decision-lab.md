# Jev Decision Lab

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser workbench for designing typed Jev questions from sample situations, then trying them in the TypeSafe Jev Playground.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nwadmark/jev-decision-lab) |
| Tags | `Open source` · `Free` |
| Product homepage | [Live workbench](https://nwadmark.github.io/jev-decision-lab/) — static site; no repo setup required. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-30**. Workbench itself is free static content. Copying examples into the TypeSafe Playground uses your TypeSafe account/key and may incur charges. Live Playground runs not executed on the review host. |
| Jev evidence | Inspected [`index.html`](https://github.com/nwadmark/jev-decision-lab/blob/7a9b59742c08bb059704fdc6eb1632f545841973/index.html) / [`app.js`](https://github.com/nwadmark/jev-decision-lab/blob/7a9b59742c08bb059704fdc6eb1632f545841973/app.js): workbench copies typed questions into the [TypeSafe Jev Playground](https://console.typesafe.ai/playground). Live Playground runs not executed on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Playground/TypeSafe calls not run on the review host. |
| Maintainer | [nwadmark](https://github.com/nwadmark). Independently curated. |
| Format | Static web workbench (GitHub Pages) + MIT source. |
| Platform and availability | Browser. Try [nwadmark.github.io/jev-decision-lab](https://nwadmark.github.io/jev-decision-lab/). |
| Jev's role | Lab prepares typed questions; the TypeSafe Playground runs Jev. Code owns examples, copy helpers, and UI. |
| Requirements | Browser. Optional TypeSafe account to run copied examples in the Playground. |
| License | [MIT](https://github.com/nwadmark/jev-decision-lab/blob/7a9b59742c08bb059704fdc6eb1632f545841973/LICENSE). |

## When to use

Use it when teaching or drafting System One questions before wiring an app. Prefer the Playground alone when you already have questions; prefer SDKs when you need API integration.

## How it works

Pick an example situation, copy State and Questions into the TypeSafe Playground, run, then edit facts to compare. Includes customer-feedback triage/theme examples.

## Get started

```sh
# Hosted:
# https://nwadmark.github.io/jev-decision-lab/

git clone https://github.com/nwadmark/jev-decision-lab.git
cd jev-decision-lab
git checkout 7a9b59742c08bb059704fdc6eb1632f545841973
```

## Examples and demos

- Live workbench: [nwadmark.github.io/jev-decision-lab](https://nwadmark.github.io/jev-decision-lab/).
- Upstream links the TypeSafe Playground for execution.

## Limits and data handling

Workbench is static. Running examples in the Playground sends state/questions to TypeSafe under your account. Catalog checks did not execute Playground runs.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 7a9b597](https://github.com/nwadmark/jev-decision-lab/tree/7a9b59742c08bb059704fdc6eb1632f545841973). AI-assisted README and license inspection; live Playground not executed.
