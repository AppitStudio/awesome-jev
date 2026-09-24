# jev-phone

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Drive a real phone with TypeSafe Jev choosing indexed UI actions while [phone-use](https://www.npmjs.com/package/@phone-use/sdk) executes taps/types on iOS Simulator, Android, or a cloud phone.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rajmeet/jev-phone) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Rajmeet/jev-phone#readme) — local/cloud phone runs; no separate hosted product page checked. |
| Pricing and access | MIT source build; configure `AI_GATEWAY_API_KEY` (Vercel AI Gateway serves Jev). phone-use cloud sessions follow upstream billing. Checked **2026-09-24**. TypeSafe/Gateway usage separate. |
| Jev evidence | Inspected [`src/jev.ts`](https://github.com/Rajmeet/jev-phone/blob/2f5924e7baf87b2d2c06cbac19a82de6d2d54f88/src/jev.ts) and [`tests/jev.test.ts`](https://github.com/Rajmeet/jev-phone/blob/2f5924e7baf87b2d2c06cbac19a82de6d2d54f88/tests/jev.test.ts). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live phone/Gateway runs not executed on the review host. |
| Maintainer | [Rajmeet](https://github.com/Rajmeet). Independently curated. |
| Format | Bun/TypeScript phone agent (`examples/run.ts`). |
| Platform and availability | iOS Simulator (macOS), Android via adb, or phone-use cloud. |
| Jev's role | Picks indexed on-screen actions; a small LLM may type when needed; phone-use executes. |
| Requirements | Bun; phone target; `AI_GATEWAY_API_KEY` (see `.env.example`). |
| License | [MIT](https://github.com/Rajmeet/jev-phone/blob/2f5924e7baf87b2d2c06cbac19a82de6d2d54f88/LICENSE). |

## When to use

Use it for **goal-driven phone UI automation** where Jev only chooses from a code-built action index. Prefer browser Playwright skills when the target is the web, not a phone OS.

## How it works

Each step observes on-screen elements, asks Jev for the next indexed action, and executes via phone-use. The agent loop and action space live in application code; Jev does not generate free-form UI scripts.

## Get started

```sh
git clone https://github.com/Rajmeet/jev-phone.git
cd jev-phone
git checkout 2f5924e7baf87b2d2c06cbac19a82de6d2d54f88
bun install
cp .env.example .env   # AI_GATEWAY_API_KEY=...
# iOS Simulator example (macOS + booted simulator):
# bun examples/run.ts "Open Settings and go to General, then About"
```

## Examples and demos

- README demo GIF/MP4 (Apple Maps walkthrough).
- `examples/run.ts`; offline `tests/jev.test.ts` (not re-run here).

## Limits and data handling

Screen element text/structure leaves the device for the configured Gateway/Jev provider. Cloud phone sessions may store more—read phone-use terms. This listing did not boot a simulator or spend Gateway credits.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 2f5924e](https://github.com/Rajmeet/jev-phone/tree/2f5924e7baf87b2d2c06cbac19a82de6d2d54f88). AI-assisted README + `src/jev.ts` inspection. No live TypeSafe/Gateway spend.

Related: [Mobile Jev](mobile-jev.md), [jev-android](jev-android.md).
