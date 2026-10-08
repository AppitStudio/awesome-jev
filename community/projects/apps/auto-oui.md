# Auto-Oui

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (French UI) that watches a tab you enable and answers "Oui" — or clicks the approve button — when an AI agent on supported sites stops to ask for permission; detection is local rules by default with no network calls, and an optional Jev mode with your TypeSafe key judges ambiguous wording against a probability threshold (0.90 default). The README warns to keep it off for payments, messages, deletions and production actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jasondupontbizz/auto-oui) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jasondupontbizz/auto-oui#readme) (load unpacked in Chromium browsers). |
| Pricing and access | Free; optional Jev mode uses your own TypeSafe key and usage. Checked 2026-10-08. |
| Jev evidence | [`extension/jev.js`](https://github.com/jasondupontbizz/auto-oui/blob/80671279a90de7593adeb0387a6595b8dd628aa9/extension/jev.js) asks a yes/no question per unrecognised agent message; called from [`extension/background.js`](https://github.com/jasondupontbizz/auto-oui/blob/80671279a90de7593adeb0387a6595b8dd628aa9/extension/background.js). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [jasondupontbizz](https://github.com/jasondupontbizz). Independently curated. |
| Format | Chrome / Chromium extension (Manifest V3, developer mode) |
| Platform and availability | Chrome, Edge, Brave, Arc and other Chromium browsers. |
| Jev's role | Optional judge of whether an agent message is a permission request. |
| Requirements | Chromium browser; TypeSafe key only for Jev mode. |
| License | [MIT](https://github.com/jasondupontbizz/auto-oui/blob/80671279a90de7593adeb0387a6595b8dd628aa9/LICENSE). |

## When to use

- Keep long, low-risk agent tasks moving while you are away.
- Mismatch: auto-approval removes a safety step — use only on tasks whose consequences you accept.

## How it works

Content scripts per site adapter detect approval prompts; in hybrid mode built-in rules run first and Jev is asked only when they find nothing; answers above the threshold trigger the reply or button click.

## Get started

Load the unpacked extension (README *Installation*):

```sh
git clone https://github.com/jasondupontbizz/auto-oui.git
# chrome://extensions → Developer mode → Load unpacked → auto-oui/extension
```

Jev mode bills your TypeSafe key per judged message.

## Examples and demos

- README supported-sites table.

## Limits and data handling

With a key, new agent messages are sent to `api.typesafe.ai`. Auto-approving agent actions is risky (README warning). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 80671279a90d](https://github.com/jasondupontbizz/auto-oui/tree/80671279a90de7593adeb0387a6595b8dd628aa9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
