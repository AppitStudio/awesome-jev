# Scroll Guard (Chrome extension flagging AI slop, clickbait, bot spam and scams in your X feed with TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Open-source Chrome extension where TypeSafe Jev reads each X post as you scroll and frames flagged posts with a short verdict and a Block button that opens X's own confirmation; it never blocks automatically. Bring your own key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tameravci/scroll-guard) |
| Maintainer | [tameravci](https://github.com/tameravci). Independently curated. |
| Format | Chrome extension (JavaScript, MIT) |
| Requirements | Chrome and a TypeSafe API key. |
| License | [MIT](https://github.com/tameravci/scroll-guard/blob/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/tameravci/scroll-guard/blob/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4/src/jev.js) at the pinned commit. |

## When to use

- Spot AI-written slop, shilling and scams while scrolling X.
- Keep blocking decisions manual with Jev as a flagging aid.
- Mismatch: verdicts are evidence, not proof of authorship.

## How it works

`src/jev.js` posts each post's text to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; the manifest limits host permissions to `api.typesafe.ai`, and Jev makes every decision (no local rules). Integration evidence: [`src/jev.js`](https://github.com/tameravci/scroll-guard/blob/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4/src/jev.js).

## Get started

Download the release zip (or clone), load it unpacked from `chrome://extensions`, and paste your TypeSafe key.

```sh
git clone https://github.com/tameravci/scroll-guard.git && cd scroll-guard
export TYPESAFE_API_KEY=...
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tameravci/scroll-guard/blob/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4/README.md](https://github.com/tameravci/scroll-guard/blob/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4/README.md)

## Limits and data handling

Visible post text is sent to TypeSafe on your key; see PRIVACY.md.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit e91297eacd7e](https://github.com/tameravci/scroll-guard/tree/e91297eacd7e8bbd0326dfde5ed6c2c268d946d4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
