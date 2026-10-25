# jev-voice-use (voice control for the whole Mac or a browser, decided by Jev as you speak)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Extended fork of the listed jev-voice-browser: streams speech word by word and, on each partial transcript, asks Jev a dozen typed questions (intent, target, is the command complete, is it addressed to me, is it destructive) so code can act, wait, ask or ignore; adds whole-Mac desktop mode and Italian and English commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrea-cappelluti/jev-voice-use) |
| Maintainer | [andrea-cappelluti](https://github.com/andrea-cappelluti). Independently curated. |
| Format | Node.js app with Playwright and a native macOS helper |
| Requirements | Node 20+, npm and Chromium via Playwright; macOS for desktop mode; a TypeSafe API key. |
| License | [MIT](https://github.com/andrea-cappelluti/jev-voice-use/blob/7148b4832fa91c7f3319a912c1f0957f9857e6f4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/andrea-cappelluti/jev-voice-use/blob/7148b4832fa91c7f3319a912c1f0957f9857e6f4/src/jev.js) at the pinned commit. |

## When to use

- Control your Mac or a browser hands-free with commands that run before you finish speaking.
- Study a working pattern where Jev only picks spans that code extracted, never generates text.
- Mismatch: while the mic is on, any recognised command acts on the front app; switch it off when done.

## How it works

`src/jev.js` uses `@typesafe-ai/sdk` (`jev-latest`; thresholds tuned on `jev-1.13.0`) to send the transcript and up to 100 page or window elements in one request; thresholds in `constants.js` decide the action. Integration evidence: [`src/jev.js`](https://github.com/andrea-cappelluti/jev-voice-use/blob/7148b4832fa91c7f3319a912c1f0957f9857e6f4/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/andrea-cappelluti/jev-voice-use.git && cd jev-voice-use
npm install && npx playwright install chromium
cp .env.example .env   # TYPESAFE_API_KEY
./run.sh               # add --browser for browser mode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/andrea-cappelluti/jev-voice-use#readme](https://github.com/andrea-cappelluti/jev-voice-use#readme)
- Upstream: [github.com/moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)

## Limits and data handling

Transcripts and element labels of the front window (not text-field contents) go to TypeSafe. Destructive clicks ask for a spoken confirm; desktop mode needs macOS Accessibility permission.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 7148b4832fa9](https://github.com/andrea-cappelluti/jev-voice-use/tree/7148b4832fa91c7f3319a912c1f0957f9857e6f4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
