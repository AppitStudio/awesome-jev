# slop-block (Chrome extension filtering the YouTube feed by plain-language tags with TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Chrome extension that shows or hides YouTube feed videos by plain-language tags, with TypeSafe Jev decisions via OpenRouter on your key, a 30-day decision cache and a built-in spending limit. English and Russian UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexzomai/slop-block) |
| Maintainer | [alexzomai](https://github.com/alexzomai). Independently curated. |
| Format | Chrome extension (TypeScript, MIT) |
| Requirements | Chrome and an OpenRouter key with TypeSafe Jev access. |
| License | [MIT](https://github.com/alexzomai/slop-block/blob/b737c5632bc5bb50992f8069624b243302dfcf06/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/background/jev.ts`](https://github.com/alexzomai/slop-block/blob/b737c5632bc5bb50992f8069624b243302dfcf06/src/background/jev.ts) at the pinned commit. |

## When to use

- Keep a YouTube feed on topics you choose.
- Hide recurring content you do not want.
- Mismatch: YouTube feed only; costs depend on your OpenRouter usage.

## How it works

`src/background/jev.ts` posts to `https://openrouter.ai/api/v1/systemone`; `src/background/settings.ts` defaults the model to `typesafe/jev-1.13`; (video, tag) decisions are cached and de-duplicated. Integration evidence: [`src/background/jev.ts`](https://github.com/alexzomai/slop-block/blob/b737c5632bc5bb50992f8069624b243302dfcf06/src/background/jev.ts).

## Get started

Build the extension, load it unpacked in Chrome, and add your OpenRouter key and tags in Options.

```sh
git clone https://github.com/alexzomai/slop-block.git && cd slop-block
export OPENROUTER_API_KEY=...
npm install && npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alexzomai/slop-block/blob/b737c5632bc5bb50992f8069624b243302dfcf06/README.md](https://github.com/alexzomai/slop-block/blob/b737c5632bc5bb50992f8069624b243302dfcf06/README.md)

## Limits and data handling

Video titles/metadata are sent to OpenRouter/TypeSafe on your key; no backend, account or analytics.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit b737c5632bc5](https://github.com/alexzomai/slop-block/tree/b737c5632bc5bb50992f8069624b243302dfcf06). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
