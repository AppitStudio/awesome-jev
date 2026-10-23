# Attention Vaccine (Chrome extension that flags manipulation techniques with Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that tags posts and articles using manipulation techniques such as rage bait, easy-money pitches, impersonation notices, dehumanizing language and unsupported assertions, without judging viewpoints or fact-checking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nevrs/attention-vaccine) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/nevrs/attention-vaccine#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to install from source. Detection uses your own TypeSafe key. Checked 2026-10-24. |
| Jev evidence | [`background.js`](https://github.com/nevrs/attention-vaccine/blob/ba3b97eb238ad8fb228897cd785c3d9c34737d5b/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [nevrs](https://github.com/nevrs). Independently curated. |
| Format | Chrome extension (unpacked) |
| Platform and availability | Desktop Chrome, installed with Load unpacked (not on the Chrome Web Store yet). |
| Jev's role | Core: Jev answers one yes/no question per technique; a tag appears only above your sensitivity threshold. |
| Requirements | Desktop Chrome; a TypeSafe key (or another configured System One provider). |
| License | [MIT](https://github.com/nevrs/attention-vaccine/blob/ba3b97eb238ad8fb228897cd785c3d9c34737d5b/LICENSE) |

## When to use

- Notice manipulation patterns while reading X, Bluesky or news.
- Tune which techniques and sites are checked.
- Mismatch: a prototype; the author warns of false tags and misses.

## How it works

`background.js` posts text to `https://api.typesafe.ai/v1/systemone` with `jev-1.13.0` (Vercel AI Gateway is an alternative route). Two techniques are rule-based in code. Integration evidence: [`background.js`](https://github.com/nevrs/attention-vaccine/blob/ba3b97eb238ad8fb228897cd785c3d9c34737d5b/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/nevrs/attention-vaccine
# chrome://extensions > Developer mode > Load unpacked
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese and English): [github.com/nevrs/attention-vaccine#english](https://github.com/nevrs/attention-vaccine#english)

## Limits and data handling

Text from pages you read is sent to TypeSafe. The author does not take issues or pull requests.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit ba3b97eb238a](https://github.com/nevrs/attention-vaccine/tree/ba3b97eb238ad8fb228897cd785c3d9c34737d5b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
