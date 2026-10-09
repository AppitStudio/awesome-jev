# Signal & Noise

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that hides X timeline posts you don't want: tap noise bubbles (rage bait, crypto shilling, engagement bait, spoilers…) or write your own in plain words, and TypeSafe Jev judges each tweet with one `choice` question (keep vs each mute) before it scrolls into view; hidden posts fold into a bar that says why, and your Good hide / Shouldn't have hidden feedback is kept locally.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/icpmacdo/signal-and-noise) |
| Tags | `Source unverified` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/icpmacdo/signal-and-noise#readme) (unpacked extension). |
| Pricing and access | No fee; load the unpacked extension. Needs your own TypeSafe API key (billed by TypeSafe), or an OpenAI Decisions key, or a self-hosted `/v1/systemone` server. Checked 2026-10-09. |
| Jev evidence | [`src/wire.js`](https://github.com/icpmacdo/signal-and-noise/blob/f249923dd74a4ec92bec241df08e8bf0d07fed10/src/wire.js) defines the default TypeSafe route (`https://api.typesafe.ai/v1/systemone`, pinned `jev-1.13.0`) and reads answers; [`src/background.js`](https://github.com/icpmacdo/signal-and-noise/blob/f249923dd74a4ec92bec241df08e8bf0d07fed10/src/background.js) holds the key and sends one request per tweet. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. **No LICENSE at the pinned commit.** Listing is not an endorsement. Extension not run on the review host. |
| Maintainer | [icpmacdo](https://github.com/icpmacdo). Independently curated. |
| Format | Chrome extension (load unpacked) |
| Platform and availability | Google Chrome on desktop (developer-mode unpacked install). |
| Jev's role | Decides per tweet whether it matches one of your mutes; a strictness threshold on P(keep) (default 35%) decides hiding, and tweets show anyway after 2 s if Jev is slow. |
| Requirements | Chrome; a TypeSafe API key (or an alternative route configured in settings). |
| License | **Unspecified** at the pinned commit (no LICENSE file). |

## When to use

- Filter an X timeline by plain-language categories instead of keyword mutes.
- Mismatch: every judged tweet's text is sent to the chosen model provider.

## How it works

A content script keeps each rendered tweet invisible until the background worker returns a verdict; verdicts are cached per tweet id. Accounts on an always-show list and the tweet you opened directly are never sent or hidden. Optional decision pages use synthetic tweets for threshold tuning.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/icpmacdo/signal-and-noise.git
# chrome://extensions -> Developer mode -> Load unpacked -> pick the folder
npm test   # optional unit tests
```

## Limits and data handling

Tweet text, author handle and image alt text go to the model you pick (TypeSafe by default); with the OpenAI route and images on, post images too. Keys stay in `chrome.storage.local`. No LICENSE file at the pinned commit. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit f249923dd74a](https://github.com/icpmacdo/signal-and-noise/tree/f249923dd74a4ec92bec241df08e8bf0d07fed10). Inspected the upstream README, LICENSE status, and the Jev integration files linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
