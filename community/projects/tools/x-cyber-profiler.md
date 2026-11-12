# X Cyber-Profiler (Tampermonkey script that labels X accounts from Jev assessments)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Local-first Tampermonkey userscript that reads public posts already rendered on your X timeline, asks a System One endpoint (Jev by default via a local Magpie server or TypeSafe) 22 typed questions about each account, and has a chat model name an evolving profile label; it never blocks, hides or writes to X.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JohnWangggg/x-cyber-profiler) |
| Maintainer | [JohnWangggg](https://github.com/JohnWangggg). Independently curated. |
| Format | Tampermonkey userscript (JavaScript, MIT; README in Chinese and English) |
| Requirements | A browser with Tampermonkey, plus either a local Magpie server (no key) or a TypeSafe key and an OpenAI-compatible chat endpoint for naming. |
| License | [MIT](https://github.com/JohnWangggg/x-cyber-profiler/blob/28f70ef31ec4672b3e66b726335d9c36be0cd314/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers.js`](https://github.com/JohnWangggg/x-cyber-profiler/blob/28f70ef31ec4672b3e66b726335d9c36be0cd314/src/providers.js) at the pinned commit. |

## When to use

- Get playful, evolving labels for accounts on your own timeline.
- See a typed assessment with evidence cards behind each label.
- Mismatch: labels are model inferences, not facts; reads only what is on screen.

## How it works

`src/providers.js` posts to the configured `/systemone` URL (default `https://api.typesafe.ai/v1` or local Magpie at `http://127.0.0.1:3425/v1`) with category, trait, valence/energy and evidence questions; a rename gate only calls the chat model when the assessment really changes. Integration evidence: [`src/providers.js`](https://github.com/JohnWangggg/x-cyber-profiler/blob/28f70ef31ec4672b3e66b726335d9c36be0cd314/src/providers.js).

## Get started

Install the userscript from the repo's `dist` folder, open X, and pick the local Magpie or TypeSafe settings in the script menu.

```sh
https://raw.githubusercontent.com/JohnWangggg/x-cyber-profiler/main/dist/x-cyber-profiler.user.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/JohnWangggg/x-cyber-profiler/blob/28f70ef31ec4672b3e66b726335d9c36be0cd314/README.en.md](https://github.com/JohnWangggg/x-cyber-profiler/blob/28f70ef31ec4672b3e66b726335d9c36be0cd314/README.en.md)

## Limits and data handling

Public post samples go to the evaluator and naming endpoints you configure; profiles stay in local userscript storage. Labels are inferences about real people; use them with care.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 28f70ef31ec4](https://github.com/JohnWangggg/x-cyber-profiler/tree/28f70ef31ec4672b3e66b726335d9c36be0cd314). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
