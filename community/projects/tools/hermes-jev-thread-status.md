# hermes-jev-thread-status (Hermes Agent plugin that keeps Discord and Telegram thread titles at a live status judged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for Hermes Agent that prefixes each Discord thread title with a status you define, such as `[Running]`, `[Needs feedback]` or `[Done]`. New user messages set a status directly; tool results and replies are judged by one small Jev request per batch that picks a status or `NO_CHANGE`, acting only at confidence 0.9 or higher. Optional stale-title detection and double-checked archiving are opt-in, renames respect Discord's budget, and it is off until you enable channels.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xiaoyaner0201/hermes-jev-thread-status) |
| Maintainer | [xiaoyaner0201](https://github.com/xiaoyaner0201). Independently curated. |
| Format | Python Hermes plugin with YAML status rules |
| Requirements | Hermes Agent (tested against v0.22.2), a Discord or Telegram bot setup and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/xiaoyaner0201/hermes-jev-thread-status/blob/99f188c9cc7d83d784ee0c47168df18b740d56fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/xiaoyaner0201/status/2118017004506591498)). |
| Jev evidence | [`thread_status/jev.py`](https://github.com/xiaoyaner0201/hermes-jev-thread-status/blob/99f188c9cc7d83d784ee0c47168df18b740d56fc/thread_status/jev.py) at the pinned commit. |

## When to use

- See at a glance which agent threads are running, waiting for you or finished without reading each one.
- Mismatch: it only works inside Hermes Agent, and archiving a thread on a model's say-so is something to enable carefully.

## How it works

`thread_status/jev.py` posts a state description with a `choice` question over your allowed statuses plus `noul` questions for completion, closing and a stale title to `https://api.typesafe.ai/v1/systemone`; code applies the confidence threshold and the rename budget. Integration evidence: [`thread_status/jev.py`](https://github.com/xiaoyaner0201/hermes-jev-thread-status/blob/99f188c9cc7d83d784ee0c47168df18b740d56fc/thread_status/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
hermes plugins install xiaoyaner0201/hermes-jev-thread-status
hermes config set TYPESAFE_API_KEY <your-key>
# copy examples/discord.yaml, list the channels it may manage, then enable it
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with statuses, rules and the flow diagram: [github.com/xiaoyaner0201/hermes-jev-thread-status#readme](https://github.com/xiaoyaner0201/hermes-jev-thread-status#readme)
- Announcement post on X: [x.com/xiaoyaner0201/status/2118017004506591498](https://x.com/xiaoyaner0201/status/2118017004506591498)

## Limits and data handling

Recent tool results and replies from enabled channels go to TypeSafe on your key; the main model only writes new titles when you opt in. A code comment records the author's own calibration (should-rename cases scored .72-.93); it was not reproduced. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 99f188c9cc7d](https://github.com/xiaoyaner0201/hermes-jev-thread-status/tree/99f188c9cc7d83d784ee0c47168df18b740d56fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
