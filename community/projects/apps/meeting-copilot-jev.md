# Meeting copilot by Dzmitry Harupa (Russian-language Google Meet helper where Jev spots questions aimed at you and picks an answer card or hands off to Claude Code)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Self-hosted call helper for Google Meet on a Mac: a Chrome extension streams the call tab and your microphone to a local server, Deepgram transcribes, and a Jev judge decides whether a question is addressed to you, which card from your answer bank fits and how hard it is; harder ones go to a read-only Claude Code session in your project folder. Answers appear in Chrome's side panel. Interface and prompts are in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d7561985/meeting-copilot) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/d7561985/meeting-copilot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free to build from source; you pay for your own Deepgram and TypeSafe usage and need a Claude Code subscription. No licence file, so no reuse rights are granted. Checked 2026-11-27. |
| Jev evidence | [`server/router.js`](https://github.com/d7561985/meeting-copilot/blob/b88a6bf628a69c62d3db40000399c911123507b9/server/router.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Dzmitry Harupa](https://github.com/d7561985) (d7561985). Independently curated. |
| Format | Chrome extension + Node.js local server + Swift tray app |
| Platform and availability | macOS with Chrome (unpacked extension), Node.js 20+ local server under launchd and a menu-bar tray app. |
| Jev's role | `server/router.js` sends each finished utterance with your profile and card list to Jev as typed questions (to you or not, which card, difficulty); with no TypeSafe key the judge falls back to Claude Haiku, which the README says is slower (about 3 s). |
| Requirements | macOS, Chrome, Node.js 20+, Claude Code signed in, Deepgram and TypeSafe API keys. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Russian-speaking people who take many calls on Google Meet and want prepared answers from their own notes and project.
- Mismatch: other meeting apps or languages; it is built for Meet in Chrome and its prompts are Russian.

## How it works

Deepgram Nova-3 transcribes the two channels; `server/router.js` posts each utterance to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) and routes to a bank card or to Claude Code, which is limited to Read, Grep, Glob and Skill tools. Integration evidence: [`server/router.js`](https://github.com/d7561985/meeting-copilot/blob/b88a6bf628a69c62d3db40000399c911123507b9/server/router.js).

## Get started

Add keys to `.env`, copy the example profile, install the service and load the extension.

```sh
git clone https://github.com/d7561985/meeting-copilot && cd meeting-copilot
cp .env.example .env    # DEEPGRAM_API_KEY=..., TYPESAFE_API_KEY=...
cp -r profile.example profile
bash tray/install.sh
# chrome://extensions → Load unpacked → extension/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example profile: [github.com/d7561985/meeting-copilot/tree/main/profile.example](https://github.com/d7561985/meeting-copilot/tree/main/profile.example)

## Limits and data handling

Call audio of every participant goes to Deepgram and utterances go to TypeSafe; transcripts are saved locally. Tell participants and follow local recording-consent rules. No licence file. Not run on the review host.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit b88a6bf628a6](https://github.com/d7561985/meeting-copilot/tree/b88a6bf628a69c62d3db40000399c911123507b9). Inspected the README, `server/router.js`, `server/pipeline.js` and the extension folder at the pinned commit; no licence file present. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
