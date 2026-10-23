# DSB (trust-first Android AI assistant with a Jev command gate)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Open-source Android assistant built on DeepSeek Harness that operates apps on a background virtual display of your own phone, with execution gates, a task ledger and audit logs; an optional Jev gate classifies suspicious shell commands before they run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tianye1999/dsb) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/tianye1999/dsb#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free to install. DeepSeek and TypeSafe usage are billed to your keys. Checked 2026-10-23. |
| Jev evidence | [`agent/check_gate.py`](https://github.com/tianye1999/dsb/blob/6e33bf90410cef9bdf904be574a1ef944fce1dda/agent/check_gate.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tianye1999](https://github.com/tianye1999). Independently curated. |
| Format | Android runtime and installer (Python agent with DeepSeek Harness) |
| Platform and availability | Android 11+ via the project's installer; validated so far on the maintainer's device and an arm64 emulator. |
| Jev's role | Optional safety gate: Jev classifies the kind of each suspicious shell command and whether it would leak secrets, in shadow (log-only) mode by default. |
| Requirements | Android 11+ phone (no root); a DeepSeek API key; optional TypeSafe API key for the Jev gate. |
| License | [Apache-2.0](https://github.com/tianye1999/dsb/blob/6e33bf90410cef9bdf904be574a1ef944fce1dda/LICENSE) |

## When to use

- Delegate app chores on your phone while keeping risky actions blocked.
- Add a second, semantic check to deterministic command rules.
- Mismatch: gates are not a safety guarantee, per the README.

## How it works

`agent/check_gate.py` runs on DSH's PreToolUse hook, allows clearly read-only commands by whitelist, and sends the rest through `agent/jev_client.py` to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with a choice and a noul question; it fails open if Jev is unavailable. Integration evidence: [`agent/check_gate.py`](https://github.com/tianye1999/dsb/blob/6e33bf90410cef9bdf904be574a1ef944fce1dda/agent/check_gate.py).

## Get started

Follow the [install guide](https://github.com/tianye1999/dsb/blob/main/docs/INSTALL.md) (not run on the review host); it starts from a clone:

```sh
git clone https://github.com/tianye1999/dsb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture: [github.com/tianye1999/dsb/blob/main/docs/ARCHITECTURE.md](https://github.com/tianye1999/dsb/blob/main/docs/ARCHITECTURE.md)
- Threat model: [github.com/tianye1999/dsb/blob/main/docs/THREAT-MODEL.md](https://github.com/tianye1999/dsb/blob/main/docs/THREAT-MODEL.md)

## Limits and data handling

With a TypeSafe key, suspicious command excerpts (up to 1,500 characters) go to TypeSafe; DeepSeek receives conversation and screen context.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 6e33bf90410c](https://github.com/tianye1999/dsb/tree/6e33bf90410cef9bdf904be574a1ef944fce1dda). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
