# Jev VJ (audio-reactive visuals where three Jev units deliberate every few bars on section, scene, intensity and palette)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser VJ prototype: in-page audio analysis tracks beats and bars and drives frame-level effects, while every few bars a summary of recent bars goes to Jev, asked by three deliberating units (MAGI-style), to decide the current section, whether a drop is coming, the next scene, intensity, palette and transitions; a pre-armed drop scene cuts in when the audio confirms the drop. three.js/GLSL with ISF and Shadertoy plugins, served from Cloudflare Workers. README is in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TakuyaAbe/jev-vj) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://jevj.sayuno.me) |
| Pricing and access | Public demo at [jevj.sayuno.me](https://jevj.sayuno.me) opens without an account (checked 2026-11-15; Jev calls run on the maker's key and are rate-limited). Self-hosting needs your own TypeSafe key and Cloudflare costs. Source has no license file. |
| Jev evidence | [`worker/index.ts`](https://github.com/TakuyaAbe/jev-vj/blob/f8f1fab639e39ee5f12db95289a0a484ec695de5/worker/index.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TakuyaAbe](https://github.com/TakuyaAbe). Independently curated. |
| Format | Web app (TypeScript, three.js) on Cloudflare Workers; public demo site |
| Platform and availability | Web (hosted demo on Cloudflare Workers; no login) · local dev build |
| Jev's role | Jev reads summaries of recent bars and decides section, upcoming drop, scene, intensity, palette and transitions; code handles beat-level reactions. |
| Requirements | Modern browser for the demo; for your own copy, Node.js, a `TYPESAFE_API_KEY` and optionally a Cloudflare account. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Use Jev for slow, bar-level musical judgements while code handles every frame.
- Mismatch: direct audio understanding; Jev only sees text summaries of the audio.

## How it works

`worker/index.ts` relays `/api/jev` to `https://api.typesafe.ai/v1/systemone` (`jev-latest` from `wrangler.jsonc`) with the key held as a Worker secret, same-origin checks, an allow-list of question IDs and rate limits. Integration evidence: [`worker/index.ts`](https://github.com/TakuyaAbe/jev-vj/blob/f8f1fab639e39ee5f12db95289a0a484ec695de5/worker/index.ts).

## Get started

Open the public demo, or run locally with your key.

```sh
git clone https://github.com/TakuyaAbe/jev-vj && cd jev-vj
export TYPESAFE_API_KEY=...
npm install
npm run dev        # http://localhost:5183
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Public demo: [jevj.sayuno.me](https://jevj.sayuno.me)
- README (Japanese): [github.com/TakuyaAbe/jev-vj/blob/f8f1fab639e39ee5f12db95289a0a484ec695de5/README.md](https://github.com/TakuyaAbe/jev-vj/blob/f8f1fab639e39ee5f12db95289a0a484ec695de5/README.md)

## Limits and data handling

Bar summaries (text, not audio) are sent to TypeSafe on the maker's key on the public site, or on yours locally. Bundled demo tracks carry their own Creative Commons licenses, several non-commercial. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit f8f1fab639e3](https://github.com/TakuyaAbe/jev-vj/tree/f8f1fab639e39ee5f12db95289a0a484ec695de5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
