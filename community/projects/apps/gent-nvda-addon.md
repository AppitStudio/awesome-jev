# gent (NVDA screen-reader add-on that changes speech settings from a plain-words request, with Jev choosing the setting through a relay)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

NVDA add-on from Blind Ant: press NVDA+G, type what you want changed in plain words ("talk a bit faster", "stop reading so much punctuation", "undo that") and gent works out which speech, typing or keys setting you mean and changes it. If it is unsure it asks "Did you mean...?" first, and it can undo the last five changes. The repository also holds the Cloudflare Worker relay that holds the TypeSafe key and asks Jev the one question. The authors call it a design-fiction experiment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Carrados/nvda-addons) |
| Tags | `Open source` · `Pricing unverified` |
| Product homepage | [Product homepage](https://github.com/Carrados/nvda-addons) |
| Pricing and access | The add-on is distributed from GitHub releases and no price or relay usage terms are stated in the README, so pricing and long-term relay availability are unverified. Checked 2026-11-04. |
| Jev evidence | [`relay/src/gent.js`](https://github.com/Carrados/nvda-addons/blob/161d5e931e55fcbe754a464da5b2a488a1e1313e/relay/src/gent.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Carrados](https://github.com/Carrados). Independently curated. |
| Format | NVDA add-on (`.nvda-addon`, Python) and a Cloudflare Worker relay (JavaScript) |
| Platform and availability | Windows with NVDA 2025.1 or later; needs the maintainer's hosted relay. |
| Jev's role | Chooses which NVDA setting a typed request means and how big the change is. |
| Requirements | NVDA 2025.1 or later on Windows; the add-on talks to Blind Ant's hosted relay. |
| License | [GPL-2.0](https://github.com/Carrados/nvda-addons/blob/161d5e931e55fcbe754a464da5b2a488a1e1313e/LICENSE.txt) |

## When to use

- Let a blind or low-vision NVDA user change speech settings by typing a plain-language request instead of navigating settings panels.
- Mismatch: it only covers Speech settings plus typing and keys, and needs the Blind Ant relay to be online.

## How it works

`relay/src/gent.js` builds a Choice question over the supported actions (plus a size choice) for `https://api.typesafe.ai/v1/systemone`, and the relay returns the action and Jev's confidence to the add-on; the add-on asks "Did you mean...?" when unsure. Integration evidence: [`relay/src/gent.js`](https://github.com/Carrados/nvda-addons/blob/161d5e931e55fcbe754a464da5b2a488a1e1313e/relay/src/gent.js).

## Get started

From the upstream README (not run on the review host):

```sh
# download the .nvda-addon file from the latest release, open it, and NVDA offers to install it
# then press NVDA+G and type a request such as: talk a bit faster
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Add-on readme with what it can change and its privacy notes: [github.com/Carrados/nvda-addons/blob/161d5e931e55fcbe754a464da5b2a488a1e1313e/addons/gent/readme.md](https://github.com/Carrados/nvda-addons/blob/161d5e931e55fcbe754a464da5b2a488a1e1313e/addons/gent/readme.md)
- Latest release (gent v0.3.0, 2026-11-04): [github.com/Carrados/nvda-addons/releases/latest](https://github.com/Carrados/nvda-addons/releases/latest)

## Limits and data handling

What you type into gent and the names of its last few changes go to Blind Ant's relay and then to TypeSafe's Jev; the add-on asks before first use and sends a random install ID for rate limiting, and the README says the relay keeps no logs (not verified here). It is an experiment run by one company. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 161d5e931e55](https://github.com/Carrados/nvda-addons/tree/161d5e931e55fcbe754a464da5b2a488a1e1313e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
