# Jev Companion (read-only WeChat conversation companion with typed Jev judgments)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Native macOS and Windows companion that reads the text of the current WeChat window (or pasted text) and places Jev judgment cards under each message: communication needs, next actions and conversation tension, plus optional reply drafts from a local OpenAI-compatible model; it never sends messages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jimmy1340/jev-companion) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jimmy1340/jev-companion#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-25. |
| Jev evidence | [`macos/backend/typesafe_client.py`](https://github.com/jimmy1340/jev-companion/blob/413ec458688aad73c88cfdacb1741f50cdb699f5/macos/backend/typesafe_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jimmy1340](https://github.com/jimmy1340). Independently curated. |
| Format | Native desktop app (Swift and Python on macOS, C# on Windows) |
| Platform and availability | macOS (app 0.3.1) and Windows preview (0.4.1); build from source. |
| Jev's role | Core: Jev Noul, Choice and Score questions produce the judgment cards; an optional separate model writes reply drafts. |
| Requirements | macOS 13+ with Python 3.9+ to build, or Windows 10 2004+/11 x64 with .NET SDK 10 to build; a TypeSafe API key. |
| License | [MIT](https://github.com/jimmy1340/jev-companion/blob/413ec458688aad73c88cfdacb1741f50cdb699f5/LICENSE) |

## When to use

- Get a second opinion on a tense WeChat conversation before you reply.
- Keep drafts local with your own OpenAI-compatible endpoint.
- Mismatch: README is partly Chinese; probabilities are estimates about text, not about the other person.

## How it works

`macos/backend/typesafe_client.py` posts the conversation prefix up to each message to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); the Windows client in `windows/Core/ModelClient.cs` does the same. Integration evidence: [`macos/backend/typesafe_client.py`](https://github.com/jimmy1340/jev-companion/blob/413ec458688aad73c88cfdacb1741f50cdb699f5/macos/backend/typesafe_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jimmy1340/jev-companion.git && cd jev-companion
bash macos/test.sh && bash macos/build.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy notes: [github.com/jimmy1340/jev-companion/blob/main/docs/PRIVACY.md](https://github.com/jimmy1340/jev-companion/blob/main/docs/PRIVACY.md)
- Validation record: [github.com/jimmy1340/jev-companion/blob/main/docs/VALIDATION.md](https://github.com/jimmy1340/jev-companion/blob/main/docs/VALIDATION.md)

## Limits and data handling

Conversation text goes to TypeSafe (and to your reply model if enabled). It does not send messages, modify WeChat or decrypt databases. The Windows OCR path is untested on real machines per the README.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 413ec458688a](https://github.com/jimmy1340/jev-companion/tree/413ec458688aad73c88cfdacb1741f50cdb699f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
