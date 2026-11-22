# jev-dynamic-ui by Felix Glush (chat box that opens the right banking form and pre-fills it, with Jev picking the form)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A research demo: type "Send $50 to Sam for dinner" and the matching one of fourteen prebuilt banking forms opens with recipient and amount filled in, anything unstated left blank and highlighted. Jev picks the action and its choice fields in one request; a fine-tuned 350M model in Ollama extracts the free-text fields. An experimental voice mode fills the form while you talk.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/felixglush/jev-dynamic-ui) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/felixglush/jev-dynamic-ui#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build run locally with your own TypeSafe key and Ollama; no license file, so reuse terms are not granted. No hosted app (the write-up site is static). Checked 2026-11-22. |
| Jev evidence | [`src/lib/jev/classify.ts`](https://github.com/felixglush/jev-dynamic-ui/blob/29c871686c6da937f517a25cd20941ea58897c23/src/lib/jev/classify.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [felixglush](https://github.com/felixglush). Independently curated. |
| Format | Next.js web app + fine-tuned extractor |
| Platform and availability | Local Next.js web app (Node 22+), Ollama for the extractor; optional local speech servers for voice. |
| Jev's role | One Jev request per message picks the action (or none) and speculatively answers every choice parameter of every action; code keeps only the chosen action's answers. |
| Requirements | Node 22+, Ollama (downloads a ~380 MB fine-tuned model) and a TypeSafe API key; Python 3 and a 4-core CPU for voice mode. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See how Jev can route free-form requests to structured UI and pre-fill choice fields with low latency.
- Mismatch: real banking; the forms are mock-ups and nothing is submitted.

## How it works

`src/lib/jev/classify.ts` follows TypeSafe's function-calling pattern with the `@typesafe-ai/sdk` client, server-side only so the key never reaches the browser; actions and fields are defined in `src/lib/jev/catalog.ts`. Integration evidence: [`src/lib/jev/classify.ts`](https://github.com/felixglush/jev-dynamic-ui/blob/29c871686c6da937f517a25cd20941ea58897c23/src/lib/jev/classify.ts).

## Get started

Install, add your TypeSafe key, register the fine-tuned extractor in Ollama and start the dev server.

```sh
git clone https://github.com/felixglush/jev-dynamic-ui && cd jev-dynamic-ui
npm install
cp .env.example .env.local   # add TYPESAFE_API_KEY
scripts/ollama/use-tuned.sh
npm run dev   # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up and results: [felixglush.github.io/jev-dynamic-ui/](https://felixglush.github.io/jev-dynamic-ui/)
- README: [github.com/felixglush/jev-dynamic-ui/blob/29c871686c6da937f517a25cd20941ea58897c23/README.md](https://github.com/felixglush/jev-dynamic-ui/blob/29c871686c6da937f517a25cd20941ea58897c23/README.md)

## Limits and data handling

Each typed message is sent to TypeSafe; free-text extraction runs locally. Demo forms only. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 29c871686c6d](https://github.com/felixglush/jev-dynamic-ui/tree/29c871686c6da937f517a25cd20941ea58897c23). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
