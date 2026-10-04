# Warren Duffer

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Intraday Nifty-50 trading bot where TypeSafe Jev ranks names and code sizes/stops live broker orders (experimental; real-money risk).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arimanyus/warrenduffer) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [https://github.com/arimanyus/warrenduffer](https://github.com/arimanyus/warrenduffer) |
| Pricing and access | Free source build; BYOK TypeSafe/Vercel AI Gateway + broker API. Places real orders—no paper mode. Checked 2026-10-04. |
| Jev evidence | [Upstream README](https://github.com/arimanyus/warrenduffer/blob/9accc86e872c9925c63b5b04cf6984356c8c08fa/README.md) documents Jev/System One use. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/trading/UI paths not run on the Linux review host. Risk: places real broker orders. |
| Maintainer | [arimanyus](https://github.com/arimanyus). Independently curated. |
| Format | Node.js intraday trading bot + local dashboard (MIT) |
| Platform and availability | Desktop/self-hosted Node process with local dashboard on 127.0.0.1:8080 |
| Jev's role | Jev (via Vercel AI Gateway / TypeSafe) classifies, ranks, and decides take-profit; application code sizes orders, places stops, and enforces loss halt. |
| Requirements | See upstream README; TypeSafe/provider keys and any broker credentials when using live paths. |
| License | [MIT](https://github.com/arimanyus/warrenduffer/blob/9accc86e872c9925c63b5b04cf6984356c8c08fa/LICENSE). Provider/broker usage may incur charges when live. |

## When to use

Use when intraday Nifty-50 trading bot where TypeSafe Jev ranks names and code sizes/stops live broker orders (experimental; real-money risk). Prefer other catalog trading/game tools when you need paper-trading or non-Jev judges.

## How it works

Jev (via Vercel AI Gateway / TypeSafe) classifies, ranks, and decides take-profit; application code sizes orders, places stops, and enforces loss halt. Application code owns orchestration and side effects beyond the judgment.

## Get started

```sh
git clone https://github.com/arimanyus/warrenduffer.git
cd warrenduffer
git checkout 9accc86e872c9925c63b5b04cf6984356c8c08fa
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 9accc86e872c](https://github.com/arimanyus/warrenduffer/tree/9accc86e872c9925c63b5b04cf6984356c8c08fa). AI-assisted README and license inspection; live paths not executed.
