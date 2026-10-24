# Call Coach by Darlison (live interview checklist on macOS, ticked by Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Live checklist for interviews and discovery calls: whisper.cpp transcribes both sides on your Mac, Jev ticks off each question once it is answered, tracks which listed question you just asked and flags answers worth a follow-up, and an MCP server lets your AI add follow-ups.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ByronDarlison/call-coach) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/ByronDarlison/call-coach#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-24. |
| Jev evidence | [`callcoach/jev.py`](https://github.com/ByronDarlison/call-coach/blob/d831f4a531a2eb64dd0847a667fc2a5b4afff957/callcoach/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ByronDarlison](https://github.com/ByronDarlison). Independently curated. |
| Format | Local web app with Swift audio helper and MCP server (Python) |
| Platform and availability | macOS on Apple silicon; local page at localhost:4800 after running the installer. |
| Jev's role | Core for automatic ticking: yes/no and choice questions on recent transcript lines. Without a key you tick by hand. |
| Requirements | macOS 15+ on Apple silicon, Homebrew, Command Line Tools, headphones; a TypeSafe key for automatic ticking. |
| License | [MIT](https://github.com/ByronDarlison/call-coach/blob/d831f4a531a2eb64dd0847a667fc2a5b4afff957/LICENSE) |

## When to use

- Keep track of your question list during an interview without taking notes.
- Get a follow-up suggestion only when an answer is worth it.
- Mismatch: needs headphones; audio capture is macOS only.

## How it works

`callcoach/jev.py` posts the last few minutes of transcript and your questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), or to your own proxy that holds the key. Integration evidence: [`callcoach/jev.py`](https://github.com/ByronDarlison/call-coach/blob/d831f4a531a2eb64dd0847a667fc2a5b4afff957/callcoach/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ByronDarlison/call-coach.git
cd call-coach
./scripts/install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ByronDarlison/call-coach#readme](https://github.com/ByronDarlison/call-coach#readme)

## Limits and data handling

Audio never leaves the Mac; transcript text and your questions go to TypeSafe. Tell the other person if you transcribe a call.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit d831f4a531a2](https://github.com/ByronDarlison/call-coach/tree/d831f4a531a2eb64dd0847a667fc2a5b4afff957). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
