# LONELY-EU D3.1 (research pipeline that keeps a European database of loneliness surveys current, with Jev screening the literature)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Code, briefs and coding manual for the yearly update of the LONELY-EU database of loneliness surveys (Horizon Europe, University of Milan). Jev screens thousands of titles and abstracts against preregistered criteria, and scripts check every model output against the source documents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arturobertero/LONELY-EU_D3.1) |
| Maintainer | [arturobertero](https://github.com/arturobertero). Independently curated. |
| Format | Python scripts (research code, no data) |
| Requirements | Python 3.12, `openpyxl`, Poppler `pdftotext`; `TYPESAFE_API_KEY` for the Jev steps. |
| License | [MIT](https://github.com/arturobertero/LONELY-EU_D3.1/blob/4fd295fbc94f22b2070f5fe5897e02e26ae455b8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`search/s04_screen_jev.py`](https://github.com/arturobertero/LONELY-EU_D3.1/blob/4fd295fbc94f22b2070f5fe5897e02e26ae455b8/search/s04_screen_jev.py) at the pinned commit. |

## When to use

- See Jev used for preregistered, audited literature screening.
- Mismatch: research infrastructure for one project; the data are not in the repository.

## How it works

`search/s04_screen_jev.py` sends each record's title and abstract to Jev through the small stdlib client `jev.py`, with one Noul per criterion (empirical study, measures loneliness, listed countries); the cut-off is set afterwards on a hand-checked sample. Integration evidence: [`search/s04_screen_jev.py`](https://github.com/arturobertero/LONELY-EU_D3.1/blob/4fd295fbc94f22b2070f5fe5897e02e26ae455b8/search/s04_screen_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python jev.py --selftest
python search/s04_screen_jev.py --year 2025 --round <round folder>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Preregistered updating procedure: [doi.org/10.5281/zenodo.23887433](https://doi.org/10.5281/zenodo.23887433)

## Limits and data handling

Titles, abstracts and dataset documentation are sent to TypeSafe. Independent research code; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 4fd295fbc94f](https://github.com/arturobertero/LONELY-EU_D3.1/tree/4fd295fbc94f22b2070f5fe5897e02e26ae455b8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
