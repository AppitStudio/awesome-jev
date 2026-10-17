# HA_SystemOne

[All projects](../README.md) · [Home automation](README.md#home-automation)

Polish-language Home Assistant command layer: local embedding and reranker models narrow about 100 possible actions to five, Jev picks one or none with a confidence, and the action runs only at 0.8 or above; otherwise it asks back.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jarekmor/HA_SystemOne) |
| Maintainer | [jarekmor](https://github.com/jarekmor). Independently curated. |
| Format | Python service with Docker Compose and Home Assistant REST integration |
| Requirements | Home Assistant, Linux with Python 3.12+ (Docker recommended), about 4.5 GB for local models, a TypeSafe API key, an HA access token. |
| License | [MIT](https://github.com/jarekmor/HA_SystemOne/blob/f5e85b4d80a2faa1b9fc4b02d8ae4ee1547d565c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision_ha/decide.py`](https://github.com/jarekmor/HA_SystemOne/blob/f5e85b4d80a2faa1b9fc4b02d8ae4ee1547d565c/src/decision_ha/decide.py) at the pinned commit. |

## When to use

- Control Home Assistant with plain Polish sentences through Assist, with a safe 'did you mean' fallback.
- Study a retrieve, rerank, then decide pipeline where the decision model can only choose from a fixed list.
- Mismatch: Polish templates only; locks, alarms, gates and blinds are deliberately not on the allowed action list.

## How it works

Commands are matched against about 1,200 example sentences with bge-m3, reranked with bge-reranker-v2-m3, and the top five plus 'none' go to Jev as a Choice from `decide.py`. Nothing executes by default: the CLI needs `--execute`, and the server needs a token and only sends actions on the `ALLOWED` list. Integration evidence: [`src/decision_ha/decide.py`](https://github.com/jarekmor/HA_SystemOne/blob/f5e85b4d80a2faa1b9fc4b02d8ae4ee1547d565c/src/decision_ha/decide.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jarekmor/HA_SystemOne.git
cd HA_SystemOne
cp .env_example .env   # add keys
docker compose pull && docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Step-by-step Home Assistant setup (REST command and Assist automation) in the README.

## Limits and data handling

Your command text and the five candidate actions go to TypeSafe on your key; the embedding and reranker models run locally.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit f5e85b4d80a2](https://github.com/jarekmor/HA_SystemOne/tree/f5e85b4d80a2faa1b9fc4b02d8ae4ee1547d565c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
