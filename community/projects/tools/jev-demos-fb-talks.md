# Jev demos and talk (Fabio Biondi) (twelve Next.js demos of Jev alone, with Gemini and with images, plus slides and a comment-moderation tutorial)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Talk material by Fabio Biondi: a Next.js app with demos grouped as Jev alone (one yes/no question, Choice/Score/Noul, a moderation policy with thresholds, CSV evaluation), Jev with Gemini (Gemini rewrites and Jev confirms, Gemini proposes and Jev picks, email to structured data with a hidden-instruction check, Jev vs Gemini on 20 websites, a smart support router) and Jev with images, plus slides and a step-by-step comment-moderation article using Vercel AI Gateway.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fb-talks/jev) |
| Maintainer | [fb-talks](https://github.com/fb-talks). Independently curated. |
| Format | Next.js demo app, slides and article (TypeScript) |
| Requirements | Node.js 22+ and a TypeSafe or Vercel AI Gateway key (entered in the app's key panel or set as environment variables); a Gemini path for the combined demos. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/keys.ts`](https://github.com/fb-talks/jev/blob/b9fef58c3cc3846a28a16661df76f5b56d492cfd/lib/keys.ts) at the pinned commit. |

## When to use

- Walk through Jev's question types and Jev + LLM patterns in a talk or workshop.
- Mismatch: a production moderation service; these are teaching demos.

## How it works

`lib/keys.ts` creates a `TypeSafeClient` from `@typesafe-ai/sdk` with your TypeSafe key, or routes through Vercel AI Gateway, reading keys from the browser-side key panel cookies or `TYPESAFE_API_KEY` / `AI_GATEWAY_API_KEY`. Integration evidence: [`lib/keys.ts`](https://github.com/fb-talks/jev/blob/b9fef58c3cc3846a28a16661df76f5b56d492cfd/lib/keys.ts).

## Get started

Run the demos locally, or open the hosted demo and paste your own key.

```sh
git clone https://github.com/fb-talks/jev && cd jev
npm install
export TYPESAFE_API_KEY=...   # or AI_GATEWAY_API_KEY=...
npm run dev    # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demos (bring your own key): [jev-eight-mu.vercel.app/](https://jev-eight-mu.vercel.app/)
- Slides: [fb-talks.github.io/jev/](https://fb-talks.github.io/jev/)
- Tutorial article: [github.com/fb-talks/jev/blob/b9fef58c3cc3846a28a16661df76f5b56d492cfd/article.md](https://github.com/fb-talks/jev/blob/b9fef58c3cc3846a28a16661df76f5b56d492cfd/article.md)

## Limits and data handling

Demo inputs go to TypeSafe or Vercel AI Gateway (and Google for Gemini demos) on the key you supply; keys entered in the panel are stored in browser cookies for the demo site. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit b9fef58c3cc3](https://github.com/fb-talks/jev/tree/b9fef58c3cc3846a28a16661df76f5b56d492cfd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
