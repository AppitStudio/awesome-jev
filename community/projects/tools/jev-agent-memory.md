# jev-agent-memory (no vector DB: Jev picks which past chats and profile facts a Claude Code agent recalls)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Unattended memory for a Claude Code agent you talk to through Telegram or Discord: hooks capture the chat, Claude Haiku summarizes it into daily Markdown logs every 30 minutes, and on each message Jev picks the topic and which past excerpts would help, injecting at most four. A daily job distills up to three evidence-backed traits into a user profile. Unofficial; English and Korean docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hojeongna/jev-agent-memory) |
| Maintainer | [hojeongna](https://github.com/hojeongna). Independently curated. |
| Format | Python CLI (`jevmem`) with Claude Code hooks |
| Requirements | Claude Code with a chat channel plugin, Python (pipx) and a TypeSafe API key; launchd or cron. |
| License | [MIT](https://github.com/hojeongna/jev-agent-memory/blob/d74c1896095855b535fcc77cf146017b545182b0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevmem/jev_client.py`](https://github.com/hojeongna/jev-agent-memory/blob/d74c1896095855b535fcc77cf146017b545182b0/src/jevmem/jev_client.py) at the pinned commit. |

## When to use

- Give a long-running chat agent memory without running a vector database.
- Mismatch: routing quality depends on writing a topic list for your own logs.

## How it works

`src/jevmem/jev_client.py` is a small client that posts the message, topics and candidate excerpts to the configured Jev URL (`jev-latest` by default). Integration evidence: [`src/jevmem/jev_client.py`](https://github.com/hojeongna/jev-agent-memory/blob/d74c1896095855b535fcc77cf146017b545182b0/src/jevmem/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hojeongna/jev-agent-memory.git && pipx install ./jev-agent-memory
cd ~/my-agent && jevmem init --logs memory
jevmem install-hook && jevmem doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/hojeongna/jev-agent-memory#readme](https://github.com/hojeongna/jev-agent-memory#readme)

## Limits and data handling

Messages and log excerpts go to TypeSafe for recall and to Claude for summaries; logs stay as local Markdown.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit d74c18960958](https://github.com/hojeongna/jev-agent-memory/tree/d74c1896095855b535fcc77cf146017b545182b0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
