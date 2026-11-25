# A2UI decision-model playground by Shahriar Bijoy (voice-driven generative UI where Claude builds each screen and Jev handles the follow-up edits)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Voice playground for generative UI: ask for something and Claude answers with a screen built from a fixed catalog of 27 A2UI components; follow-ups such as "we're six, and later" go to Jev, which decides whether the request changes the current screen and picks the new values, so the screen updates in about 0.2 seconds without calling the large model. Shown at AI Tinkerers Bremen on 25 November 2026.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ShahriarBijoy/A2ui) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ShahriarBijoy/A2ui#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-26. |
| Jev evidence | [`src/worker/router.ts`](https://github.com/ShahriarBijoy/A2ui/blob/9858719d9b6fec8e14a4c6f0ae593d93d0d5b025/src/worker/router.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Shahriar Bijoy](https://github.com/ShahriarBijoy). Independently curated. |
| Format | TypeScript web app (Cloudflare Worker + React) |
| Platform and availability | Web app on Cloudflare Workers (Bun, React, shadcn/ui); run locally with `bun run dev`. |
| Jev's role | One Jev request per utterance decides change versus new screen and, for a change, picks the new values from those the screen allows; while you speak it also guesses which components the request is about. |
| Requirements | Bun; API keys for Anthropic, Soniox (speech to text) and TypeSafe (Jev). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See how a small decision model can take the cheap follow-up turns in a generative UI while a large model builds new screens.
- Mismatch: if you need a production UI framework; this is a demo playground with a known open issue in its Image component.

## How it works

`src/worker/router.ts` sends one Jev request per utterance and either patches the screen with an A2UI `updateDataModel` message or hands the turn to Claude Sonnet 5.5; `src/worker/jev.ts` is a small Jev client (Bearer auth, `{model, state, questions}`, hard timeout). The author reports 30 of 30 test sentences routed correctly. Integration evidence: [`src/worker/router.ts`](https://github.com/ShahriarBijoy/A2ui/blob/9858719d9b6fec8e14a4c6f0ae593d93d0d5b025/src/worker/router.ts).

## Get started

Clone, add your keys to `.dev.vars`, and start the dev server.

```sh
git clone https://github.com/ShahriarBijoy/A2ui
cd A2ui
bun install
cp .dev.vars.example .dev.vars   # add Anthropic, Soniox and TypeSafe keys
bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Notes and measurements: [github.com/ShahriarBijoy/A2ui/blob/9858719d9b6fec8e14a4c6f0ae593d93d0d5b025/NOTES.md](https://github.com/ShahriarBijoy/A2ui/blob/9858719d9b6fec8e14a4c6f0ae593d93d0d5b025/NOTES.md)
- Event: [bremen.aitinkerers.org/](https://bremen.aitinkerers.org/)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Speech goes to Soniox, new screens and live web search to Anthropic (non-TypeSafe), and routing to TypeSafe. The README notes an unfixed issue: the Image component loads any http(s) address, so a typed value could leave through an image URL. Cost and latency figures are the author's own.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 9858719d9b6f](https://github.com/ShahriarBijoy/A2ui/tree/9858719d9b6fec8e14a4c6f0ae593d93d0d5b025). Inspected the README, `NOTES.md` and the Worker's router and Jev client at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
