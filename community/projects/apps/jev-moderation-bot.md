# Jev Moderation Bot

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

A self-hosted Discord bot that uses Jev to classify messages for automated moderation and produce moderator-requested summaries of member activity.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brainstormity/Jev-Moderation-Bot) |
| Tags | `Source unverified` · `Pricing unverified` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/brainstormity/Jev-Moderation-Bot#readme) |
| Pricing and access | [Self-hosting instructions](https://github.com/brainstormity/Jev-Moderation-Bot#setup) require Discord bot credentials, a TypeSafe key and a running Python host. Provider/hosting costs are separate; app pricing terms were not established on 2026-09-19. |
| Jev evidence | [Moderation pipeline](https://github.com/brainstormity/Jev-Moderation-Bot/blob/1629ac80bea758883ee7541ffc654c83acfae4b6/moderator.py), [profiling questions](https://github.com/brainstormity/Jev-Moderation-Bot/blob/1629ac80bea758883ee7541ffc654c83acfae4b6/profiler.py) and [API adapter](https://github.com/brainstormity/Jev-Moderation-Bot/blob/1629ac80bea758883ee7541ffc654c83acfae4b6/typesafe/__init__.py). |
| Disclosure | Public source was inspected. README says MIT, but no complete license file was found. AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |
| Maintainer | [brainstormity](https://github.com/brainstormity) |
| Format | Python / discord.py bot with SQLite persistence; source distribution |
| Platform and availability | Self-hosted process connected to Discord; no managed service or packaged release verified. |
| Jev's role | Chooses legitimate/spam/scam classes, judges malicious-message urgency and summarizes behavioral signals in sampled messages. |
| Requirements | Python 3.10+, Discord bot token, TypeSafe API key, enabled message-content/member intents and appropriate Discord moderation permissions. |
| License | [README license declaration](https://github.com/brainstormity/Jev-Moderation-Bot#license) says MIT; full grant/notice was not found, so open-source terms remain unverified. |

## When to use

Use this as an experimental self-hosted moderation workflow or implementation reference.
It provides automatic message handling, a moderator log, configurable thresholds/timeouts,
pardons and an activity-profile command. It has no documented review-only startup mode:
connecting it to a server can delete messages and apply sanctions immediately.
Model-generated member labels are uncertain summaries of sampled text, not reliable
judgments of a person's character or intent.

## How it works

For each non-bot guild message, code caches the content in SQLite and asks Jev for a
Choice classification plus a Noul judgment about malicious-scam urgency. The adapter
uses `jev-latest` by default through `typesafe-sdk`, with a direct
`https://api.typesafe.ai/v1/systemone` fallback.

Code applies default thresholds of `0.95` and `0.70`. A flagged message is deleted;
the first two active offenses send warning DMs, the third applies a ten-minute timeout,
and later offenses default to one hour. The Noul question mentions an immediate ban,
but the automatic implementation uses the same escalation ladder. Permanent ban buttons
require an administrator and a second confirmation.

`/profile` sends sampled messages and prior offenses for Noul signals and Choice persona/
recommended-action labels. Pardons add recent message text to future model context as
safe precedents. This is in-context prompting, not training, and cannot guarantee that
the same content will never be flagged again.

## Get started

The upstream README clone URL is a placeholder. Use the actual repository:

```sh
git clone https://github.com/brainstormity/Jev-Moderation-Bot.git
cd Jev-Moderation-Bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Privately configure `DISCORD_TOKEN` and `TYPESAFE_API_KEY`; optionally set
`DATABASE_PATH` and `COMMAND_PREFIX`. Enable Message Content and Server Members intents
in Discord's developer portal. The [setup guide](https://github.com/brainstormity/Jev-Moderation-Bot#4-discord-bot-permissions)
lists Manage Messages, Moderate Members, Ban Members and channel/history permissions.

`python3 main.py` connects the bot, initializes SQLite and activates live moderation.
Run it first in a controlled test server with suitable sample messages. This is a live
external-action workflow, sends message context to TypeSafe and can incur inference charges.
The owner must sync commands with `!sync`; moderators can then use `/set-mod-log`,
`/mod-config`, `/set-thresholds`, `/set-timeouts` and `/profile` as permitted.

## Examples and demos

No separate live demo or packaged sample server was established. The
[command reference](https://github.com/brainstormity/Jev-Moderation-Bot#commands) explains
the interface. [Mock-based tests](https://github.com/brainstormity/Jev-Moderation-Bot/tree/1629ac80bea758883ee7541ffc654c83acfae4b6/tests)
cover the adapter, escalation, moderator buttons, profiles, database and command handlers.
The documented test command is `python3 -m pytest -v`; it was not executed in this review.

## Limits and data handling

Provider failures or missing classification answers let the message through.
The adapter converts values to floats but does not comprehensively enforce allowed
choices, completeness or finite `[0,1]` ranges. Moderation gates on Choice `confidence`,
not the selected-choice probability; treat its thresholds as unvalidated application
policy. A broad SDK exception handler can make a second HTTP request after an SDK failure.

Deletion or timeout failures can still be followed by offense recording and warnings,
so stored outcomes do not prove that Discord applied the action. Profile errors return
an error summary with default zero scores; missing individual answers also become zero.
Those defaults must not be interpreted as evidence of benign behavior.

TypeSafe receives message content, author/channel identifiers, account-age metadata and
up to five safe precedents. Profiles add names, roles, account/server dates, sampled
messages and prior offenses. No anonymization layer was found in these state builders.
SQLite retains cached chat, offense text/context and feedback; channel fallback scanning
can cache messages from other members too. A pruning method exists, but no scheduled
caller was found, so automatic thirty-day deletion is not established.

The bot's native and custom logs can expose moderation content to server administrators.
Review permissions and retention before real use. Unknown licensing, unverified live API
compatibility and the absence of independent false-positive evaluation limit adoption.

## Review and maintenance

Reviewed **2026-09-19** at
[`1629ac80bea758883ee7541ffc654c83acfae4b6`](https://github.com/brainstormity/Jev-Moderation-Bot/tree/1629ac80bea758883ee7541ffc654c83acfae4b6).
Inspected README/setup, requirements, environment template, configuration, entry point,
API adapter, moderation/escalation and admin confirmation code, profile handling,
database retention methods and representative adapter/moderation tests. No install,
test execution, Discord connection, external message, deletion, timeout or live request
was performed. This listing describes inspected behavior rather than validated moderation quality.
