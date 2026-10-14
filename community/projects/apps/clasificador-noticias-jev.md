# Clasificador de noticias regionales con Jev

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Spanish-language Windows workflow that turns a monthly multi-portal news Excel into a reviewed list of Arequipa economic news, using Jev to classify headlines before scraping.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EdgarTapara/clasificador-noticias-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/EdgarTapara/clasificador-noticias-jev#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-14. |
| Jev evidence | [`app/jev.py`](https://github.com/EdgarTapara/clasificador-noticias-jev/blob/eb6bef5c31f2376b19384ada1c91591d01efbf7e/app/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [EdgarTapara](https://github.com/EdgarTapara). Independently curated. |
| Format | Python CLI with a local interface (Windows launchers) |
| Platform and availability | Windows (Python source build) |
| Jev's role | Jev classifies each Arequipa headline/summary as economic news before scraping. |
| Requirements | Python 3, Windows (launchers provided), your own news Excel file, Jev/TypeSafe key in `.env`. |
| License | [MIT](https://github.com/EdgarTapara/clasificador-noticias-jev/blob/eb6bef5c31f2376b19384ada1c91591d01efbf7e/LICENSE) |

## When to use

- A regional analyst who receives 2,000+ mixed news rows per month and needs the economic subset for human review.
- Mismatch: tailored to Arequipa/Peru economic news and Spanish-language data; no sample news data is shipped.

## How it works

A lexical geographic rule filters to Arequipa first (no network). Jev then classifies headline and summary as economic or not, before any scraping, so fewer pages are fetched. Code handles dating, duplicate detection and grouping, and the result goes to human review. Integration evidence: [`app/jev.py`](https://github.com/EdgarTapara/clasificador-noticias-jev/blob/eb6bef5c31f2376b19384ada1c91591d01efbf7e/app/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
.\.venv\Scripts\python.exe procesador_noticias.py completo datos\DATA_SUCIA_AGOSTO.xlsx --periodo 2026-08
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline stages are listed in `app/corrida_completa.py` (`ETAPAS`).
- About 380 tests run without the private news data (per upstream README).

## Limits and data handling

Headlines and summaries are sent to Jev when live. Upstream result figures were measured on unpublished data and were not reproduced here.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit eb6bef5c31f2](https://github.com/EdgarTapara/clasificador-noticias-jev/tree/eb6bef5c31f2376b19384ada1c91591d01efbf7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
