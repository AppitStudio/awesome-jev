# agentmailguard (daemon that sits between an AI agent and your Microsoft 365 or Gmail mailbox, with Jev screening each message for prompt injection)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Daemon and small command-line client that give an agent your mail and calendar without giving it your mailbox. Jev screens every message for prompt injection before the agent reads it (green, yellow, red, sealed or error, failing closed), hides unsafe text, checks the text of each draft or send, and a write policy plus a password-protected approval console decide what runs. It is marked experimental.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ivanrvpereira/agentmailguard) |
| Maintainer | [ivanrvpereira](https://github.com/ivanrvpereira). Independently curated. |
| Format | Go daemon and CLI (`amgd`, `amg`; Homebrew) |
| Requirements | Go 1.26 and a C compiler to build, or Homebrew; a Microsoft 365 or Gmail account; an OpenRouter or TypeSafe key for Jev screening (a fake screener is available for tests). |
| License | [Apache-2.0](https://github.com/ivanrvpereira/agentmailguard/blob/81d403b1edec76ff1de06e738d586ef37a371369/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/screening/screening.go`](https://github.com/ivanrvpereira/agentmailguard/blob/81d403b1edec76ff1de06e738d586ef37a371369/internal/screening/screening.go) at the pinned commit. |

## When to use

- Put a screening and approval layer between an AI agent and your inbox, so injected instructions in mail cannot make it act.
- Mismatch: experimental; the agent must not have a shell as the daemon's user, and a green verdict does not guarantee text is safe.

## How it works

`internal/screening/screening.go` sends each message or agent action to the System One endpoint through OpenRouter (`typesafe/jev-1.14`) or TypeSafe directly and maps the typed verdict to green, yellow or red; missing or failed screening gives the agent no body, and the write policy runs, holds or refuses each action. Integration evidence: [`internal/screening/screening.go`](https://github.com/ivanrvpereira/agentmailguard/blob/81d403b1edec76ff1de06e738d586ef37a371369/internal/screening/screening.go).

## Get started

From the upstream README (not run on the review host):

```sh
brew install ivanrvpereira/tap/agentmailguard
export AMG_HOME="$(mktemp -d)"
amgd config set screening.provider fake   # tests only, no key
amgd account add demo --provider fake
amgd serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the verdicts, write policy and approval console: [github.com/ivanrvpereira/agentmailguard#readme](https://github.com/ivanrvpereira/agentmailguard#readme)
- Screening and privacy notes: [github.com/ivanrvpereira/agentmailguard/blob/main/docs/screening.md](https://github.com/ivanrvpereira/agentmailguard/blob/main/docs/screening.md)

## Limits and data handling

Mail content, calendar details, rule instructions and agent action text go to Jev through OpenRouter (or TypeSafe) before any verdict exists, including mail the agent never sees; the project promises no zero-retention or processing region. Screening is probabilistic. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 81d403b1edec](https://github.com/ivanrvpereira/agentmailguard/tree/81d403b1edec76ff1de06e738d586ef37a371369). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
