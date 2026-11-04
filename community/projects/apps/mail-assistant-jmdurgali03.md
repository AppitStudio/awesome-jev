# Mail Assistant by jmdurgali03 (local-first Gmail read-only assistant that stages GPT preparation, a Jev priority decision and GPT rendering)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Experimental email assistant in Python and SQLite that reads Gmail read-only, gathers evidence, classifies priority and drafts short summaries, with private Telegram notifications through OpenClaw. Each analysis is staged: GPT prepares verified facts, Jev answers typed questions on priority, promotional and financial content, and GPT renders the result. It never sends, archives or changes mail, and the core and demo run without accounts. English and Spanish READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmdurgali03/mail-assistant) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jmdurgali03/mail-assistant#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; live use needs your own GPT, OpenClaw and TypeSafe access with their charges. No hosted plan was found. Checked 2026-11-04. |
| Jev evidence | [`src/jev_decisions.py`](https://github.com/jmdurgali03/mail-assistant/blob/17fd8163f3a6d82fea0b78052d3e93d72d1d77cd/src/jev_decisions.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jmdurgali03](https://github.com/jmdurgali03). Independently curated. |
| Format | Python 3.12 and Node.js 24 scripts with SQLite and optional systemd timers (Linux reference platform) |
| Platform and availability | Linux (reference platform), run from source; Telegram notifications through OpenClaw. |
| Jev's role | Classifies each prepared email's priority, promotional and financial nature as typed decisions. |
| Requirements | Linux, Python 3.12+, Node.js 24.16+, and for live use OpenClaw with its TypeSafe plugin, gogcli and Google OAuth. |
| License | [MIT](https://github.com/jmdurgali03/mail-assistant/blob/17fd8163f3a6d82fea0b78052d3e93d72d1d77cd/LICENSE) |

## When to use

- See a cautious email-triage pipeline where Jev classifies only prepared, bounded evidence and a failure means needs review.
- Mismatch: it is version 0.1.0, Linux-first, and live use depends on OpenClaw and operator-specific configuration.

## How it works

`src/jev_decisions.py` builds a bounded batch of prepared facts and asks `jev-1.13.0` choice questions through OpenClaw's maintained TypeSafe provider (`src/jev_gateway.mjs`), with no direct provider HTTP and no GPT fallback. Integration evidence: [`src/jev_decisions.py`](https://github.com/jmdurgali03/mail-assistant/blob/17fd8163f3a6d82fea0b78052d3e93d72d1d77cd/src/jev_decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jmdurgali03/mail-assistant.git
# see the README for the synthetic demo and scripts/check.sh; live Gmail and OpenClaw setup is operator-specific
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with architecture and the staged analysis flow: [github.com/jmdurgali03/mail-assistant#readme](https://github.com/jmdurgali03/mail-assistant#readme)

## Limits and data handling

Prepared email facts (not raw mail) go to TypeSafe through OpenClaw on your key, and earlier stages use a GPT provider; live integrations may incur provider charges. Install and live runs were not tested. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 17fd8163f3a6](https://github.com/jmdurgali03/mail-assistant/tree/17fd8163f3a6d82fea0b78052d3e93d72d1d77cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
