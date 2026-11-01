# nyotti-xray (replay and fill-by-fill check of a public BitMEX trade history, with Jev reading 10,169 decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Analysis of the 2018–2021 BitMEX execution history a trader published: a 30-second replay, a fill-by-fill check against BitMEX's public trade tape, and an x-ray where code describes each of 10,169 Bitcoin decisions and Jev answers eight typed questions about it. Results are published as a thirty-reading atlas page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/viva-lee/nyotti-xray) |
| Maintainer | [viva-lee](https://github.com/viva-lee). Independently curated. |
| Format | Python analysis scripts and a static atlas site |
| Requirements | Python; the public data download; a TypeSafe API key for the Jev pass. |
| License | [MIT](https://github.com/viva-lee/nyotti-xray/blob/52610722a80087373f7d8ba55fb7a957b3799cd9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`nyotti/jev.py`](https://github.com/viva-lee/nyotti-xray/blob/52610722a80087373f7d8ba55fb7a957b3799cd9/nyotti/jev.py) at the pinned commit. |

## When to use

- See Jev used for bulk typed labeling of historical decisions.
- Mismatch: past records only; no signals, bot or strategy.

## How it works

`nyotti/jev.py` is a paced, retried, standard-library Jev client (`https://api.typesafe.ai`, `jev-latest` by default); `nyotti/judge.py` sends each decision's short English description with eight questions and stores the probabilities. Integration evidence: [`nyotti/jev.py`](https://github.com/viva-lee/nyotti-xray/blob/52610722a80087373f7d8ba55fb7a957b3799cd9/nyotti/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/viva-lee/nyotti-xray && cd nyotti-xray
pip install -r requirements.txt
python -I bin/nyotti.py fetch && python -I bin/nyotti.py build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Atlas: [viva-lee.github.io/nyotti-xray/atlas.html](https://viva-lee.github.io/nyotti-xray/atlas.html)
- Korean README: [github.com/viva-lee/nyotti-xray/blob/main/README.ko.md](https://github.com/viva-lee/nyotti-xray/blob/main/README.ko.md)

## Limits and data handling

Decision descriptions are sent to TypeSafe. Not investment advice; unofficial and unaffiliated with the trader or BitMEX. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 52610722a800](https://github.com/viva-lee/nyotti-xray/tree/52610722a80087373f7d8ba55fb7a957b3799cd9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
