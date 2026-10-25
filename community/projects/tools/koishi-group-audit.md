# koishi-plugin-group-audit (QQ group moderation with OpenAI Moderation, Jev or an LLM)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Koishi plugin for QQ groups: first-stage filters for QR codes, contact and group cards and Tencent online docs, then content review by OpenAI Moderation, TypeSafe Jev or an OpenAI-compatible LLM, each optional, with message recall and escalating mutes when a rule matches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DNAlec/koishi-plugin-group-audit) |
| Maintainer | [DNAlec](https://github.com/DNAlec). Independently curated. |
| Format | Koishi plugin (TypeScript, npm) |
| Requirements | Node.js 22+, Koishi 4.18+ with database and http services, a QQ adapter that supports recall and mute, and group admin rights for the bot; a TypeSafe key for the Jev channel. |
| License | [MIT](https://github.com/DNAlec/koishi-plugin-group-audit/blob/168c3f4873029b93c4c22614ceb96500c50d39a7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/channels/jev.ts`](https://github.com/DNAlec/koishi-plugin-group-audit/blob/168c3f4873029b93c4c22614ceb96500c50d39a7/src/channels/jev.ts) at the pinned commit. |

## When to use

- Moderate a busy QQ group with your own rules instead of manual review.
- Combine Jev with OCR text or images for rule checks alongside other channels.
- Mismatch: README is in Chinese; Jev is one of three independent review channels.

## How it works

`src/channels/config.ts` defaults the Jev channel to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); `jev.ts` asks one question per configured rule. Timeouts, errors and uncertain answers are only logged, and one channel's failure does not affect the others. Integration evidence: [`src/channels/jev.ts`](https://github.com/DNAlec/koishi-plugin-group-audit/blob/168c3f4873029b93c4c22614ceb96500c50d39a7/src/channels/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install koishi-plugin-group-audit
# or search group-audit in the Koishi plugin market, then set the typesafeJev channel's apiKey and rules
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/DNAlec/koishi-plugin-group-audit#readme](https://github.com/DNAlec/koishi-plugin-group-audit#readme)
- npm: [www.npmjs.com/package/koishi-plugin-group-audit](https://www.npmjs.com/package/koishi-plugin-group-audit)

## Limits and data handling

Message text (and OCR text or images if enabled) is sent to each enabled review provider. A match recalls the message and can mute the sender with escalating durations; test rules before enabling enforcement.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 168c3f487302](https://github.com/DNAlec/koishi-plugin-group-audit/tree/168c3f4873029b93c4c22614ceb96500c50d39a7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
