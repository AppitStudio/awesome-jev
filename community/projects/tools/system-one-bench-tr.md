# system-one-bench-tr by Ülkü Tuncer Küçüktaş (Turkish benchmark of 66 System One tasks comparing Jev, Microsoft-Decision-1, open models and the authors' own fine-tunes)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turkish benchmark that turns 66 public datasets (routing, opinion, safety, fact-checking, judging and more, plus a Turkish jev-bench) into System One Choice, Noul and Score requests, and reports accuracy and calibration. In the authors' table Jev scores 77.6% on the 25 main tasks, behind their own d3 and Pusula 2.0 models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/UlkuTuncerKucuktas/system-one-bench-tr) |
| Maintainer | [UlkuTuncerKucuktas](https://github.com/UlkuTuncerKucuktas). Independently curated. |
| Format | Python benchmark package with results |
| Requirements | Python; a TypeSafe API key to evaluate Jev, and keys or local weights for other models. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`s1bench/api.py`](https://github.com/UlkuTuncerKucuktas/system-one-bench-tr/blob/609e8a7c31e4fd007c7af1ab2f3ba6230a4faed4/s1bench/api.py) at the pinned commit. |

## When to use

- Compare Jev with other decision models and LLMs on Turkish classification tasks, including calibration.
- Mismatch: English-only evaluation; see the listed System One Bench for that.

## How it works

`s1bench/api.py` defines a `SystemOneAPI` client and points the Jev entry at `https://api.typesafe.ai/v1/systemone` with `jev-latest`; other entries use the same request format against other providers or local models. Integration evidence: [`s1bench/api.py`](https://github.com/UlkuTuncerKucuktas/system-one-bench-tr/blob/609e8a7c31e4fd007c7af1ab2f3ba6230a4faed4/s1bench/api.py).

## Get started

Clone, install the package, and follow the README's "Running it" section to evaluate a model.

```sh
git clone https://github.com/UlkuTuncerKucuktas/system-one-bench-tr.git && cd system-one-bench-tr
pip install -e .
# see README: Running it
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table: [github.com/UlkuTuncerKucuktas/system-one-bench-tr/blob/609e8a7c31e4fd007c7af1ab2f3ba6230a4faed4/README.md#results](https://github.com/UlkuTuncerKucuktas/system-one-bench-tr/blob/609e8a7c31e4fd007c7af1ab2f3ba6230a4faed4/README.md#results)
- Related: [jevlist.ai/projects/system-one-bench](https://jevlist.ai/projects/system-one-bench)

## Limits and data handling

Results are the authors' own, and the top-ranked d3 and Pusula 2.0 are their own fine-tuned models. Benchmark texts are sent to each provider evaluated. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 609e8a7c31e4](https://github.com/UlkuTuncerKucuktas/system-one-bench-tr/tree/609e8a7c31e4fd007c7af1ab2f3ba6230a4faed4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
