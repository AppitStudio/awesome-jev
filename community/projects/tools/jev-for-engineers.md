# Jev for engineers (eight runnable Jev examples for mechanical and electrical engineering)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Eight minimal Python examples applying Jev to CAD/CAE/CAM work (FEM log triage, DFM screens, BOM alignment, CAM guardrails, confidence routing), each ending with the decision made in plain Python.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Foadsf/jev-for-engineers) |
| Maintainer | [Foadsf](https://github.com/Foadsf). Independently curated. |
| Format | Python examples with a stdlib System One client (MIT) |
| Requirements | Python 3 and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/jev.py) at the pinned commit. |

## When to use

- Learn the three Jev question types on engineering data.
- Copy a confidence-routing or guardrail pattern into CAE/CAM tooling.
- Mismatch: sample data only (part numbers are invented); quoted results are author-reported.

## How it works

`jev.py` is a ~100-line stdlib client for `POST /v1/systemone` (`jev-latest`) covering `noul`, `choice` and `score`; each numbered script batches its typed questions into one call and applies the policy in code. The README reports the examples were run live on 2026-09-17 (author-reported). Integration evidence: [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/jev.py).

## Get started

Set your key and run any numbered example.

```sh
git clone https://github.com/Foadsf/jev-for-engineers.git && cd jev-for-engineers
export TYPESAFE_API_KEY=...
python 03_fem_triage.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with recorded results: [github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/README.md](https://github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/README.md)

## Limits and data handling

Example inputs go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 181e75208ac3](https://github.com/Foadsf/jev-for-engineers/tree/181e75208ac3b982c80889267a28a1ed718452a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
