# Jevdex by robpob10 (experiment that ranks S&P 500 stocks by daily pairwise Jev comparisons and tracks the top 100)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Public experiment asking whether Jev can tell which of two stocks is the better value. Each trading day it shows Jev about 950 pairs of S&P 500 companies (figures plus recent headlines), updates chess-style ratings and rebalances a tracked portfolio of the 100 highest rated; the site publishes the daily record.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/robpob10/jevdex) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://www.jevdex.app) |
| Pricing and access | The [jevdex.app](https://www.jevdex.app) tracking site is free to read with no account. Running the MIT Rust tool yourself needs your own TypeSafe, Finnhub and Trading 212 keys. Checked 2026-11-25. |
| Jev evidence | [`src/jev.rs`](https://github.com/robpob10/jevdex/blob/99878d682b41843526a737b188cd883d43e26048/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [robpob10](https://github.com/robpob10). Independently curated. |
| Format | Rust CLI with a static website |
| Platform and availability | Web (tracking site on Vercel); the daily tool is a Rust CLI you can run yourself. |
| Jev's role | Jev answers a Choice between company A and company B with a probability; the ratings move by more when Jev is more confident. |
| Requirements | Rust stable; `TYPESAFE_API_KEY`, `FINNHUB_API_KEY`, and Trading 212 API key and secret (the shipped address is Trading 212's demo API). |
| License | [MIT](https://github.com/robpob10/jevdex/blob/99878d682b41843526a737b188cd883d43e26048/LICENSE) |

## When to use

- See a transparent, long-running test of pairwise Jev judgments on a real-world question.
- Reuse the pairwise-rating pattern for your own ranking problems.
- Mismatch: if you want investment advice; this is an experiment.

## How it works

`src/jev.rs` posts each pair to `https://api.typesafe.ai/v1/systemone`; `prompts/` holds what Jev is asked. Jev spending is logged in `data/jev_spend.json` and capped with `--budget-usd`. Integration evidence: [`src/jev.rs`](https://github.com/robpob10/jevdex/blob/99878d682b41843526a737b188cd883d43e26048/src/jev.rs).

## Get started

Check keys, build, then run a two-company trial that saves and sends nothing.

```sh
bash tools/check_keys.sh
cargo build --release
./target/release/jevdex daily --tickers KO,PEP   # trial: nothing saved or sent
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [www.jevdex.app](https://www.jevdex.app)
- Trials: [github.com/robpob10/jevdex/blob/99878d682b41843526a737b188cd883d43e26048/trials/README.md](https://github.com/robpob10/jevdex/blob/99878d682b41843526a737b188cd883d43e26048/trials/README.md)

## Limits and data handling

Not investment advice. The one-year backtest (Jev's 100 at +27.6% versus a +19.8% random-set median and +9.4% for the S&P 500, with pairwise accuracy of 50.5%) is the author's own, covers a single year, and the README itself calls the edge small. `daily --send` places orders on the configured Trading 212 account; as shipped that is the demo API.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 99878d682b41](https://github.com/robpob10/jevdex/tree/99878d682b41843526a737b188cd883d43e26048). Inspected the README, trials summary and the Jev client at the pinned commit and loaded the public site; the tool was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
