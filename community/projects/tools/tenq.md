# tenq (cited SEC 10-Q/10-K change briefs checked by TypeSafe Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Daily GitHub Actions pipeline that emails cited what-changed briefs from SEC 10-Q/10-K filings for a software watchlist, using TypeSafe Jev typed questions plus XBRL number checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jelbirt/tenq) |
| Maintainer | [jelbirt](https://github.com/jelbirt). Independently curated. |
| Format | Python pipeline + GitHub Actions (MIT) |
| Requirements | Python 3, GitHub Actions or local run, and an OpenRouter key with access to TypeSafe Jev. |
| License | [MIT](https://github.com/jelbirt/tenq/blob/66afd8dbef50246ea0a3b61734bc564327077345/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/tenq/jev.py`](https://github.com/jelbirt/tenq/blob/66afd8dbef50246ea0a3b61734bc564327077345/src/tenq/jev.py) at the pinned commit. |

## When to use

- Get cited filing briefs with numbers verified against XBRL.
- Study a Jev-as-judge pattern with deterministic fallbacks.
- Mismatch: slice 1 covers one company; not investment advice.

## How it works

`src/tenq/jev.py` calls the `systemone` endpoint (via OpenRouter, model `typesafe/jev-*`) with versioned typed questions; rules in code decide what reaches the brief. Integration evidence: [`src/tenq/jev.py`](https://github.com/jelbirt/tenq/blob/66afd8dbef50246ea0a3b61734bc564327077345/src/tenq/jev.py).

## Get started

Clone, configure the watchlist and keys per README, and run the daily workflow.

```sh
git clone https://github.com/jelbirt/tenq.git && cd tenq
export TYPESAFE_API_KEY=...
pip install -e . && python -m tenq --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jelbirt/tenq/blob/66afd8dbef50246ea0a3b61734bc564327077345/README.md](https://github.com/jelbirt/tenq/blob/66afd8dbef50246ea0a3b61734bc564327077345/README.md)

## Limits and data handling

Filing passages are sent to the configured provider; briefs are informational only.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 66afd8dbef50](https://github.com/jelbirt/tenq/tree/66afd8dbef50246ea0a3b61734bc564327077345). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
