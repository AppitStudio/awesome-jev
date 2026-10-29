# Pi Jev Compact (bounded Jev-assisted context compaction for Pi, plus a repeated tool-failure guard)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi package with two separate extensions: a compactor that replaces Pi's generated summary with a bounded, extractive checkpoint (your requests kept verbatim, selected exact evidence kept, full history recallable), using at most one Jev request per compaction and none without a key; and a loop guard that blocks the fourth identical tool call after three identical failures and offers `/loop-recover`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maccagnit/pi-jev-compact) |
| Maintainer | [maccagnit](https://github.com/maccagnit). Independently curated. |
| Format | Pi package (TypeScript) |
| Requirements | Node.js 22.19+, Pi 1.4.0 (tested) and optionally a TypeSafe API key. |
| License | [MIT](https://github.com/maccagnit/pi-jev-compact/blob/f73032ac942dd2da389fafee14c1770cb26ae926/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.ts`](https://github.com/maccagnit/pi-jev-compact/blob/f73032ac942dd2da389fafee14c1770cb26ae926/jev.ts) at the pinned commit. |

## When to use

- Keep long Pi sessions within context without losing exact evidence.
- Mismatch: Pi only.

## How it works

`jev.ts` posts candidate context blocks to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` to choose what the checkpoint keeps. Integration evidence: [`jev.ts`](https://github.com/maccagnit/pi-jev-compact/blob/f73032ac942dd2da389fafee14c1770cb26ae926/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/maccagnit/pi-jev-compact@v0.3.0
mkdir -p ~/.config/jev && (umask 077 && printf '%s' 'YOUR_KEY' > ~/.config/jev/typesafe.key)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/maccagnit/pi-jev-compact#readme](https://github.com/maccagnit/pi-jev-compact#readme)

## Limits and data handling

Conversation excerpts go to TypeSafe during compaction.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit f73032ac942d](https://github.com/maccagnit/pi-jev-compact/tree/f73032ac942dd2da389fafee14c1770cb26ae926). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
