# jev-cascade

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Python cascade that uses Jev as a cheap, recall-tuned first stage over many questions per item, then only escalates the uncertain band to a stronger second-stage command and reports whether stage two actually improves accuracy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CapCurious/jev-cascade) |
| Maintainer | [CapCurious](https://github.com/CapCurious). Independently curated. |
| Format | Python CLI (stdlib) with recorded demos and a browser explainer |
| Requirements | Python 3.10+; JEV_API_KEY or TYPESAFE_API_KEY for live runs (optional recorded --demo). |
| License | [MIT](https://github.com/CapCurious/jev-cascade/blob/edf944258dd4e7306dc32455e11e6993cbfcdcea/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/CapCurious/jev-cascade/blob/edf944258dd4e7306dc32455e11e6993cbfcdcea/jev_client.py) at the pinned commit. |

## When to use

- Want a measurable escalate path after Jev instead of guessing second-stage value.
- Need cost and latency accounting for stage one versus stage two on the same items.
- Mismatch: stage-two command and thresholds are yours to configure; no hosted product.

## How it works

`jev_client.py` POSTs System One requests to `https://api.typesafe.ai/v1/systemone`. `jev_cascade.py` scores items with Jev, keeps confident answers, and shells out only for the uncertain band, then compares stage-two accuracy on that band. Integration evidence: [`jev_client.py`](https://github.com/CapCurious/jev-cascade/blob/edf944258dd4e7306dc32455e11e6993cbfcdcea/jev_client.py).

## Get started

Clone the repo, optionally set a TypeSafe key, and run the recorded demo or a live cascade.

```sh
git clone https://github.com/CapCurious/jev-cascade && cd jev-cascade
python3 jev_cascade.py --demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [capcurious.github.io/jev-cascade/](https://capcurious.github.io/jev-cascade/) interactive explainer
- README cascade report on 120 tickets

## Limits and data handling

Live calls bill TypeSafe usage. Stage-two strength is not guaranteed; the report warns when it is weaker than Jev alone.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit edf944258dd4](https://github.com/CapCurious/jev-cascade/tree/edf944258dd4e7306dc32455e11e6993cbfcdcea). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
