# Bagel (MCP server for robotics, drone and IoT logs whose beta anomaly gate uses a Jev backend to name what is not normal)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server that lets an agent ask plain-English questions about ROS, flight-log, CAN and MQTT data with auditable DuckDB SQL. Its beta edge data-reduction pipeline includes an anomaly gate that learns normal behaviour, asks Jev (hosted System One, or an on-robot decision model) to name what is not, and keeps only those slices.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Extelligence-ai/bagel) |
| Maintainer | [Extelligence-ai](https://github.com/Extelligence-ai). Independently curated. |
| Format | Python package `bagel-mcp` (PyPI) and Docker images |
| Requirements | Python 3.10–3.12 and uv/pip for recorded data; the Jev backend needs `TYPESAFE_API_KEY` (hosted) or the `-jev` image. |
| License | [Apache-2.0](https://github.com/Extelligence-ai/bagel/blob/bd3f65c885330b4029fbcaa383a92fe806b3dc2c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bagel_mcp/pipeline/decide/backends.py`](https://github.com/Extelligence-ai/bagel/blob/bd3f65c885330b4029fbcaa383a92fe806b3dc2c/bagel_mcp/pipeline/decide/backends.py) at the pinned commit. |

## When to use

- Reduce robot logs by keeping only slices a decision model flags.
- Mismatch: Jev is a beta, optional backend of one pipeline in a broader robotics-data tool.

## How it works

`backends.py` defines a backend protocol with a hosted `jev` backend (`POST /v1/systemone`, `jev-latest`, `TYPESAFE_API_KEY`) and an on-robot option; `gates/anomaly.py` and `gates/decide.py` use it in the anomaly pipeline. Integration evidence: [`bagel_mcp/pipeline/decide/backends.py`](https://github.com/Extelligence-ai/bagel/blob/bd3f65c885330b4029fbcaa383a92fe806b3dc2c/bagel_mcp/pipeline/decide/backends.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude mcp add bagel -- uvx --from "bagel-mcp[ros]" bagel-mcp --transport stdio
# anomaly gate runbook: doc/runbooks/anomaly_detection.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Anomaly detection with Jev runbook (beta): [github.com/Extelligence-ai/bagel/blob/bd3f65c885330b4029fbcaa383a92fe806b3dc2c/doc/runbooks/anomaly_detection.md](https://github.com/Extelligence-ai/bagel/blob/bd3f65c885330b4029fbcaa383a92fe806b3dc2c/doc/runbooks/anomaly_detection.md)

## Limits and data handling

Hosted Jev backend sends data slices to TypeSafe on your key (the README offers an on-robot alternative); beta feature. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit bd3f65c88533](https://github.com/Extelligence-ai/bagel/tree/bd3f65c885330b4029fbcaa383a92fe806b3dc2c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
