# mail-agent (always-on Gmail agent that uses Jev to sort mail into alerts, digests and todos in Telegram or Lark)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Personal email agent that runs on your own Mac or Linux machine: it watches Gmail over IMAP IDLE, Jev scores each email for importance, needed action and dates, and important mail reaches Telegram or Lark/Feishu within seconds while the rest waits for a twice-daily digest. You can chat with it to search mail or draft replies; it never sends without your tap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jaydccq/mail-agent) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/Jaydccq/mail-agent#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under Apache-2.0; you pay TypeSafe and any model provider through your own keys. Checked 2026-11-03. |
| Jev evidence | [`src/mailagent/ai/jev.py`](https://github.com/Jaydccq/mail-agent/blob/a78392b4f3057cf9f0cf6e741d6a7f7006d0fb3a/src/mailagent/ai/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Jaydccq](https://github.com/Jaydccq). Independently curated. |
| Format | Self-hosted Python service + Telegram or Lark/Feishu bot |
| Platform and availability | Self-hosted on macOS or Linux; Telegram or Lark/Feishu. |
| Jev's role | Scores each email for importance, needed action and dates. |
| Requirements | Mac or Linux, Python 3.11+, a Gmail app password, a Telegram bot token or Lark app, a Jev API key; optionally a Claude, Codex or Gemini CLI or another model for summaries. |
| License | [Apache-2.0](https://github.com/Jaydccq/mail-agent/blob/a78392b4f3057cf9f0cf6e741d6a7f7006d0fb3a/LICENSE) |

## When to use

- Get only the email that matters pushed to your chat app, with deadlines turned into reminders.
- Mismatch: Gmail via IMAP only; summaries and drafts need a separate generative model.

## How it works

`src/mailagent/ai/jev.py` posts each email to Jev's `/systemone` endpoint (`jev-latest` at `api.typesafe.ai/v1` by default) with fixed importance, action and date questions; your VIP and mute rules run first, and the answers route mail to an alert, the digest, skip or a todo. Integration evidence: [`src/mailagent/ai/jev.py`](https://github.com/Jaydccq/mail-agent/blob/a78392b4f3057cf9f0cf6e741d6a7f7006d0fb3a/src/mailagent/ai/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Jaydccq/mail-agent.git
cd mail-agent
./install.sh
mail-agent doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide: [github.com/Jaydccq/mail-agent/blob/master/docs/setup.md](https://github.com/Jaydccq/mail-agent/blob/master/docs/setup.md)

## Limits and data handling

Email content is sent to TypeSafe for triage and, for important mail, to the generative model you choose; data stays in a local SQLite file. It never marks mail read or changes labels. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit a78392b4f305](https://github.com/Jaydccq/mail-agent/tree/a78392b4f3057cf9f0cf6e741d6a7f7006d0fb3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
