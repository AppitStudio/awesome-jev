# Dungeon of Jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Turn-based browser dungeon crawler where Jev picks which champion to send, which form the shapeshifting boss opens with, and every enemy move, as single Choice questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ericosg/doj) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://doj.blocbrain.xyz) |
| Pricing and access | Free to play on the author's demo; free source build with your own TypeSafe key. Checked 2026-10-15. |
| Jev evidence | [`src/server/jev.ts`](https://github.com/ericosg/doj/blob/ae4ce49fe11c042c6fe3f8aee1560a25d5cb1310/src/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ericosg](https://github.com/ericosg). Independently curated. |
| Format | Browser game (Phaser 4, TypeScript, Bun server) |
| Platform and availability | Web (author's hosted demo or self-hosted) |
| Jev's role | Jev chooses champions, boss forms and every enemy move. |
| Requirements | Bun to self-host; TypeSafe API key on the server. |
| License | [Apache-2.0](https://github.com/ericosg/doj/blob/ae4ce49fe11c042c6fe3f8aee1560a25d5cb1310/LICENSE) |

## When to use

- Play against a decision model as a game AI.
- See how Choice questions over legal moves can drive enemies without a scripted AI.
- Mismatch: a small exploration game (five rooms), not a full RPG.

## How it works

On each enemy turn the server sends the battle state and the legal moves to Jev as one Choice question and plays the chosen move; champion selection and boss form use the same pattern. Integration evidence: [`src/server/jev.ts`](https://github.com/ericosg/doj/blob/ae4ce49fe11c042c6fe3f8aee1560a25d5cb1310/src/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
bun run dev   # http://127.0.0.1:3210
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Play online: [doj.blocbrain.xyz](https://doj.blocbrain.xyz)

## Limits and data handling

Battle state goes to TypeSafe from the server; on the author's deployment calls use the author's key, self-hosting uses yours.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit ae4ce49fe11c](https://github.com/ericosg/doj/tree/ae4ce49fe11c042c6fe3f8aee1560a25d5cb1310). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
