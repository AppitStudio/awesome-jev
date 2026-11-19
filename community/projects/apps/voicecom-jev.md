# voicecom-jev by Matthew Ruiz Diaz (hold a key, say several commands at once, and Jev decides what your Mac does)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Push-to-talk voice control for macOS: local faster-whisper transcribes, Jev decides which command each part of the sentence is, whether it is destructive or just filler, and which button you meant, and plain code runs the actions with a confirm step for risky or unsure ones.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MatthewRuizDiaz/voicecom-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/MatthewRuizDiaz/voicecom-jev#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source build; Jev calls are billed to your own TypeSafe key. Speech-to-text runs locally. Checked 2026-11-20. |
| Jev evidence | [`voicecom/jev.py`](https://github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/voicecom/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [MatthewRuizDiaz](https://github.com/MatthewRuizDiaz). Independently curated. |
| Format | Python macOS app (MIT) |
| Platform and availability | macOS (Apple Silicon or Intel). |
| Jev's role | Choice over the command set for the whole sentence and each candidate split, plus Noul checks for destructive steps and filler; thresholds decide run, ask or ignore. |
| Requirements | macOS, Python 3.10+, PortAudio, a TypeSafe API key, and Microphone, Input Monitoring and Accessibility permissions. |
| License | [MIT](https://github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/LICENSE) |

## When to use

- Control windows, apps, typing and buttons on a Mac by voice, several steps per sentence, with a visible confidence panel.
- Mismatch: Windows or Linux, or fully offline use (decisions need the TypeSafe API).

## How it works

`voicecom/jev.py` uses the `typesafe_sdk` client to send one request per sentence with a `Choice` over up to 255 commands for the whole sentence and every candidate part, and `Noul` questions for destructive and meaningful speech; code runs at 80% or more, asks between 40% and 80% and ignores the rest. Integration evidence: [`voicecom/jev.py`](https://github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/voicecom/jev.py).

## Get started

Clone, install the requirements, add your key and run the permission check.

```sh
brew install python@3.12 portaudio
git clone https://github.com/MatthewRuizDiaz/voicecom-jev.git && cd voicecom-jev
python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env   # add TYPESAFE_API_KEY
.venv/bin/python -m voicecom --check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with demo video: [github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/README.md](https://github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/README.md)
- Glossary: [github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/GLOSSARY.md](https://github.com/MatthewRuizDiaz/voicecom-jev/blob/3fc9cacc11d333a461d76242cbabb072df719998/GLOSSARY.md)

## Limits and data handling

Audio stays on the Mac; transcripts and command candidates are sent to TypeSafe. It needs broad macOS permissions (Accessibility, Input Monitoring). Unofficial personal project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 3fc9cacc11d3](https://github.com/MatthewRuizDiaz/voicecom-jev/tree/3fc9cacc11d333a461d76242cbabb072df719998). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
