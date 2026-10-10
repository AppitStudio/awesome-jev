# Discord Policy Checker

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Experimental Chrome extension that checks your outgoing Discord messages and edits against plain-language policies with TypeSafe Jev and holds violations before they send; an optional Active mode adds Gemini rewriting (via OpenRouter) with Jev checking each candidate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kennethwolters/discord-policy-checker) |
| Maintainer | [kennethwolters](https://github.com/kennethwolters). Independently curated. |
| Format | Chrome extension (build from source) |
| Requirements | Node.js 22.12+, desktop Chrome 120+; TypeSafe key (plus OpenRouter key for Active mode). |
| License | [MIT](https://github.com/kennethwolters/discord-policy-checker/blob/1086c1a2445a08b6d176d856a79706ae69f2cbc5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch messages that break your own or a server's rules before you hit Send.
- Mismatch: experimental and uncalibrated per the README; not a moderation or safety guarantee.

## How it works

On Send or Save, Jev estimates whether the draft violates your Global and Server policies; violations stay unsent and editable. (Summarized from the upstream [README](https://github.com/kennethwolters/discord-policy-checker/blob/1086c1a2445a08b6d176d856a79706ae69f2cbc5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `npm ci && npm run build`, then load `dist/` unpacked in Chrome and connect a TypeSafe key.

## Limits and data handling

Drafts, policies, and optional conversation context go to external providers; missing keys mean no checking. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 1086c1a2445a](https://github.com/kennethwolters/discord-policy-checker/tree/1086c1a2445a08b6d176d856a79706ae69f2cbc5). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
