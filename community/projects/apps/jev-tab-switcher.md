# Jev Tab Switcher (Chrome extension where you type a vague phrase and Jev picks the open tab to jump to)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Press ⌘⇧K, type a vague phrase like "board slides", and Chrome jumps to the right tab: instant local matches appear first, and on Enter Jev chooses among up to 80 candidate tabs (with a `none` option); below 55% confidence you get a ranked list with probabilities instead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ido-foundation/jev-tab-switcher) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ido-foundation/jev-tab-switcher#readme) (source-built; no separate product site verified). |
| Pricing and access | Public source with no license file (all rights reserved by default); no purchase fee, OpenRouter usage on your key. Checked 2026-11-13. |
| Jev evidence | [`src/jev.js`](https://github.com/ido-foundation/jev-tab-switcher/blob/4d10c4b3b6ee3dce1dff59a600e6b9f1b1ba53f8/src/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ido-foundation](https://github.com/ido-foundation). Independently curated. |
| Format | Chrome MV3 extension loaded unpacked (JavaScript; no license file) |
| Platform and availability | Desktop Chrome (load unpacked); no Chrome Web Store listing verified |
| Jev's role | Jev chooses which open tab matches your phrase, or says none match. |
| Requirements | Desktop Chrome and an OpenRouter key with Jev access. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Find one tab among dozens by describing it loosely.
- Mismatch: if you cannot send tab titles and URLs to a provider.

## How it works

`src/jev.js` posts a `choice` question to OpenRouter's Decisions API (`https://openrouter.ai/api/alpha/decisions`); the model is configurable (`typesafe/jev-1.14`, `typesafe/jev-1.13` or `~typesafe/jev-latest`). `src/matcher.js` holds the unit-tested candidate selection and switch-or-ask rule. Without a key or on API errors it falls back to local matching. Integration evidence: [`src/jev.js`](https://github.com/ido-foundation/jev-tab-switcher/blob/4d10c4b3b6ee3dce1dff59a600e6b9f1b1ba53f8/src/jev.js).

## Get started

Load the folder unpacked, paste an OpenRouter key in the options page and test the connection.

```sh
# chrome://extensions → Developer mode → Load unpacked → jev-tab-switcher
# then press Cmd+Shift+K (Ctrl+Shift+K) and type a phrase
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ido-foundation/jev-tab-switcher/blob/4d10c4b3b6ee3dce1dff59a600e6b9f1b1ba53f8/README.md](https://github.com/ido-foundation/jev-tab-switcher/blob/4d10c4b3b6ee3dce1dff59a600e6b9f1b1ba53f8/README.md)

## Limits and data handling

Titles and host/path of open tabs (up to 80) go to OpenRouter on your key when you press Enter.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 4d10c4b3b6ee](https://github.com/ido-foundation/jev-tab-switcher/tree/4d10c4b3b6ee3dce1dff59a600e6b9f1b1ba53f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
