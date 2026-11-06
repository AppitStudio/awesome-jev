# Rajzolj Mircinek (drawing game judged by TypeSafe Jev on Cloudflare Workers AI)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser/PWA drawing game where Mirci the cat keeps guessing what you draw; judgments come from TypeSafe's Jev model on Cloudflare Workers AI (`typesafe/jev`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Slityak/rajzolj-mircinek) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://deszepmacskavagymirci.kornel-dc5.workers.dev) |
| Pricing and access | Hosted demo is free to play; self-host needs Cloudflare Workers AI. Checked 2026-11-07. |
| Jev evidence | [`worker/jev.ts`](https://github.com/Slityak/rajzolj-mircinek/blob/190611fe27a3509db738bef8aacd6f92005c8cdc/worker/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Slityak](https://github.com/Slityak). Independently curated. |
| Format | Cloudflare Workers PWA (TypeScript, MIT) |
| Platform and availability | Browser / installable PWA (Cloudflare Workers). |
| Jev's role | Judges live drawings with typed questions to Workers AI `typesafe/jev` (TypeSafe Jev on Cloudflare). |
| Requirements | Play on the hosted worker, or deploy with a Cloudflare account that can call Workers AI `typesafe/jev`. |
| License | [MIT](https://github.com/Slityak/rajzolj-mircinek/blob/190611fe27a3509db738bef8aacd6f92005c8cdc/LICENSE) |

## When to use

- Play a drawing-guess game powered by Jev.
- Self-host the Workers AI judge.
- Mismatch: Hungarian-first UI; English via `?lang=en`.

## How it works

`worker/jev.ts` wraps Cloudflare Workers AI calls to `typesafe/jev` and returns typed guesses used by the game loop. Integration evidence: [`worker/jev.ts`](https://github.com/Slityak/rajzolj-mircinek/blob/190611fe27a3509db738bef8aacd6f92005c8cdc/worker/jev.ts).

## Get started

Open the hosted demo, or deploy the worker per README with Workers AI access.

```sh
git clone https://github.com/Slityak/rajzolj-mircinek.git && cd rajzolj-mircinek
# follow README Cloudflare Workers deploy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Slityak/rajzolj-mircinek/blob/190611fe27a3509db738bef8aacd6f92005c8cdc/README.md](https://github.com/Slityak/rajzolj-mircinek/blob/190611fe27a3509db738bef8aacd6f92005c8cdc/README.md)

## Limits and data handling

Drawing strokes / image features under judgment are sent to Cloudflare Workers AI. Demo traffic uses the maintainer's Workers AI quota.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 190611fe27a3](https://github.com/Slityak/rajzolj-mircinek/tree/190611fe27a3509db738bef8aacd6f92005c8cdc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
