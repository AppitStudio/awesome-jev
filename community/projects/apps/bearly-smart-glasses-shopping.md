# Bearly (smart-glasses shopping helper where Jev reads what each spoken sentence asks for and boxes the items you look at)

[All projects](../README.md) · [iOS apps](README.md#ios-apps)

Hackathon prototype for Meta smart glasses: look at something and say what you want, and Bearly identifies it, finds the cheapest match in the Shopify catalog and buys it on "yup" (Stripe test mode), can email the invoice and logs inspection notes with photos. Gemini Live is the voice agent; Jev classifies each sentence into intents like find, buy, skip or note and draws the boxes around items in view.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jungkeun-hong/bearly) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jungkeun-hong/bearly#readme) (source-built; no separate product site verified). |
| Pricing and access | Public source with no license file (all rights reserved by default); no purchase fee, provider usage on your keys, Stripe in test mode. Checked 2026-11-15. |
| Jev evidence | [`app/api/twin/intent/route.ts`](https://github.com/jungkeun-hong/bearly/blob/81f64ae44f11c4f337e9cf62c2311d4848a5073d/app/api/twin/intent/route.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jungkeun-hong](https://github.com/jungkeun-hong). Independently curated. |
| Format | Next.js laptop screen plus an iPhone app for Meta glasses (TypeScript, Swift) |
| Platform and availability | iPhone app with Meta smart glasses plus a laptop web screen; source build only, no App Store listing verified |
| Jev's role | Jev classifies each spoken sentence into a shopping or inspection intent and draws boxes around items in the camera view. |
| Requirements | Meta Ray-Ban or Oakley glasses in Developer Mode, an iPhone, a laptop, and keys for Jev (`JEV_API_KEY`), Gemini, Shopify, Stripe (test), LiveKit and ElevenLabs. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Prototype hands-free shopping or inspection logging on smart glasses.
- Mismatch: real purchases; payments run in Stripe test mode.

## How it works

`app/api/twin/intent/route.ts` posts each sentence to `https://api.typesafe.ai/v1/systemone` (model `jev-latest` unless `JEV_MODEL` is set) with ten intent options and falls back to word matching on failure; `app/api/twin/see/route.ts` asks Jev for item boxes. Integration evidence: [`app/api/twin/intent/route.ts`](https://github.com/jungkeun-hong/bearly/blob/81f64ae44f11c4f337e9cf62c2311d4848a5073d/app/api/twin/intent/route.ts).

## Get started

Start the laptop screen, then build the iPhone app and connect the glasses.

```sh
git clone https://github.com/jungkeun-hong/bearly && cd bearly
npm install
cp .env.example .env.local   # add your keys
npm run dev                  # http://localhost:3127/demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jungkeun-hong/bearly/blob/81f64ae44f11c4f337e9cf62c2311d4848a5073d/README.md](https://github.com/jungkeun-hong/bearly/blob/81f64ae44f11c4f337e9cf62c2311d4848a5073d/README.md)

## Limits and data handling

Transcribed sentences and camera frames go to TypeSafe and Google (Gemini) on your keys, plus the other listed services. Built at a hackathon on 14 November 2026.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 81f64ae44f11](https://github.com/jungkeun-hong/bearly/tree/81f64ae44f11c4f337e9cf62c2311d4848a5073d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
