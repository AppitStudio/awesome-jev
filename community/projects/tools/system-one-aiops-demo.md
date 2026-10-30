# System One AIOps demo (a fake Kubernetes shop where a System One model sorts every alert into page, Slack or noise)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reproducible demo: a small shop runs on a kind cluster with Prometheus, Alertmanager and Grafana, a chaos script breaks it in seven realistic ways, and each alert plus its logs goes to a System One model that answers typed questions with probabilities. Confident, serious alerts page on-call, unsure ones go to Slack with the best guess, and confident noise is closed. Defaults to the open Laya model on your machine; the same code runs against TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blacksoxx/system-one-aiops-demo) |
| Maintainer | [blacksoxx](https://github.com/blacksoxx). Independently curated. |
| Format | Shell, Python and Kubernetes manifests |
| Requirements | Docker, kind, kubectl and Helm; a local Laya server (GPU optional) or a TypeSafe API key for Jev. |
| License | [MIT](https://github.com/blacksoxx/system-one-aiops-demo/blob/8c69f8c3c3c06d0c94db02cfeee113311a25f668/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`triage.py`](https://github.com/blacksoxx/system-one-aiops-demo/blob/8c69f8c3c3c06d0c94db02cfeee113311a25f668/triage.py) at the pinned commit. |

## When to use

- See what calibrated typed decisions do to alert fatigue before wiring a model into real on-call.
- Mismatch: synthetic shop and 30 labelled alerts; not a production triage system.

## How it works

`triage.py` sends each alert to `SYSTEMONE_BASE_URL` (`/v1/systemone`, local Laya by default; `https://api.typesafe.ai/v1` with `TYPESAFE_API_KEY` for Jev) and maps the answers to the three lanes. Integration evidence: [`triage.py`](https://github.com/blacksoxx/system-one-aiops-demo/blob/8c69f8c3c3c06d0c94db02cfeee113311a25f668/triage.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/blacksoxx/system-one-aiops-demo && cd system-one-aiops-demo
./scripts/serve-laya.sh   # or point SYSTEMONE_BASE_URL at TypeSafe
./demo.sh up
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with dashboards and incident list: [github.com/blacksoxx/system-one-aiops-demo#readme](https://github.com/blacksoxx/system-one-aiops-demo#readme)

## Limits and data handling

With Laya everything stays on your machine; with Jev, alert text and log excerpts go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 8c69f8c3c3c0](https://github.com/blacksoxx/system-one-aiops-demo/tree/8c69f8c3c3c06d0c94db02cfeee113311a25f668). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
