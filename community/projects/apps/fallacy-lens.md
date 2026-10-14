# Fallacy Lens

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension: select text, right-click and Jev (via OpenRouter, your own key) scores it for 69 logical fallacies, showing the highest-scoring ones first with explanations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cobmuddybug/fallacylens-extension) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/cobmuddybug/fallacylens-extension#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`src/config.js`](https://github.com/cobmuddybug/fallacylens-extension/blob/699a0bd1bf713f4753a57de3613c7c3fcab69f24/src/config.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [cobmuddybug](https://github.com/cobmuddybug). Independently curated. |
| Format | Chrome extension (JavaScript, load unpacked) |
| Platform and availability | Chrome (load unpacked from source) |
| Jev's role | Jev scores the text for each fallacy. |
| Requirements | Chrome; your OpenRouter API key with Jev access. |
| License | [MIT](https://github.com/cobmuddybug/fallacylens-extension/blob/699a0bd1bf713f4753a57de3613c7c3fcab69f24/LICENSE) |

## When to use

- Check an argument on any web page for common fallacies.
- Learn what each fallacy means with an example.
- Mismatch: scores are Jev's estimates, not verdicts.

## How it works

The selected text is sent to Jev through OpenRouter with one score question per fallacy; the card ranks the scores and links explanations. Integration evidence: [`src/config.js`](https://github.com/cobmuddybug/fallacylens-extension/blob/699a0bd1bf713f4753a57de3613c7c3fcab69f24/src/config.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/cobmuddybug/fallacylens-extension
# chrome://extensions → Developer mode → Load unpacked
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install-from-source steps in the upstream README.

## Limits and data handling

Selected text is sent to OpenRouter and TypeSafe only when you run a check, billed to your OpenRouter key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 699a0bd1bf71](https://github.com/cobmuddybug/fallacylens-extension/tree/699a0bd1bf713f4753a57de3613c7c3fcab69f24). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
