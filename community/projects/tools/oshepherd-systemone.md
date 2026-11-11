# oshepherd (Ollama orchestration that also queues System One decision requests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Orchestration layer that spreads Ollama inference across worker machines through a queue; its `POST /v1/systemone` route sends decision requests to workers running decision models, so the TypeSafe SDK can point at your own fleet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mnemonica-ai/oshepherd) |
| Maintainer | [mnemonica-ai](https://github.com/mnemonica-ai). Independently curated. |
| Format | API server and workers (Python, MIT) |
| Requirements | Python, the queue backend from the README, and Ollama 0.35+ workers with a decision model pulled. |
| License | [MIT](https://github.com/mnemonica-ai/oshepherd/blob/1ed65b05de73315cbd07063850adda6dec4c3ca0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`oshepherd/api/systemone/routes.py`](https://github.com/mnemonica-ai/oshepherd/blob/1ed65b05de73315cbd07063850adda6dec4c3ca0/oshepherd/api/systemone/routes.py) at the pinned commit. |

## When to use

- Share a pool of Ollama machines for local decision models.
- Use the TypeSafe SDK against a self-hosted decision fleet.
- Mismatch: serves local models, not Jev itself.

## How it works

`oshepherd/api/systemone/routes.py` accepts System One requests and hands them to workers (`oshepherd/worker/tasks.py`); the README shows the Ollama client's `client.systemone()` and `typesafe-sdk` with `TYPESAFE_BASE_URL` pointed at oshepherd. Integration evidence: [`oshepherd/api/systemone/routes.py`](https://github.com/mnemonica-ai/oshepherd/blob/1ed65b05de73315cbd07063850adda6dec4c3ca0/oshepherd/api/systemone/routes.py).

## Get started

Install from PyPI, start the API and workers per the README, then point a System One client at the API.

```sh
pip install oshepherd
export TYPESAFE_BASE_URL=http://127.0.0.1:5001
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mnemonica-ai/oshepherd/blob/1ed65b05de73315cbd07063850adda6dec4c3ca0/README.md](https://github.com/mnemonica-ai/oshepherd/blob/1ed65b05de73315cbd07063850adda6dec4c3ca0/README.md)
- PyPI: [pypi.org/project/oshepherd/](https://pypi.org/project/oshepherd/)

## Limits and data handling

Self-hosted; requests go only to your workers.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 1ed65b05de73](https://github.com/mnemonica-ai/oshepherd/tree/1ed65b05de73315cbd07063850adda6dec4c3ca0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
