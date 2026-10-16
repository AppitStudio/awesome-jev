# Jev Vision Benchmarks

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmarks of Jev 1.14 image input on marketplace tasks (product-photo moderation, photo-to-listing matching, classification, package-label reading) against GPT vision models, AWS Rekognition and OpenAI moderation, with checked-in labels and results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MaceTenth/jev-vision-benchmarks) |
| Maintainer | [MaceTenth](https://github.com/MaceTenth). Independently curated. |
| Format | Python benchmark scripts with data and write-ups |
| Requirements | Python; a TypeSafe key for Jev runs (plus OpenAI/AWS keys for the comparison engines). |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/macetenth/status/2110743654365282464)). |
| Jev evidence | [`scripts/moderation_bench.py`](https://github.com/MaceTenth/jev-vision-benchmarks/blob/90abaad872711cb372c4ddbcd957044fddf43b8c/scripts/moderation_bench.py) at the pinned commit. |

## When to use

- Gauge Jev image moderation latency, throughput and cost on catalog photos before trying it on your own marketplace.
- Reuse the harness to compare engines on your own labelled images.
- Mismatch: small sample (60 photos, 8 policy cases) measured once on 15 Oct 2026; image input is experimental at TypeSafe. Numbers are the author's.

## How it works

Each engine adapter runs the same photos sequentially and in parallel; the Jev adapter reads `TYPESAFE_API_KEY` and asks typed questions per image with the opt-in `TypeSafe-Danger-Zone-Images` header, and scoring scripts compare answers with hand-written labels. Integration evidence: [`scripts/moderation_bench.py`](https://github.com/MaceTenth/jev-vision-benchmarks/blob/90abaad872711cb372c4ddbcd957044fddf43b8c/scripts/moderation_bench.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/MaceTenth/jev-vision-benchmarks.git && cd jev-vision-benchmarks
python -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/moderation_bench.py --limit 3 --engines jev-1.14.0
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Methodology and caveats: `article/MODERATION.md`.
- Scored results and labels: `data/moderation/`.

## Limits and data handling

Photos go to each engine's provider on your keys.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 90abaad87271](https://github.com/MaceTenth/jev-vision-benchmarks/tree/90abaad872711cb372c4ddbcd957044fddf43b8c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
