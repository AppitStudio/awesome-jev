# OpenJev toolkit (installer, server script and Python client for running OpenJev locally on Apple silicon)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Installs OpenJev MLX builds (27B 8-bit or 4-bit, or the 9B Flash builds) at pinned revisions with uv, starts a local `POST /v1/systemone` server on port 3000 and adds a stdlib Python client, CLI and worked examples for Choice, yes/no and Score questions. Profiles are chosen by RAM (16 GB for Flash 4-bit up to 64 GB for 27B 8-bit). MLX builds are text only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/geekychris/open_jev_toolkit) |
| Maintainer | [geekychris](https://github.com/geekychris). Independently curated. |
| Format | Shell installer + Python client |
| Requirements | Apple silicon Mac with 16-64 GB RAM depending on profile, 5-27 GB disk; no cloud key (runs locally). |
| License | [Apache-2.0](https://github.com/geekychris/open_jev_toolkit/blob/be4bfd278e4671d248c2cdf4e72ac221401c4294/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`openjev_client/__init__.py`](https://github.com/geekychris/open_jev_toolkit/blob/be4bfd278e4671d248c2cdf4e72ac221401c4294/openjev_client/__init__.py) at the pinned commit. |

## When to use

- Run a System One decision model fully on a Mac with no per-call cost or data leaving the machine.
- Mismatch: text only on MLX (no screenshots); larger profiles need 32-64 GB RAM.

## How it works

`scripts/install.sh` builds the venv and downloads the model plus a checksum-verified upstream shim; `scripts/serve.sh` runs the server; `openjev_client` posts typed questions to it and returns probabilities. Integration evidence: [`openjev_client/__init__.py`](https://github.com/geekychris/open_jev_toolkit/blob/be4bfd278e4671d248c2cdf4e72ac221401c4294/openjev_client/__init__.py).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/geekychris/open_jev_toolkit/main/scripts/install.sh | bash
scripts/serve.sh start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- curl example: [github.com/geekychris/open_jev_toolkit/blob/be4bfd278e4671d248c2cdf4e72ac221401c4294/examples/01_curl.sh](https://github.com/geekychris/open_jev_toolkit/blob/be4bfd278e4671d248c2cdf4e72ac221401c4294/examples/01_curl.sh)

## Limits and data handling

Runs locally; set `SHIM_TOKEN` before binding anything other than localhost. Model weights keep their own OpenJev licence. Independent project; not affiliated with the OpenJev authors or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit be4bfd278e46](https://github.com/geekychris/open_jev_toolkit/tree/be4bfd278e4671d248c2cdf4e72ac221401c4294). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
