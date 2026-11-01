# Jev Ants by gkvoelkl (Streamlit ant colony where every ant asks a decision model what to do, with a German and English tutorial)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Streamlit game: you are the queen and give the colony an order in plain text, and each ant asks Jev (or a local Ollama model) which next step fits its situation. A step-by-step tutorial in German and English builds the app from one ant upward.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gkvoelkl/python-streamlit-jev-ant) |
| Maintainer | [gkvoelkl](https://github.com/gkvoelkl). Independently curated. |
| Format | Python Streamlit app and tutorial site |
| Requirements | Python with uv; a TypeSafe API key (or Ollama for the local path). |
| License | [MIT](https://github.com/gkvoelkl/python-streamlit-jev-ant/blob/5e871a66d74f051e6d7525e468ec104fe142561b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app.py`](https://github.com/gkvoelkl/python-streamlit-jev-ant/blob/5e871a66d74f051e6d7525e468ec104fe142561b/app.py) at the pinned commit. |

## When to use

- Learn typed decisions with a small, visual Python project.
- Mismatch: a teaching game, not a library.

## How it works

`app.py` uses the `typesafe_sdk` `AsyncTypeSafeClient` with a `Choice` question per ant, offering only the actions available at that moment, and shows Jev's last answer above each ant. Integration evidence: [`app.py`](https://github.com/gkvoelkl/python-streamlit-jev-ant/blob/5e871a66d74f051e6d7525e468ec104fe142561b/app.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gkvoelkl/python-streamlit-jev-ant && cd python-streamlit-jev-ant
uv run streamlit run app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tutorial (English): [gkvoelkl.github.io/python-streamlit-jev-ant/en/](https://gkvoelkl.github.io/python-streamlit-jev-ant/en/)
- Tutorial (Deutsch): [gkvoelkl.github.io/python-streamlit-jev-ant/](https://gkvoelkl.github.io/python-streamlit-jev-ant/)

## Limits and data handling

Game state and your order are sent to TypeSafe on every ant decision. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 5e871a66d74f](https://github.com/gkvoelkl/python-streamlit-jev-ant/tree/5e871a66d74f051e6d7525e468ec104fe142561b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
