# JARVIS · GNANI Edition (voice-controlled Windows agent with a control ladder where Jev resolves ambiguous UI targets before OCR or Claude vision)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Hold a hotkey and speak: Gnani speech APIs transcribe, Claude Code plans, and JARVIS carries the task out on the real Windows desktop (apps, windows, browser, files, terminal, keyboard and mouse) and checks the result. Each action goes down a ladder: deterministic shortcuts, Windows UI Automation, a Jev reflex for ambiguous targets, OCR, Claude vision, and finally the human for UAC, logins, MFA and CAPTCHAs. Destructive actions wait for your click; a contextual bandit learns which rung works.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prabindersinghh/Jarvis-GNANI) |
| Maintainer | [prabindersinghh](https://github.com/prabindersinghh). Independently curated. |
| Format | Python Windows agent with an 18-tool MCP surface (setup script) |
| Requirements | Windows 11, a Claude plan that includes Claude Code, Gnani speech API access, microphone; optional TypeSafe key for the Jev layer. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jarvis/jev/adapter.py`](https://github.com/prabindersinghh/Jarvis-GNANI/blob/0e4ad3ee67d25235c35375784e8072bbd9bdd34e/jarvis/jev/adapter.py) at the pinned commit. |

## When to use

- Cut vision calls in desktop automation by letting Jev pick among ambiguous UI candidates.
- Mismatch: macOS or Linux; it targets Windows 11.

## How it works

`jarvis/jev/adapter.py` sends one `POST /v1/systemone` with an operation head and a speculative target head (adapted from browser-use/jev-ultrafast), with retries and validation; `jarvis/jev/budget.py` enforces a local monthly spending cap and fails closed. Without a key, routing falls through to the next tier. Integration evidence: [`jarvis/jev/adapter.py`](https://github.com/prabindersinghh/Jarvis-GNANI/blob/0e4ad3ee67d25235c35375784e8072bbd9bdd34e/jarvis/jev/adapter.py).

## Get started

Clone and run the setup script (or open the folder in Claude Code and type /setup).

```sh
git clone https://github.com/prabindersinghh/Jarvis-GNANI.git D:\JARVIS
D:\JARVIS\setup.cmd
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/prabindersinghh/Jarvis-GNANI/blob/0e4ad3ee67d25235c35375784e8072bbd9bdd34e/README.md](https://github.com/prabindersinghh/Jarvis-GNANI/blob/0e4ad3ee67d25235c35375784e8072bbd9bdd34e/README.md)

## Limits and data handling

Speech goes to Gnani, planning to Claude, and ambiguous-target choices to TypeSafe on your key. The Jev layer is optional. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 0e4ad3ee67d2](https://github.com/prabindersinghh/Jarvis-GNANI/tree/0e4ad3ee67d25235c35375784e8072bbd9bdd34e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
