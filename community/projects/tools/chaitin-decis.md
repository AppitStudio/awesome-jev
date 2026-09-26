# Decis

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted System One–compatible `/v1/systemone` server with open Laya/kev Docker images (independent of hosted TypeSafe Jev).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chaitin/Decis) |
| Maintainer | [chaitin](https://github.com/chaitin). Independently curated. |
| Format | Self-hosted decision-model API server (Docker images per engine). |
| Requirements | Docker Compose; DECIS_API_KEY in .env; no TypeSafe cloud key required for local engines. |
| License | [Apache-2.0](https://github.com/chaitin/Decis/blob/5c8f7f709d303f1709652165b350f72d229b468c/LICENSE). Independent open-weight / self-hosted path—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for **local/open-weight System One–compatible** inference with the official SDK `base_url` pointed at Decis. Prefer hosted TypeSafe Jev for the official cloud model.

## How it works

Serves the TypeSafe System One wire contract (`/v1/systemone`) from open engines (Laya, kev) with weights in the image; playground games call the same endpoint. Independent of hosted TypeSafe Jev.

## Get started

```sh
git clone https://github.com/chaitin/Decis.git
cd Decis
git checkout 5c8f7f709d303f1709652165b350f72d229b468c
# cp .env.example .env; docker compose up -d --wait — independent of hosted Jev
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 5c8f7f7](https://github.com/chaitin/Decis/tree/5c8f7f709d303f1709652165b350f72d229b468c). AI-assisted README and license inspection; install/live paths not executed.
