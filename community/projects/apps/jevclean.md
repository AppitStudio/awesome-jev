# JevClean

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Local IMAP mail organizer: write natural-language rules (one action each), Jev judges every message against them, and you review and confirm delete, archive, move, spam or flag actions with undo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sufferfml/JevClean) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/sufferfml/JevClean#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-16. |
| Jev evidence | [`src/core/jev.ts`](https://github.com/sufferfml/JevClean/blob/4e8722b7b27516b730342c4c30769add1d51f44f/src/core/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [sufferfml](https://github.com/sufferfml). Independently curated. |
| Format | Local Node.js app with browser UI; macOS Apple Silicon package (ad-hoc signed) or source build |
| Platform and availability | Desktop (macOS Apple Silicon package; source build on macOS, Windows, Linux) |
| Jev's role | Jev judges each email against your natural-language rules; code gates and executes confirmed actions. |
| Requirements | Node.js 22+ for source builds, an IMAP account (TLS, password/app password), OS credential store, your Jev API key. |
| License | [MIT](https://github.com/sufferfml/JevClean/blob/4e8722b7b27516b730342c4c30769add1d51f44f/LICENSE) |

## When to use

- Clean up promotions, verification codes and expired events across folders with rules written in plain language.
- Inspect per-message analysis details (rule, probabilities, call status) before anything moves.
- Mismatch: UI and docs are mainly Chinese; macOS package is not notarized; Windows/Linux source paths were not hardware-tested by the author.

## How it works

For each message in the chosen range, the app sends the text and enabled rules to `https://api.typesafe.ai/v1/systemone` as Choice and Noul questions, validates answers with Zod schemas, and only proposes actions when condition and timing thresholds both pass; execution is checked separately and always needs confirmation. Integration evidence: [`src/core/jev.ts`](https://github.com/sufferfml/JevClean/blob/4e8722b7b27516b730342c4c30769add1d51f44f/src/core/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sufferfml/JevClean.git && cd JevClean
npm ci
npm run build
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage guide: `docs/usage.zh-CN.md`.

## Limits and data handling

Message text needed for analysis goes to TypeSafe on your key; configuration and records are encrypted locally, and credentials use the OS keychain.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 4e8722b7b275](https://github.com/sufferfml/JevClean/tree/4e8722b7b27516b730342c4c30769add1d51f44f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
