# Jarvis by craigraphics (macOS voice-command CLI where patterns go first, Jev decides the rest and an LLM only writes)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Say "Jarvis, ..." and it opens apps, plays music, sets reminders, checks the calendar, drafts emails (always left for you to send), writes Obsidian notes and runs Shortcuts. Exact command shapes are handled by patterns; with a TypeSafe key, Jev picks the action for natural phrasing and ignores questions and small talk; an optional LLM only fills details and writes drafts. Early experiment, macOS only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/craigraphics/jarvis) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/craigraphics/jarvis#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; Jev needs your own TypeSafe key and an LLM key is optional, each with provider charges. No hosted plan found. Checked 2026-11-05. |
| Jev evidence | [`jarvis/router.py`](https://github.com/craigraphics/jarvis/blob/d15552540a4f05270f184c12f05267cdc0202d12/jarvis/router.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/willcraigz/status/2118083436347068696)). |
| Maintainer | [craigraphics](https://github.com/craigraphics). Independently curated. |
| Format | Python 3.11+ CLI installed with uv (macOS only) |
| Platform and availability | macOS (terminal command installed with uv); no other platform. |
| Jev's role | Picks which skill action a spoken or typed command means, and answers 'unknown' for questions and small talk. |
| Requirements | macOS, Python 3.11+ and uv; a TypeSafe key (early-access console) for the Jev step, an LLM key only for email drafts and dates. |
| License | [MIT](https://github.com/craigraphics/jarvis/blob/d15552540a4f05270f184c12f05267cdc0202d12/LICENSE) |

## When to use

- Control a Mac by voice or typed commands with a cheap, mostly offline decision path and Jev as the fallback for loose phrasing.
- Mismatch: it is an early one-person experiment on macOS 26, and the Jev step needs an early-access TypeSafe key.

## How it works

`jarvis/router.py` tries exact patterns first, then asks Jev (`jev-latest` by default, via the TypeSafe SDK) to choose among the skill actions in one call; below a 0.6 confidence the optional LLM chooses from the same list, and only then keywords. Integration evidence: [`jarvis/router.py`](https://github.com/craigraphics/jarvis/blob/d15552540a4f05270f184c12f05267cdc0202d12/jarvis/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install git+https://github.com/craigraphics/jarvis
jarvis setup
jarvis doctor
jarvis
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the decision ladder, built-in skills and email flow: [github.com/craigraphics/jarvis#readme](https://github.com/craigraphics/jarvis#readme)
- Announcement post on X: [x.com/willcraigz/status/2118083436347068696](https://x.com/willcraigz/status/2118083436347068696)

## Limits and data handling

With a Jev key, the command text goes to TypeSafe on your key; email drafting sends details to the LLM you choose. The README's figures (69 measured commands, patterns on 54% and Jev on 46% with a 116 ms median) are the author's own and were not reproduced. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit d15552540a4f](https://github.com/craigraphics/jarvis/tree/d15552540a4f05270f184c12f05267cdc0202d12). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
