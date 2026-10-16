# Facet

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Photo culling and sorting app for photographers: an AI model checks every photo against built-in and your own labels (blurry, eyes closed, the couple kissing), faces are grouped locally, and you filter and sort into folders with undo. Jev or OpenAI vision can be chosen.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ceelnok/facet-photo) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ceelnok/facet-photo#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-16. |
| Jev evidence | [`facet/jev_client.py`](https://github.com/ceelnok/facet-photo/blob/fc316b6e871cf541570c0a87b1179842b2017b75/facet/jev_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ceelnok](https://github.com/ceelnok). Independently curated. |
| Format | Desktop app (Python/Qt) for macOS and Windows; source launchers |
| Platform and availability | macOS and Windows (source launchers) |
| Jev's role | Jev scores each photo against your labels and can search for people by reference faces. |
| Requirements | Python 3.10+ (or uv); a TypeSafe or OpenAI API key. |
| License | [MIT](https://github.com/ceelnok/facet-photo/blob/fc316b6e871cf541570c0a87b1179842b2017b75/LICENSE) |

## When to use

- Cull a wedding or holiday shoot by label probability, then sort keepers into folders.
- Find a named person across new photos with local face recognition, with Jev as an optional face search.
- Mismatch: Jev image input is a beta feature at TypeSafe; face recognition is not perfect; ZIP download may need macOS Gatekeeper approval.

## How it works

For each photo, `JevClient` posts the image and your labels as typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and stores per-label probabilities; face detection and grouping run locally, and one API call is made per photo. Integration evidence: [`facet/jev_client.py`](https://github.com/ceelnok/facet-photo/blob/fc316b6e871cf541570c0a87b1179842b2017b75/facet/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/CeelNok/facet-photo.git && cd facet-photo
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python run.py   # or double-click Facet.app (macOS) / Facet.bat (Windows)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hungarian README: `README.hu.md`.
- Screenshots in `docs/`.

## Limits and data handling

Photos are sent to the chosen provider (TypeSafe or OpenAI) on your key for analysis; face recognition stays on your computer.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit fc316b6e871c](https://github.com/ceelnok/facet-photo/tree/fc316b6e871cf541570c0a87b1179842b2017b75). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
