# Jarvis (Discord voice assistant for game nights, with Jev deciding whether a follow-up was meant for the bot)

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

Say "Hey Jarvis" in a Discord voice channel, ask out loud, and hear the answer in the call. Each speaker gets their own wake-word detector, answers start speaking before they are finished, and per-game patch notes keep answers current. After a reply the person can carry on without the wake word; with a TypeSafe key, Jev checks whether each follow-up was meant for the bot or a friend, so it stays quiet when unsure. Answers come from Qwen on Cerebras.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DarrenRM/jarvis-voice) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/DarrenRM/jarvis-voice#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own Discord, Cerebras, Groq and Inworld keys, plus TypeSafe for Jev. Checked 2026-10-30. |
| Jev evidence | [`src/llm/addressee_judge.py`](https://github.com/DarrenRM/jarvis-voice/blob/dbcc642981351f70515cdf277e756cedc7dd449e/src/llm/addressee_judge.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [DarrenRM](https://github.com/DarrenRM). Independently curated. |
| Format | Self-hosted Discord bot (Python) |
| Platform and availability | Self-hosted Discord bot; no public instance verified. |
| Jev's role | Optional addressee check: decides whether a follow-up was meant for the bot. |
| Requirements | Python 3.11+, ffmpeg and libopus; Discord, Cerebras, Groq and Inworld keys; TypeSafe key optional. |
| License | [MIT](https://github.com/DarrenRM/jarvis-voice/blob/dbcc642981351f70515cdf277e756cedc7dd449e/LICENSE) |

## When to use

- Run a hands-free helper in your group's voice channel that doesn't butt into side conversations.
- Mismatch: Jev handles one optional check; the main answers come from Qwen.

## How it works

`src/llm/addressee_judge.py` asks Jev one probability question per follow-up (is this for the bot?) and treats errors and unclear answers as not addressed; Qwen is the fallback judge. Integration evidence: [`src/llm/addressee_judge.py`](https://github.com/DarrenRM/jarvis-voice/blob/dbcc642981351f70515cdf277e756cedc7dd449e/src/llm/addressee_judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv venv --python 3.12 .venv && VIRTUAL_ENV=.venv uv pip install -e ".[dev]"
cp .env.example .env   # fill in the keys
.venv/bin/python -m src.main
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with design notes: [github.com/DarrenRM/jarvis-voice#readme](https://github.com/DarrenRM/jarvis-voice#readme)

## Limits and data handling

Voice is transcribed by Groq; follow-up text goes to TypeSafe when the key is set. The bot listens to everyone in the channel; tell people it is there.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit dbcc64298135](https://github.com/DarrenRM/jarvis-voice/tree/dbcc642981351f70515cdf277e756cedc7dd449e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
