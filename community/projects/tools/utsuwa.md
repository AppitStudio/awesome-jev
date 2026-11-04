# utsuwa (Japanese-language harness that gives an Obsidian-defined persona a Discord presence, with Jev deciding when to reply and what to remember)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python harness that keeps one agent per Obsidian folder (persona, rules, memories and state as Markdown, JSON and JSONL) and runs it in Discord chat. Code and Jev (`jev-latest`) make the judgments, such as whether to reply, stay quiet or reply later, which kind of memory applies, which stored notes are relevant, whether a draft stays in the persona and what to record, while the conversation LLM only writes the text. Documentation is in Japanese. The source is PolyForm Noncommercial, not open source.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/3208noname-arch/utsuwa) |
| Maintainer | [3208noname-arch](https://github.com/3208noname-arch). Independently curated. |
| Format | Python harness (Discord bot, Obsidian vault folders, optional persona engines) |
| Requirements | Python and the packages in `requirements.txt`; a Discord bot, an LLM key and a TypeSafe key in `.env`. |
| License | [PolyForm Noncommercial 1.0.0](https://github.com/3208noname-arch/utsuwa/blob/7962a9a64989299f775fdf7a1f5ab7f5627a186e/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/api.py`](https://github.com/3208noname-arch/utsuwa/blob/7962a9a64989299f775fdf7a1f5ab7f5627a186e/harness/api.py) at the pinned commit. |

## When to use

- Run a persistent Discord persona whose reply decisions, memory typing and consistency checks are typed Jev decisions while an LLM only writes sentences.
- Mismatch: the docs are Japanese-only, the license forbids commercial use, and the project is a harness rather than a packaged app.

## How it works

`harness/api.py` posts typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, 15 s timeout by default); the flow in the README uses one Jev call per decision point (reply or not, memory type, memory selection, recording, persona check, nightly merge of similar memories). Integration evidence: [`harness/api.py`](https://github.com/3208noname-arch/utsuwa/blob/7962a9a64989299f775fdf7a1f5ab7f5627a186e/harness/api.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
cp .env.example .env
python -m harness "template/あかり" --check   # reads the folder without connecting to Discord
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese) with the folder layout, flow and persona parts: [github.com/3208noname-arch/utsuwa#readme](https://github.com/3208noname-arch/utsuwa#readme)

## Limits and data handling

Conversation text, memories and persona checks go to TypeSafe on your key and to the LLM you configure; the README says an agent's own statements are not used as memory sources. License is PolyForm Noncommercial 1.0.0 (source available; no commercial use). Tests use a fake Jev, so live decision quality was not checked. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 7962a9a64989](https://github.com/3208noname-arch/utsuwa/tree/7962a9a64989299f775fdf7a1f5ab7f5627a186e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
