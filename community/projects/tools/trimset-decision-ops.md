# trimset (self-hosted decision ops that recalibrate Jev thresholds from real outcomes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted decision ops for decision models such as Jev: a proxy logs every `/v1/systemone` decision, joins outcomes that arrive later, recalibrates probabilities, compiles thresholds for a target error rate, and lets your app gate locally with the approved policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trimset/trimset) |
| Maintainer | [trimset](https://github.com/trimset). Independently curated. |
| Format | Self-hosted server, Rust proxy and Python SDK (Apache-2.0) |
| Requirements | Docker with Compose (one machine with Postgres), and your existing Jev key upstream. |
| License | [Apache-2.0](https://github.com/trimset/trimset/blob/233c7ed9c75dfad01da771f6180f65d6d053f10b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`proxy/src/main.rs`](https://github.com/trimset/trimset/blob/233c7ed9c75dfad01da771f6180f65d6d053f10b/proxy/src/main.rs) at the pinned commit. |

## When to use

- Keep Jev decision thresholds calibrated as real outcomes arrive.
- Audit and roll back the thresholds behind automated decisions.
- Mismatch: pre-alpha; needs labeled outcomes before thresholds can be certified.

## How it works

`proxy/src/main.rs` forwards `/v1/systemone` and OpenAI-style `/v1/decisions` calls unchanged to `TRIMSET_UPSTREAM_JEV_URL` and logs them; the CLI then runs `trimset calibrate`, `simulate` and `policy compile` per question and model such as `jev-1.14.0`. Integration evidence: [`proxy/src/main.rs`](https://github.com/trimset/trimset/blob/233c7ed9c75dfad01da771f6180f65d6d053f10b/proxy/src/main.rs).

## Get started

Start the stack with Docker Compose, create a project and keys, then point your app's base URL at the proxy.

```sh
git clone https://github.com/trimset/trimset && cd trimset
echo "TRIMSET_UPSTREAM_JEV_URL=https://api.typesafe.ai" >> .env
docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Website: [trimset.dev](https://trimset.dev)
- Dashboard demo: [demo.trimset.dev](https://demo.trimset.dev)

## Limits and data handling

Decision requests and responses are stored in your own Postgres; requests are forwarded to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 233c7ed9c75d](https://github.com/trimset/trimset/tree/233c7ed9c75dfad01da771f6180f65d6d053f10b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
