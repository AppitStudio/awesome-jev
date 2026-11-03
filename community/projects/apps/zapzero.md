# zapzero (inbox zero for WhatsApp on your Mac, where Jev triages every chat and you send each draft yourself)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac tool that reads the WhatsApp Desktop app's own database read-only and triages every chat: who is waiting on whom, how urgent, and who the person is to you. Jev does the triage and a small chat model drafts replies in your own tone; you review each draft and press Enter in WhatsApp yourself. The panel UI is in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vibegui/zapzero) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://zapzero.dev) |
| Pricing and access | Free source build under MIT; you pay OpenRouter through your own key. Checked 2026-11-03. |
| Jev evidence | [`server/ai.ts`](https://github.com/vibegui/zapzero/blob/3dcdc4beefbe69140d6f5b1d6063f51ec5212933/server/ai.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [vibegui](https://github.com/vibegui). Independently curated. |
| Format | Local Bun server with web panel and a launchd agent |
| Platform and availability | macOS with WhatsApp Desktop (source build; launchd agent installed by setup). |
| Jev's role | Triages each WhatsApp chat for wait state, urgency, person and area. |
| Requirements | macOS with WhatsApp Desktop linked to your phone; Bun 1.3+; an OpenRouter key; Full Disk Access for your terminal and `bun`. |
| License | [MIT](https://github.com/vibegui/zapzero/blob/3dcdc4beefbe69140d6f5b1d6063f51ec5212933/LICENSE) |

## When to use

- Clear a backlog of WhatsApp chats by urgency with drafts in your own voice.
- Mismatch: Portuguese UI, macOS and WhatsApp Desktop only, and message excerpts go to the models you choose.

## How it works

`server/ai.ts` sends each changed chat's excerpt to OpenRouter's decisions API with the Jev model (`typesafe/jev-1.14` by default, about US$0.00005 per chat per the README) for wait, urgency, who and area; drafts and suggestions use a separate chat model. Integration evidence: [`server/ai.ts`](https://github.com/vibegui/zapzero/blob/3dcdc4beefbe69140d6f5b1d6063f51ec5212933/server/ai.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/vibegui/zapzero && cd zapzero
bun install
cp .env.example .env   # paste your OpenRouter key
bun run setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product site: [zapzero.dev](https://zapzero.dev)

## Limits and data handling

zapzero copies WhatsApp's database read-only and keeps snapshots in `~/Library/Application Support/zap`; only the excerpt of each conversation goes to OpenRouter (Jev) and the draft model on your key. Nothing is sent by zapzero. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 3dcdc4beefbe](https://github.com/vibegui/zapzero/tree/3dcdc4beefbe69140d6f5b1d6063f51ec5212933). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
