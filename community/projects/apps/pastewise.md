# Pastewise

[All projects](../README.md) · [Web apps](README.md#web-apps)

One paste box that recognizes JSON, JWTs, cron, stack traces, colors, and more, then morphs into the matching tool. TypeSafe Jev classifies ambiguous pastes; deterministic helpers format and decode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nuu-maan/pastewise) |
| Tags | `Source unverified` · `Free` · `BYOK` |
| Product homepage | [pastewise.vercel.app](https://pastewise.vercel.app) |
| Pricing and access | Hosted demo returned HTTP 200 on review (pricing/limits unchecked). Source-build with Bun; optional `TYPESAFE_API_KEY` for online Jev (`jev-latest` default). No app purchase fee; TypeSafe usage is separate. Reviewed **2026-09-23**. |
| Jev evidence | [`src/lib/jev/questions.ts`](https://github.com/Nuu-maan/pastewise/blob/b1ee44e52486b05829e977e5495fb4284a574949/src/lib/jev/questions.ts) and [`src/lib/jev/client.ts`](https://github.com/Nuu-maan/pastewise/blob/b1ee44e52486b05829e977e5495fb4284a574949/src/lib/jev/client.ts) call System One with three Choice questions (kind, language, cause); [`/api/classify`](https://github.com/Nuu-maan/pastewise/blob/b1ee44e52486b05829e977e5495fb4284a574949/src/app/api/classify/route.ts) is the server path. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Public source was inspected, but **no LICENSE file** was present at the reviewed commit—do not treat it as open source. Hosted demo and live TypeSafe calls were **not** run on the review host. Distinct from [JevPaste](jevpaste.md) (macOS Smart Paste) and [Shapeshift](shapeshift.md) (intent → UI cards; inspiration noted by the author). |
| Maintainer | [Nuu-maan](https://github.com/Nuu-maan) ([@Numankhannnnn](https://x.com/Numankhannnnn)). Independently curated from X. |
| Format | Next.js / Bun web app **pastewise 0.1.0** (`@typesafe-ai/sdk`). |
| Platform and availability | Web ([hosted demo](https://pastewise.vercel.app) or local `bun dev`). Early public release. |
| Jev's role | For pastes the browser rules cannot pin down, Jev answers kind (stacktrace/code/text), language, and likely error cause; code always runs the tools. Offline heuristic classifier when no key. Exact formats (JSON, JWT, URL, timestamp, color, cron, base64, SQL) stay local. |
| Requirements | [Bun](https://bun.sh) for local; optional `TYPESAFE_API_KEY` (server-only) and `JEV_MODEL`. |
| License | No license file found at the reviewed commit; public source is not established as open source. |

## When to use

Use it when you paste developer snippets into one box and want the matching formatter/decoder without opening many tabs. Prefer [Shapeshift](shapeshift.md) when the input is natural-language intent that should become productivity UI cards. Prefer [JevPaste](jevpaste.md) / [Smart Paste](smart-paste.md) when the problem is filling form fields from clipboard values.

## How it works

Browser rules detect exact formats instantly with no network. Fuzzy cases POST to `/api/classify`, which asks Jev three typed Choice questions via `@typesafe-ai/sdk` System One (`jev-latest` by default). Application code maps the answers onto tool components (JSON → TS, JWT decode, cron explain, stack parsing, colors, and so on). Without a key, a built-in heuristic classifier keeps the UI usable offline.

## Get started

```sh
git clone https://github.com/Nuu-maan/pastewise.git
cd pastewise
git checkout b1ee44e52486b05829e977e5495fb4284a574949
bun install && bun dev
# Open http://localhost:3000 — rules + offline heuristic by default
# Optional: cp .env.example .env.local and set TYPESAFE_API_KEY
```

Live classification sends pasted text to TypeSafe from the server route and can incur charges. The review host did not run `bun install`, `bun run check`, or live Jev.

## Examples and demos

- Hosted site: [pastewise.vercel.app](https://pastewise.vercel.app) (HTTP 200 observed; workflow not exercised).
- Author demo: [X post](https://x.com/numankhannnnn/status/2102780024411869576) (video demo of paste → tool morph; not independently reproduced here).
- Upstream README samples cover JSON, JWT, cron, stack traces, colors, timestamps, URLs, SQL, and base64.

## Limits and data handling

With a key, pasted text for fuzzy cases goes to TypeSafe via the server; the key never reaches the browser. Exact rule matches stay local. Without a key, classification stays on the heuristic path. Do not paste secrets into a hosted deployment you do not control. This listing did not call live Jev.

## Review and maintenance

Reviewed on **2026-09-23** (Europe/Sofia) at [commit b1ee44e](https://github.com/Nuu-maan/pastewise/tree/b1ee44e52486b05829e977e5495fb4284a574949) (**0.1.0**). AI-assisted source review of README, package metadata, `.env.example`, and `src/lib/jev/*` plus `/api/classify`. No LICENSE in the tree. Hosted homepage HTTP 200. No `bun` install/check and no live TypeSafe spend. x_post_url retained: [X post](https://x.com/numankhannnnn/status/2102780024411869576).

Related: [Shapeshift](shapeshift.md), [JevPaste](jevpaste.md), [Smart Paste](smart-paste.md).
