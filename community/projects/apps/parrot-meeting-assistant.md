# Parrot (native macOS meeting recorder with a live AI assistant that can use Jev for instant answers from your own documents)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native SwiftUI meeting recorder for macOS 14+ that transcribes and detects speakers on-device, suggests answers from your own documents during a call and writes the report afterwards; no bot joins the meeting. With Claude mode and an optional TypeSafe key, Jev ranks up to twelve knowledge-base passages for a fast document answer and judges duplicate coaching cards.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/turantekin/Parrot) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://openparrot.app) |
| Pricing and access | Free per the README (no meeting bot or time limit); the assistant, cloud transcription and Jev path use your own keys or a local model. Checked 2026-11-05. |
| Jev evidence | [`Parrot/Services/JevDocMatcher.swift`](https://github.com/turantekin/Parrot/blob/c3510636a699584e0c2b03a439fe5e999e22f901/Parrot/Services/JevDocMatcher.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [turantekin](https://github.com/turantekin). Independently curated. |
| Format | Native macOS app (SwiftUI; GPL-3.0; signed and notarized releases) |
| Platform and availability | macOS 14+ (Apple Silicon recommended); releases via GitHub and the website |
| Jev's role | Optional fast path that scores which of up to twelve document chunks answers the question being asked, and judges whether two coaching cards flag the same issue. |
| Requirements | macOS 14 or newer (Apple Silicon recommended); an Assistant brain of your choice (Claude with your key, Ollama or an OpenAI-compatible server); a TypeSafe key only for the optional Jev document-answer path. |
| License | [GPL-3.0](https://github.com/turantekin/Parrot/blob/c3510636a699584e0c2b03a439fe5e999e22f901/LICENSE) |

## When to use

- Surface the passage from your FAQ or pricing sheet that answers the other side's question within a second of it being asked.
- Keep transcription, speaker detection and your documents on the Mac while choosing the assistant model.
- Mismatch: the Jev path is optional and exists only in Claude mode when a TypeSafe key is in the Keychain; everything else works without it.

## How it works

`JevDocMatcher.swift` posts the other side's question and up to twelve knowledge-base chunks to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` and a 0.7 second budget, reading one noul probability per chunk, and also compares pairs of coaching cards for duplicates. Integration evidence: [`Parrot/Services/JevDocMatcher.swift`](https://github.com/turantekin/Parrot/blob/c3510636a699584e0c2b03a439fe5e999e22f901/Parrot/Services/JevDocMatcher.swift).

## Get started

From the upstream README (not run on the review host):

```sh
# download the signed, notarized release from https://github.com/turantekin/Parrot/releases
# or build from source with XcodeGen (see README); add a TypeSafe key in Settings for Jev answers
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (features, engines, privacy, tech stack): [github.com/turantekin/Parrot/blob/c3510636a699584e0c2b03a439fe5e999e22f901/README.md](https://github.com/turantekin/Parrot/blob/c3510636a699584e0c2b03a439fe5e999e22f901/README.md)
- Website: [openparrot.app](https://openparrot.app)

## Limits and data handling

With the Jev path on, the question and a handful of matching document passages are sent to TypeSafe on your key; the Assistant and reports send call context to the model you pick unless you use a local one. Cloud speech engines and the Claude API need their own keys.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit c3510636a699](https://github.com/turantekin/Parrot/tree/c3510636a699584e0c2b03a439fe5e999e22f901). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
