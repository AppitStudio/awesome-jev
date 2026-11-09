# howsure (open-source calibration gateway for System One decision models such as Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Gateway between your app and any System One model: calibrates confidence on labeled cases, then marks every answer `auto` or `review` to stay within your chosen error rate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sailaukan/howsure) |
| Maintainer | [Sailaukan](https://github.com/Sailaukan). Independently curated. |
| Format | Python gateway + CLI (MIT) |
| Requirements | Python, `pipx install git+https://github.com/Sailaukan/howsure`, labeled examples, and a TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/Sailaukan/howsure/blob/e60f56e572999f43f491a9f58695c1e4e3d99f2c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/howsure/client.py`](https://github.com/Sailaukan/howsure/blob/e60f56e572999f43f491a9f58695c1e4e3d99f2c/src/howsure/client.py) at the pinned commit. |

## When to use

- Decide when Jev answers can skip human review.
- Recalibrate and watch drift over time.
- Mismatch: needs your own labeled cases.

## How it works

`client.py` posts each labeled example to `/v1/systemone` (TypeSafe or the OpenRouter preset); `gateway.py` serves the same path and adds the auto/review mark from the calibrated threshold. Integration evidence: [`src/howsure/client.py`](https://github.com/Sailaukan/howsure/blob/e60f56e572999f43f491a9f58695c1e4e3d99f2c/src/howsure/client.py).

## Get started

Install with pipx, calibrate on your labeled cases, then point your app's base URL at the gateway.

```sh
pipx install git+https://github.com/Sailaukan/howsure
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Sailaukan/howsure/blob/e60f56e572999f43f491a9f58695c1e4e3d99f2c/README.md](https://github.com/Sailaukan/howsure/blob/e60f56e572999f43f491a9f58695c1e4e3d99f2c/README.md)

## Limits and data handling

Requests are forwarded to your configured System One provider.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit e60f56e57299](https://github.com/Sailaukan/howsure/tree/e60f56e572999f43f491a9f58695c1e4e3d99f2c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
