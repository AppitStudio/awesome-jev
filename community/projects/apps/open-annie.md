# open-annie

[All projects](../README.md) · [Web apps](README.md#web-apps)

Voice-driven 3D character in the browser: GPT-Live-1 talks with you over WebRTC while TypeSafe Jev reads the live transcript and picks every face, gesture and dance (51 decisions at p50 118 ms and $0.0026 of Jev in the recorded session); lip-sync and rendering run in the browser behind a thin broker on fal serverless.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rehan-remade/open-annie) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/rehan-remade/open-annie#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the Apache-2.0 source; the scripted preview and recorded replay need no keys. Live conversation needs your own OpenAI key with GPT-Live access and a TypeSafe key (usage billed by each); optional fal deployment billed by fal. Checked 2026-10-07. |
| Jev evidence | [`packages/core/src/decide.js`](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/packages/core/src/decide.js) and [`instinct.js`](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/packages/core/src/instinct.js) choose expressions from the transcript; the broker's [`decide.py`](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/broker/annie_broker/decide.py) calls Jev; the recorded session ships with its real Jev decisions. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [rehan-remade](https://github.com/rehan-remade). Independently curated. |
| Format | Static browser stage + Python broker (local or fal serverless) |
| Platform and availability | Any modern browser; self-hosted static server plus local or fal-hosted broker; source build only. |
| Jev's role | Jev picks Annie's face while you talk and her gestures and body language while she talks; GPT-Live-1 generates the speech; code lip-syncs and animates. |
| Requirements | Python 3.12 (uv) for the broker; `OPENAI_API_KEY` with GPT-Live access and `TYPESAFE_API_KEY` for live sessions. |
| License | [Apache-2.0](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/LICENSE). |

## When to use

- See a live split between a talking model and a fast decision model that moves a character.
- Replay the recorded session frame by frame with its real Jev decisions, no keys needed.
- Mismatch: live talk requires GPT-Live access on your OpenAI account.

## How it works

The browser sends transcript fragments to the broker; Jev answers which expression or gesture fits (an 'instinct' while you speak, a few asks while she speaks). Persona and safety rules: [`persona/character.md`](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/persona/character.md). Assets carry their own licences ([`NOTICE`](https://github.com/rehan-remade/open-annie/blob/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507/NOTICE)).

## Get started

Look around without keys (README *Quick start*):

```sh
git clone https://github.com/rehan-remade/open-annie.git && cd open-annie
python3 -m http.server 8080      # open http://localhost:8080/stage/
# live: cp .env.example .env (OPENAI_API_KEY, TYPESAFE_API_KEY); run the broker per README
```

Live sessions bill GPT-Live-1 to OpenAI and expression decisions to TypeSafe.

## Examples and demos

- README demo video (one real recorded session) and replay URL with `demo/live/decisions.json`.

## Limits and data handling

Mic audio goes to OpenAI and transcript text to TypeSafe; upstream states the broker does not log transcripts and Annie discloses she is an AI. Avatars are pixiv VRoid samples under their own terms. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 1a3aebfe3234](https://github.com/rehan-remade/open-annie/tree/1a3aebfe32343b119263c8b7eba3b7cb1d4e4507). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
