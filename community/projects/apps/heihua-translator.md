# Heihua Translator

[All projects](../README.md) · [Web apps](README.md#web-apps)

Paste workplace jargon, guess the meaning, then see TypeSafe Jev’s typed reading and how sure it is

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/casperkwok/heihua-translator) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/casperkwok/heihua-translator#readme) |
| Pricing and access | Free MIT source build; bring your own TypeSafe key. Zero third-party deps beyond stdlib+curl per README. Checked 2026-09-29. |
| Jev evidence | README: Jev typed judgments + confidence drive UI cards (≥0.85 / 0.55–0.85 / <0.55). Includes a 30-sentence evaluation corpus. [README](https://github.com/casperkwok/heihua-translator/blob/94dc68ba3afc7f817f3171dea82e5dd0c7199438/README.md). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |
| Maintainer | [casperkwok](https://github.com/casperkwok). Independently curated. |
| Format | Python stdlib HTTP server + single-page HTML UI (MIT). |
| Platform and availability | Local web UI after `python3 server.py` (default port 8765 per upstream). |
| Jev's role | Jev judges interpretation/confidence for opaque workplace messages; UI exposes uncertainty instead of fluent hallucination. |
| Requirements | Python 3; TypeSafe API key in `.env` (server-side only). |
| License | [MIT](https://github.com/casperkwok/heihua-translator/blob/94dc68ba3afc7f817f3171dea82e5dd0c7199438/LICENSE). Provider usage may incur charges when live. |

## When to use

Use to practice reading opaque workplace messages with calibrated System One confidence. Prefer general translators when you need free-form paraphrase.

## How it works

Server calls TypeSafe System One; frontend shows guess-then-reveal cards keyed to confidence thresholds, including explicit low-confidence abstention.

## Get started

```sh
git clone https://github.com/casperkwok/heihua-translator.git
cd heihua-translator
git checkout 94dc68ba3afc7f817f3171dea82e5dd0c7199438
cp .env.example .env  # add TypeSafe key
set -a; . ./.env; set +a
python3 server.py
```

Pin revision `94dc68ba3afc7f817f3171dea82e5dd0c7199438` when reproducing this review.

## Examples and demos

README describes the confidence UI and 30-sentence eval set. Live server not started on the review host.

## Limits and data handling

Chinese workplace-jargon focus. Live TypeSafe UI not run on the review host. Message text is sent to TypeSafe when live.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 94dc68b](https://github.com/casperkwok/heihua-translator/tree/94dc68ba3afc7f817f3171dea82e5dd0c7199438). AI-assisted README and LICENSE inspection; install/live paths not executed.
