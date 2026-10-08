# NucleiSniper

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Security-testing pipeline that fingerprints each authorised target and has TypeSafe Jev score every Nuclei template's relevance (0–4) in batches, then runs Nuclei with all templates ordered highest-relevance first, so likely findings surface early; scans are resumable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MorDavid/NucleiSniper) |
| Maintainer | [MorDavid](https://github.com/MorDavid). Independently curated. |
| Format | Python script `NucleiSniper.py` |
| Requirements | Python 3.10+, Nuclei on PATH with templates, `TYPESAFE_API_KEY`; only scan targets you are authorised to test. |
| License | [PolyForm Strict 1.0.0](https://github.com/MorDavid/NucleiSniper/blob/c5d15c4d274622a8ce205da0579e35d1f4c88115/LICENSE.md) — source available, not open source (noncommercial use, no modifications/redistribution). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Get high-value Nuclei checks first on large authorised scopes.
- Mismatch: noncommercial license; still runs every template, so total scan time is unchanged.

## How it works

[`NucleiSniper.py`](https://github.com/MorDavid/NucleiSniper/blob/c5d15c4d274622a8ce205da0579e35d1f4c88115/NucleiSniper.py) profiles each target (tech fingerprints, headers, assets), sends template batches with the profile to Jev for 0–4 scores (auto-splitting oversized batches), then calls Nuclei in score order.

## Get started

Set up and run (README *Installation* / *Usage*):

```sh
git clone https://github.com/MorDavid/NucleiSniper.git && cd NucleiSniper
pip install -r requirements.txt
export TYPESAFE_API_KEY=...
python NucleiSniper.py https://target.example
```

Template scoring is Jev usage on your key, scaling with template count × targets.

## Examples and demos

- README *How Scoring Works* section.

## Limits and data handling

Target profile data is sent to TypeSafe. Authorised testing only (README legal disclaimer). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c5d15c4d2746](https://github.com/MorDavid/NucleiSniper/tree/c5d15c4d274622a8ce205da0579e35d1f4c88115). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
