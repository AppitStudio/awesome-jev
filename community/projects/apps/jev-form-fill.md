# Jev Form Fill

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that matches clipboard/source text to form fields with TypeSafe Jev, lets you review proposals, fill selected fields in page order, read back values, and undo—you submit the form yourself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/takasek/jev-form-fill) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/takasek/jev-form-fill#readme) |
| Pricing and access | Free source build; BYOK TypeSafe. Checked 2026-10-04. |
| Jev evidence | [Upstream README](https://github.com/takasek/jev-form-fill/blob/9faa3158a29100a987786167875ea61a14a9bcff/README.md) documents Create proposals with TypeSafe (jev-latest / api.typesafe.ai/v1/systemone) and privacy boundaries. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Preview v0.1.5. Creating proposals sends source text and field metadata to TypeSafe (not existing values/URL/full body). Live install/UI paths not run on the Linux review host. |
| Maintainer | [takasek](https://github.com/takasek). Independently curated. |
| Format | Chrome extension (MIT, preview v0.1.5) |
| Platform and availability | Chrome extension (Developer mode / load unpacked) |
| Jev's role | Jev proposes field values from source text + field metadata via System One; UI owns review, apply, readback, and undo. Exact quoted values—no paraphrasing. |
| Requirements | Chrome 116+; TypeSafe API key; clipboard/source text |
| License | [MIT](https://github.com/takasek/jev-form-fill/blob/9faa3158a29100a987786167875ea61a14a9bcff/LICENSE). Provider usage may incur charges when live. |

## When to use

Use to fill Chrome forms from notes with human review. Prefer other browser tools when you need full agent computer-use loops.

## How it works

Chrome extension that matches clipboard/source text to form fields with TypeSafe Jev, lets you review proposals, fill selected fields in page order, read back values, and undo—you submit the form yourself. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/takasek/jev-form-fill.git
cd jev-form-fill
git checkout 9faa3158a29100a987786167875ea61a14a9bcff
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 9faa3158a291](https://github.com/takasek/jev-form-fill/tree/9faa3158a29100a987786167875ea61a14a9bcff). AI-assisted README and license inspection; live paths not executed.
