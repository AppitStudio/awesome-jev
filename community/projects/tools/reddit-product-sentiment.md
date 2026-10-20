# Reddit product sentiment

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Daily pipeline that collects product subreddit posts and comments, asks Jev typed questions about each comment and product pair (is it about this product, a five-level sentiment score, five aspects and nine themes), stores answers in SQLite, and shows trends with a drill-down to the source text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/STVPJ/reddit-sentiment) |
| Maintainer | [STVPJ](https://github.com/STVPJ). Independently curated. |
| Format | Python pipeline with SQLite and a web dashboard |
| Requirements | Python; a TypeSafe key (`TYPESAFE_API_KEY`), or an Anthropic key for the Claude backend. |
| License | [MIT](https://github.com/STVPJ/reddit-sentiment/blob/cde00d688ae67679f9aff4655b9802c6ac2535ac/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sentiment/backends/jev.py`](https://github.com/STVPJ/reddit-sentiment/blob/cde00d688ae67679f9aff4655b9802c6ac2535ac/sentiment/backends/jev.py) at the pinned commit. |

## When to use

- Track whether practitioner sentiment about your product and competitors is moving, and why.
- Watch the reaction to a launch or pricing change with event annotations.
- Mismatch: thresholds were tuned on Jev; re-check them before comparing Claude results.

## How it works

Code fixes the sequence: collect from the Arctic Shift Reddit archive, match products by regex (or one Jev Choice for ambiguous comments), then `sentiment/backends/jev.py` sends one request per comment and product to `https://api.typesafe.ai/v1/systemone`. Only answers with `about` and confidence at least 0.6 are counted on the dashboard. Integration evidence: [`sentiment/backends/jev.py`](https://github.com/STVPJ/reddit-sentiment/blob/cde00d688ae67679f9aff4655b9802c6ac2535ac/sentiment/backends/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/STVPJ/reddit-sentiment.git && cd reddit-sentiment
cp .env.example .env   # JUDGE_BACKEND=jev, TYPESAFE_API_KEY=
# edit config.yaml for your products, then follow the README run steps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Dashboard screenshot with synthetic demo data (docs/screenshot.png)
- README section 'Key decisions and the evidence behind them'

## Limits and data handling

Comment text goes to TypeSafe (or Anthropic). The example config tracks AI coding assistants; the screenshot data is synthetic.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit cde00d688ae6](https://github.com/STVPJ/reddit-sentiment/tree/cde00d688ae67679f9aff4655b9802c6ac2535ac). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
