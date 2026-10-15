# Jev Voice Chat (Japanese)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Japanese voice conversation in the browser where Jev handles turn-taking (end of utterance, backchannel vs interruption, restatement vs new content) and OpenAI models handle recognition, replies and speech.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snowconed/jev_gpt_voice_chat_jp) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/snowconed/jev_gpt_voice_chat_jp#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-16. |
| Jev evidence | [`jev_client.py`](https://github.com/snowconed/jev_gpt_voice_chat_jp/blob/f754060ebc0dd12eb94a7617ecad1bcb6574d0fe/jev_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [snowconed](https://github.com/snowconed). Independently curated. |
| Format | Local Python server + browser UI (Windows) |
| Platform and availability | Web UI served locally on Windows |
| Jev's role | Jev decides turn-taking: when to answer, wait, continue or stop. |
| Requirements | Windows, Python 3.11+, Chrome or Edge with a microphone; `OPENAI_API_KEY` and `JEV_API_KEY`/`TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/snowconed/jev_gpt_voice_chat_jp/blob/f754060ebc0dd12eb94a7617ecad1bcb6574d0fe/LICENSE) |

## When to use

- Hold a natural Japanese voice chat that tolerates fillers, backchannels and mid-reply corrections.
- Study using Jev Choice questions for turn-taking decisions next to a separate reply generator.
- Mismatch: Japanese only, Windows scripts; recognition and speech quality depend on OpenAI models.

## How it works

The server sends recent transcript context to `https://api.typesafe.ai/v1/systemone` with Choice questions (finished speaking? backchannel, stop or correction? does a restatement change meaning?) and validates each answer's shape; replies come from the OpenAI model and are passed to TTS verbatim. Integration evidence: [`jev_client.py`](https://github.com/snowconed/jev_gpt_voice_chat_jp/blob/f754060ebc0dd12eb94a7617ecad1bcb6574d0fe/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
.\setup.bat
.\start_jev.bat   # then open http://127.0.0.1:8783
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Filler and voice settings: README sections フィラーを使う and 会話と声の設定.

## Limits and data handling

Speech goes to OpenAI for recognition, replies and synthesis, and transcripts to TypeSafe for turn-taking, on your keys.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit f754060ebc0d](https://github.com/snowconed/jev_gpt_voice_chat_jp/tree/f754060ebc0dd12eb94a7617ecad1bcb6574d0fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
