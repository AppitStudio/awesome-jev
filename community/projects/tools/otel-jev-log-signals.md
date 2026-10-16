# OTEL Jev Log Signals

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OTLP/HTTP JSON relay that adds Jev decisions to OpenTelemetry logs grouped by template (for example Drain's `log.record.template`): every record is kept, each distinct template is evaluated once per cache lifetime, and low-probability results become `review`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/otel-jev-log-signals) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python relay (standard library), EN/FR/ES docs |
| Requirements | Python 3; `TYPESAFE_API_KEY` and an HTTPS (or localhost) OTLP `/v1/logs` upstream. |
| License | [MIT](https://github.com/gbesse/otel-jev-log-signals/blob/0d692a33a3cb6a2e46ab961463e63d251e77045e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`relay.py`](https://github.com/gbesse/otel-jev-log-signals/blob/0d692a33a3cb6a2e46ab961463e63d251e77045e/relay.py) at the pinned commit. |

## When to use

- Tag noisy log templates with a Jev outcome before they reach your log backend.
- Try it offline with the bundled demo and tests first.
- Mismatch: a relay, not a native Collector processor; not tested against a live Collector or live Jev account by the author; cache is in memory only.

## How it works

The relay receives OTLP/HTTP JSON on `127.0.0.1:8091/v1/logs`, asks `https://api.typesafe.ai/v1/systemone` once per new template, adds `jev.log.*` attributes, forwards to the upstream, and returns HTTP 503 on a Jev or upstream failure so senders retry. Integration evidence: [`relay.py`](https://github.com/gbesse/otel-jev-log-signals/blob/0d692a33a3cb6a2e46ab961463e63d251e77045e/relay.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbesse/otel-jev-log-signals.git && cd otel-jev-log-signals
python3 -m unittest discover -s tests -v
python3 relay.py --demo
# live: TYPESAFE_API_KEY=... OTLP_UPSTREAM_URL=https://.../v1/logs python3 relay.py --serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples: `examples/`.

## Limits and data handling

Log templates go to TypeSafe on your key; every record is forwarded downstream unchanged apart from added attributes.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 0d692a33a3cb](https://github.com/gbesse/otel-jev-log-signals/tree/0d692a33a3cb6a2e46ab961463e63d251e77045e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
