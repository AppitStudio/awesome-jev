# Jev Ad Block

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome Manifest V3 ad blocker that blocks ad requests with network rules and sends candidate page elements to Jev for semantic ad judgement, falling back to local rules without a key or when quota runs out (README in Chinese).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lingengyuan/jev-adblock) |
| Maintainer | [lingengyuan](https://github.com/lingengyuan). Independently curated. |
| Format | Chrome MV3 extension (load unpacked from `dist/`) |
| Requirements | Node.js to build; Chrome; optional TypeSafe API key. |
| License | [GPL-3.0](https://github.com/lingengyuan/jev-adblock/blob/3301511e14e836ec07231f5c36ebda2708601f00/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Hide in-page ads that static filter lists miss.
- Mismatch: Chinese-language docs; element snippets are sent to a hosted API when Jev is enabled.

## How it works

Layered detection: CSS and community rules first, then scored candidates go to Jev; verdicts are cached per site and slot for seven days. (Summarized from the upstream [README](https://github.com/lingengyuan/jev-adblock/blob/3301511e14e836ec07231f5c36ebda2708601f00/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `npm run build`, then load `dist/` unpacked at `chrome://extensions`.

## Limits and data handling

Candidate element content is sent to the TypeSafe API when a key is set. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 3301511e14e8](https://github.com/lingengyuan/jev-adblock/tree/3301511e14e836ec07231f5c36ebda2708601f00). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
