# steezen-stt (push-to-talk dictation with a TypeSafe Jev dictionary corrector)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Native Rust push-to-talk speech-to-text for Linux X11 and Windows that transcribes with OpenAI, Groq or whisper.cpp, then fixes misheard dictionary words with TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/slgotting/steezen-stt) |
| Maintainer | [slgotting](https://github.com/slgotting). Independently curated. |
| Format | Rust desktop app (no SPDX license file on the reviewed commit) |
| Requirements | Rust toolchain or release binary, a transcription backend, and a TypeSafe API key for correction. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/src/corrector.rs`](https://github.com/slgotting/steezen-stt/blob/d37d657c8c9e5cabd7cef26807470018e2f8b191/core/src/corrector.rs) at the pinned commit. |

## When to use

- Dictate with domain words fixed automatically.
- Run local whisper.cpp with a fast correction step.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`core/src/corrector.rs` posts to `https://api.typesafe.ai/v1/systemone` to choose dictionary corrections for transcribed text. Integration evidence: [`core/src/corrector.rs`](https://github.com/slgotting/steezen-stt/blob/d37d657c8c9e5cabd7cef26807470018e2f8b191/core/src/corrector.rs).

## Get started

Build with cargo, set the TypeSafe key in settings, and bind the hotkey.

```sh
git clone https://github.com/slgotting/steezen-stt.git && cd steezen-stt
export TYPESAFE_API_KEY=...
cargo build --release
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/slgotting/steezen-stt/blob/d37d657c8c9e5cabd7cef26807470018e2f8b191/README.md](https://github.com/slgotting/steezen-stt/blob/d37d657c8c9e5cabd7cef26807470018e2f8b191/README.md)

## Limits and data handling

Transcribed text is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit d37d657c8c9e](https://github.com/slgotting/steezen-stt/tree/d37d657c8c9e5cabd7cef26807470018e2f8b191). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
