# AI, SI, or Whatever

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that lets TypeSafe Jev choose AI / SI / alternating / custom webpage terminology per page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SjJ1017/ai-si-or-whatever) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/SjJ1017/ai-si-or-whatever#readme](https://github.com/SjJ1017/ai-si-or-whatever#readme) |
| Pricing and access | Free MIT source; Jev mode uses your TypeSafe key. Checked 2026-10-13. |
| Jev evidence | [`jev.js`](https://github.com/SjJ1017/ai-si-or-whatever/blob/084193ff31af03d84111e0bf77f2b8413137ad94/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [SjJ1017](https://github.com/SjJ1017). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Chrome (load unpacked / source) |
| Jev's role | Optional: Jev picks terminology mode from short candidate snippets. |
| Requirements | Chrome; TypeSafe API key for Jev mode. |
| License | [MIT](https://github.com/SjJ1017/ai-si-or-whatever/blob/084193ff31af03d84111e0bf77f2b8413137ad94/LICENSE) |

## When to use

- Prefer consistent AI/SI wording on pages with optional Jev arbitration.
- Mismatch: Jev is optional; default modes work without a key.

## How it works

When enabled, short candidates are scored by Jev and the chosen mode rewrites labels. (Summarized from the upstream [README](https://github.com/SjJ1017/ai-si-or-whatever/blob/084193ff31af03d84111e0bf77f2b8413137ad94/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): load the extension unpacked, optionally paste a TypeSafe key under Jev settings.

## Limits and data handling

Candidate snippets may go to TypeSafe when Jev is enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 084193ff31af](https://github.com/SjJ1017/ai-si-or-whatever/tree/084193ff31af03d84111e0bf77f2b8413137ad94). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
