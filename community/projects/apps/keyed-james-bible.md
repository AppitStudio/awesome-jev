# keyed james bible

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Turns a question into a span of King James Version verses by keying it through TypeSafe Jev choice requests (book and extent → chapter → verse) and clipping the passage verbatim from a local KJV corpus; nothing is generated, and the author documents measured Jev quirks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mccartykim/keyed_james_bible) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/mccartykim/keyed_james_bible#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT source (LICENSE text is MIT; GitHub's detector reports NOASSERTION); requires your own Jev key via TypeSafe or OpenRouter (usage billed by the provider). Checked 2026-10-08. |
| Jev evidence | [`jev_kjv/jev.py`](https://github.com/mccartykim/keyed_james_bible/blob/d97d289a2a5628a7fa37f22a729161d104d626f2/jev_kjv/jev.py) and [`resolver.py`](https://github.com/mccartykim/keyed_james_bible/blob/d97d289a2a5628a7fa37f22a729161d104d626f2/jev_kjv/resolver.py) run the three-request chain; [`docs/how-it-keys.md`](https://github.com/mccartykim/keyed_james_bible/blob/d97d289a2a5628a7fa37f22a729161d104d626f2/docs/how-it-keys.md) records behaviour. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [mccartykim](https://github.com/mccartykim). Independently curated. |
| Format | Python CLI (`ask.py`) and small local web service |
| Platform and availability | Any OS with Python 3.11+ (standard library only); local web service on `127.0.0.1:8765`. |
| Jev's role | Chooses book, extent, chapter and verse; code clips verses from the local corpus. |
| Requirements | Python 3.11+ and a Jev API key (see README for TypeSafe/OpenRouter setup). |
| License | [MIT](https://github.com/mccartykim/keyed_james_bible/blob/d97d289a2a5628a7fa37f22a729161d104d626f2/LICENSE). |

## When to use

- Look up KJV passages related to a plain-language question.
- Study how to chain dependent choice questions through shared state.
- Mismatch: the author's own Jev self-assessment rates it as probably not a useful Bible study tool.

## How it works

Three requests: the question picks book + extent, then chapter, then verse, each with the earlier answers in `state`; code then clips the verses from the local corpus. Option sets stay under Jev's 255-option cap (largest 176, Psalm 119).

## Get started

Build the corpus and ask from the command line (README *Running it*):

```sh
git clone https://github.com/mccartykim/keyed_james_bible && cd keyed_james_bible
python3 scripts/build_corpus.py
python3 ask.py "What should I do when I am afraid?"
```

Each question makes three Jev requests (cached unless `--no-cache`), billed by your provider.

## Examples and demos

- README sample output and *Is this blasphemy or a useful Bible study tool?*.
- Raw self-assessment response: [`experiments/jev-self-assessment.json`](https://github.com/mccartykim/keyed_james_bible/blob/d97d289a2a5628a7fa37f22a729161d104d626f2/experiments/jev-self-assessment.json).

## Limits and data handling

Your question goes to the Jev provider; verses come from the local corpus. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit d97d289a2a56](https://github.com/mccartykim/keyed_james_bible/tree/d97d289a2a5628a7fa37f22a729161d104d626f2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
