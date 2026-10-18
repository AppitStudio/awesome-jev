# vd-jev (VisiData + Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VisiData plugin that asks closed Jev questions over every cell of a text column via OpenRouter (default `typesafe/jev-1.14`) and writes typed probability/label/score columns back into the sheet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ondata/vd-jev) |
| Maintainer | [ondata](https://github.com/ondata). Independently curated. |
| Format | Python VisiData plugin |
| Requirements | VisiData; OpenRouter API key; network access (cell text leaves your machine). |
| License | [GPL-3.0](https://github.com/ondata/vd-jev/blob/0aa2dd6e90cf971ea62c5d08a7996f055acf2300/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`vd_jev.py`](https://github.com/ondata/vd-jev/blob/0aa2dd6e90cf971ea62c5d08a7996f055acf2300/vd_jev.py) at the pinned commit. |

## When to use

- Explore tabular text in VisiData with typed decision-model columns.
- Want yes/no, choice, or score answers with confidence next to the source cells.
- Mismatch: GPL-3.0 plugin; data is sent to OpenRouter/TypeSafe.

## How it works

`vd_jev.py` calls OpenRouter's decisions API with model ids such as `typesafe/jev-1.14`, mapping each cell into typed columns. Demo scripts show batch questions over citizen-request text. Integration evidence: [`vd_jev.py`](https://github.com/ondata/vd-jev/blob/0aa2dd6e90cf971ea62c5d08a7996f055acf2300/vd_jev.py).

## Get started

Install the plugin into VisiData, set OPENROUTER_API_KEY, and run a jev command on a text column.

```sh
git clone https://github.com/ondata/vd-jev && cd vd-jev
# follow README plugin install; set OPENROUTER_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo GIF on citizen requests
- demo/ted_descriptions.py batch example

## Limits and data handling

GPL-3.0. Cell text is transmitted to OpenRouter and the model provider. Not a hosted SaaS.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 0aa2dd6e90cf](https://github.com/ondata/vd-jev/tree/0aa2dd6e90cf971ea62c5d08a7996f055acf2300). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
