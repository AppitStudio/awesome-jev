# Jev Agent Builder

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-file visual builder for Jev requests: compose Choice, Score and Noul questions with `{{parameters}}`, validate against documented limits, and export the exact `/v1/systemone` JSON, cURL, a TypeScript function or a reusable agent definition.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enzotripoli/jev-agent-builder) |
| Maintainer | [enzotripoli](https://github.com/enzotripoli). Independently curated. |
| Format | Static web page (one `index.html`; hosted on GitHub Pages) |
| Requirements | A modern browser. A TypeSafe account only to run the exported request or open it in the TypeSafe Playground. |
| License | [MIT](https://github.com/enzotripoli/jev-agent-builder/blob/6d2e7beac239431ec62bb657e756685671d080df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/TripoliEnzo/status/2110809788846313880)). |
| Jev evidence | [`index.html`](https://github.com/enzotripoli/jev-agent-builder/blob/6d2e7beac239431ec62bb657e756685671d080df/index.html) at the pinned commit. |

## When to use

- Draft and validate a Jev request (duplicate ids, unused parameters, context limits) before writing integration code.
- Hand teammates a reusable agent definition with placeholders kept.
- Mismatch: builds requests only; it never calls Jev itself.

## How it works

Everything runs in the browser: the form is turned into the request body live, validated against the API limits (up to 255 Choice options, 2-10 Score levels), drafts stay in local storage, and a link opens the request in the official TypeSafe Playground. Integration evidence: [`index.html`](https://github.com/enzotripoli/jev-agent-builder/blob/6d2e7beac239431ec62bb657e756685671d080df/index.html).

## Get started

From the upstream README (not run on the review host):

```sh
# Hosted: https://enzotripoli.github.io/jev-agent-builder/
git clone https://github.com/enzotripoli/jev-agent-builder.git && open jev-agent-builder/index.html
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live page: [enzotripoli.github.io/jev-agent-builder/](https://enzotripoli.github.io/jev-agent-builder/)
- Seven starter examples (support triage, moderation, lead qualification and more) in the page.

## Limits and data handling

The page sends nothing; requests you export and run go to TypeSafe on your own key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 6d2e7beac239](https://github.com/enzotripoli/jev-agent-builder/tree/6d2e7beac239431ec62bb657e756685671d080df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
