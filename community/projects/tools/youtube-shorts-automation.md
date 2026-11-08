# YouTube Shorts automation (trend ranking and faceless Shorts production judged by TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Python pipeline that discovers trending Shorts, judges each video with TypeSafe Jev, ranks formats you can copy as a faceless creator, then writes, voices, captions, renders and optionally uploads a new Short.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bigmo6286/youtube-shorts-automation) |
| Maintainer | [bigmo6286](https://github.com/bigmo6286). Independently curated. |
| Format | Python CLI + local console (no SPDX license file on the reviewed commit) |
| Requirements | Python 3, ffmpeg, yt-dlp, a TypeSafe API key, an Anthropic key for scripts, and optionally YouTube Data API credentials. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`shorts_pipeline/hooks.py`](https://github.com/bigmo6286/youtube-shorts-automation/blob/d18b7a4b69da4619188d1c722ef9ebeb83c7ed3a/shorts_pipeline/hooks.py) at the pinned commit. |

## When to use

- Find which Shorts formats are working before you produce.
- Automate a faceless Shorts pipeline end to end.
- Mismatch: relies on several paid APIs; check YouTube terms before auto-uploading; no OSI license on the reviewed commit.

## How it works

`shorts_pipeline/hooks.py`, `footage.py` and `interrupt.py` use `typesafe_sdk.TypeSafeClient` with `Noul`/`Score`/`Choice` questions to judge hooks, footage and pacing. Integration evidence: [`shorts_pipeline/hooks.py`](https://github.com/bigmo6286/youtube-shorts-automation/blob/d18b7a4b69da4619188d1c722ef9ebeb83c7ed3a/shorts_pipeline/hooks.py).

## Get started

Install requirements, copy `.env.example`, fill in keys, and run the pipeline stages from the console or CLI.

```sh
git clone https://github.com/bigmo6286/youtube-shorts-automation.git && cd youtube-shorts-automation
export TYPESAFE_API_KEY=...
pip install -r requirements.txt && python main.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bigmo6286/youtube-shorts-automation/blob/d18b7a4b69da4619188d1c722ef9ebeb83c7ed3a/README.md](https://github.com/bigmo6286/youtube-shorts-automation/blob/d18b7a4b69da4619188d1c722ef9ebeb83c7ed3a/README.md)

## Limits and data handling

Video metadata/transcripts go to TypeSafe and script prompts to Anthropic on your keys.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit d18b7a4b69da](https://github.com/bigmo6286/youtube-shorts-automation/tree/d18b7a4b69da4619188d1c722ef9ebeb83c7ed3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
