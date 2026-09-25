# talktojev (Jev Prime)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted chatbot with **no language model in the loop**: every word is chosen by TypeSafe Jev via the OpenRouter Decisions API (Choice over a vocabulary), with confidence-driven lookahead and self-critique.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xucian/talktojev) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [talktojev.com](https://talktojev.com) |
| Pricing and access | Hosted demo is free with communal daily budget and per-visitor rate limits; visitors may supply an OpenRouter key for unlimited use (BYOK). MIT source build. Checked 2026-09-25. |
| Jev evidence | Issue [#533](https://github.com/AppitStudio/awesome-jev/issues/533) and [README](https://github.com/xucian/talktojev/blob/257dcd3828b766e2af5412b76a49b9abda41aba2/README.md) document word-by-word Jev Choices (Jev 1.13 via OpenRouter Decisions). Paper: [doi.org/10.5281/zenodo.22940945](https://doi.org/10.5281/zenodo.22940945). |
| Disclosure | Open source MIT. Hosted free tier + optional BYOK. Independently curated from community submission #533 (author-affiliated submitter). Listing is not an endorsement. Live chat and billed Decisions paths were not exercised on the review host. |
| Maintainer | [xucian](https://github.com/xucian). Community submission #533. |
| Format | Application (Python server + vanilla JS frontend). |
| Platform and availability | Web: [talktojev.com](https://talktojev.com). Local: Python 3 + `requirements.txt`, OpenRouter key in `.env`. |
| Jev's role | Jev is the sole intelligence layer—no LLM generates tokens; code orchestrates memory, beam search, and tools around repeated Choice questions. |
| Requirements | OpenRouter API key with access to TypeSafe Jev Decisions (`OPENROUTER_API_KEY` per `.env.example`). |
| License | [MIT](https://github.com/xucian/talktojev/blob/257dcd3828b766e2af5412b76a49b9abda41aba2/LICENSE). |

## When to use

Use to **see generation-as-classification**: a research/demo chatbot whose replies are composed only from Jev Choices. Prefer ordinary LLM chat apps when you need fluent long-form generation without hundreds of decision calls.

## How it works

The server asks Jev typed questions at reply, sentence, word, and letter grains; probabilities drive lookahead and critique. Hosted `gate.py` enforces length, rate, and communal budget limits (or the visitor's own key).

## Get started

```sh
git clone https://github.com/xucian/talktojev.git
cd talktojev
git checkout 257dcd3828b766e2af5412b76a49b9abda41aba2
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
cp .env.example .env   # OpenRouter key
./.venv/bin/python server.py   # http://localhost:8787
```

Or open [talktojev.com](https://talktojev.com).

## Examples and demos

- Live site and paper PDF linked from the README.
- `python bench.py run --only v11,s7` for offline bench prompts (credentials may still be required depending on config).

## Limits and data handling

Conversation text goes to OpenRouter/TypeSafe for Decisions. Short replies ~dozen calls; long replies can be hundreds of calls and up to a minute. Hosted communal budget and rate limits apply without BYOK.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 257dcd3](https://github.com/xucian/talktojev/tree/257dcd3828b766e2af5412b76a49b9abda41aba2) for submission [#533](https://github.com/AppitStudio/awesome-jev/issues/533). AI-assisted README/LICENSE/issue inspection; live Decisions spend not run.
