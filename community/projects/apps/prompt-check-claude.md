# Prompt Check (live overlay that grades the prompt you type into the Claude app and suggests an effort level, using Jev)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Mac and Windows overlay that sits above the Claude desktop app's message box and, as you type, has Jev decide whether the message is a task, follow-up, reply or question, grade it, list what is missing and suggest the effort level to run it at; a side window works with any app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jjlinucb/prompt-check) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jjlinucb/prompt-check#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-13. |
| Jev evidence | [`server.mjs`](https://github.com/jjlinucb/prompt-check/blob/8bcc7852e3af700251c45f9dc6f7781b6e344073/server.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jjlinucb](https://github.com/jjlinucb). Independently curated. |
| Format | Local Node server with a Swift (Mac) or PowerShell (Windows) overlay (no license file) |
| Platform and availability | macOS and Windows (source launchers); Windows path untested by the author; no packaged release verified |
| Jev's role | Jev classifies each draft (task, follow-up, reply or question), grades clarity and missing parts, and picks a suggested effort level. |
| Requirements | Node 20+, a TypeSafe API key saved in `~/.config/prompt-check/.env`, and the Claude desktop app for the live overlay; macOS Accessibility permission on Mac. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Catch vague task prompts before sending them to Claude, and pick an effort level.
- Mismatch: if you can't send what you type to a third party; pause it for sensitive text.

## How it works

`server.mjs` listens on 127.0.0.1 and sends the draft (plus the end of Claude's last reply, read from local Claude Code transcripts) to `https://api.typesafe.ai` with the model pinned to `jev-1.13.0`; the author reports 70 to 200 ms and about USD 0.00005 per check. The Windows overlay is marked as not yet run on Windows. Integration evidence: [`server.mjs`](https://github.com/jjlinucb/prompt-check/blob/8bcc7852e3af700251c45f9dc6f7781b6e344073/server.mjs).

## Get started

Save your key once, then double-click the launcher for the live overlay or the side window.

```sh
mkdir -p ~/.config/prompt-check
# save TYPESAFE_API_KEY=... in ~/.config/prompt-check/.env
open "Prompt Check Live.command"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jjlinucb/prompt-check/blob/8bcc7852e3af700251c45f9dc6f7781b6e344073/README.md](https://github.com/jjlinucb/prompt-check/blob/8bcc7852e3af700251c45f9dc6f7781b6e344073/README.md)

## Limits and data handling

While the overlay runs, everything typed into Claude's message box and the end of Claude's last reply go to TypeSafe on your key. The overlay reads the box through accessibility APIs.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 8bcc7852e3af](https://github.com/jjlinucb/prompt-check/tree/8bcc7852e3af700251c45f9dc6f7781b6e344073). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
