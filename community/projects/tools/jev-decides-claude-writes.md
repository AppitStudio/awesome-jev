# Jev Decides, Claude Writes (Claude Code hook that delegates each message to Haiku, Sonnet, Opus or Fable)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code `UserPromptSubmit` hook: Jev answers one Choice question about each message (the smallest model that can do the job) and the main session delegates to one of four helper agents; short follow-ups, low-confidence picks, slow answers and messages that look like they contain a secret stay with the main session.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TechPreacher/jev_router) |
| Maintainer | [TechPreacher](https://github.com/TechPreacher). Independently curated. |
| Format | Claude Code hook (Python, standard library) |
| Requirements | macOS or Linux with Claude Code; a TypeSafe API key. |
| License | [MIT](https://github.com/TechPreacher/jev_router/blob/dea7d22260f96d0c13565b693cf4fe78da3903c8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`files/router.py`](https://github.com/TechPreacher/jev_router/blob/dea7d22260f96d0c13565b693cf4fe78da3903c8/files/router.py) at the pinned commit. |

## When to use

- Push routine Claude Code work to cheaper helper models.
- Mismatch: the main model still reads every message, so savings come only from delegated work.

## How it works

`files/router.py` posts the message to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and delegates when the top pick is at least 60% likely. Integration evidence: [`files/router.py`](https://github.com/TechPreacher/jev_router/blob/dea7d22260f96d0c13565b693cf4fe78da3903c8/files/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/TechPreacher/jev_router && cd jev_router
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How it works and limits: [github.com/TechPreacher/jev_router/blob/main/files/README.md](https://github.com/TechPreacher/jev_router/blob/main/files/README.md)

## Limits and data handling

Each message (unless it looks like a secret) goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit dea7d22260f9](https://github.com/TechPreacher/jev_router/tree/dea7d22260f96d0c13565b693cf4fe78da3903c8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
