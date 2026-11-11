# Phone menu (voice IVR where Jev picks the stored reply line)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Next.js builder for phone menus run as a Vapi assistant: Deepgram listens, Jev picks the stored line for the current menu, and the agent speaks it instead of inventing a reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nayeemrahman13/voice-ivr) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nayeemrahman13/voice-ivr#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; no license file on the reviewed commit. You pay TypeSafe, Deepgram and Vapi usage. Checked 2026-11-11. |
| Jev evidence | [`lib/jev.ts`](https://github.com/nayeemrahman13/voice-ivr/blob/55d4e8f5e3e969fddd5624ee043d68ca08dfb83a/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. X poster's name matches the GitHub owner, but no cross-link was found. Discovered via X ([post](https://x.com/nayeemrahman_/status/2120227640002928678)). |
| Maintainer | [nayeemrahman13](https://github.com/nayeemrahman13). Independently curated. |
| Format | Web app (Next.js/TypeScript, source only) |
| Platform and availability | Web (self-hosted Next.js; Vapi phone calls) |
| Jev's role | Jev chooses which stored menu line or submenu matches what the caller said. |
| Requirements | Node.js, `TYPESAFE_API_KEY` (or `JEV_API_KEY`), plus Deepgram and Vapi keys for transcription and calls. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Route callers through an IVR by meaning, not keypresses.
- Keep a voice agent to pre-written lines.
- Mismatch: no license file (source-available); small demo project.

## How it works

`lib/jev.ts` posts the caller's words and the current menu options to `/v1/systemone` as a choice; `lib/decide.ts` maps the pick to the stored line or nested menu, and the app serves as a custom LLM for Vapi. Integration evidence: [`lib/jev.ts`](https://github.com/nayeemrahman13/voice-ivr/blob/55d4e8f5e3e969fddd5624ee043d68ca08dfb83a/lib/jev.ts).

## Get started

Copy `.env.example` to `.env.local`, add the keys, run the dev server and try a menu on the page before creating a Vapi assistant.

```sh
git clone https://github.com/nayeemrahman13/voice-ivr.git && cd voice-ivr
npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nayeemrahman13/voice-ivr/blob/55d4e8f5e3e969fddd5624ee043d68ca08dfb83a/README.md](https://github.com/nayeemrahman13/voice-ivr/blob/55d4e8f5e3e969fddd5624ee043d68ca08dfb83a/README.md)

## Limits and data handling

Caller transcripts go to TypeSafe, and audio to Deepgram/Vapi, on your keys.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 55d4e8f5e3e9](https://github.com/nayeemrahman13/voice-ivr/tree/55d4e8f5e3e969fddd5624ee043d68ca08dfb83a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
