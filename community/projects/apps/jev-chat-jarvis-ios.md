# Jev Jarvis for iOS (custom keyboard that shows a chat message's intent, risk and ranked reply suggestions in any chat app)

[All projects](../README.md) · [iOS apps](README.md#ios-apps)

iPhone custom keyboard from the jev-chat-jarvis family: copy a message (or turn on Live Mode, which reads the screen with on-device OCR), and the keyboard shows the message's intent and risk and ranks drafted reply candidates with Jev; one tap inserts a reply. Chinese and English UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jev-chat/jev-chat-jarvis-ios) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jev-chat/jev-chat-jarvis-ios#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (a free Apple ID works for signing); judge and LLM usage on your own keys. Checked 2026-11-13. |
| Jev evidence | [`Shared/JevModel.swift`](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/Shared/JevModel.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Companion to the listed Android app jev-chat-jarvis. |
| Maintainer | [jev-chat](https://github.com/jev-chat). Independently curated. |
| Format | iOS app with keyboard and broadcast extensions, built in Xcode (Swift, MIT) |
| Platform and availability | iPhone, iOS 16+; self-built and signed in Xcode (no App Store listing verified) |
| Jev's role | Jev judges each message's intent and risk and ranks the drafted reply candidates. |
| Requirements | A Mac with Xcode 15+ and an Apple ID to sign, an iPhone on iOS 16+, a TypeSafe, OpenRouter or Vercel AI Gateway key for the Jev judge, and an LLM key for drafting replies. |
| License | [MIT](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/LICENSE) |

## When to use

- Get intent, risk and reply suggestions without leaving WeChat or any other chat app.
- Mismatch: if you need an App Store install; it is a self-signed Xcode build.

## How it works

`Shared/JevModel.swift` defines the judge presets: TypeSafe direct (`https://api.typesafe.ai`, `jev-latest`, the default), OpenRouter Decisions (`typesafe/jev-1.13`) and Vercel AI Gateway (`typesafe-ai/jev`); `Shared/JevJudge.swift` asks for intent, risk and ranking. Reply drafts come from an OpenAI-compatible LLM preset (default Zhipu glm-4-flash). Without a judge key it only drafts, with no intent or risk. Integration evidence: [`Shared/JevModel.swift`](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/Shared/JevModel.swift).

## Get started

Open the Xcode project on a Mac, sign with your Apple ID, run on your iPhone, enable the keyboard and enter your keys in the app.

```sh
open JevJarvis.xcodeproj   # select your Team, choose your iPhone, Cmd+R
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (English): [github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/README.en.md](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/README.en.md)
- Demo GIF: [github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/docs/demo.gif](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03/docs/demo.gif)

## Limits and data handling

Copied or OCR-read message text goes to the judge provider and to the LLM provider you configure, on your keys. Keys are stored in the shared App Group.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 2877e61a6f0b](https://github.com/jev-chat/jev-chat-jarvis-ios/tree/2877e61a6f0b3ca719602d7cf955eb02f1f8fd03). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
