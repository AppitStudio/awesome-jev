# 1 Million Emojis

[All projects](../README.md) · [Web apps](README.md#web-apps)

Shared 1,000×1,000 emoji canvas where humans paint and TypeSafe Jev paints alongside them—choosing emoji and placement from the stroke’s local context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cwdx/1-million-emojis) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Live canvas](https://chriswijnia.com/lab/emoji) — shared web app; no account required. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-30**. Hosted canvas is free to use (ink regenerates); live Jev strokes use the site’s TypeSafe path (vendor-hosted). Self-host needs a TypeSafe key. Hosted quota and live paint were not re-measured here. |
| Jev evidence | Inspected [`packages/emoji/src/jev-join.ts`](https://github.com/cwdx/1-million-emojis/blob/f26be2b20abd0f14777f93425e3b6e0c1459825f/packages/emoji/src/jev-join.ts) and [`packages/jev`](https://github.com/cwdx/1-million-emojis/tree/f26be2b20abd0f14777f93425e3b6e0c1459825f/packages/jev): typed placement/emoji choices after strokes. Live Jev paint not run on the review host. |
| Disclosure | AI-assisted catalog review; community self-submit (issue #773). No affiliation. Listing is not an endorsement. Hosted product path inspected via public README/homepage; live TypeSafe calls not run on the review host. |
| Maintainer | [cwdx](https://github.com/cwdx). Independently curated from public source + issue #773. |
| Format | MIT web app (canvas, palette, Jev painter) behind chriswijnia.com/lab/emoji. |
| Platform and availability | Browser. Try [chriswijnia.com/lab/emoji](https://chriswijnia.com/lab/emoji) or clone the source. |
| Jev's role | Chooses emoji and placement relative to a stroke; code owns canvas sync, ink limits, and rendering. |
| Requirements | Browser for hosted use. Self-host per upstream README (TypeSafe key for Jev painter). |
| License | [MIT](https://github.com/cwdx/1-million-emojis/blob/f26be2b20abd0f14777f93425e3b6e0c1459825f/LICENSE). |

## When to use

Use it as a collaborative creative demo of typed System One choices on sparse visual context. Prefer simpler offline labs when you only need a single-player Jev game.

## How it works

Humans paint with a limited ink budget. After each stroke, Jev ranks typed emoji/placement options from local canvas context and may continue an unfinished stroke when the unfinished noul is high. Probabilities drive wider exploration when unsure; top candidates can flash before the pick lands.

## Get started

```sh
# Hosted (no setup):
# https://chriswijnia.com/lab/emoji

git clone https://github.com/cwdx/1-million-emojis.git
cd 1-million-emojis
git checkout f26be2b20abd0f14777f93425e3b6e0c1459825f
# follow upstream README for local/self-host setup
```

## Examples and demos

- Live: [chriswijnia.com/lab/emoji](https://chriswijnia.com/lab/emoji).
- Upstream README describes Jev’s painter and data sent (drawing context only).

## Limits and data handling

Stroke shape/emoji context may leave the client on live Jev evaluates. Catalog checks did not run live integrations or measure hosted ink/Jev quotas.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit f26be2b](https://github.com/cwdx/1-million-emojis/tree/f26be2b20abd0f14777f93425e3b6e0c1459825f). AI-assisted README and license inspection; install/live paths not executed. Related: issue [#773](https://github.com/AppitStudio/awesome-jev/issues/773).
