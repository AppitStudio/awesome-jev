# jev-fanout-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible billing measurement for TypeSafe Jev parallel questions: does one request with N questions bill the state once versus N separate requests?

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blowxian/jev-fanout-bench) |
| Maintainer | [blowxian](https://github.com/blowxian). Independently curated. |
| Format | Python benches + published results/ (raw JSONL, checksums). |
| Requirements | Python; OpenRouter/TypeSafe access only for live reruns. Offline report is in-repo. |
| License | [MIT](https://github.com/blowxian/jev-fanout-bench/blob/e5a761eacc1dc41756af368331ebfca4802a1fe7/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Upstream 2,976-request metrics not independently reproduced. |

## When to use

Use to **verify fan-out billing** behavior or estimate multi-question savings. See also [https://jevpricing.com/fan-out/](https://jevpricing.com/fan-out/).

## How it works

[`bench.py`](https://github.com/blowxian/jev-fanout-bench/blob/e5a761eacc1dc41756af368331ebfca4802a1fe7/bench.py) calls OpenRouter TypeSafe-compatible System One across state sizes; [`results/summary.md`](https://github.com/blowxian/jev-fanout-bench/blob/e5a761eacc1dc41756af368331ebfca4802a1fe7/results/summary.md) reports linearity and savings.

## Get started

```sh
git clone https://github.com/blowxian/jev-fanout-bench.git
cd jev-fanout-bench
git checkout e5a761eacc1dc41756af368331ebfca4802a1fe7
# read results/summary.md offline; live rerun needs provider keys per README
```

## Examples and demos

- results/fanout.svg and SHA256SUMS over raw JSONL.
- Companion Laya benches under laya/.

## Limits and data handling

Live synthetic states/questions go to the provider. Fixed overhead findings are author-measured on the pinned run.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit e5a761e](https://github.com/blowxian/jev-fanout-bench/tree/e5a761eacc1dc41756af368331ebfca4802a1fe7). AI-assisted README and LICENSE inspection of bench scripts and results; install/live paths not executed.
