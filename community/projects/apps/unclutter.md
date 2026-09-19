# Unclutter

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

A browser extension that uses Jev to classify page clutter and saves reversible hiding rules for similar pages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kitze/unclutter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/kitze/unclutter#unclutter) |
| Pricing and access | [Source installation](https://github.com/kitze/unclutter#install-from-source) has no app purchase fee. Bring a TypeSafe or Vercel AI Gateway key with Jev access; provider charges apply. Reviewed 2026-09-19. |
| Jev evidence | [Request construction and answer validation](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/lib/jev.ts) classify candidate page elements into keep, ad, promotion, newsletter, social, cookie or uncertain. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. Source inspected; installation and live browsing were not tested. |
| Maintainer | [Kitze](https://github.com/kitze) |
| Format | TypeScript / WXT browser extension, version 0.3.0 |
| Platform and availability | Source-built Chrome/Chromium extension; Firefox 140+ temporary add-on. No Safari packaging. Store distribution was not verified. |
| Jev's role | Selects which locally extracted candidate elements can be hidden; code generates and validates selectors, caches rules and restores the page. |
| Requirements | Bun, Node.js 22.12+, supported browser, provider account/key. |
| License | [MIT](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/LICENSE) |

## When to use

Use it to hide recurring advertising, promotional overlays or newsletter invitations,
then reuse those choices on pages with a similar structure. The popup lets you pause a
page type, keep individual elements visible, re-analyze, or forget saved rules.
Cookie notices can be hidden visually, but this neither rejects tracking nor records a
consent choice. Pause the extension when you need those controls.

## How it works

The [DOM module](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/lib/dom.ts) collects up to
60 candidates using structural signals and bounded text. It constructs selectors locally
and excludes recognized main content, navigation, forms and sensitive controls.
Jev supplies typed Choice answers; it does not generate selectors or executable code.
The direct backend calls TypeSafe `/v1/systemone` with `jev-latest`; the Vercel backend
uses evaluation-model v4 with `typesafe-ai/jev`.

`keep` and `uncertain` remain visible. If supplied, selected-choice probability and
confidence must each reach `0.9`; **these fields are optional**, so a valid removable
choice with neither field can still produce a rule. Invalid or incomplete responses
reject the analysis. These cutoffs are operational policy, not validated accuracy.

The [background worker](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/entrypoints/background.ts)
saves rules by origin, route family and inferred template. It discards results after
navigation or concurrent rule changes and preserves existing rules on failure. Cached
rules are applied locally, with reversible styles rather than deleting nodes.

## Get started

From a source checkout, follow the [upstream setup](https://github.com/kitze/unclutter#install-from-source):

```sh
git clone https://github.com/kitze/unclutter.git
cd unclutter
bun install --frozen-lockfile
bun run build
```

In your Chromium browser's extensions page, enable Developer mode and load unpacked
`.output/chrome-mv3`. Refresh existing website tabs, pin the extension, and open its popup.
Under **Connection**, select TypeSafe or Vercel AI Gateway and save the corresponding key.
Keep **Manual**, the default, and click **Analyze page** on a suitable nonsensitive page.
This live action sends element descriptions to the selected provider and can incur charges.
Review **Hidden elements**; uncheck rules to restore content or use **Pause**.

Firefox uses `bun run build:firefox` and **Load Temporary Add-on** at
`about:debugging#/runtime/this-firefox`, selecting `.output/firefox-mv2/manifest.json`.
Temporary installations disappear on restart; permanent Firefox distribution needs signing.

## Examples and demos

No separate hosted demo was established. The
[behavior guide](https://github.com/kitze/unclutter#behavior) documents the popup workflow;
[synthetic tests](https://github.com/kitze/unclutter/tree/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/tests) illustrate article
route reuse, protected elements, reversible hiding, consent overlays, provider requests,
and malformed answers. `bun run check` runs type checks, lint, formatting and tests.
The optional smoke script contacts a provider and is separate from these offline checks.

## Limits and data handling

The extension requests HTTP(S) host access to apply saved rules on future visits.
Keys and profiles use local extension storage, without encryption or browser sync.
One key is stored: changing provider immediately reuses that key unless replaced.
Background code owns provider requests; content scripts do not receive the key.

Requests contain bounded candidate descriptions and short snippets, with email-like and
long numeric strings redacted. They exclude full URLs, form values and raw HTML, but
redaction does not guarantee anonymity. Saved profile metadata includes origin and route
information locally. Analyze only pages whose snippets may be sent to the provider.

Optional **On page visit** automatically analyzes unseen templates and can incur charges;
manual mode avoids those automatic model requests. Failed automatic attempts are persisted
and require an explicit retry. Cached rules keep working after removal of the API key.

Template recognition and protected-element checks are heuristics. Site changes can need
manual re-analysis; mismatched templates can hide unintended content. Shadow DOM and
cross-origin iframe contents are not traversed, though identified iframe containers can
be hidden. Browser-internal pages, stores, PDFs and file URLs are unsupported. Hiding ads
does not block their network activity, and nonstandard modal scroll locks may remain.

## Review and maintenance

Reviewed **2026-09-19** at
[`9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6`](https://github.com/kitze/unclutter/tree/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6).
Inspected README/setup, MIT license, package scripts, manifest permissions, provider and
answer handling, DOM extraction/protection, template keys, background storage/actions,
content lifecycle, popup controls and test definitions. This was a source review: no
installation, build, test execution, live provider request or browser action was performed.
